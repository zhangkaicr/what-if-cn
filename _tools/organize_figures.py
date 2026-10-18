#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Organize extracted images: map page->chapter, filter artifacts, rename by chapter order."""
import os, re, json, shutil

ROOT = r"C:/WorkBuddy/what-if-cn"
RAW = os.path.join(ROOT, "figures", "raw")
MAP = json.load(open(os.path.join(ROOT, "_build", "chapter_map.json"), encoding="utf-8"))

# page ranges from map (1-based)
pranges = []
for label, p0, p1 in MAP["ranges"]:
    if label in ("refs", "index"):
        continue
    pranges.append((label, p0+1, p1+1))

def page_to_label(p):
    for label, a, b in pranges:
        if a <= p <= b:
            return label
    return None

files = sorted(os.listdir(RAW))
out = os.path.join(ROOT, "figures")
info = []
for fn in files:
    m = re.match(r"fig-(\d+)-(\d+)\.(\w+)", fn)
    if not m:
        continue
    page, idx, ext = int(m.group(1)), int(m.group(2)), m.group(3)
    src = os.path.join(RAW, fn)
    size = os.path.getsize(src)
    info.append((page, idx, ext, size, fn))

# dimensions via a tiny PNG/JPEG parser is overkill; use file size + pixel dims via pypdf-free: use PIL if available
try:
    from PIL import Image
    HAVE_PIL = True
except ImportError:
    HAVE_PIL = False
print("PIL:", HAVE_PIL)

kept, dropped = [], []
for page, idx, ext, size, fn in info:
    w = h = 0
    if HAVE_PIL:
        try:
            with Image.open(os.path.join(RAW, fn)) as im:
                w, h = im.size
        except Exception:
            pass
    label = page_to_label(page)
    if label is None:
        dropped.append((fn, page, w, h, size, "no chapter"))
        continue
    # filter tiny artifacts (rules, bullets): small pixel dims and small bytes
    if (w and h and (w < 160 or h < 120)) or size < 3000:
        dropped.append((fn, page, w, h, size, "tiny"))
        continue
    kept.append((page, idx, ext, size, fn, label, w, h))

print(f"kept {len(kept)}, dropped {len(dropped)}")

# per chapter, order by page then idx, rename fig-<chap>-<seq>.<ext>
os.makedirs(out, exist_ok=True)
counter = {}
manifest = []
for page, idx, ext, size, fn, label, w, h in sorted(kept, key=lambda x: (x[0], x[1])):
    counter[label] = counter.get(label, 0) + 1
    seq = counter[label]
    dst = os.path.join(out, f"{label}-{seq:02d}.{ext}")
    shutil.copyfile(os.path.join(RAW, fn), dst)
    manifest.append({"file": f"{label}-{seq:02d}.{ext}", "chapter": label,
                     "page": page, "w": w, "h": h, "bytes": size})

with open(os.path.join(ROOT, "_build", "figures_manifest.json"), "w", encoding="utf-8") as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)

# summary per chapter
from collections import Counter
c = Counter(m["chapter"] for m in manifest)
for k in sorted(c, key=lambda x: (x != "intro", x)):
    print(f"  {k}: {c[k]} figures")
print("manifest saved.")

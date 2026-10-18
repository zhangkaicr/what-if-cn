#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Crop Figure/Table regions from What If (margin-layout book). v2
- Figures: attach raster images to the nearest caption label BELOW them; grow up absorbing
  small-font graphics labels (any x).
- Tables: grow down absorbing margin-zone blocks (x1 < main_x0 - 10).
"""
import os, re, json
from collections import Counter
import pymupdf

SRC = r"C:/Users/85330/Desktop/HTE-202610/1.模块一：从平均治疗效果到个体化治疗效果/ref/Causal-Inference-What-If.pdf"
ROOT = r"C:/WorkBuddy/what-if-cn"
MAP = json.load(open(os.path.join(ROOT, "_build", "chapter_map.json"), encoding="utf-8"))
ZOOM = 2.5
LABEL = re.compile(r"^\s*(Figure|Table)\s+(\d+\.\d+)\s*$")

pranges = [(l, a+1, b+1) for l, a, b in MAP["ranges"] if l not in ("refs", "index")]
def page_to_label(p):
    for label, a, b in pranges:
        if a <= p <= b:
            return label
    return None

doc = pymupdf.open(SRC)
outdir = os.path.join(ROOT, "figures")
os.makedirs(outdir, exist_ok=True)
manifest, problems = [], []

def dom_size(spans):
    c = Counter(round(s["size"], 1) for s in spans)
    return c.most_common(1)[0][0] if c else 10

for pno in range(len(doc)):
    label = page_to_label(pno+1)
    if label is None:
        continue
    page = doc[pno]
    d = page.get_text("dict")
    tblocks, labels = [], []
    for b in d["blocks"]:
        if b.get("type") != 0:
            continue
        lines = []
        for ln in b.get("lines", []):
            txt = "".join(s["text"] for s in ln.get("spans", []))
            lines.append((pymupdf.Rect(ln["bbox"]), txt, dom_size(ln.get("spans", []))))
        if not lines:
            continue
        spans = [s for ln in b.get("lines", []) for s in ln.get("spans", [])]
        tblocks.append({"rect": pymupdf.Rect(b["bbox"]), "lines": lines,
                        "size": dom_size(spans)})
        for lrect, ltxt, lsz in lines:
            m = LABEL.match(ltxt)
            if m:
                labels.append({"kind": m.group(1).lower(), "num": m.group(2),
                               "rect": pymupdf.Rect(lrect)})
    if not labels:
        continue
    imgs = [pymupdf.Rect(i["bbox"]) for i in page.get_image_info()]
    wide = [b["rect"].x0 for b in tblocks if b["rect"].width > 320 and b["rect"].x0 > 100]
    main_x0 = min(wide) if wide else 190.0

    # attach each image to nearest FIGURE label below it
    attach = {}
    for ir in imgs:
        best, bd = None, 1e9
        for lb in labels:
            if lb["kind"] != "figure":
                continue
            dist = lb["rect"].y0 - ir.y1   # positive if image fully above label
            if -80 <= dist < 420 and dist < bd:
                best, bd = lb, dist
        if best is not None:
            attach.setdefault(id(best), []).append(ir)

    for lb in labels:
        kind, num = lb["kind"], lb["num"]
        region = pymupdf.Rect(lb["rect"])
        if kind == "figure":
            for ir in attach.get(id(lb), []):
                region |= ir
            for _ in range(30):
                changed = False
                for b in tblocks:
                    r = b["rect"]
                    if region.contains(r):
                        continue
                    gap = region.y0 - r.y1
                    if -8 <= gap <= 40 and b["size"] < 9.7:
                        region |= r; changed = True
                for ir in attach.get(id(lb), []):
                    if not region.contains(ir) and ir.intersects(pymupdf.Rect(
                            region.x0-200, region.y0-40, region.x1+200, region.y1+8)):
                        region |= ir; changed = True
                if not changed:
                    break
        else:
            for _ in range(60):
                changed = False
                for b in tblocks:
                    r = b["rect"]
                    if region.contains(r):
                        continue
                    gap_up = region.y0 - r.y1
                    gap_dn = r.y0 - region.y1
                    gap = min(gap_up if gap_up >= -8 else 1e9,
                              gap_dn if gap_dn >= -8 else 1e9)
                    if gap <= 40 and r.x1 < main_x0 - 10:
                        region |= r; changed = True
                if not changed:
                    break
        y0 = max(region.y0 - 4, 26)
        y1 = min(region.y1 + 4, page.rect.y1 - 8)
        clip = pymupdf.Rect(min(region.x0 - 4, 26.9), y0,
                            max(region.x1 + 4, 0), y1)
        clip.x0 = max(clip.x0, 24)
        clip.x1 = min(max(clip.x1, region.x1 + 4), page.rect.x1 - 20)
        if clip.height < 36 or clip.width < 55:
            problems.append((label, kind, num, pno+1, f"h={clip.height:.0f} w={clip.width:.0f}"))
            continue
        pix = page.get_pixmap(matrix=pymupdf.Matrix(ZOOM, ZOOM), clip=clip, alpha=False)
        fn = f"{kind}-{num.replace('.', '_')}.png"
        pix.save(os.path.join(outdir, f"{label}--{fn}"))
        manifest.append({"chapter": label, "kind": kind, "num": num, "page": pno+1,
                         "file": f"{label}--{fn}", "w": pix.width, "h": pix.height})

with open(os.path.join(ROOT, "_build", "crops_manifest.json"), "w", encoding="utf-8") as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)

c = Counter((m["chapter"], m["kind"]) for m in manifest)
for k in sorted(c):
    print(f"  {k[0]} {k[1]}: {c[k]}")
print("total:", len(manifest), "| problems:", len(problems))
for p in problems:
    print("  !!", p)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""What If PDF: robust chapter split via 'Chapter N' openers; clean -layout text per chapter."""
import os, re, json, subprocess, sys

SRC = r"C:/Users/85330/Desktop/HTE-202610/1.模块一：从平均治疗效果到个体化治疗效果/ref/Causal-Inference-What-If.pdf"
BUILD = r"C:/WorkBuddy/what-if-cn/_build"
os.makedirs(BUILD, exist_ok=True)
PDFTEXT = r"C:/Users/85330/AppData/Local/Programs/MiKTeX/miktex/bin/x64/pdftotext.exe"
PDFTOTEXT_OK = os.path.exists(PDFTEXT)

from pypdf import PdfReader
reader = PdfReader(SRC)
N = len(reader.pages)

# detect opener pages: first non-empty line matches 'Chapter N' (1-23), or Introduction/References/Index
def first_lines(i, k=6):
    t = reader.pages[i].extract_text() or ""
    ls = [l.strip() for l in t.splitlines() if l.strip()]
    return ls[:k]

openers = {}  # label -> pdf index
for i in range(N):
    ls = first_lines(i, 6)
    for ln in ls:
        m = re.match(r"^Chapter\s+(\d{1,2})$", ln, re.I)
        if m:
            num = int(m.group(1))
            if 1 <= num <= 23:
                openers.setdefault(f"ch{num}", i)
                break
        if re.match(r"^Introduction$", ln, re.I) and "intro" not in openers:
            openers["intro"] = i; break
        if re.match(r"^References$", ln, re.I) and "refs" not in openers:
            openers["refs"] = i; break
        if re.match(r"^Index$", ln, re.I) and "index" not in openers:
            openers["index"] = i; break

# ensure intro detection (the intro might be titled 'Towards less casual...')
if "intro" not in openers:
    for i in range(N):
        ls = first_lines(i, 8)
        if any("TOWARDS LESS CASUAL" in l.upper() for l in ls):
            openers["intro"] = i; break

print("openers:", {k: v+1 for k, v in sorted(openers.items(), key=lambda kv: kv[1])})

# build ordered ranges
order = sorted(openers.items(), key=lambda kv: kv[1])
ranges = []
for idx, (label, p0) in enumerate(order):
    p1 = order[idx+1][1]-1 if idx+1 < len(order) else N-1
    ranges.append((label, p0, p1))

# dump clean text per range via pdftotext -layout
for label, p0, p1 in ranges:
    out = os.path.join(BUILD, f"{label}.txt")
    if PDFTOTEXT_OK:
        subprocess.run([PDFTEXT, "-layout", "-f", str(p0+1), "-l", str(p1+1),
                        SRC, out], check=True, capture_output=True)
    else:
        # fallback to pypdf
        with open(out, "w", encoding="utf-8") as f:
            for i in range(p0, p1+1):
                f.write(f"\n\n===== PAGE {i+1} =====\n" + (reader.pages[i].extract_text() or ""))
    sz = os.path.getsize(out)
    print(f"  {label}: PDF pages {p0+1}-{p1+1} ({p1-p0+1} pp), text {sz}B")

with open(os.path.join(BUILD, "chapter_map.json"), "w", encoding="utf-8") as f:
    json.dump({"N": N, "openers": openers, "ranges": ranges}, f, ensure_ascii=False, indent=2)
print("done.")

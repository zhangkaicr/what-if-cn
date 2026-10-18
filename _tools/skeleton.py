# -*- coding: utf-8 -*-
"""Extract chapter titles + numbered section skeleton from extracted PDF text.

Reads  : _build/ch<N>.txt  (pdftotext -layout output, one file per chapter)
Writes : stdout (chapter title + numbered section headings)
         _build/skeleton.json (machine-readable form, reused by later stages)
"""
import json
import pathlib
import re

BUILD = pathlib.Path(r"C:/WorkBuddy/what-if-cn/_build")
NUM = re.compile(r"^\s{0,8}(\d{1,2}\.\d{1,2})\s+(.{2,90}?)\s*$")


def chapter_key(p: pathlib.Path) -> int:
    return int(p.stem[2:])


def main() -> None:
    out = {}
    for f in sorted(BUILD.glob("ch*.txt"), key=chapter_key):
        lines = f.read_text(encoding="utf-8", errors="replace").splitlines()

        title = ""
        for ln in lines[:80]:
            s = ln.strip()
            if len(s) > 3 and not s.isdigit() and not NUM.match(ln):
                title = s
                break

        secs, seen = [], set()
        for ln in lines:
            m = NUM.match(ln)
            if m and m.group(1) not in seen:
                seen.add(m.group(1))
                secs.append({"id": m.group(1), "title": m.group(2)})

        num = f.stem[2:]
        out[f"ch{num}"] = {"title": title, "sections": secs}

        print(f"### ch{num} | {title}")
        for s in secs:
            print(f"    {s['id']} {s['title']}")
        print()

    (BUILD / "skeleton.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    total = sum(len(v["sections"]) for v in out.values())
    print(f"[done] {len(out)} chapters, {total} sections -> _build/skeleton.json")


if __name__ == "__main__":
    main()

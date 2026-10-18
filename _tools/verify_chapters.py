# -*- coding: utf-8 -*-
"""翻译产出质量校验：图表文件名是否真实存在、占位符是否清除、小节是否覆盖。

用法：python _tools/verify_chapters.py [ch1 ch15 ...]
      不带参数则校验全部章节。

检查项：
1. 是否残留 {{...}} 占位符（只允许 <!--NAV--> 与 CONTENT 标记）
2. 嵌入的每个 <img src="../figures/..."> 文件是否真实存在（防臆造文件名）
3. 该章清单里的图表是否全部被嵌入（漏嵌检查）
4. 是否仍是占位页
5. 是否残留 HTML 未闭合的常见问题（<figure> 与 </figure> 配平）
6. **小节完整性**：译文的小节数必须覆盖原文全部小节（防止上一版那种"只译一半"的残篇）
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(r"C:/WorkBuddy/what-if-cn")
CHAPTERS = ROOT / "chapters"
FIGURES = ROOT / "figures"
PER_CH = json.loads((ROOT / "_build" / "figures_per_chapter.json").read_text(encoding="utf-8"))
SKEL = json.loads((ROOT / "_build" / "skeleton.json").read_text(encoding="utf-8"))

IDS = ["intro"] + [f"ch{i}" for i in range(1, 24)]
PLACEHOLDER_MARK = "翻译进行中"
IMG_RE = re.compile(r'<img[^>]+src="\.\./figures/([^"]+)"')
SEC_RE = re.compile(r'id="s-(\d+)-(\d+)"')


def _sort_key(s: str) -> tuple[int, ...]:
    return tuple(int(p) for p in s.replace("-", ".").split("."))


def _skeleton_ids(cid: str) -> set[str]:
    """原文小节号集合。skeleton 按抽取顺序可能混入相邻章的编号，
    因此只保留与本章前缀一致的条目，避免串章误报。"""
    prefix = cid.replace("intro", "")
    ids = {s["id"] for s in SKEL.get(cid, {}).get("sections", [])}
    if prefix:
        want = prefix.lstrip("ch") + "."
        ids = {i for i in ids if i.startswith(want)}
    return ids


def check(cid: str) -> list[str]:
    path = CHAPTERS / f"{cid}.html"
    if not path.exists():
        return [f"{cid}: 文件不存在"]

    text = path.read_text(encoding="utf-8")
    errs: list[str] = []

    if PLACEHOLDER_MARK in text:
        errs.append(f"{cid}: 仍是占位页（未翻译）")

    # 1) 残留占位符
    leftovers = re.findall(r"\{\{[^}]+\}\}", text)
    if leftovers:
        errs.append(f"{cid}: 残留占位符 {sorted(set(leftovers))}")

    # 2) 引用的图表文件是否存在
    refs = set(IMG_RE.findall(text))
    missing = sorted(f for f in refs if not (FIGURES / f).exists())
    if missing:
        errs.append(f"{cid}: 引用了不存在的图表 {missing}")

    # 3) 清单里的图表是否漏嵌
    want = set(PER_CH.get(cid, []))
    if want:
        got = {f for f in refs}
        lost = sorted(want - got)
        if lost:
            errs.append(f"{cid}: 漏嵌 {len(lost)} 个: {lost}")

    # 3b) 同一张图被重复嵌入（原书某表在两节分别引用时属于合理例外，
    #     故只报告不判错，交由人工确认）
    if refs:
        all_srcs = re.findall(r'<img[^>]+src="\.\./figures/([^"]+)"', text)
        dup = sorted({f for f in all_srcs if all_srcs.count(f) > 1})
        if dup:
            errs.append(f"{cid}: 以下图表出现多次（请确认是否为原书两处引用的合理重复）: {dup}")

    # 4) figure 标签配平
    if text.count("<figure") != text.count("</figure>"):
        errs.append(f"{cid}: <figure> 未配平（{text.count('<figure')} 开 / {text.count('</figure>')} 闭）")

    # 5) 小节完整性——防止"只译了一半"的残篇
    want_secs = _skeleton_ids(cid)
    if want_secs:
        got_secs = {f"{a}.{b}" for a, b in SEC_RE.findall(text)}
        missing_secs = sorted(want_secs - got_secs, key=_sort_key)
        if missing_secs:
            errs.append(
                f"{cid}: 小节残缺，缺 {len(missing_secs)}/{len(want_secs)} 节 -> "
                + ", ".join(missing_secs)
            )

    return errs


def main() -> None:
    targets = sys.argv[1:] or IDS
    all_errs: list[str] = []
    done = placeholder = 0
    for cid in targets:
        p = CHAPTERS / f"{cid}.html"
        if p.exists():
            t = p.read_text(encoding="utf-8")
            if PLACEHOLDER_MARK in t:
                placeholder += 1
            else:
                done += 1
        all_errs.extend(check(cid))

    print(f"已翻译 {done} / {len(targets)}    占位 {placeholder}")
    if all_errs:
        print(f"\n发现 {len(all_errs)} 个问题：")
        for e in all_errs:
            print("  -", e)
        sys.exit(1)
    print("全部校验通过：图表文件名真实、无占位符残留、小节完整、figure 配平。")


if __name__ == "__main__":
    main()
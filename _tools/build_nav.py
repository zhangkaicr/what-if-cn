#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build nav (inject into all pages) + search_index.json for what-if-cn."""
import os, re, json, html

ROOT = r"C:/WorkBuddy/what-if-cn"

CHAPTERS = [
    ("intro", "导言：少一点“随便”的因果推断", "导言"),
    ("ch1", "第 1 章 · 因果效应的定义", "第一部分"),
    ("ch2", "第 2 章 · 随机化试验", "第一部分"),
    ("ch3", "第 3 章 · 观察性研究", "第一部分"),
    ("ch4", "第 4 章 · 效应修饰", "第一部分"),
    ("ch5", "第 5 章 · 交互作用", "第一部分"),
    ("ch6", "第 6 章 · 因果效应的图形表示", "第一部分"),
    ("ch7", "第 7 章 · 混杂", "第一部分"),
    ("ch8", "第 8 章 · 选择偏倚", "第一部分"),
    ("ch9", "第 9 章 · 测量偏倚与“非因果”图", "第一部分"),
    ("ch10", "第 10 章 · 随机变异", "第一部分"),
    ("ch11", "第 11 章 · 为什么需要模型", "第二部分"),
    ("ch12", "第 12 章 · 逆概率加权与边际结构模型", "第二部分"),
    ("ch13", "第 13 章 · 标准化与参数化 g 算法", "第二部分"),
    ("ch14", "第 14 章 · 结构嵌套模型的 g 估计", "第二部分"),
    ("ch15", "第 15 章 · 结局回归与倾向性评分", "第二部分"),
    ("ch16", "第 16 章 · 工具变量估计", "第二部分"),
    ("ch17", "第 17 章 · 因果生存分析", "第二部分"),
    ("ch18", "第 18 章 · 变量选择与高维数据", "第二部分"),
    ("ch19", "第 19 章 · 时变处理", "第三部分"),
    ("ch20", "第 20 章 · 处理-混杂反馈", "第三部分"),
    ("ch21", "第 21 章 · 时变处理的 g 方法", "第三部分"),
    ("ch22", "第 22 章 · 目标试验模拟", "第三部分"),
    ("ch23", "第 23 章 · 因果中介", "第三部分"),
]
PARTS = [("导言", "导言"), ("第一部分", "第一部分 · 无模型的因果推断"),
         ("第二部分", "第二部分 · 基于模型的因果推断"),
         ("第三部分", "第三部分 · 时变处理的因果推断")]

def nav_html(base):
    # base: "./" for root pages, "../" for chapters/
    parts = []
    sel = ['<select aria-label="章节跳转">']
    sel.append(f'<option value="{base}index.html">📖 目录</option>')
    for key, gname, _ in PARTS:
        group = [c for c in CHAPTERS if c[2] == key]
        sel.append(f'<optgroup label="{gname}">')
        for cid, title, _p in group:
            cur = " selected" if os.path.basename(base) == ".." and f"{cid}.html" else ""
            sel.append(f'<option value="{base}chapters/{cid}.html"{cur}>{title}</option>')
        sel.append("</optgroup>")
    sel.append("</select>")
    return ('<nav class="cw-nav">' +
            f'<a class="brand" href="{base}index.html">What If 中文版</a>' +
            "".join(sel) +
            '<span class="spacer"></span>' +
            f'<input class="q" type="text" placeholder="站内搜索（按 / 聚焦）" data-base="{base}">' +
            '<button class="tbtn" title="切换明暗">🌙</button>' +
            '</nav>')

def strip_tags(s):
    s = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", s, flags=re.S)
    s = re.sub(r"<[^>]+>", " ", s)
    return html.unescape(re.sub(r"\s+", " ", s)).strip()

def build_index_page():
    pages = []
    for cid, title, part in CHAPTERS:
        p = os.path.join(ROOT, "chapters", f"{cid}.html")
        if not os.path.exists(p):
            print(f"  !! missing {cid}.html")
            continue
        txt = open(p, encoding="utf-8").read()
        h2s = re.findall(r'<h([23])[^>]*id="([^"]+)"[^>]*>(.*?)</h\1>', txt, re.S)
        # split content by section headings
        sections = []
        body = txt.split("<!-- CONTENT-START -->")[-1].split("<!-- CONTENT-END -->")[0]
        parts_split = re.split(r'<h([23])[^>]*id="([^"]+)"[^>]*>.*?</h\1>', body, flags=re.S)
        # parts_split: [pre, level, id, seg, level, id, seg, ...]
        pre = strip_tags(parts_split[0])
        if pre:
            sections.append({"id": "", "head": title, "text": pre[:1500]})
        it = iter(parts_split[1:])
        for lvl, hid in zip(it, it):
            seg = next(it)
            head = strip_tags(re.search(rf'<h{lvl}[^>]*id="{hid}"[^>]*>(.*?)</h{lvl}>',
                                        body, re.S).group(1))
            sections.append({"id": hid, "head": head, "text": strip_tags(seg)[:4000]})
        pages.append({"file": f"chapters/{cid}.html", "title": title,
                      "part": part, "sections": sections})
    with open(os.path.join(ROOT, "search_index.json"), "w", encoding="utf-8") as f:
        json.dump({"site": "因果推断：What If 中文版", "pages": pages}, f, ensure_ascii=False)
    print(f"search_index.json: {len(pages)} pages")

def inject_nav():
    for cid, *_ in CHAPTERS:
        p = os.path.join(ROOT, "chapters", f"{cid}.html")
        if not os.path.exists(p):
            continue
        txt = open(p, encoding="utf-8").read()
        if "<!--NAV-->" in txt:
            txt = txt.replace("<!--NAV-->", nav_html("../"))
            open(p, "w", encoding="utf-8").write(txt)
            print(f"  nav -> {cid}.html")
    for f in ("index.html", "search.html"):
        p = os.path.join(ROOT, f)
        if os.path.exists(p):
            txt = open(p, encoding="utf-8").read()
            if "<!--NAV-->" in txt:
                txt = txt.replace("<!--NAV-->", nav_html("./"))
                open(p, "w", encoding="utf-8").write(txt)
                print(f"  nav -> {f}")

if __name__ == "__main__":
    inject_nav()
    build_index_page()

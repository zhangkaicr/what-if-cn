# -*- coding: utf-8 -*-
"""为尚未完成翻译的章节生成"翻译进行中"占位页，保证站内零死链。

输入  : _build/skeleton.json（章节标题）+ _tools/build_nav.py 的 CHAPTERS
输出  : chapters/<id>.html（仅当该章节尚无译文时创建）
特点  : 占位页复用正式章节的 HTML 骨架与 <!--NAV--> 标记，
        因此 build_nav.py 的 inject_nav() 会像对待正文一样注入导航下拉框。
"""
import json
import pathlib

ROOT = pathlib.Path(r"C:/WorkBuddy/what-if-cn")
BUILD = ROOT / "_build"
CHAPTERS_DIR = ROOT / "chapters"

# 与 build_nav.py 的 CHAPTERS 保持一致（id, 标题, 部分）
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

TEMPLATE = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · 翻译进行中 · 因果推断：What If 中文版</title>
<link rel="stylesheet" href="../assets/style.css">
</head>
<body>
<!--NAV-->
<main class="content">
<article>
<h1>{title}</h1>
<p class="muted">{part} · Hernán &amp; Robins, <em>Causal Inference: What If</em> (2020)</p>

<div class="tnote">
<p><strong>本章翻译进行中。</strong>原书文本已提取完毕，中文译文正在补齐。</p>
<p>在译文上线前，您可以：</p>
<ul>
<li>阅读<a href="ch{prev_id}.html">上一章</a>与<a href="ch{next_id}.html">下一章</a>已完成的译文；</li>
<li>按上方搜索框检索全站已翻译内容；</li>
<li>回到<a href="index.html">目录页</a>查看当前进度。</li>
</ul>
<p class="muted">本章原有小节结构（供对照原书阅读）：</p>
<ul>{sections}</ul>
</div>
<!-- CONTENT-END -->
</article>
</main>
<script src="../assets/site.js"></script>
</body>
</html>
"""


def prev_next(cid: str) -> tuple[str, str]:
    """返回 (上一章 id, 下一章 id)；首章/末章用 index.html 兜底。"""
    ids = [c[0] for c in CHAPTERS]
    i = ids.index(cid)
    prev_id = ids[i - 1] if i > 0 else "index"
    next_id = ids[i + 1] if i < len(ids) - 1 else "index"
    return prev_id, next_id


def main() -> None:
    skeleton = json.loads((BUILD / "skeleton.json").read_text(encoding="utf-8"))
    created, skipped = [], []

    for cid, title, part in CHAPTERS:
        target = CHAPTERS_DIR / f"{cid}.html"
        if target.exists() and target.stat().st_size > 2000:
            skipped.append(cid)
            continue

        secs = skeleton.get(cid, {}).get("sections", [])
        sec_html = "\n".join(f"    <li>{s['id']} {s['title']}</li>" for s in secs)
        prev_id, next_id = prev_next(cid)

        target.write_text(
            TEMPLATE.format(
                title=title,
                part=part,
                prev_id=prev_id,
                next_id=next_id,
                sections=sec_html or "    <li class=\"muted\">（原书目录提取中）</li>",
            ),
            encoding="utf-8",
        )
        created.append(cid)

    print(f"[ok] 生成占位页 {len(created)} 个: {' '.join(created)}")
    print(f"[skip] 已有译文 {len(skipped)} 个: {' '.join(skipped)}")


if __name__ == "__main__":
    main()

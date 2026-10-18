# -*- coding: utf-8 -*-
"""把 gen_bundle.py 单行字符串里的 ASCII 直引号替换为直角引号，消除 Python 语法错误。

只针对 `"key": "..."` 形式的单行字符串内部出现的直引号；
三引号包裹的能力卡正文不受影响，无需处理。
"""
from pathlib import Path

P = Path(r"C:/WorkBuddy/what-if-cn/_cangjie/gen_bundle.py")

PAIRS = [
    ('and "Noncausal" diagrams', 'and 「Noncausal」 diagrams'),
    ('讲授的"在未测混杂下仍可识别"的路径', '讲授的「在未测混杂下仍可识别」的路径'),
    ('作者指出"效应修饰"与"交互"在', '作者指出「效应修饰」与「交互」在'),
    ('不是"交互"）', '不是「交互」）'),
    ('在"调整中介"之前', '在「调整中介」之前'),
    ('只有当"把中介固定在某值"是', '只有当「把中介固定在某值」是'),
    ('或问"这个变量是不是中介"时用', '或问「这个变量是不是中介」时用'),
    ('只有当"把中介变量设定为某值"是', '只有当「把中介变量设定为某值」是'),
    ('选变量不看"能不能预测结局"', '选变量不看「能不能预测结局」'),
    ('当用户问"该把哪些变量放进模型"', '当用户问「该把哪些变量放进模型」'),
]


def main() -> None:
    text = P.read_text(encoding="utf-8")
    hit = 0
    for old, new in PAIRS:
        if old in text:
            text = text.replace(old, new)
            hit += 1
        else:
            print(f"[warn] 未命中: {old}")
    P.write_text(text, encoding="utf-8")
    print(f"[ok] 替换 {hit}/{len(PAIRS)} 处 -> {P}")


if __name__ == "__main__":
    main()

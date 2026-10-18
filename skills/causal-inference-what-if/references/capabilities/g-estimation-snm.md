<!-- capability_id: cap.what-if.g-estimation-snm | revision: 1 | status: active -->
<!-- 来源: Causal Inference: What If (Hernan & Robins, 2020) / 第 14 章 G-estimation of structural nested models（14.1-14.6）；第 17.6 节 G-estimation of structural nested models；第 21.4 节 G-estimation for time-varying treatments -->

## R — 原文

结构定位：第 14.3 节 "Structural nested mean models"；14.4 "Rank preservation"；14.5 "G-estimation"；14.6 "Structural nested models with two or more parameters"；第 21.4 节 "G-estimation for time-varying treatments"。

## I — 自述

三类 G 方法的差别在于**把模型建在哪儿**：
- g-formula 建在结局上；
- IP 加权建在治疗的机制上；
- **G-estimation 直接建在效应上**。

结构嵌套均值模型（SNMM）写的是：在给定协变量下，接受治疗者相对未接受治疗者的**均值差**是多少，即 E[Yᵃ − Y⁰ | A=1, L] = ψ（可含 L 的交互项）。参数 ψ 就是待估的效应。

求解思路很巧妙：从个体观测结局 Y 中"扣除"掉假设的效应 ψ，得到一个"若从未治疗"的潜在结局的估计值 Y⁰(ψ)。如果这个 ψ 猜对了，那么在给定 L 的条件下，Y⁰(ψ) 应当与当期治疗 A **无关**（因为在扣掉真实的治疗效应之后，剩下的部分不该再携带治疗的信息）。于是估计 ψ 就变成：搜索那个使 A 与 Y⁰(ψ) 独立的值。

## A1 — 书中案例

- **第 14.1-14.2 节**：作者用同一个戒烟与体重增加的例子重述问题与可交换性，让读者看到三种 G 方法面对的是**同一个 estimand**，只是算法路线不同。
- **第 14.4 节 "Rank preservation"**：作者坦率讨论这一额外假设——它要求个体间的潜在结局排序在治疗下保持不变。书里指出这是个强假设，也是 SNMM 在多参数情形下的软肋。
- **第 21.4 节**：推广到时变处理，G-estimation 成为处理治疗-混杂反馈的第三条路。

## A2 — 未来触发

场景：
1. 用户明确说要用 G-estimation 或结构嵌套模型。
2. 用户在比较三类 G 方法该选哪个。
3. 用户关心效应如何随协变量变化，且不希望在结局模型上做重假设。
4. 用户在时变处理场景下需要一条不依赖结局模型正确设定的路线。

语言信号：G-estimation / G 估计 / 结构嵌套模型 / structural nested model / SNMM / rank preservation / g-methods 怎么选。

与相邻能力区分：若用户只是要边际效应且是单期，IP 加权或标准化更简单；若治疗随时间变化，三类方法都有对应版本（第 21.1-21.4 节），选择取决于愿意把模型建在哪儿。

## E — 执行步骤

1. 确认识别条件（尤其可交换性）成立。
2. 写出结构嵌套均值模型的形式：单参数还是含 L 的交互项（多参数见第 14.6 节）。
3. 计算 Y⁰(ψ) = Y − ψ·A（或含交互项的一般形式）。
4. 建立检验：在给定 L 下，A 是否与 Y⁰(ψ) 独立（常用方式是在 A 的模型中加入 Y⁰(ψ) 作为协变量，检验其系数是否为 0）。
5. 搜索使该检验最不显著的 ψ，即为估计值。
6. 置信区间取"检验不拒绝"的 ψ 集合。
7. 完成标准：能解释"为什么对的时候 A 与 Y⁰(ψ) 应该无关"。

## B — 边界

- **多参数 SNMM 往往需要秩保持假设**（第 14.4 节），这是一个无法检验的强假设，使用前必须说明。
- **比 IP 加权和 g-formula 更少被软件支持**，实现成本高。
- **不解决未测混杂**。
- 若只需一个简单的边际效应，用 G-estimation 属于杀鸡用牛刀。

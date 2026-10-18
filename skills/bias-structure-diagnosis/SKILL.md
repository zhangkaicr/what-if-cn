---
name: bias-structure-diagnosis
description: |
  当用户问'这算混杂还是选择偏倚''这个偏倚能不能校正'时用。
  按因果图的结构给偏倚定类：共同原因 → 混杂；条件于共同结果（对撞节点）→ 选择偏倚；
  变量测错或用了代理 → 测量偏倚。定类之后才知道该调整什么、能不能调整。
  触发信号：这是哪种偏倚 / 混杂 vs 选择偏倚 / 能不能校正 / bias 分类 / collider 引入的偏倚。
  不适用于：只想找调整集合（走因果图识别）、已经确定是时间零点不对齐导致的永恒时间偏倚（走专项能力）、
  以及纯统计的随机误差问题（走识别与估计的区分）。
metadata:
  cangjie.generated-by: cangjie-tools v2.5.0
  cangjie.capability-id: cap.what-if.bias-structure-diagnosis
  cangjie.capability-revision: 1
  cangjie.bundle-id: bundle.causal-inference-what-if
  cangjie.source-title: Causal Inference - What If
  cangjie.tags: causal-inference, bias, diagnosis
---
<!-- capability_id: cap.what-if.bias-structure-diagnosis | revision: 1 | status: active -->
<!-- 来源: Causal Inference: What If (Hernan & Robins, 2020) / 第 6.5 节 A structural classification of bias；第 7 章 Confounding；第 8 章 Selection bias；第 9 章 Measurement bias and 「Noncausal」 diagrams -->

## R — 原文

结构定位：第 6.5 节标题 "A structural classification of bias"；第 7 章 "Confounding"；第 8 章 "Selection bias"；第 9 章 "Measurement bias and 'Noncausal' diagrams"。

> "causal inference cannot be reduced to a collection of recipes for data analysis."
> —— Introduction, p. vii

## I — 自述

教科书里"偏倚"有几十个名字——回忆偏倚、检出偏倚、适应证偏倚、健康工人效应……这些名字是**历史遗留下来的标签**，不是分析工具。作者的提议是：忘掉名字，看图。

三类偏倚对应三种图结构：
- **混杂**：治疗与结局共享**共同原因**，且我们没处理它 → 存在开放的后门路径。
- **选择偏倚**：我们**条件于治疗与结局的共同结果**（对撞节点或其后代）。注意，它不要求真的"选了人"，只要分析中以某种方式做了条件化，包括删失、失访、只纳入住院者等。
- **测量偏倚**：变量测错了，或测的是一个代理而非真正的节点。

这个分类之所以有用，是因为**处理方式完全不同**：混杂通常可调整；选择偏倚要看能否重建选择机制（第 8.5 节）；测量偏倚往往无法用现有数据校正，只能做敏感性分析。

## A1 — 书中案例

- **第 8.2 节 "Examples of selection bias"**：作者用若干经典实例说明选择偏倚如何伪装成真实效应——很多"风险因素"其实只是进入了分析人群的门票。
- **第 8.4 节 "Selection bias and censoring"**：把删失明确归入选择偏倚的图结构，这正是 Part III 把"删失当作一种时变处理"（第 21.5 节）来处理的伏笔。
- **第 9.3 节 "Mismeasured confounders and colliders"**：测错的混杂因子和对撞节点会同时制造混杂与选择偏倚，单纯"调整"往往修不好。

## A2 — 未来触发

场景：
1. 用户报告一个可疑的效应估计，问"这可能是哪种偏倚"。
2. 用户要写研究的局限性（limitation）段落，需要系统地列举偏倚来源。
3. 用户问"这个偏倚能不能用统计方法校正，还是只能做敏感性分析"。
4. 团队里出现"我觉得这是回忆偏倚""不对，这是适应证偏倚"这类靠名字争论的对话。

语言信号：这是哪种偏倚 / 混杂还是选择偏倚 / 能不能校正 / selection bias / collider / 健康工人效应 / 检出偏倚 / 失访偏倚。

与相邻能力区分：本能力管**定类与分流**。定类之后需要具体处理 → 混杂交给因果图识别 + 标准化/IP 加权；选择偏倚交给选择偏倚与永恒时间偏倚；测量偏倚通常只能敏感性分析。

## E — 执行步骤

1. 画出研究者**实际所做的分析**的图，而不是理想研究的图——包括谁被纳入、谁被删失、测了什么。
2. 找出 A 与 Y 之间所有开放的非因果路径。
3. 逐条判断路径结构：是共同原因（混杂）、共同结果（选择偏倚），还是节点测错（测量偏倚）。
4. 对每一条标注**可否校正**：共同原因且已测量 → 可调整；共同结果 → 需重建选择机制；未测量或测错 → 只能敏感性分析或承认不可校正。
5. 输出一张偏倚清单，每条写明：路径、类型、可校正性、拟用方法。
6. 完成标准：清单上的每一条都能在图上指出对应的那条路径。

## B — 边界

- **不要只用名字下结论。** 同一个"检出偏倚"在不同研究里可能是选择偏倚也可能是混杂。
- **选择偏倚不只在"选人"时发生。** 分析中的任何条件化（含分层、删失、纳入标准）都可能触发。
- **测量偏倚常常无法用现有数据修复**；此时应做定量偏倚分析，而不是假装调整了就好。
- 本分类不覆盖**随机误差**（第 10 章）——那是识别与估计的区别，不是偏倚的类型。

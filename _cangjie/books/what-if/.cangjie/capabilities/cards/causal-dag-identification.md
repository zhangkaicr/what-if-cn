<!-- capability_id: cap.what-if.causal-dag-identification | revision: 1 | status: active -->
<!-- 来源: Causal Inference: What If (Hernan & Robins, 2020) / 第 6 章（6.1-6.6）；第 7.3 节 Confounding and the backdoor criterion；第 7.6 节 Confounding adjustment -->

## R — 原文

> "This is not a philosophy book. We remain largely agnostic about metaphysical concepts like causality and cause. Instead, we focus on the identification and estimation of causal effects in populations."
> —— Introduction, p. vii

结构定位：第 6.1 节 "Causal diagrams"；6.2 "Causal diagrams and marginal independence"；6.3 "Causal diagrams and conditional independence"；6.6 "The structure of effect modification"；第 7.3 节 "Confounding and the backdoor criterion"。

## I — 自述

因果图（DAG）是一台**把假设外置的机器**。节点是变量，箭头是直接因果效应，缺一条箭头就是一个"不存在直接效应"的断言。图一旦画定，哪些变量边际独立、哪些在条件于某集合后独立，都由 d-分离机械地给出——不再靠直觉争论。

识别因果效应时，我们关心的是**后门路径**：从治疗到结局、但箭头是从治疗"倒着"进入的那些非因果路径。后门准则说：找一个协变量集合 L，使得（1）L 阻断所有后门路径，（2）L 中不含治疗的后代。满足这两条，以 L 分层即可识别效应。关键在于：调整集合由**图的结构**决定，不由"这个变量显著不显著"决定。

## A1 — 书中案例

- **第 6.5 节 "A structural classification of bias"**：作者用同一套图语言把混杂、选择偏倚、测量偏倚统一归类——它们只是**路径结构不同**，而不是三个互不相干的术语。
- **第 7.4 节 "Confounding and confounders"**：书里刻意区分"混杂"（一个现象）与"混杂因子"（一个变量），指出脱离图去争论"X 是不是混杂因子"往往没有答案。
- **第 9.5 节**：作者指出大量已发表的因果图里画进了非因果箭头，并专辟一节讨论"这要不要紧"。

## A2 — 未来触发

场景：
1. 用户问"我该调整哪些变量 / 控制哪些混杂"。
2. 用户想把自己的研究假设画成图。
3. 用户怀疑某个变量是对撞节点（collider），担心"调整反而引入偏倚"。
4. 用户报告"加了某个变量后效应值变了，不知道该信哪个"。

语言信号：DAG / 因果图 / directed acyclic graph / backdoor / 后门 / d-separation / collider / 对撞 / 混杂因子 / 调整集合 / adjustment set。

与相邻能力区分：本能力管**从图到调整集合**这一步。若用户问的是"这属于哪一类偏倚"，走偏倚结构化分类；若问"要不要用数据驱动选变量"，走因果变量选择；若治疗随时间变化，走时变 G 方法。

## E — 执行步骤

1. 列出所有相关变量（治疗 A、结局 Y，以及所有可能影响二者的变量）。完成标准：变量名清单写全，不漏已知的 common cause。
2. 画箭头，只画**直接**因果效应。完成标准：每一条箭头都能说出"若干预上游，下游会变"。
3. 检查有无环；有环则回到第 2 步（DAG 必须无环）。
4. 枚举 A 到 Y 的所有路径，标出哪些是后门路径（存在指向 A 的箭头）。
5. 用后门准则挑调整集合 L：阻断全部后门路径，且 L 不含 A 的后代。完成标准：能逐条说明每条后门路径被 L 中的哪个节点阻断。
6. **反向检查**：确认 L 中没有对撞节点、没有纯工具变量。条件于对撞节点会打开路径，条件于强工具变量会放大偏倚与方差。
7. 记录图本身作为分析的公开假设——图变了，结论就得重算。

## B — 边界

- **图不是从数据里学出来的。** 常规因果发现算法在观测数据上并不可靠；图来自领域知识，数据只用来检验其蕴含的独立性。
- **不要条件于对撞节点。** 这是最反直觉也最常见的错误：调整一个"看起来很像混杂"的 collider 会凭空造出关联。
- **不要条件于中介。** 若问题问的是总效应，调整中介会切断真实路径。
- **图里可能画了非因果箭头（第 9.5 节）**，此时后门准则的结论要谨慎。
- DAG 不表达**效应的大小与尺度**，只表达谁影响谁。

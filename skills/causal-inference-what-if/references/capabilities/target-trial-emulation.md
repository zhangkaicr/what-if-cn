<!-- capability_id: cap.what-if.target-trial-emulation | revision: 1 | status: active -->
<!-- 来源: Causal Inference: What If (Hernan & Robins, 2020) / 导言 p.vii；第 3.6 节 The target trial；第 22 章目标试验模拟（22.1-22.5） -->

## R — 原文

> "In this book, we stress the need to take the causal question seriously enough to articulate it, and to delineate the separate roles of data and assumptions for causal inference."
> —— Introduction, p. vii

> "causal inference cannot be reduced to a collection of recipes for data analysis."
> —— Introduction, p. vii

结构定位：第 3.6 节标题为 "The target trial"；第 22.5 节标题为 "A unified approach to answer What If questions with data"。

## I — 自述

观察性数据分析出错，极少是因为模型选错了，多半是因为**没人把要回答的那个问题写下来**。目标试验框架要求：在碰数据之前，先把你想做但做不了的那个随机试验的完整方案写出来。方案定型后，"数据 + 假设"各自承担什么角色就分开了——随机化那一步由假设（条件可交换性）顶替，其余部分照旧。

方案七件套：① 入组标准；② 治疗策略（含参照策略）；③ 治疗分配机制；④ 时间零点（随访起点）；⑤ 随访终点；⑥ 结局；⑦ 感兴趣的因果对比（ITT 还是 per-protocol）。第 ⑧ 项分析计划才轮到估计方法。

## A1 — 书中案例

- **心衰患者心脏移植（Introduction, p. vii）**：书开篇就示范什么叫"把问题说清楚"——要估的是"若在严重心衰患者中做心脏移植 vs 不做，死亡风险各是多少"。这是关于**干预**的问题，不是关于"移植者与未移植者"的关联。
- **第 22.1 节 ITT 与 per-protocol**：同一个目标试验可以定义两种不同的因果对比——ITT 对比"被分配到某策略"，per-protocol 对比"始终遵循某策略"。两者回答不同的决策问题；把它们混为一谈是真实世界研究中"结论互相打架"的头号来源。

## A2 — 未来触发

场景：
1. 用户拿着回顾性队列/电子病历数据问"A 治疗能不能降低 B 风险"。
2. 用户在纠结"入组时间怎么算""随访从哪一刻开始"。
3. 用户问 ITT 和 per-protocol 该报哪个。
4. 用户想做真实世界研究，但还没写方案就开始挑模型。

语言信号（中英）：目标试验 / target trial / 真实世界证据 / RWE / 因果问题怎么定义 / time zero / eligibility / ITT vs per-protocol / 研究设计能不能回答这个问题。

与相邻能力区分：本能力只管**问题的定义**。方案定好之后选估计方法 → IP 加权或 g-formula；若治疗随时间变化且受既往治疗影响 → 时变 G 方法；若怀疑时间零点没对齐 → 选择偏倚与永恒时间偏倚。

## E — 执行步骤

1. 写入组标准（谁、何时、满足什么条件可入组）。完成标准：能翻译成一条可执行的数据库筛选条件。
2. 写出各治疗策略，**每个策略必须是现实中可实施的干预**，并明确写出参照策略（如"全程不治疗"）。
3. 写出治疗分配机制。试验里是随机化；观察性数据里只能写成"假定在 L 分层内等价于随机化"。
4. 定义时间零点。**入组、治疗分配、随访开始三者必须落在同一时刻**。完成标准：写下来三个时间点是同一个。
5. 定义随访终点与结局测量方式。
6. 选定因果对比：ITT（按分配）还是 per-protocol（按实际遵循）。
7. 写分析计划，估计第 6 步选定的那一个对比——此刻才进入 IP 加权 / g-formula / G-estimation。

判停点：若第 2 步写不出可实施的干预动作，说明这不是一个因果效应问题。停下来，回到临床或政策问题本身重新表述，不要硬套估计方法。

## B — 边界

- **干预定义不清时不要用。** "多运动""吃得健康"不是单一干预；书里反复强调 well-defined intervention 是因果效应的前提。
- **纯预测问题不要用。** "谁会发病"不问干预，走预测建模而非因果推断。
- **时间零点无法对齐时，套用本框架仍会残留永恒时间偏倚。** 此时必须并读"选择偏倚与永恒时间偏倚"。
- **别把方案当免责声明。** 写全七件套不等于假设成立；方案只让假设无处可藏。
- 书里明确："This is not a philosophy book."（Introduction）——本框架不问"因果的本质是什么"，只问"这个数值能不能被数据识别"。

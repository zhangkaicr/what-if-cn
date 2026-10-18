<!-- capability_id: cap.what-if.effect-modification-interaction | revision: 1 | status: active -->
<!-- 来源: Causal Inference: What If (Hernan & Robins, 2020) / 第 4 章 Effect modification（4.1-4.6）；第 5 章 Interaction（5.1-5.6）：5.1 交互需要联合干预；5.3 反事实反应类型与交互；5.4 充分原因；5.5 充分原因交互；第 6.6 节 The structure of effect modification -->

## R — 原文

结构定位：第 4.1 节 "Heterogeneity of treatment effects"；4.2 "Stratification to identify effect modification"；4.3 "Why care about effect modification"；4.6 "Effect modification and adjustment methods"；第 5.1 节 "Interaction requires a joint intervention"；5.4 "Sufficient causes"；5.5 "Sufficient cause interaction"；5.6 "Counterfactuals or sufficient-component causes?"；第 6.6 节 "The structure of effect modification"。

## I — 自述

这两个词在论文里经常被当成同义词，但在本书里它们是两件事：

**效应修饰（effect modification）**：治疗效应**随某个变量 V 的取值而变化**。它是一个描述性的陈述，且**依赖你用哪个尺度**——在风险差上没有修饰，在风险比上可能有；反过来也一样。所以"有没有效应修饰"这个问题必须带上尺度才有意义。它不是在说 V 和治疗"一起起了作用"。

**交互（interaction）**：真正的因果交互要求**两个干预能被联合施加**。只有当"同时给予 A 和 B"这件事是一个可执行的操作时，才谈得上 A 与 B 的交互（第 5.1 节）。这跟"把样本按 B 分层、看 A 的效应在两层里是否不同"是完全不同的两件事。

后果很实际：**分层观察到效应差异 ≠ 存在因果交互**。前者可能只是尺度效应，或者只是 V 与 A 的边际分布不同。

## A1 — 书中案例

- **第 5.1 节 "Interaction requires a joint intervention"**：作者用一个直白的例子说明，很多被称作"基因-环境交互"的量根本不是交互，因为"同时干预基因和环境"不是一个可执行的操作。
- **第 5.3 节 "Counterfactual response types and interaction"**：用反事实反应类型刻画交互，说明交互与个体层面的"反应类型"分布有关。
- **第 5.4-5.5 节 充分原因**：引入充分组分原因模型，定义"充分原因交互"，并指出它与反事实交互**不是同一件事**（第 5.6 节）。
- **第 4.3 节 "Why care about effect modification"**：从决策角度说明，识别谁获益更大对个体化治疗很关键，但识别它的方法论门槛比想象中高。

## A2 — 未来触发

场景：
1. 用户做了亚组分析，问"这个亚组效应算不算真的"。
2. 用户问"基因和环境有没有交互"。
3. 用户报告"在风险差上没有交互，在比值比上有交互"，不知如何解读。
4. 用户要解释异质性治疗效果（HTE）。

语言信号：效应修饰 / effect modification / 交互 / interaction / 亚组分析 / subgroup / 异质性 / heterogeneity / HTE / 尺度依赖 / 相加交互 vs 相乘交互 / 充分原因交互。

与相邻能力区分：本能力管**解读**。若要估计分层效应，用标准化（其天然支持交互项）；若要做变量选择，走因果变量选择；若涉及高维 HTE 估计，需配合双重稳健机器学习估计量。

## E — 执行步骤

1. 先声明尺度：风险差还是风险比？效应修饰的结论只在声明的尺度上成立。
2. 用标准化框架估计各层效应（允许 A × V 交互项），而非只看分层后模型里的交互项 p 值。
3. 判断是**效应修饰**还是**因果交互**：V 是否可被干预？若不可（如基因型、性别），严格说只能谈效应修饰。
4. 若 V 可被干预且联合干预可执行，才可进一步讨论交互；明确用反事实框架还是充分原因框架（第 5.6 节，两者不等价）。
5. 报告时给出各层的效应估计与置信区间，不要只给交互项的 p 值。
6. 完成标准：能说清"我报告的是哪一个尺度上的、修饰还是交互"。

## B — 边界

- **不要用交互项的 p 值判断"有没有异质性"**——它同样受尺度与样本量影响，且不等于效应差异的大小。
- **多重比较问题**：亚组分析做得越多，假阳性越多；应预先声明亚组。
- **不可干预的变量（基因型、性别、种族）严格来说只谈效应修饰，不谈因果交互**（第 5.1 节）。
- **充分原因交互 ≠ 反事实交互**（第 5.6 节），引用时须指明框架。

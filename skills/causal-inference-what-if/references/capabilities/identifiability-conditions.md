<!-- capability_id: cap.what-if.identifiability-conditions | revision: 1 | status: active -->
<!-- 来源: Causal Inference: What If (Hernan & Robins, 2020) / 第 3.1 节 Identifiability conditions；3.2 Exchangeability；3.3 Positivity；3.4 Consistency: First, define the counterfactual outcome；3.5 Consistency: Second, link counterfactuals to the observed data；第 6.4 节 Positivity and consistency in causal diagrams -->

## R — 原文

结构定位：第 3.1 节 "Identifiability conditions"；3.2 "Exchangeability"；3.3 "Positivity"；3.4 "Consistency: First, define the counterfactual outcome"；3.5 "Consistency: Second, link counterfactuals to the observed data"；第 6.4 节 "Positivity and consistency in causal diagrams"。

> "In this book, we stress the need to take the causal question seriously enough to articulate it, and to delineate the separate roles of data and assumptions for causal inference."
> —— Introduction, p. vii

## I — 自述

观察性数据要能回答因果问题，需要三张门票，缺一张就进不去：

1. **可交换性（exchangeability）**：治疗组与未治疗组的潜在结局分布可以互换。换句话说，"谁接受了治疗"这件事本身不携带关于预后的额外信息（在已测混杂 L 分层内）。这是观察性研究里**无法用数据验证**的那一步——它就是我们要替随机化垫上的那个假设。
2. **正值性（positivity）**：在每一个由 L 定义的层里，接受各种治疗的概率都大于 0。若某类患者在现实中永远只接受一种治疗，那这类人的反事实在数据里根本不存在，无从比较。
3. **一致性（consistency）**：分两半。第一，干预必须**定义明确**——"减肥""加强锻炼"不是一个干预，因为实现方式不同会对应不同的潜在结局。第二，观测到的结局要等于该个体在其实际接受治疗下的潜在结局。

三者齐备，因果效应才被**识别**；至于用什么方法把它算出来，那是**估计**问题（第 10.1 节）。

## A1 — 书中案例

- **第 3.4 节用心脏移植说明"定义干预"**：若不说明是什么规格的移植、由谁做、在什么时机做，"心脏移植的效应"就没有单一答案——这就是一致性被违反时的样子。
- **第 3.3 节正值性**：作者指出，正值性违反时，估计量并非"有点偏"，而是根本不存在；实践中表现为按层分布重叠不足、权重爆炸。
- **第 6.4 节**：在因果图语言里重述正值性与一致性，说明这两个条件如何在 DAG 上读出。

## A2 — 未来触发

场景：
1. 用户要写研究的假设部分，不知道该交代什么。
2. 用户问"观察性研究凭什么能得到因果结论"。
3. 用户怀疑自己的数据里有某类患者几乎只接受一种治疗。
4. 用户问"识别和估计有什么不同"。

语言信号：可交换性 / exchangeability / 正值性 / positivity / 一致性 / consistency / 可识别性 / identifiability / 需要什么假设 / well-defined intervention。

与相邻能力区分：本能力是**入场检查**。条件满足后选方法 → IP 加权或标准化；要画图标出假设 → 因果图识别；要写清问题 → 目标试验模拟。

## E — 执行步骤

1. 明确写出干预是什么，检查是否为 well-defined intervention。
2. 检查可交换性：列出需要满足它的协变量 L（用因果图识别），并直言"这是假设，不是数据结论"。
3. 检查正值性：按 L 分层，看各层内各治疗水平的比例是否有接近 0 的。若有，标记该层的效应不可识别。
4. 检查一致性：确认"实际接受的治疗"能被映射到所定义的干预版本之一。
5. 三者齐备后再进入估计；否则退回目标试验模拟重新定义问题。
6. 完成标准：三条件逐条有明确结论（满足 / 不满足 / 无法判断），且不满足的那条有应对说明。

## B — 边界

- **可交换性无法用数据证明**，只能论证或做敏感性分析；声称"我检验了平衡所以可交换"是循环论证。
- **正值性是硬约束**，不是可以通过更多数据缓解的问题——结构性违反（如某类患者从不接受手术）需要重新定义目标人群。
- **不定义干预就谈效应，是本书点名批评的"草率因果推断"。**
- 本能力不涉及具体估计方法的选择。

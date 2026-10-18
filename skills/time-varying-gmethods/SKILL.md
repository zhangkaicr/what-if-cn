---
name: time-varying-gmethods
description: |
  当治疗随随访多次变更、且既往治疗会影响后续混杂因子（治疗-混杂反馈）时用。
  传统回归条件于时变混杂会同时阻断路径并引入对撞偏倚，必须用三类 G 方法：
  多期 g-formula、时变 IP 加权（MSM）、或结构嵌套模型的 G-estimation。
  触发信号：时变治疗 / time-varying treatment / 治疗混杂反馈 / treatment-confounder feedback / 纵向数据因果推断 / 顺序可交换性 / 传统回归为什么有偏 / 多期 g-formula。
  不适用于：治疗在时间零点一次性固定的研究（走 IP 加权或常规标准化）。
metadata:
  cangjie.generated-by: cangjie-tools v2.5.0
  cangjie.capability-id: cap.what-if.time-varying-gmethods
  cangjie.capability-revision: 1
  cangjie.bundle-id: bundle.causal-inference-what-if
  cangjie.source-title: Causal Inference - What If
  cangjie.tags: causal-inference, longitudinal, g-methods
---
<!-- capability_id: cap.what-if.time-varying-gmethods | revision: 1 | status: active -->
<!-- 来源: Causal Inference: What If (Hernan & Robins, 2020) / 第 19 章 Time-varying treatments（19.1-19.6）；第 20 章 Treatment-confounder feedback（20.1-20.5）；第 21 章 G-methods for time-varying treatments（21.1-21.6） -->

## R — 原文

结构定位：第 19.4 节 "Sequential exchangeability"；第 20.1 节 "The elements of treatment-confounder feedback"；20.2 "The bias of traditional methods"；20.3 "Why traditional methods fail"；20.4 "Why traditional methods cannot be fixed"；第 21 章 "G-methods for time-varying treatments"（21.1-21.6）。

## I — 自述

这是全书最难、也最反直觉的一段。

当治疗在多个时点反复决定，而**既往治疗又会改变日后的混杂因子**时（例如：治疗改善了某个指标，而这个指标同时是下一次要不要继续治疗的依据、也是结局的危险因素），我们就掉进了**治疗-混杂反馈**。

这时传统的"把时变混杂当协变量调整"会犯两重错：
- 它**阻断**了治疗经由该混杂到达结局的真实因果路径（过度调整，抹掉了部分总效应）；
- 同时该混杂又是既往治疗的后代，条件于它等于条件于一个**对撞节点**，凭空造出治疗与结局之间的虚假关联。

第 20.4 节把话说死了：传统方法**修不好**——不是调参或加交互项能解决的，是估计目标本身错了。正确做法是把 estimand 换成"**治疗策略**"（如"CD4 < 200 即启动治疗" vs "永不启动"），并用三类 G 方法之一估计：
- **多期 g-formula**（21.1）：逐期模拟。
- **时变 IP 加权**（21.2）：权重是各期条件概率的乘积。
- **G-estimation**（21.4）：直接对结构嵌套模型求解。

## A1 — 书中案例

- **第 20 章以 HIV 治疗与 CD4 计数为线索**：CD4 既是启动抗逆转录病毒治疗的依据，又受该治疗影响，同时预测结局——教科书式的治疗-混杂反馈。作者用它演示传统调整为何产生"治疗有害"的荒谬结论。
- **第 19.3 节 "Sequentially randomized experiments"**：作者先用"序贯随机试验"这个思想实验把识别条件讲清楚，再退化到观察性情形，这样假设落点一目了然。
- **第 21.5 节 "Censoring is a time-varying treatment"**：把删失完全当作一种时变处理来处理，用同一套 G 方法校正，这是本书非常漂亮的一次统一。
- **第 21.6 节 "The big g-formula"**：把所有期、所有变量一次性纳入模拟，展示 G 方法的完整形态。

## A2 — 未来触发

场景：
1. 用户的治疗在随访中多次变更，且疗效会影响下一次的治疗决定。
2. 用户发现纵向数据里"调整时变混杂后效应方向反了"。
3. 用户要比较的是**治疗策略**（动态方案）而非"某时刻是否用药"。
4. 用户要处理长期随访中的依从与失访。

语言信号：时变治疗 / time-varying treatment / 治疗混杂反馈 / treatment-confounder feedback / 纵向因果推断 / 顺序可交换性 / sequential exchangeability / g-methods / 动态治疗方案 / 多期 g-formula。

与相邻能力区分：若治疗在时间零点一次性固定 → 走常规 IP 加权或标准化。若问题只是时间零点没对齐 → 走选择偏倚与永恒时间偏倚（不过两者常常并存）。若用户已确定用时变框架，再看选哪一类 G 方法：标准化派 → 多期 g-formula；加权派 → 时变 IP 加权。

## E — 执行步骤

1. 把临床问题表述为**治疗策略**的对比，而不是"某一刻是否用药"。完成标准：每个策略能写成一条可执行的规则。
2. 画出含多期的 DAG，标出哪些变量是既往治疗的后代——这些就是时变混杂。
3. 检查**顺序可交换性**：在每个时点，给定既往治疗与混杂历史，当期治疗是否与潜在结局独立。
4. 检查每期的正值性。
5. 选择 G 方法：多期 g-formula（21.1）/ 时变 IP 加权（21.2）/ 双重稳健（21.3）/ G-estimation（21.4）。
6. 实施并诊断：加权看权重分布与平衡；g-formula 看是否有极端外推。
7. 完成标准：能说明"传统回归在这里错在哪"，以及所选 G 方法对应的是同一个治疗策略对比。

## B — 边界

- **不要试图用加交互项或分层来"修"传统回归**（第 20.4 节），这是估计目标错了。
- **顺序可交换性无法从数据检验**，它依赖未测混杂的假设，必须明示。
- **时变 IP 权重的方差会随期数指数恶化**，必须检查极端权重并考虑稳定化。
- **策略必须是可实施的**（第 19.2 节）："让所有人的 CD4 永远保持在 500 以上"这类策略在现实中不可执行，效应也就没有决策意义。
- 若只有基线一期数据，本能力不适用。

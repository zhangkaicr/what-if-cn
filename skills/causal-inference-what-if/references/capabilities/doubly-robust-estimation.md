<!-- capability_id: cap.what-if.doubly-robust-estimation | revision: 1 | status: active -->
<!-- 来源: Causal Inference: What If (Hernan & Robins, 2020) / 第 18.3 节 Causal inference and machine learning；18.4 Doubly robust machine learning estimators；第 21.3 节 A doubly robust estimator for time-varying treatments -->

## R — 原文

结构定位：第 18.3 节 "Causal inference and machine learning"；18.4 "Doubly robust machine learning estimators"；第 21.3 节 "A doubly robust estimator for time-varying treatments"。

## I — 自述

g-formula 的全部赌注压在**结局模型**上，IP 加权的全部赌注压在**治疗模型**上。双重稳健估计的思路是：两个都建，然后构造一个估计量，使得**只要其中一个是对的**，最终效应估计就是一致的。

构造上，它把标准化（结局回归的预测）和 IP 加权（治疗概率的倒数）组合起来，加权残差项起到"纠偏"的作用：结局模型错得越厉害，加权残差补得越多，反之亦然。

为什么它和机器学习特别搭？因为机器学习擅长预测但不给有效推断。若直接把 ML 预测塞进 g-formula，过拟合会污染估计量。双重稳健 + **交叉拟合（cross-fitting）**（用一部分数据拟合 nuisance 模型、另一部分评估）可以把这个污染压到可忽略，从而在大样本下恢复有效的置信区间。

## A1 — 书中案例

- **第 18.3 节**：作者区分"用机器学习做预测"与"用机器学习做因果推断"，指出后者关心的不是预测精度，而是 nuisance 参数的一致性与推断的有效性。
- **第 18.4 节**：给出双重稳健机器学习估计量，并说明它为何允许对治疗模型和结局模型都使用灵活的学习器。
- **第 21.3 节**：给出时变处理下的双重稳健估计量，把这一思路推广到纵向 G 方法的框架里。

## A2 — 未来触发

场景：
1. 用户协变量维度很高（几十上百个），想用 LASSO/随机森林/梯度提升拟合 nuisance 模型。
2. 用户听说 TMLE / AIPTW / Double ML，想知道和本书方法的关系。
3. 用户担心"结局模型设定错了怎么办"。
4. 用户在时变处理场景下要双重稳健版本。

语言信号：双重稳健 / doubly robust / AIPTW / TMLE / 双重机器学习 / DML / double machine learning / cross-fitting / 因果推断 + 机器学习 / 高维因果推断。

与相邻能力区分：这是 IP 加权与标准化的**组合升级版**。若协变量少且模型设定有把握，直接用前者更简单；若只是要选变量，走因果变量选择。

## E — 执行步骤

1. 确定调整集合 L 与识别条件。
2. 拟合治疗模型 P(A=1|L)，得到倾向性评分。
3. 拟合结局模型 E[Y|A,L]，对 A=1 与 A=0 分别预测。
4. 用交叉拟合（如 K 折）：每一折用其余折拟合 nuisance 模型，再在本折上评估，避免过拟合污染。
5. 组装双重稳健估计量（标准化项 + 加权残差项）。
6. 用影响函数或 bootstrap 计算置信区间。
7. 完成标准：能说明"两个模型里哪一个我更有把握"，并检查倾向性评分是否远离 0 与 1。

## B — 边界

- **"双重稳健"不等于"两个都错也没事"。** 两个模型都错时，它通常比单一方法更糟。
- **倾向性评分接近 0 或 1 时，加权项会放大方差**，需检查并考虑截断。
- **机器学习给不出可解释的效应异质性**，除非配合专门的异质性估计方法。
- **交叉拟合不是可选项，是前提条件**——不做交叉拟合直接用 ML 预测会得到有效但严重偏倚的推断。

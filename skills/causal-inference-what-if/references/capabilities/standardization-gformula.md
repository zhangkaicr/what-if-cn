<!-- capability_id: cap.what-if.standardization-gformula | revision: 1 | status: active -->
<!-- 来源: Causal Inference: What If (Hernan & Robins, 2020) / 第 2.3 节 Standardization；第 13 章 Standardization and the parametric g-formula（13.1-13.5）；第 21.1 节 The g-formula for time-varying treatments -->

## R — 原文

结构定位：第 2.3 节 "Standardization"；第 13.1 节 "Standardization as an alternative to IP weighting"；13.2 "Estimating the mean outcome via modeling"；13.3 "Standardizing the mean outcome to the confounder distribution"；13.4 "IP weighting or standardization?"；第 21.1 节 "The g-formula for time-varying treatments"。

## I — 自述

标准化的思路极其朴素，朴素到常被误认为"只是又一个回归"：

1. 用数据拟合结局的条件均值 E[Y | A, L]——把治疗 A 和协变量 L 都放进去。
2. 对**每一个**个体，把这个模型当作一台模拟器：先令 A=1 预测一次，再令 A=0 预测一次。于是每个人有了两个潜在结局的预测值。
3. 对全人群分别对这两列预测值取平均，得到 E[Yᵃ⁺¹] 与 E[Yᵃ⁰]。
4. 两者相减（或相除），就是平均因果效应。

它和"直接读回归系数"的区别是决定性的：回归系数是**条件**效应，只有当模型没有交互项、且效应在所有人身上相同时才等于边际效应。标准化始终估计的是**边际**（人群平均）效应，因为它把两个反事实都铺到了同一个真实人群分布上。

参数 g-formula 就是把这个流程换成参数模型；推广到多期就是"big g-formula"（第 21.6 节）。

## A1 — 书中案例

- **第 2.3 节（Part I，无模型）**：作者在尚未引入任何模型时就先用标准化算出平均因果效应，以此说明**识别与估计是两件事**——识别靠假设，标准化只是把假设兑现成数字的一种算法。
- **第 13.4 节 "IP weighting or standardization?"**：作者正面比较两条路径，指出两者都依赖同样的三个识别条件，差别在于你把模型建在**治疗机制**上还是**结局机制**上。
- **第 13.5 节 "How seriously do we take our estimates?"**：紧接着讨论模型依赖带来的不确定性，提醒标准化把全部赌注压在结局模型的正确设定上。

## A2 — 未来触发

场景：
1. 用户要估计人群平均因果效应，而不是条件效应。
2. 用户在 IP 加权与标准化之间犹豫。
3. 用户的结局模型已经建好了，想把它转成因果估计。
4. 用户问"回归系数为什么不能直接当效应"。

语言信号：标准化 / standardization / g-formula / 参数 g-formula / 结局回归 / outcome regression / 平均因果效应 / 边际效应 vs 条件效应 / noncollapsibility。

与相邻能力区分：标准化把模型建在**结局**上；IP 加权把模型建在**治疗**上。若治疗随时间变化，两者都要升级为第 21 章的多期版本。若想两者兼得，走双重稳健估计。

## E — 执行步骤

1. 确认识别条件成立（可交换性、正值性、一致性），并确定调整集合 L。
2. 拟合结局模型 E[Y | A, L]。**允许包含 A × L 交互项**——这正是标准化能容纳效应异质性的原因。
3. 复制数据集两次：一份全部令 A=1，一份全部令 A=0（L 保持原值不动）。
4. 用第 2 步的模型分别预测两份数据，得到 Ŷ¹ 与 Ŷ⁰。
5. 对 Ŷ¹ 与 Ŷ⁰ 各求均值，相减（或取比值）得效应估计。
6. 置信区间用 bootstrap 或非参数方法；不要用普通回归输出的标准误。
7. 完成标准：能说明"我把两个反事实都铺在了同一个 L 分布上"。

## B — 边界

- **外推风险。** 若某些 L 组合下几乎没人接受 A=1（正值性接近违反），第 3 步的预测就是模型在外推，结果不可信。务必先检查按层分布。
- **全部赌注压在结局模型上。** 第 13.5 节明确指出，g-formula 的正确性完全依赖结局模型设定正确。
- **不要直接读回归系数当边际效应**，尤其在有交互项或非碰撞性（noncollapsibility）的尺度（如比值比、风险比）上。
- **时变情形不能简单套用单期版本**——若 L 是治疗的后代，标准回归会引入偏倚，须走第 21.1 节的多期 g-formula。

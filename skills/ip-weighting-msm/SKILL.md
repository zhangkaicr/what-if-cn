---
name: ip-weighting-msm
description: |
  当用户要用逆概率加权估计因果效应、拟合边际结构模型、或遇到权重诊断问题时用。
  IP 加权给每个个体一个权重，使加权人群中治疗与已测混杂独立，再用加权回归估计边际效应；
  稳定化权重可显著降低方差。
  触发信号：IPTW / IP 加权 / 倾向性评分加权 / 边际结构模型 / MSM / 稳定化权重 / 权重太大怎么办 / 权重分布怎么检查 / 删失用加权校正。
  不适用于：倾向于建结局模型的场景（走标准化）、时变混杂反馈（需先走时变 G 方法）、
  以及未测混杂（加权无能为力）。
metadata:
  cangjie.generated-by: cangjie-tools v2.5.0
  cangjie.capability-id: cap.what-if.ip-weighting-msm
  cangjie.capability-revision: 1
  cangjie.bundle-id: bundle.causal-inference-what-if
  cangjie.source-title: Causal Inference - What If
  cangjie.tags: causal-inference, estimation, weighting
---
<!-- capability_id: cap.what-if.ip-weighting-msm | revision: 1 | status: active -->
<!-- 来源: Causal Inference: What If (Hernan & Robins, 2020) / 第 2.4 节 Inverse probability weighting；第 12 章 IP weighting and marginal structural models（12.1-12.6）；第 17.4 节 IP weighting of marginal structural models；第 21.2 节 IP weighting for time-varying treatments -->

## R — 原文

结构定位：第 2.4 节 "Inverse probability weighting"；第 12.2 节 "Estimating IP weights via modeling"；12.3 "Stabilized IP weights"；12.4 "Marginal structural models"；12.5 "Effect modification and marginal structural models"；12.6 "Censoring and missing data"。

## I — 自述

IP 加权不做模型外推，它做的是**重新造人**。

思路：在原始人群里，接受治疗 A=1 的概率依赖混杂 L，所以"用药的人"和"不用药的人"本来就不可比。给每个人加一个权重：接受 A=1 者权重 1/P(A=1|L)，接受 A=0 者权重 1/P(A=0|L)。加权之后，在每一个 L 层内，治疗组与对照组的**人数被放大回原层的规模**，于是 L 的分布在整个治疗组与整个对照组之间变得一样——混杂被"配平"了。

在这个伪人群里，直接比较两组的加权结局均值即可识别边际因果效应。

两个实用要点：
- **稳定化权重**把分子换成 P(A|L 的某个边缘分布)，不改变一致性但显著降低方差（第 12.3 节）。
- **边际结构模型（MSM）**让我们能在加权人群里直接对"治疗作为自变量"建模，从而估计边际效应、并处理效应修饰（第 12.4-12.5 节）。

## A1 — 书中案例

- **第 12 章全程以戒烟对体重增加的影响（NHEFS 数据）为线索**：从"因果问题"（12.1）出发，建权重模型（12.2），算稳定化权重（12.3），拟合 MSM（12.4），再处理效应修饰（12.5）与删失（12.6）。
- **第 12.6 节 "Censoring and missing data"**：把逆概率加权的思想直接搬到删失与缺失上——对"未被删失"这件事再乘一层权重，这是 IPCW 的雏形。
- **第 17.4 节**：推广到生存结局，用 IP 加权拟合边际结构模型来处理删失下的风险与生存函数。
- **第 21.2 节**：推广到时变处理，权重变成逐期累积的乘积。

## A2 — 未来触发

场景：
1. 用户想用倾向性评分/逆概率加权估计效应。
2. 用户要拟合边际结构模型（尤其是时变或生存结局）。
3. 用户发现权重极大、方差爆炸，需要诊断。
4. 用户要用加权处理删失或缺失数据。

语言信号：IPTW / IP 加权 / 倾向性评分加权 / 边际结构模型 / MSM / stabilized weights / 权重太大 / weight truncation / 权重分布 / IPCW。

与相邻能力区分：IP 加权把模型建在**治疗机制**上，标准化建在**结局机制**上。若治疗随时间变化且受既往治疗影响，必须用第 21.2 节的时变版本，不能直接套单期权重。若想两个模型都建并取其一正确即可，走双重稳健估计。

## E — 执行步骤

1. 确定调整集合 L（用因果图识别），确认可交换性与正值性。
2. 拟合治疗模型 P(A=1|L)（常用 logistic 回归）。
3. 计算权重：未稳定化 1/P(A|L)；**推荐稳定化** P(A)/P(A|L)（第 12.3 节）。
4. **诊断权重**：看均值（应接近 1）、看最大值、看分布。若出现极端权重 → 回到第 2 步检查正值性与模型设定，必要时做权重截断并说明代价。
5. 检查加权后 L 在各治疗组间的平衡（标准化差异）。
6. 拟合边际结构模型：以 A 为自变量做**加权**回归，估计边际效应。
7. 标准误用**稳健（三明治）方差**——加权后观测不再独立。
8. 完成标准：权重均值接近 1、协变量平衡、且能说明标准误为何必须用稳健估计。

## B — 边界

- **权重爆炸是正值性接近违反的信号，不是技术问题。** 截断权重能救方差，但换来了偏倚，必须说明。
- **必须用稳健标准误。** 用普通标准误会严重低估不确定性（第 12 章反复强调）。
- **未测混杂加权救不了。** IP 加权只处理已测量并纳入 L 的混杂。
- **时变情形下，单期权重会因治疗-混杂反馈而偏倚**（第 20 章），须用时变版本。
- 加权后的伪人群不再是真实人群，其"样本量"不能直接照搬解释。

---
name: causal-inference-what-if
description: |
  全书 14 个能力的统一入口，含未晋级能力卡与索引。
metadata:
  cangjie.generated-by: cangjie-tools v2.5.0
  cangjie.variant: router
  cangjie.bundle-id: bundle.causal-inference-what-if
  cangjie.capability-count: 14
  cangjie.entrypoint-count: 8
---
# Causal Inference - What If — 来源路由入口（compact pack）

## 触发与不触发

**适用**：与本书能力域相关的咨询与任务（见下方路由表的意图列）。
**不适用**：
- 纯预测 / 预后建模（不问干预效应）
- 统计软件操作、代码调试与包用法教学
- 与因果推断无关的通用数据清洗与可视化
- 哲学层面的因果本体论讨论（本书明确声明不做）
- 本书未覆盖的主题：干扰（interference / spillover）、贝叶斯因果推断、网络实验设计

## 核心原则（常驻速览，概览类问题读到这里即可回答）

1. 识别先于估计：先问「在给定假设下这个效应能否被数据唯一确定」，再问用什么方法把它算出来。
2. 干预必须定义明确：说不出可执行操作的「效应」没有单一答案，一致性条件首先就过不了。
3. 按因果图的结构认偏倚，不按名字认偏倚：共同原因是混杂，条件于共同结果是选择偏倚，变量测错是测量偏倚。
4. 目标试验先行：拿到观察性数据先写清 eligibility、治疗策略、时间零点、结局与因果对比，再选估计方法。
5. 同一个 estimand 有多条算法路径：g-formula 建在结局上，IP 加权建在治疗上，G-estimation 建在效应上。
6. 治疗一旦随时间变化并改变自身的混杂因子，传统回归无论怎么调整都有偏，只能用 G 方法。
7. 效应修饰依赖尺度，交互要求干预可被联合施加——两者不是一回事。

## 能力路由（先读本表，按意图加载 1 张能力卡）

| 用户意图 | 先读 | 补读/备注 |
|---|---|---|
| 用真实世界数据估计某个治疗/暴露的因果效应；判断一个回顾性分析能不能回答所提的因果问题；厘清 ITT 效应与 per-protocol（依从方案）效应的区别；确定队列研究的时间零点与入组标准 | references/capabilities/target-trial-emulation.md | 已晋级为独立 Skill `target-trial-emulation`（已安装时优先直接使用；本卡仅作原文与背景补充） |
| 画出某个研究问题的因果图（DAG）；判断该调整哪些变量、不该调整哪些；用后门准则找出可识别的调整集合；判断某变量是混杂因子、中介还是对撞节点 | references/capabilities/causal-dag-identification.md | 已晋级为独立 Skill `causal-dag-identification`（已安装时优先直接使用；本卡仅作原文与背景补充） |
| 判断一个观察到的偏倚属于混杂、选择偏倚还是测量偏倚；用一个统一的框架梳理研究中所有可能的偏倚来源；判断某偏倚能否用已有数据校正 | references/capabilities/bias-structure-diagnosis.md | 已晋级为独立 Skill `bias-structure-diagnosis`（已安装时优先直接使用；本卡仅作原文与背景补充） |
| 识别并改正永恒时间偏倚（immortal time bias）；判断研究中是否存在因条件于未来事件而产生的选择偏倚；为生存/随访研究确定正确的时间零点；处理删失与失访带来的选择偏倚 | references/capabilities/selection-bias-immortal-time.md | 已晋级为独立 Skill `selection-bias-immortal-time`（已安装时优先直接使用；本卡仅作原文与背景补充） |
| 用标准化（standardization）估计平均因果效应；用参数 g-formula 估计治疗效应；比较 IP 加权与标准化的取舍；估计时变处理的 g-formula | references/capabilities/standardization-gformula.md | 已晋级为独立 Skill `standardization-gformula`（已安装时优先直接使用；本卡仅作原文与背景补充） |
| 用逆概率加权（IPTW）估计平均因果效应；拟合边际结构模型（MSM）；计算并诊断稳定化权重；用 IP 加权处理删失与缺失数据 | references/capabilities/ip-weighting-msm.md | 已晋级为独立 Skill `ip-weighting-msm`（已安装时优先直接使用；本卡仅作原文与背景补充） |
| 估计随时间变化的治疗策略的效应；处理治疗-混杂反馈（treatment-confounder feedback）；判断传统回归在纵向数据中为何失效；用多期 g-formula / 时变 IP 加权 / G-estimation 分析纵向数据 | references/capabilities/time-varying-gmethods.md | 已晋级为独立 Skill `time-varying-gmethods`（已安装时优先直接使用；本卡仅作原文与背景补充） |
| 检查某个观察性研究是否满足可识别性条件；理解并解释可交换性、正值性、一致性；判断干预是否被明确定义（well-defined intervention）；区分识别问题与估计问题 | references/capabilities/identifiability-conditions.md | references/capabilities/causal-dag-identification.md、references/capabilities/target-trial-emulation.md、references/capabilities/bias-structure-diagnosis.md |
| 用 G-estimation 估计结构嵌套均值模型（SNMM）；理解 G-estimation 相对 IP 加权与 g-formula 的定位；判断秩保持（rank preservation）假设是否可接受 | references/capabilities/g-estimation-snm.md | references/capabilities/time-varying-gmethods.md、references/capabilities/ip-weighting-msm.md、references/capabilities/standardization-gformula.md |
| 用双重稳健估计量（AIPTW/TMLE 类）估计因果效应；在高维数据或机器学习 nuisance 模型下估计因果效应；理解双重稳健性的含义与代价 | references/capabilities/doubly-robust-estimation.md | references/capabilities/ip-weighting-msm.md、references/capabilities/standardization-gformula.md、references/capabilities/variable-selection-causal.md |
| 用工具变量估计因果效应；检查某个变量能否作为工具变量；理解 IV 的四个识别条件与 LATE 的含义；比较工具变量与其他方法的取舍 | references/capabilities/instrumental-variable.md | references/capabilities/identifiability-conditions.md、references/capabilities/ip-weighting-msm.md、references/capabilities/standardization-gformula.md |
| 判断某变量是否是效应修饰因子；区分效应修饰（effect modification）与交互（interaction）；正确解读亚组分析与分层结果；理解充分原因交互与反事实交互的区别 | references/capabilities/effect-modification-interaction.md | references/capabilities/causal-dag-identification.md、references/capabilities/standardization-gformula.md、references/capabilities/variable-selection-causal.md |
| 正确地做因果中介分析；区分总效应、直接效应与间接效应；判断某变量能否作为中介被干预；理解传统中介分析方法受批评的原因 | references/capabilities/causal-mediation.md | references/capabilities/causal-dag-identification.md、references/capabilities/identifiability-conditions.md、references/capabilities/effect-modification-interaction.md |
| 为因果分析选择要调整的协变量；判断某个变量该不该纳入调整集合；理解为什么数据驱动的变量选择会伤害因果估计；区分预测建模与因果推断的变量选择标准 | references/capabilities/variable-selection-causal.md | references/capabilities/causal-dag-identification.md、references/capabilities/bias-structure-diagnosis.md、references/capabilities/doubly-robust-estimation.md |

**非能力类查询**：
- 书名/作者/章节/整书概览 → references/overview.md
- 术语解释 → references/glossary.md
- 决策规则速查（不需要原文依据时） → references/cheatsheet.md
- 完整意图与关键词索引（本表未覆盖的意图先查这里） → references/capability-index.md

## 加载规则

- 每次任务先读本文件，再按路由表加载 **1** 张能力卡；任务明确跨域时最多加载 2 张。
- 概览/书名类问题不加载能力卡，用「核心原则」与 overview.md 回答。
- 路由表与 capability-index.md 都无法命中的意图，明确告知超出本书范围，不要硬套。

## 边界与判停

- 干预写不出可执行的操作时停止估计，先回到问题定义（目标试验模拟）。
- 正值性结构性违反（某类患者从不接受某种治疗）时，该亚群的效应不可识别，不要硬估。
- 可交换性无法论证时应转向敏感性分析或工具变量，并明确报告未测混杂的存在。
- 路由表与能力索引都无法命中的意图，明确说明超出本书范围，不要硬套某张能力卡。

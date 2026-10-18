# GLOSSARY — Causal Inference: What If 术语词典

> 阶段 3 产出。全书共享术语，供各能力卡引用时保持一致。

## 反事实与效应

| 术语 | 英文 | 释义 |
|---|---|---|
| 潜在结局 / 反事实结局 | potential / counterfactual outcome | 个体若接受某治疗时会出现的结局，记为 Yᵃ。同一时刻只有一个可被观测。 |
| 个体因果效应 | individual causal effect | 同一个体在两种治疗下的潜在结局之差 Yᵃ⁺¹ − Yᵃ⁰。原则上不可观测。 |
| 平均因果效应 | average causal effect | 人群中潜在结局均值之差 E[Yᵃ⁺¹] − E[Yᵃ⁰]。这是本书的标准 estimand。 |
| 一致（可交换）性 | consistency | 观测结局等于该个体在实际接受治疗下的潜在结局；前提是干预已被明确定义。 |
| 干预定义明确 | well-defined intervention | 干预必须对应现实中可实施的具体操作。"减肥""多运动"不满足此要求。 |

## 识别条件

| 术语 | 英文 | 释义 |
|---|---|---|
| 可交换性 | exchangeability | 治疗组与未治疗组的潜在结局分布可互换。观察性研究中无法用数据验证。 |
| 条件可交换性 | conditional exchangeability | 在协变量 L 分层之内可交换。这是观察性研究要垫上的核心假设。 |
| 正值性 | positivity | 每个 L 层内接受各种治疗的概率都大于 0。违反时估计量根本不存在。 |
| 可识别性 | identifiability | 在给定的假设下，因果效应能否由观测数据的分布唯一确定。与"能否估准"是两件事。 |

## 因果图

| 术语 | 英文 | 释义 |
|---|---|---|
| 因果图 / DAG | causal diagram / directed acyclic graph | 节点为变量、箭头为直接因果效应的无环图，是假设的外置载体。 |
| 后门路径 | backdoor path | 从治疗到结局、但含有指向治疗的箭头的非因果路径。 |
| 后门准则 | backdoor criterion | 调整集合 L 需满足：阻断全部后门路径，且 L 不含治疗的后代。 |
| d-分离 | d-separation | 判断图中两个节点在给定某集合后是否（条件）独立的图算法。 |
| 对撞节点 | collider | 两个变量的共同结果。条件于它会**打开**一条原本关闭的路径，凭空造出关联。 |
| 混杂 vs 混杂因子 | confounding vs confounder | 前者是"存在未阻断的后门路径"这一**现象**；后者是造成该现象的那个变量。脱离图争论"X 是不是混杂因子"往往无解。 |
| 单世界干预图 | single-world intervention graph (SWIG) | 把干预拆分到图上的表示法，用于统一处理混杂与效应修饰。 |

## 估计方法

| 术语 | 英文 | 释义 |
|---|---|---|
| 标准化 | standardization | 拟合 E[Y\|A,L]，对每人分别预测 A=1 与 A=0 下的结局，再对全人群各求平均并相减。 |
| 参数 g-formula | parametric g-formula | 标准化的参数模型版本；多期推广即"big g-formula"。 |
| 逆概率加权 | inverse probability weighting (IPW/IPTW) | 给每个个体加权 1/P(A\|L)，造出治疗与混杂独立的伪人群。 |
| 稳定化权重 | stabilized weights | 分子换成 P(A) 的权重，不改一致性但显著降低方差。 |
| 边际结构模型 | marginal structural model (MSM) | 在加权人群中直接对治疗建模，估计**边际**效应并容纳效应修饰。 |
| G-estimation | G-estimation | 直接对效应建模；搜索使治疗与"扣除效应后的反事实"独立的参数值。 |
| 结构嵌套模型 | structural nested model (SNM/SNMM) | G-estimation 所用的效应模型，直接刻画"接受治疗者相对未接受者的均值差"。 |
| 秩保持 | rank preservation | 多参数 SNMM 常需的强假设：个体间潜在结局的排序在治疗下保持不变。 |
| 双重稳健 | doubly robust | 同时建结局模型与治疗模型，只要其中一个正确设定，效应估计即一致。 |
| 交叉拟合 | cross-fitting | 用一部分数据拟合 nuisance 模型、另一部分评估，使机器学习方法保持有效推断。 |
| 工具变量 | instrumental variable (IV) | 满足三个条件（相关性、排除限制、独立性）外加第四条件（同质性或单调性）的变量。 |
| LATE | local average treatment effect | 单调性下 IV 所估计的量：依从者（compliers）的平均因果效应，是**局部**而非全人群效应。 |
| 逆概率删失加权 | IPCW | 对"未被删失"再乘一层权重，把删失当作一种处理来校正。 |

## 时变处理

| 术语 | 英文 | 释义 |
|---|---|---|
| 治疗策略 | treatment strategy | 一组随时间展开的、可实施的治疗规则。时变情形下的 estimand 是不同策略的对比。 |
| 顺序可交换性 | sequential exchangeability | 每个时点上，给定既往治疗与混杂历史，当期治疗与潜在结局独立。 |
| 治疗-混杂反馈 | treatment-confounder feedback | 既往治疗影响后续混杂因子，而该混杂又影响后续治疗与结局。此时传统回归不可修复。 |
| 序贯随机试验 | sequentially randomized experiment | 每个时点都做一次随机化的思想实验，用于阐明顺序可交换性。 |
| G 方法 | g-methods | 时变处理下的三类方法合称：多期 g-formula、时变 IP 加权、G-estimation。 |

## 目标试验

| 术语 | 英文 | 释义 |
|---|---|---|
| 目标试验 | target trial | 观察性数据分析所应当模拟的那个假想随机试验。 |
| 目标试验模拟 | target trial emulation | 用观察性数据按目标试验方案组织分析，使因果问题与假设都显式化。 |
| 时间零点 | time zero | 入组、治疗分配、随访开始三者必须对齐的那一时刻。错配即产生永恒时间偏倚。 |
| 永恒时间偏倚 | immortal time bias | 治疗组必须先存活/满足某条件才能被归为治疗，其"永生时间"被计入分母而造出的虚假优势。 |
| ITT 效应 | intention-to-treat effect | 按"被分配到某策略"对比的效应。 |
| per-protocol 效应 | per-protocol effect | 按"始终遵循某策略"对比的效应。与 ITT 回答不同的决策问题。 |

## 效应修饰与交互

| 术语 | 英文 | 释义 |
|---|---|---|
| 效应修饰 | effect modification | 效应大小随某变量变化。**依赖效应尺度**（风险差 vs 风险比），不必然是因果交互。 |
| 交互 | interaction | 真正的因果交互，要求两个干预可被**联合施加**。 |
| 充分原因 | sufficient cause | 充分组分原因模型中的基本单元：一组足以导致结局的条件组合。 |
| 充分原因交互 | sufficient cause interaction | 两个组分出现在同一个充分原因中。与反事实交互**不等价**。 |
| 尺度依赖 | scale dependence | 效应修饰的有无随所选尺度（差值 / 比值）而改变的性质。 |

## 偏倚

| 术语 | 英文 | 释义 |
|---|---|---|
| 混杂 | confounding | 治疗与结局共享共同原因，且该路径未被阻断。 |
| 选择偏倚 | selection bias | 条件于治疗与结局的共同结果（对撞节点或其后代）。删失与失访均属此类。 |
| 测量偏倚 | measurement bias | 变量测错，或测的是代理变量而非真正的节点。 |
| 偏倚的结构分类 | structural classification of bias | 按因果图的结构而非历史名称给偏倚定类。 |

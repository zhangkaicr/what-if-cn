# 《因果推断：What If》中文翻译 — 译者风格指南（译者必读）

目标：给中文读者一部**忠实、完整、读起来像人写的**译本。你负责把指定的章节源文本
（`_build/chNN.txt`，英文 pdftotext 提取）翻译成单个 HTML 页面，写入
`chapters/chNN.html`（导言写 `chapters/intro.html`）。

## 一、产出要求（硬性）

1. 以 `_tools/template.html` 为骨架，替换 `{{TITLE}}`、`{{PART_CN}}`、`{{PART_EN}}`、
   `{{SRC_REF}}` 占位符；在 `<!-- CONTENT-START -->` 与 `<!-- CONTENT-END -->` 之间写正文。
2. **覆盖全部小节**：按源文本的 `N.M 标题` 逐节翻译，节标题用
   `<h2 id="s-N-M">N.M 中文标题</h2>`。Fine Point 与 Technical Point 一律译出，分别用：
   - `<aside class="finepoint"><span class="box-label">精细辨析 N.M　英文小标题</span>…</aside>`
   - `<aside class="techpoint"><span class="box-label">技术要点 N.M　英文小标题</span>…</aside>`
   推导极长时可保留结论与关键步骤、压缩中间代数，但不得丢小节。
3. **图表必须嵌入**：源文本中出现的每个 `Figure N.M` / `Table N.M` 都要放图：
   `<figure class="fig"><img src="../figures/chNN--figure-N_M.png" alt="图 N.M">
   <figcaption><strong>图 N.M</strong> 图注译文。</figcaption></figure>`
   （表用 `table-N_M.png`，figcaption 写"表 N.M …"。）
   你那一章可用的图片文件清单已列在你的任务里，**只准引用清单里的文件名**。
4. **译注**：每章加 3–6 条译注，用
   `<aside class="tnote"><span class="box-label">译注</span>…</aside>`。
   内容任选：术语背景、英文双关、中国流行病学语境、后续章节伏笔、现实中
   （尤其中文文献/医保/临床研究）的例子。译注是你 added value 的主要体现，写具体的，别写空话。
5. 每章章首的故事性导语（斜体段落）译为 `<p class="ch-epigraph">…</p>`。
6. 数学式用 HTML/Unicode，不引外部库：`E[Y<sup>a=1</sup>]`、`Pr`、`⊥⊥`、`→`、`←`、
   `∑`、`≤`、`≈`。行内变量用 `<code>` 可读性更差时直接普通文本即可，别滥用 code。
7. 章内交叉引用保留（"见第 3 章"）；"see Fine Point 4.1"译"见本章精细辨析 4.1"。

## 二、文风（去 AI 味，同等硬性）

- **说人话**：翻译腔是大敌。"被证明是""作为一个……"式腔调不要。
  长句按中文习惯拆短；但术语定义句允许长而严密。
- 禁用这些词与套路："值得注意的是""总而言之""至关重要""深入探讨""彰显""
  赋能""画上了句号""不仅……更是……"三连排比、机械的"首先/其次/最后"。
- 破折号少用；每段别都用同一个节奏。术语首次出现给英文原文括注，后文直接用中文。
- 作者的口吻（Hernán 常有冷幽默、直接对读者说话）要留住，别写成八股。
  例如 "ready for a long name?" 这类插入语照译出味道："准备好听一个很长的名字了吗？"
- 人名保留英文（Rheia、Kronos、Zeus 等希腊神名不译，首次可括注"希腊神话人物，
  作者用他们当例子"）。NHEFS 等数据集名保留英文。

## 三、术语对照表（首次出现时括注英文，之后统一用中文）

| 英文 | 中文 |
|---|---|
| causal effect | 因果效应 |
| counterfactual / potential outcome | 反事实 / 潜在结局 |
| treatment / intervention | 处理（医学语境可译"治疗/干预"，全文以"处理"为主） |
| treatment strategy | 处理策略 |
| exchangeability | 可交换性 |
| positivity | 可阳性性 |
| consistency | 一致性 |
| confounding / confounder | 混杂 / 混杂因素 |
| selection bias | 选择偏倚 |
| measurement error / bias | 测量误差 / 测量偏倚 |
| effect modification | 效应修饰 |
| interaction | 交互作用 |
| causal DAG (directed acyclic graph) | 因果 DAG（有向无环图） |
| backdoor path / criterion | 后门路径 / 后门准则 |
| collider / mediator | 碰撞因子 / 中介变量 |
| instrumental variable | 工具变量 |
| propensity score | 倾向性评分 |
| IP (inverse probability) weighting | 逆概率加权 |
| standardization | 标准化 |
| g-formula / parametric g-formula | g 算法 / 参数化 g 算法 |
| marginal structural model | 边际结构模型 |
| structural nested model | 结构嵌套模型 |
| g-estimation | g 估计 |
| doubly robust | 双重稳健 |
| target trial (emulation) | 目标试验（模拟） |
| time-varying treatment | 时变处理 |
| treatment-confounder feedback | 处理-混杂反馈 |
| hazard / risk | 风率（hazard，也可保留"风险率"）/ 风险 |
| censoring | 删失 |
| rank preservation | 秩保持 |
| sufficient-component cause | 充分成分病因 |
| average causal effect (ACE) | 平均因果效应 |
| placebo / blind | 安慰剂 / 盲法 |
| randomized experiment | 随机化试验 |
| observational study | 观察性研究 |
| Fine Point / Technical Point | 精细辨析 / 技术要点 |

## 四、质量自检（写完必查）

- [ ] 全部小节都在，顺序同原书；
- [ ] 任务清单里每个图都嵌了且文件名一字不差；
- [ ] 占位符全部替换、无 `{{`；无 `<!--NAV-->` 以外的残留注释；
- [ ] HTML 合法（标签闭合），UTF-8；
- [ ] 抽读三段：有没有翻译腔/AI 腔。

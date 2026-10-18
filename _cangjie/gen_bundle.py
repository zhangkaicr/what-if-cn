# -*- coding: utf-8 -*-
"""生成《Causal Inference: What If》的 Capability Bundle（cangjie-skill v2.5）。

输入  : 无（能力内容由人工蒸馏，内嵌在本文件的 CAPS 中）
输出  : _cangjie/books/what-if/.cangjie/capabilities/
          verified.yaml        Capability Bundle（唯一编译事实源）
          destinations.json    晋级/路由去向映射
          cards/<slug>.md      RIA++ 能力卡（R/I/A1/A2/E/B）
          book/overview.md, book/glossary.md
"""
import json
import pathlib
import shutil

import yaml

ROOT = pathlib.Path(r"C:/WorkBuddy/what-if-cn/_cangjie/books/what-if")
BUNDLE = ROOT / ".cangjie" / "capabilities"
CARDS = BUNDLE / "cards"
BOOKDIR = BUNDLE / "book"

BOOK = {
    # 注意：title 会原样写入生成 SKILL.md 的 YAML frontmatter（cangjie.source-title）。
    # 值中不能出现 ": "（冒号 + 空格），否则 frontmatter 无法被 YAML 解析，编译硬门会失败。
    # 因此在 Bundle 元数据里用连字符；书名的原始写法见 BOOK_OVERVIEW.md 与各能力卡的来源标注。
    "title": "Causal Inference - What If",
    "authors": ["Miguel A. Hernan", "James M. Robins"],
    "year": 2020,
    "slug": "what-if",
    "source_id": "src-main-book",
    "original_language": "en",
}

CAPS = [
    # ---------------------------------------------------------------- 1
    {
        "slug": "target-trial-emulation",
        "title": "目标试验模拟：先写试验方案，再碰数据",
        "importance": "critical",
        "importance_rationale": "第 3.6 节与第 22 章是全书的方法论枢纽；作者自称本书围绕'把因果问题说清楚'展开，其余各章的估计方法都在方案定型之后才登场。",
        "one_liner": "拿到观察性数据先别建模，先把'我本来想做的那个随机试验'的 7 项方案写出来。",
        "intents": [
            "用真实世界数据估计某个治疗/暴露的因果效应",
            "判断一个回顾性分析能不能回答所提的因果问题",
            "厘清 ITT 效应与 per-protocol（依从方案）效应的区别",
            "确定队列研究的时间零点与入组标准",
        ],
        "keywords": ["目标试验", "target trial", "真实世界证据", "RWE", "ITT", "per-protocol", "time zero", "时间零点", "eligibility"],
        "also_read": ["cap.what-if.identifiability-conditions", "cap.what-if.selection-bias-immortal-time", "cap.what-if.ip-weighting-msm"],
        "destination": "promoted",
        "location": "导言 p.vii；第 3.6 节 The target trial；第 22 章目标试验模拟（22.1-22.5）",
        "tags": ["causal-inference", "study-design", "framework"],
        "description": (
            "当用户要用观察性/真实世界数据回答'X 对 Y 的因果效应'时，先把目标试验方案写实：\n"
            "eligibility、治疗策略、分配机制、时间零点、随访终点、结局、因果对比（ITT 或 per-protocol）、分析计划。\n"
            "触发信号：真实世界研究、回顾性队列、目标试验、target trial、时间零点怎么定、ITT 还是 per-protocol、"
            "这个研究设计能不能回答因果问题。\n"
            "不适用于：纯预测/预后问题（不问干预效果）、干预本身无法定义成可执行动作、"
            "以及只需选估计方法而方案已定的场景（那种情况直接走 IP 加权或 g-formula）。"
        ),
        "card": """
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
""",
    },
    # ---------------------------------------------------------------- 2
    {
        "slug": "causal-dag-identification",
        "title": "因果图识别与后门准则",
        "importance": "critical",
        "importance_rationale": "第 6、7 章是 Part I 的识别论核心，后门准则被第 7.3、7.6 节确立为混杂调整的操作标准，并被 Part II/III 所有估计方法默认依赖。",
        "one_liner": "把假设画成箭头，再用后门准则挑调整集合——调整不该靠'把所有变量都塞进模型'。",
        "intents": [
            "画出某个研究问题的因果图（DAG）",
            "判断该调整哪些变量、不该调整哪些",
            "用后门准则找出可识别的调整集合",
            "判断某变量是混杂因子、中介还是对撞节点",
        ],
        "keywords": ["DAG", "因果图", "directed acyclic graph", "backdoor criterion", "后门准则", "d-separation", "collider", "对撞节点", "confounder", "混杂"],
        "also_read": ["cap.what-if.bias-structure-diagnosis", "cap.what-if.variable-selection-causal", "cap.what-if.identifiability-conditions"],
        "destination": "promoted",
        "location": "第 6 章（6.1-6.6）；第 7.3 节 Confounding and the backdoor criterion；第 7.6 节 Confounding adjustment",
        "tags": ["causal-inference", "identification", "diagram"],
        "description": (
            "当用户需要画因果图、判断调整集合、或问'这个变量该不该放进模型'时用。\n"
            "以 d-分离判断边际/条件独立，用后门准则挑选足以阻断所有后门路径的协变量集合。\n"
            "触发信号：画 DAG / 因果图 / 混杂怎么调整 / backdoor / d-separation / collider / 对撞节点 / "
            "这个变量该不该调整 / 调整集合。\n"
            "不适用于：纯粹的变量筛选（走因果变量选择）、时间依赖的时变混杂（走时变 G 方法）、"
            "以及只想问'这是哪种偏倚'（走偏倚结构化分类）。"
        ),
        "card": """
## R — 原文

> "This is not a philosophy book. We remain largely agnostic about metaphysical concepts like causality and cause. Instead, we focus on the identification and estimation of causal effects in populations."
> —— Introduction, p. vii

结构定位：第 6.1 节 "Causal diagrams"；6.2 "Causal diagrams and marginal independence"；6.3 "Causal diagrams and conditional independence"；6.6 "The structure of effect modification"；第 7.3 节 "Confounding and the backdoor criterion"。

## I — 自述

因果图（DAG）是一台**把假设外置的机器**。节点是变量，箭头是直接因果效应，缺一条箭头就是一个"不存在直接效应"的断言。图一旦画定，哪些变量边际独立、哪些在条件于某集合后独立，都由 d-分离机械地给出——不再靠直觉争论。

识别因果效应时，我们关心的是**后门路径**：从治疗到结局、但箭头是从治疗"倒着"进入的那些非因果路径。后门准则说：找一个协变量集合 L，使得（1）L 阻断所有后门路径，（2）L 中不含治疗的后代。满足这两条，以 L 分层即可识别效应。关键在于：调整集合由**图的结构**决定，不由"这个变量显著不显著"决定。

## A1 — 书中案例

- **第 6.5 节 "A structural classification of bias"**：作者用同一套图语言把混杂、选择偏倚、测量偏倚统一归类——它们只是**路径结构不同**，而不是三个互不相干的术语。
- **第 7.4 节 "Confounding and confounders"**：书里刻意区分"混杂"（一个现象）与"混杂因子"（一个变量），指出脱离图去争论"X 是不是混杂因子"往往没有答案。
- **第 9.5 节**：作者指出大量已发表的因果图里画进了非因果箭头，并专辟一节讨论"这要不要紧"。

## A2 — 未来触发

场景：
1. 用户问"我该调整哪些变量 / 控制哪些混杂"。
2. 用户想把自己的研究假设画成图。
3. 用户怀疑某个变量是对撞节点（collider），担心"调整反而引入偏倚"。
4. 用户报告"加了某个变量后效应值变了，不知道该信哪个"。

语言信号：DAG / 因果图 / directed acyclic graph / backdoor / 后门 / d-separation / collider / 对撞 / 混杂因子 / 调整集合 / adjustment set。

与相邻能力区分：本能力管**从图到调整集合**这一步。若用户问的是"这属于哪一类偏倚"，走偏倚结构化分类；若问"要不要用数据驱动选变量"，走因果变量选择；若治疗随时间变化，走时变 G 方法。

## E — 执行步骤

1. 列出所有相关变量（治疗 A、结局 Y，以及所有可能影响二者的变量）。完成标准：变量名清单写全，不漏已知的 common cause。
2. 画箭头，只画**直接**因果效应。完成标准：每一条箭头都能说出"若干预上游，下游会变"。
3. 检查有无环；有环则回到第 2 步（DAG 必须无环）。
4. 枚举 A 到 Y 的所有路径，标出哪些是后门路径（存在指向 A 的箭头）。
5. 用后门准则挑调整集合 L：阻断全部后门路径，且 L 不含 A 的后代。完成标准：能逐条说明每条后门路径被 L 中的哪个节点阻断。
6. **反向检查**：确认 L 中没有对撞节点、没有纯工具变量。条件于对撞节点会打开路径，条件于强工具变量会放大偏倚与方差。
7. 记录图本身作为分析的公开假设——图变了，结论就得重算。

## B — 边界

- **图不是从数据里学出来的。** 常规因果发现算法在观测数据上并不可靠；图来自领域知识，数据只用来检验其蕴含的独立性。
- **不要条件于对撞节点。** 这是最反直觉也最常见的错误：调整一个"看起来很像混杂"的 collider 会凭空造出关联。
- **不要条件于中介。** 若问题问的是总效应，调整中介会切断真实路径。
- **图里可能画了非因果箭头（第 9.5 节）**，此时后门准则的结论要谨慎。
- DAG 不表达**效应的大小与尺度**，只表达谁影响谁。
""",
    },
    # ---------------------------------------------------------------- 3
    {
        "slug": "bias-structure-diagnosis",
        "title": "偏倚的结构化分类：按图的结构认偏倚，不按名字认偏倚",
        "importance": "critical",
        "importance_rationale": "第 6.5 节提出的分类是 Part I 后半段（第 7、8、9 章）的组织骨架，作者明确指出三类偏倚只是图结构不同。",
        "one_liner": "混杂 = 共同原因；选择偏倚 = 条件于共同结果；测量偏倚 = 变量测错了或测的是代理。",
        "intents": [
            "判断一个观察到的偏倚属于混杂、选择偏倚还是测量偏倚",
            "用一个统一的框架梳理研究中所有可能的偏倚来源",
            "判断某偏倚能否用已有数据校正",
        ],
        "keywords": ["偏倚", "bias", "混杂", "confounding", "选择偏倚", "selection bias", "测量偏倚", "measurement bias", "结构分类", "structural classification"],
        "also_read": ["cap.what-if.causal-dag-identification", "cap.what-if.selection-bias-immortal-time", "cap.what-if.variable-selection-causal"],
        "destination": "promoted",
        "location": "第 6.5 节 A structural classification of bias；第 7 章 Confounding；第 8 章 Selection bias；第 9 章 Measurement bias and 「Noncausal」 diagrams",
        "tags": ["causal-inference", "bias", "diagnosis"],
        "description": (
            "当用户问'这算混杂还是选择偏倚''这个偏倚能不能校正'时用。\n"
            "按因果图的结构给偏倚定类：共同原因 → 混杂；条件于共同结果（对撞节点）→ 选择偏倚；\n"
            "变量测错或用了代理 → 测量偏倚。定类之后才知道该调整什么、能不能调整。\n"
            "触发信号：这是哪种偏倚 / 混杂 vs 选择偏倚 / 能不能校正 / bias 分类 / collider 引入的偏倚。\n"
            "不适用于：只想找调整集合（走因果图识别）、已经确定是时间零点不对齐导致的永恒时间偏倚（走专项能力）、\n"
            "以及纯统计的随机误差问题（走识别与估计的区分）。"
        ),
        "card": """
## R — 原文

结构定位：第 6.5 节标题 "A structural classification of bias"；第 7 章 "Confounding"；第 8 章 "Selection bias"；第 9 章 "Measurement bias and 'Noncausal' diagrams"。

> "causal inference cannot be reduced to a collection of recipes for data analysis."
> —— Introduction, p. vii

## I — 自述

教科书里"偏倚"有几十个名字——回忆偏倚、检出偏倚、适应证偏倚、健康工人效应……这些名字是**历史遗留下来的标签**，不是分析工具。作者的提议是：忘掉名字，看图。

三类偏倚对应三种图结构：
- **混杂**：治疗与结局共享**共同原因**，且我们没处理它 → 存在开放的后门路径。
- **选择偏倚**：我们**条件于治疗与结局的共同结果**（对撞节点或其后代）。注意，它不要求真的"选了人"，只要分析中以某种方式做了条件化，包括删失、失访、只纳入住院者等。
- **测量偏倚**：变量测错了，或测的是一个代理而非真正的节点。

这个分类之所以有用，是因为**处理方式完全不同**：混杂通常可调整；选择偏倚要看能否重建选择机制（第 8.5 节）；测量偏倚往往无法用现有数据校正，只能做敏感性分析。

## A1 — 书中案例

- **第 8.2 节 "Examples of selection bias"**：作者用若干经典实例说明选择偏倚如何伪装成真实效应——很多"风险因素"其实只是进入了分析人群的门票。
- **第 8.4 节 "Selection bias and censoring"**：把删失明确归入选择偏倚的图结构，这正是 Part III 把"删失当作一种时变处理"（第 21.5 节）来处理的伏笔。
- **第 9.3 节 "Mismeasured confounders and colliders"**：测错的混杂因子和对撞节点会同时制造混杂与选择偏倚，单纯"调整"往往修不好。

## A2 — 未来触发

场景：
1. 用户报告一个可疑的效应估计，问"这可能是哪种偏倚"。
2. 用户要写研究的局限性（limitation）段落，需要系统地列举偏倚来源。
3. 用户问"这个偏倚能不能用统计方法校正，还是只能做敏感性分析"。
4. 团队里出现"我觉得这是回忆偏倚""不对，这是适应证偏倚"这类靠名字争论的对话。

语言信号：这是哪种偏倚 / 混杂还是选择偏倚 / 能不能校正 / selection bias / collider / 健康工人效应 / 检出偏倚 / 失访偏倚。

与相邻能力区分：本能力管**定类与分流**。定类之后需要具体处理 → 混杂交给因果图识别 + 标准化/IP 加权；选择偏倚交给选择偏倚与永恒时间偏倚；测量偏倚通常只能敏感性分析。

## E — 执行步骤

1. 画出研究者**实际所做的分析**的图，而不是理想研究的图——包括谁被纳入、谁被删失、测了什么。
2. 找出 A 与 Y 之间所有开放的非因果路径。
3. 逐条判断路径结构：是共同原因（混杂）、共同结果（选择偏倚），还是节点测错（测量偏倚）。
4. 对每一条标注**可否校正**：共同原因且已测量 → 可调整；共同结果 → 需重建选择机制；未测量或测错 → 只能敏感性分析或承认不可校正。
5. 输出一张偏倚清单，每条写明：路径、类型、可校正性、拟用方法。
6. 完成标准：清单上的每一条都能在图上指出对应的那条路径。

## B — 边界

- **不要只用名字下结论。** 同一个"检出偏倚"在不同研究里可能是选择偏倚也可能是混杂。
- **选择偏倚不只在"选人"时发生。** 分析中的任何条件化（含分层、删失、纳入标准）都可能触发。
- **测量偏倚常常无法用现有数据修复**；此时应做定量偏倚分析，而不是假装调整了就好。
- 本分类不覆盖**随机误差**（第 10 章）——那是识别与估计的区别，不是偏倚的类型。
""",
    },
    # ---------------------------------------------------------------- 4
    {
        "slug": "selection-bias-immortal-time",
        "title": "选择偏倚与永恒时间偏倚：时间零点一错，全盘皆错",
        "importance": "critical",
        "importance_rationale": "第 8 章专章讨论，第 22.4 节单列 'Time zero'；永恒时间偏倚是真实世界研究最高发、也最难自查的设计性错误，本书把它归入选择偏倚的图结构。",
        "one_liner": "入组、治疗分配、随访开始必须落在同一时刻；只要它们错开，就有人必须先活够一段时间才'配'被治疗。",
        "intents": [
            "识别并改正永恒时间偏倚（immortal time bias）",
            "判断研究中是否存在因条件于未来事件而产生的选择偏倚",
            "为生存/随访研究确定正确的时间零点",
            "处理删失与失访带来的选择偏倚",
        ],
        "keywords": ["永恒时间偏倚", "immortal time bias", "选择偏倚", "selection bias", "time zero", "时间零点", "删失", "censoring", "失访", "survivor bias"],
        "also_read": ["cap.what-if.target-trial-emulation", "cap.what-if.bias-structure-diagnosis", "cap.what-if.time-varying-gmethods"],
        "destination": "promoted",
        "location": "第 8 章（8.1-8.6）；第 8.4 节 Selection bias and censoring；第 22.4 节 Time zero；第 21.5 节 Censoring is a time-varying treatment",
        "tags": ["causal-inference", "bias", "survival-analysis", "study-design"],
        "description": (
            "当用户的研究存在'必须先存活/满足某条件才能进入治疗组'的结构，或入组与治疗开始不同步时用。\n"
            "永恒时间偏倚是选择偏倚的特例：条件于一个发生在治疗之后、又是结局共同结果的事件。\n"
            "触发信号：永恒时间偏倚 / immortal time bias / 时间零点 / time zero / 入组和用药不同步 / "
            "生存分析里的存活者偏倚 / 删失失访怎么校正。\n"
            "不适用于：治疗不随时间变化且时间零点已对齐的常规混杂问题（走因果图识别）、\n"
            "以及时变混杂反馈导致的偏倚（走时变 G 方法）。"
        ),
        "card": """
## R — 原文

结构定位：第 8.1 节 "The structure of selection bias"；第 8.4 节 "Selection bias and censoring"；第 8.5 节 "How to adjust for selection bias"；第 8.6 节 "Selection without bias"；第 22.4 节 "Time zero"。

## I — 自述

选择偏倚的图结构是：**条件于治疗与结局的共同结果**。永恒时间偏倚是它最阴险的一个特例，因为触发它的那个"条件"常常藏在研究设计里，而不是分析代码里。

典型结构：研究比较"用药者"与"未用药者"的死亡风险。但入组发生在时间 T0，用药发生在 T1 > T0，而且只有活到 T1 的人才可能用药。于是"用药"这个分组变量，隐含地以"活到 T1"为条件——而"活到 T1"正是治疗与死亡的共同结果。用药组在 [T0, T1] 这段区间内**不可能死亡**，这段"永生时间"被算进了用药组的分母，凭空造出生存优势。

修法不是换模型，而是**把时间零点对齐**：让入组、治疗分配、随访开始落在同一时刻，使每一组的随访风险从同一个起点开始计。做不到对齐时，就得把"治疗"重新定义为随时间变化的处理，用处理策略（如"立即启动" vs "永不启动"）来表述，并交给时变 G 方法。

## A1 — 书中案例

- **第 8.2 节 "Examples of selection bias"**：作者给出若干经典实例，说明"暴露组看起来更健康"往往只是因为他们必须先满足某个准入条件。
- **第 8.4 节 "Selection bias and censoring"**：把删失与失访统一到选择偏倚的图结构中，为 Part III 用 IP 加权处理删失铺路。
- **第 22.4 节 "Time zero"**：作者把时间零点单列一节，正是因为它是目标试验模拟中最容易做错、后果最严重的一个组件。
- **第 21.5 节 "Censoring is a time-varying treatment"**：把删失彻底当成一种时变处理来处理，用同一套 G 方法校正。

## A2 — 未来触发

场景：
1. 用户比较"用药 vs 不用药"，但两组的起点时间不同。
2. 用户的队列里，暴露组必须先存活或先满足某个条件才能被归为暴露。
3. 用户报告"药物效果出奇地好"，尤其是生存结局。
4. 用户在设计真实世界研究，需要确定 time zero。

语言信号：永恒时间偏倚 / immortal time bias / 时间零点 / time zero / 入组和用药不在同一天 / 存活者偏倚 / survivor bias / 删失 / 失访怎么校正。

与相邻能力区分：本能力专治**时间结构错配**导致的选择偏倚。若是一般性的"该调整哪些变量"，走因果图识别；若是治疗随时间变化且受既往治疗影响，走时变 G 方法；若只是要给偏倚定类，走偏倚结构化分类。

## E — 执行步骤

1. 写下三个时间点：入组（eligibility 判定）、治疗分配（策略开始）、随访开始。
2. **检查三者是否同一时刻。** 若不是，标记存在永恒时间偏倚风险。
3. 找出那个"必须先发生的事件"（如存活到用药日、完成某项检查、出院）。判断它是否是治疗与结局的共同结果。
4. 若是，把研究重述为**随时间变化的治疗策略**对比："立即启动" vs "全程不启动"，而不是"用药者 vs 未用药者"。
5. 用克隆-加权或目标试验模拟的方式对齐时间零点（第 22.3 节）。
6. 对删失与失访：按第 8.4 / 21.5 节，用逆概率删失加权（IPCW）处理，而非简单剔除。
7. 完成标准：重新分析后，每一组的随访风险都从同一个时间零点起算，且能说明"永生时间"去了哪里。

## B — 边界

- **不要只靠剔除"早期死亡者"来修。** 这会换一种方式引入选择偏倚。
- **第 8.6 节提醒：有的选择不带偏倚。** 条件于一个不是共同结果的变量是安全的；不要见"选择"就恐慌。
- **生存分析的常规方法（如条件于在研时间）不会自动修复此偏倚**，反而可能掩盖它。
- 若研究者无法获得治疗开始的确切时间，本偏倚通常**无法从数据内部修复**，只能做敏感性分析并如实报告。
""",
    },
    # ---------------------------------------------------------------- 5
    {
        "slug": "standardization-gformula",
        "title": "标准化与 g-formula：把结局模型铺到整个人群上",
        "importance": "critical",
        "importance_rationale": "第 2.3 节在 Part I 就给出无模型版标准化，第 13 章升级为参数 g-formula，第 21.1 节推广到时变处理——是全书两条主干估计路径之一。",
        "one_liner": "给每个人预测'若治疗'和'若不治疗'两个结局，再对全人群各求一次平均，两个平均相减。",
        "intents": [
            "用标准化（standardization）估计平均因果效应",
            "用参数 g-formula 估计治疗效应",
            "比较 IP 加权与标准化的取舍",
            "估计时变处理的 g-formula",
        ],
        "keywords": ["标准化", "standardization", "g-formula", "g-formula 参数", "parametric g-formula", "outcome regression", "结局回归", "average causal effect"],
        "also_read": ["cap.what-if.ip-weighting-msm", "cap.what-if.time-varying-gmethods", "cap.what-if.doubly-robust-estimation"],
        "destination": "promoted",
        "location": "第 2.3 节 Standardization；第 13 章 Standardization and the parametric g-formula（13.1-13.5）；第 21.1 节 The g-formula for time-varying treatments",
        "tags": ["causal-inference", "estimation", "g-methods"],
        "description": (
            "当用户要用结局模型估计平均因果效应，或在 IP 加权与标准化之间取舍时用。\n"
            "标准化（g-formula）先拟合 E[Y|A,L]，对每个个体分别预测 A=1 与 A=0 下的结局，\n"
            "再对全人群各取平均并相减；时变情形推广为多期 g-formula。\n"
            "触发信号：标准化 / standardization / g-formula / 结局回归估计因果效应 / IP 加权还是标准化 / "
            "怎么估计平均因果效应 / 时变处理的 g-formula。\n"
            "不适用于：需要估计边际结构模型参数的时变情形（走时变 G 方法的 IP 加权路径）、\n"
            "无模型可用的非参数快速核对（第 2.3 节的非参数标准化仍是首选）、以及未测混杂的内生性问题。"
        ),
        "card": """
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
""",
    },
    # ---------------------------------------------------------------- 6
    {
        "slug": "ip-weighting-msm",
        "title": "IP 加权与边际结构模型：造一个治疗与混杂无关的人群",
        "importance": "critical",
        "importance_rationale": "第 2.4 节引入，第 12 章整章展开，第 17.4 节推广到生存结局，第 21.2 节推广到时变处理；是全书使用面最广的估计方法。",
        "one_liner": "给每个人加一个权重 1/P(A|L)，造出一个'治疗与混杂无关'的伪人群，再在里面比较结局。",
        "intents": [
            "用逆概率加权（IPTW）估计平均因果效应",
            "拟合边际结构模型（MSM）",
            "计算并诊断稳定化权重",
            "用 IP 加权处理删失与缺失数据",
        ],
        "keywords": ["IP 加权", "IPTW", "inverse probability weighting", "边际结构模型", "MSM", "marginal structural model", "稳定化权重", "stabilized weights", "倾向性评分", "propensity score"],
        "also_read": ["cap.what-if.standardization-gformula", "cap.what-if.time-varying-gmethods", "cap.what-if.doubly-robust-estimation"],
        "destination": "promoted",
        "location": "第 2.4 节 Inverse probability weighting；第 12 章 IP weighting and marginal structural models（12.1-12.6）；第 17.4 节 IP weighting of marginal structural models；第 21.2 节 IP weighting for time-varying treatments",
        "tags": ["causal-inference", "estimation", "weighting"],
        "description": (
            "当用户要用逆概率加权估计因果效应、拟合边际结构模型、或遇到权重诊断问题时用。\n"
            "IP 加权给每个个体一个权重，使加权人群中治疗与已测混杂独立，再用加权回归估计边际效应；\n"
            "稳定化权重可显著降低方差。\n"
            "触发信号：IPTW / IP 加权 / 倾向性评分加权 / 边际结构模型 / MSM / 稳定化权重 / "
            "权重太大怎么办 / 权重分布怎么检查 / 删失用加权校正。\n"
            "不适用于：倾向于建结局模型的场景（走标准化）、时变混杂反馈（需先走时变 G 方法）、\n"
            "以及未测混杂（加权无能为力）。"
        ),
        "card": """
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
""",
    },
    # ---------------------------------------------------------------- 7
    {
        "slug": "time-varying-gmethods",
        "title": "时变处理的 G 方法：当治疗会改变它自己的混杂因子",
        "importance": "critical",
        "importance_rationale": "Part III（第 19-21 章）整部分围绕此展开；第 20 章论证传统方法在此结构下不可修复，是本书相对其他因果推断教材最独特的内容。",
        "one_liner": "一旦治疗会改变日后的混杂因子，传统回归无论怎么调整都有偏——只能用 g-formula、IP 加权或 G-estimation。",
        "intents": [
            "估计随时间变化的治疗策略的效应",
            "处理治疗-混杂反馈（treatment-confounder feedback）",
            "判断传统回归在纵向数据中为何失效",
            "用多期 g-formula / 时变 IP 加权 / G-estimation 分析纵向数据",
        ],
        "keywords": ["时变治疗", "time-varying treatment", "治疗混杂反馈", "treatment-confounder feedback", "g-methods", "sequential exchangeability", "顺序可交换性", "纵向数据", "marginal structural model"],
        "also_read": ["cap.what-if.ip-weighting-msm", "cap.what-if.standardization-gformula", "cap.what-if.target-trial-emulation"],
        "destination": "promoted",
        "location": "第 19 章 Time-varying treatments（19.1-19.6）；第 20 章 Treatment-confounder feedback（20.1-20.5）；第 21 章 G-methods for time-varying treatments（21.1-21.6）",
        "tags": ["causal-inference", "longitudinal", "g-methods"],
        "description": (
            "当治疗随随访多次变更、且既往治疗会影响后续混杂因子（治疗-混杂反馈）时用。\n"
            "传统回归条件于时变混杂会同时阻断路径并引入对撞偏倚，必须用三类 G 方法：\n"
            "多期 g-formula、时变 IP 加权（MSM）、或结构嵌套模型的 G-estimation。\n"
            "触发信号：时变治疗 / time-varying treatment / 治疗混杂反馈 / treatment-confounder feedback / "
            "纵向数据因果推断 / 顺序可交换性 / 传统回归为什么有偏 / 多期 g-formula。\n"
            "不适用于：治疗在时间零点一次性固定的研究（走 IP 加权或常规标准化）。"
        ),
        "card": """
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
""",
    },
    # ---------------------------------------------------------------- 8
    {
        "slug": "identifiability-conditions",
        "title": "可识别性三条件：可交换性、正值性、一致性",
        "importance": "high",
        "importance_rationale": "第 3.1-3.5 节是 Part I 的识别论基础，第 6.4 节在图语言中重述；所有估计方法都以这三条件为前提，是贯穿全书的检查清单。",
        "one_liner": "数据能回答因果问题，当且仅当：可交换、正值、且干预定义明确（一致性）。",
        "intents": [
            "检查某个观察性研究是否满足可识别性条件",
            "理解并解释可交换性、正值性、一致性",
            "判断干预是否被明确定义（well-defined intervention）",
            "区分识别问题与估计问题",
        ],
        "keywords": ["可交换性", "exchangeability", "正值性", "positivity", "一致性", "consistency", "identifiability", "可识别性", "well-defined intervention", "反事实"],
        "also_read": ["cap.what-if.causal-dag-identification", "cap.what-if.target-trial-emulation", "cap.what-if.bias-structure-diagnosis"],
        "destination": "router",
        "location": "第 3.1 节 Identifiability conditions；3.2 Exchangeability；3.3 Positivity；3.4 Consistency: First, define the counterfactual outcome；3.5 Consistency: Second, link counterfactuals to the observed data；第 6.4 节 Positivity and consistency in causal diagrams",
        "tags": ["causal-inference", "identification", "assumptions"],
        "description": (
            "当用户需要检查一项观察性研究'有没有资格'回答因果问题，或要向读者交代假设时用。\n"
            "三条件：可交换性（治疗组与未治疗组的潜在结局可互换）、正值性（每层都有接受各种治疗的机会）、\n"
            "一致性（干预定义明确且观测结局等于对应反事实结局）。\n"
            "触发信号：这个研究能不能回答因果问题 / 需要哪些假设 / 可交换性 / 正值性 / 一致性 / "
            "well-defined intervention / 识别和估计有什么区别。\n"
            "不适用于：已确认条件满足、只需挑估计方法的场景（走 IP 加权 / 标准化）。"
        ),
        "card": """
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
""",
    },
    # ---------------------------------------------------------------- 9
    {
        "slug": "g-estimation-snm",
        "title": "G-estimation 与结构嵌套模型：直接给效应建模",
        "importance": "medium",
        "importance_rationale": "第 14 章专章，第 17.6 节推广到生存结局，第 21.4 节推广到时变处理；是三类 G 方法中最不常用但在某些结构下唯一可行的一个。",
        "one_liner": "不去建治疗或结局的模型，而是直接给'效应'建一个模型，再搜索让治疗与反事实独立的那个参数值。",
        "intents": [
            "用 G-estimation 估计结构嵌套均值模型（SNMM）",
            "理解 G-estimation 相对 IP 加权与 g-formula 的定位",
            "判断秩保持（rank preservation）假设是否可接受",
        ],
        "keywords": ["G-estimation", "G 估计", "结构嵌套模型", "structural nested model", "SNMM", "rank preservation", "秩保持", "g-methods"],
        "also_read": ["cap.what-if.time-varying-gmethods", "cap.what-if.ip-weighting-msm", "cap.what-if.standardization-gformula"],
        "destination": "router",
        "location": "第 14 章 G-estimation of structural nested models（14.1-14.6）；第 17.6 节 G-estimation of structural nested models；第 21.4 节 G-estimation for time-varying treatments",
        "tags": ["causal-inference", "estimation", "g-methods"],
        "description": (
            "当用户需要直接对效应建模（而非对治疗或结局建模），或处理时变处理且倾向用结构嵌套模型时用。\n"
            "G-estimation 为效应参数搜索一个值，使得在扣除该效应后治疗与反事实结局独立。\n"
            "触发信号：G-estimation / G 估计 / 结构嵌套模型 / SNMM / rank preservation / "
            "时变处理的 G-estimation / 三类 G 方法怎么选。\n"
            "不适用于：常规单期、只需边际效应的场景（IP 加权或标准化更简单）。"
        ),
        "card": """
## R — 原文

结构定位：第 14.3 节 "Structural nested mean models"；14.4 "Rank preservation"；14.5 "G-estimation"；14.6 "Structural nested models with two or more parameters"；第 21.4 节 "G-estimation for time-varying treatments"。

## I — 自述

三类 G 方法的差别在于**把模型建在哪儿**：
- g-formula 建在结局上；
- IP 加权建在治疗的机制上；
- **G-estimation 直接建在效应上**。

结构嵌套均值模型（SNMM）写的是：在给定协变量下，接受治疗者相对未接受治疗者的**均值差**是多少，即 E[Yᵃ − Y⁰ | A=1, L] = ψ（可含 L 的交互项）。参数 ψ 就是待估的效应。

求解思路很巧妙：从个体观测结局 Y 中"扣除"掉假设的效应 ψ，得到一个"若从未治疗"的潜在结局的估计值 Y⁰(ψ)。如果这个 ψ 猜对了，那么在给定 L 的条件下，Y⁰(ψ) 应当与当期治疗 A **无关**（因为在扣掉真实的治疗效应之后，剩下的部分不该再携带治疗的信息）。于是估计 ψ 就变成：搜索那个使 A 与 Y⁰(ψ) 独立的值。

## A1 — 书中案例

- **第 14.1-14.2 节**：作者用同一个戒烟与体重增加的例子重述问题与可交换性，让读者看到三种 G 方法面对的是**同一个 estimand**，只是算法路线不同。
- **第 14.4 节 "Rank preservation"**：作者坦率讨论这一额外假设——它要求个体间的潜在结局排序在治疗下保持不变。书里指出这是个强假设，也是 SNMM 在多参数情形下的软肋。
- **第 21.4 节**：推广到时变处理，G-estimation 成为处理治疗-混杂反馈的第三条路。

## A2 — 未来触发

场景：
1. 用户明确说要用 G-estimation 或结构嵌套模型。
2. 用户在比较三类 G 方法该选哪个。
3. 用户关心效应如何随协变量变化，且不希望在结局模型上做重假设。
4. 用户在时变处理场景下需要一条不依赖结局模型正确设定的路线。

语言信号：G-estimation / G 估计 / 结构嵌套模型 / structural nested model / SNMM / rank preservation / g-methods 怎么选。

与相邻能力区分：若用户只是要边际效应且是单期，IP 加权或标准化更简单；若治疗随时间变化，三类方法都有对应版本（第 21.1-21.4 节），选择取决于愿意把模型建在哪儿。

## E — 执行步骤

1. 确认识别条件（尤其可交换性）成立。
2. 写出结构嵌套均值模型的形式：单参数还是含 L 的交互项（多参数见第 14.6 节）。
3. 计算 Y⁰(ψ) = Y − ψ·A（或含交互项的一般形式）。
4. 建立检验：在给定 L 下，A 是否与 Y⁰(ψ) 独立（常用方式是在 A 的模型中加入 Y⁰(ψ) 作为协变量，检验其系数是否为 0）。
5. 搜索使该检验最不显著的 ψ，即为估计值。
6. 置信区间取"检验不拒绝"的 ψ 集合。
7. 完成标准：能解释"为什么对的时候 A 与 Y⁰(ψ) 应该无关"。

## B — 边界

- **多参数 SNMM 往往需要秩保持假设**（第 14.4 节），这是一个无法检验的强假设，使用前必须说明。
- **比 IP 加权和 g-formula 更少被软件支持**，实现成本高。
- **不解决未测混杂**。
- 若只需一个简单的边际效应，用 G-estimation 属于杀鸡用牛刀。
""",
    },
    # ---------------------------------------------------------------- 10
    {
        "slug": "doubly-robust-estimation",
        "title": "双重稳健估计：两个模型，对一个就够",
        "importance": "medium",
        "importance_rationale": "第 18.4 节专讲双重稳健机器学习估计量，第 21.3 节给出时变版本；是本书与现代因果机器学习（TMLE、DML）的接口。",
        "one_liner": "同时建结局模型和治疗模型，只要其中一个是正确的，估计就一致——但不是两个都错也无所谓。",
        "intents": [
            "用双重稳健估计量（AIPTW/TMLE 类）估计因果效应",
            "在高维数据或机器学习 nuisance 模型下估计因果效应",
            "理解双重稳健性的含义与代价",
        ],
        "keywords": ["双重稳健", "doubly robust", "AIPTW", "TMLE", "双重机器学习", "double machine learning", "nuisance model", "因果机器学习", "cross-fitting"],
        "also_read": ["cap.what-if.ip-weighting-msm", "cap.what-if.standardization-gformula", "cap.what-if.variable-selection-causal"],
        "destination": "router",
        "location": "第 18.3 节 Causal inference and machine learning；18.4 Doubly robust machine learning estimators；第 21.3 节 A doubly robust estimator for time-varying treatments",
        "tags": ["causal-inference", "estimation", "machine-learning"],
        "description": (
            "当用户在高维数据上估计因果效应、或想用机器学习拟合 nuisance 模型时用。\n"
            "双重稳健估计同时需要结局模型与治疗模型，只要其中一个正确设定，效应估计即一致；\n"
            "配合交叉拟合（cross-fitting）可让机器学习方法保持有效推断。\n"
            "触发信号：双重稳健 / doubly robust / AIPTW / TMLE / 双重机器学习 / DML / "
            "因果推断配机器学习 / cross-fitting / 高维协变量。\n"
            "不适用于：协变量很少、模型设定有把握的简单场景（IP 加权或标准化已足够）。"
        ),
        "card": """
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
""",
    },
    # ---------------------------------------------------------------- 11
    {
        "slug": "instrumental-variable",
        "title": "工具变量估计：当可交换性没法假设时",
        "importance": "high",
        "importance_rationale": "第 16 章专章，是本书唯一系统讲授的「在未测混杂下仍可识别」的路径；四个识别条件的讨论（16.1-16.4）是其核心。",
        "one_liner": "三个条件（相关性、排除限制、独立性）之外，还必须有第四个：同质性或单调性——否则估出来的东西没有因果解释。",
        "intents": [
            "用工具变量估计因果效应",
            "检查某个变量能否作为工具变量",
            "理解 IV 的四个识别条件与 LATE 的含义",
            "比较工具变量与其他方法的取舍",
        ],
        "keywords": ["工具变量", "instrumental variable", "IV", "LATE", "monotonicity", "单调性", "exclusion restriction", "排除限制", "弱工具变量", "Mendelian randomization"],
        "also_read": ["cap.what-if.identifiability-conditions", "cap.what-if.ip-weighting-msm", "cap.what-if.standardization-gformula"],
        "destination": "router",
        "location": "第 16 章 Instrumental variable estimation（16.1-16.6）：16.1 三个工具条件；16.2 通常的 IV 估计量；16.3 第四个识别条件：同质性；16.4 另一个第四个条件：单调性；16.5 三个条件重述；16.6 IV 与其他方法的比较",
        "tags": ["causal-inference", "identification", "instrumental-variable"],
        "description": (
            "当存在未测混杂、无法假设可交换性，但存在一个满足条件的工具变量时用。\n"
            "IV 需满足三个条件（与治疗相关、无直接通向结局的路径、与未测混杂独立），\n"
            "外加第四个识别条件：同质性或单调性；在单调性下估计的是 LATE（依从者平均因果效应）。\n"
            "触发信号：工具变量 / instrumental variable / IV 估计 / 未测混杂怎么办 / 孟德尔随机化 / "
            "LATE / monotonicity / 弱工具变量。\n"
            "不适用于：已测混杂已能满足可交换性的场景（IP 加权或标准化更高效）。"
        ),
        "card": """
## R — 原文

结构定位：第 16.1 节 "The three instrumental conditions"；16.2 "The usual IV estimand"；16.3 "A fourth identifying condition: homogeneity"；16.4 "An alternative fourth condition: monotonicity"；16.5 "The three instrumental conditions revisited"；16.6 "Instrumental variable estimation versus other methods"。

## I — 自述

工具变量是给"可交换性这条假设已经破产"的情形留的后门。它不要求治疗与潜在结局独立，而是要求能找到一个变量 Z，满足：

1. **Z 与治疗 A 相关**（相关性）；
2. **Z 对结局 Y 没有不经过 A 的路径**（排除限制）；
3. **Z 与未测混杂 U 独立**，即 Z 与潜在结局独立（独立性）。

但这三条**还不够**。第 16.3、16.4 节是本章的要害：要得到一个有因果解释的量，还必须有第四个条件——
- **同质性**：效应在所有人身上相同；或
- **单调性**：Z 对 A 的影响方向在所有人身上一致（不存在"被 Z 劝退"的人）。

在单调性下，通常的 IV 估计量估计的是 **LATE**：依从者（compliers，即被 Z 推动才接受治疗的那部分人）的平均因果效应。这是一个**局部**效应，不是全人群平均效应——这一点必须写在结论里。

## A1 — 书中案例

- **第 16.3 节**：作者演示在只有三个条件时，IV 估计量可以是两个子人群效应的某种混合，甚至符号都可能与真实效应相反——这是"三个条件够了吗"这一问的答案。
- **第 16.4 节**：用单调性替换同质性，说明此时估计量获得了 LATE 这一清晰解释。
- **第 16.6 节**：把 IV 与 IP 加权、标准化、G-estimation 并排比较，指出 IV 的代价是**更弱的假设换更局部的 estimand、更大的方差**。

## A2 — 未来触发

场景：
1. 用户明知存在未测混杂，问"还能不能估"。
2. 用户想用孟德尔随机化（遗传变异作为工具）。
3. 用户想用"医生偏好""就诊距离""政策变动"作为工具变量。
4. 用户报告了 IV 估计，但没说估的是谁的效应。

语言信号：工具变量 / instrumental variable / IV / 未测混杂 / unmeasured confounding / 孟德尔随机化 / Mendelian randomization / LATE / complier / 单调性 / monotonicity / 弱工具变量。

与相邻能力区分：IV 是**可交换性不可信时**的备选。若已测混杂足以支撑可交换性，IP 加权或标准化效率更高、解释更直接。

## E — 执行步骤

1. 明确写出工具变量 Z 是什么，以及它影响 A 的机制。
2. 逐条论证三个条件：相关性、排除限制、独立性。**每一条都要给出领域理由，不能只靠统计检验。**
3. 明确第四个条件：假设同质性还是单调性？
4. 若用单调性：承认估计的是 LATE，并描述"依从者"这个子人群长什么样。
5. 检查弱工具变量：第一阶段 F 统计量或 Z 与 A 的关联强度。弱工具会放大偏倚。
6. 估计并报告：效应、适用人群（LATE）、以及假设的敏感性。
7. 完成标准：能说清楚"我估的是谁的效应"。

## B — 边界

- **三个条件不足以识别**，必须有第四个（第 16.3-16.4 节）。这是最常见的误用。
- **估的是 LATE 不是 ATE**。把 LATE 当成全人群效应外推是常见错误。
- **弱工具变量极其危险**：不仅方差大，还会把排除限制的微小违反放大成严重偏倚。
- **排除限制与独立性都不可检验**（第 16.5 节），只能论证。
- **不要在有充分已测混杂数据时默认用 IV**——第 16.6 节指出它的方差代价很高。
""",
    },
    # ---------------------------------------------------------------- 12
    {
        "slug": "effect-modification-interaction",
        "title": "效应修饰与交互：两个常被混为一谈的概念",
        "importance": "high",
        "importance_rationale": "第 4、5 章连续两章专门辨析；作者指出「效应修饰」与「交互」在因果推断中是不同的对象，混淆二者是文献中最普遍的解读错误之一。",
        "one_liner": "效应修饰：效应大小随某变量变（换尺度就可能消失，不是「交互」）；交互：两个干预必须联合施加才能谈。",
        "intents": [
            "判断某变量是否是效应修饰因子",
            "区分效应修饰（effect modification）与交互（interaction）",
            "正确解读亚组分析与分层结果",
            "理解充分原因交互与反事实交互的区别",
        ],
        "keywords": ["效应修饰", "effect modification", "交互", "interaction", "亚组分析", "subgroup", "异质性", "heterogeneity", "sufficient cause", "充分原因", "scale dependence", "尺度依赖"],
        "also_read": ["cap.what-if.causal-dag-identification", "cap.what-if.standardization-gformula", "cap.what-if.variable-selection-causal"],
        "destination": "router",
        "location": "第 4 章 Effect modification（4.1-4.6）；第 5 章 Interaction（5.1-5.6）：5.1 交互需要联合干预；5.3 反事实反应类型与交互；5.4 充分原因；5.5 充分原因交互；第 6.6 节 The structure of effect modification",
        "tags": ["causal-inference", "heterogeneity", "interpretation"],
        "description": (
            "当用户做亚组分析、解读异质性、或问'这两个因素有没有交互'时用。\n"
            "效应修饰是效应大小随某变量变化（且依赖效应尺度，非因果性的'交互'）；\n"
            "交互则要求两个干预可被联合施加，是真正的因果概念。\n"
            "触发信号：效应修饰 / effect modification / 交互作用 / interaction / 亚组分析 / "
            "异质性 / heterogeneity / 分层分析 / 尺度依赖 / 充分原因交互。\n"
            "不适用于：只想选变量（走因果变量选择）或只想要单一边际效应（走标准化）。"
        ),
        "card": """
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
""",
    },
    # ---------------------------------------------------------------- 13
    {
        "slug": "causal-mediation",
        "title": "因果中介分析：在「调整中介」之前先问能不能干预它",
        "importance": "medium",
        "importance_rationale": "第 23 章专章，作者直面学界的批评（23.1）并给出辩护（23.2-23.4）；是把全书的干预主义立场推到最远处的一章。",
        "one_liner": "中介分析的前提是中介变量可被干预；只有当「把中介固定在某值」是一个可执行操作时，直接/间接效应才有因果意义。",
        "intents": [
            "正确地做因果中介分析",
            "区分总效应、直接效应与间接效应",
            "判断某变量能否作为中介被干预",
            "理解传统中介分析方法受批评的原因",
        ],
        "keywords": ["中介分析", "mediation", "直接效应", "direct effect", "间接效应", "indirect effect", "controlled direct effect", "干预主义", "interventionist", "机制"],
        "also_read": ["cap.what-if.causal-dag-identification", "cap.what-if.identifiability-conditions", "cap.what-if.effect-modification-interaction"],
        "destination": "router",
        "location": "第 23 章 Causal mediation（23.1-23.4）：23.1 Mediation analysis under attack；23.2 A defense of mediation analysis；23.3 Empirically verifiable mediation；23.4 An interventionist theory of mediation",
        "tags": ["causal-inference", "mediation", "mechanism"],
        "description": (
            "当用户要拆解机制、估计直接效应与间接效应，或问「这个变量是不是中介」时用。\n"
            "干预主义立场：只有当「把中介变量设定为某值」是一个可执行的干预时，直接/间接效应才有因果意义。\n"
            "触发信号：中介分析 / mediation / 直接效应 / 间接效应 / 机制分析 / "
            "controlled direct effect / 调整了中介之后的效应 / 中介分析被批评。\n"
            "不适用于：只需总效应的场景；也不适用于中介无法被干预的情形（那时应直接说明不可识别）。"
        ),
        "card": """
## R — 原文

结构定位：第 23.1 节 "Mediation analysis under attack"；23.2 "A defense of mediation analysis"；23.3 "Empirically verifiable mediation"；23.4 "An interventionist theory of mediation"。

## I — 自述

中介分析在方法学界长期挨批（第 23.1 节），本书给出的辩护（23.2）与解法（23.3-23.4）都建立在一个核心立场上：**因果效应只针对可执行的干预而定义**。

因此"直接效应""间接效应"要成立，前提是"把中介 M 固定在某个值 m"这件事是一个可实施的干预。对照两条路：
- 若 M（如性别、基因型、某个不可直接设定的生理指标）无法被干预，那么"控制直接效应"在严格意义上不可识别——不是估不准，是没定义。
- 若 M 可被干预（如"把血压维持在 120"是一个可执行的临床方案），那么直接效应与间接效应都有清晰的干预定义，可以用全书一贯的 g-formula / IP 加权框架估计。

第 23.3 节进一步提出"经验上可验证的中介"：与其争论形而上学的机制，不如要求中介分析对应的干预在原则上能被检验。

## A1 — 书中案例

- **第 23.1 节**：作者先摆出批评意见——传统中介分析（如把中介放进回归看系数变小）依赖一整套未被陈述的假设，包括中介与结局之间无未测混杂、且无治疗-中介的混杂反馈。
- **第 23.2 节**：辩护的要点不是"传统方法其实没问题"，而是"中介问题本身可以被良好地定义"，只要回到干预。
- **第 23.4 节**：给出干预主义的中介理论，把它接回全书统一的反事实框架。

## A2 — 未来触发

场景：
1. 用户问"X 通过什么机制影响 Y"。
2. 用户报告"调整中介后效应变小了，说明机制成立"。
3. 用户要估计直接效应与间接效应。
4. 用户看到"中介分析不可靠"的批评，不知还能不能做。

语言信号：中介分析 / mediation / 直接效应 / 间接效应 / direct effect / indirect effect / 机制 / mechanism / controlled direct effect / 调整中介后。

与相邻能力区分：若要拆解的是"效应在不同人群中是否不同"，走效应修饰与交互；若只是要总效应，用标准化或 IP 加权；中介分析额外要求中介本身可干预且识别条件更强。

## E — 执行步骤

1. 明确要拆解的因果对比：总效应、控制直接效应，还是自然直接/间接效应。
2. **关键一步**：判断中介 M 是否可被干预。若否，停止——说明该分解不可识别，不要报告数字。
3. 画出含 A → M → Y 的 DAG，标出 M→Y 之间是否存在未测混杂（这是传统方法最容易忽略的一条）。
4. 检查是否存在治疗-中介的混杂反馈（即受 A 影响又影响 M 的变量）。
5. 在干预主义定义下，用 g-formula 或 IP 加权估计相应的效应分解。
6. 完成标准：能说明"我把 M 固定在某值"这个干预在现实中对应什么操作。

## B — 边界

- **"调整中介后系数变小"不是中介证据。** 这是第 23.1 节点名批评的做法。
- **M→Y 之间存在未测混杂时，传统分解无效。**
- **中介不可被干预时，严格来说效应分解没有定义**（不是估计困难）。
- 自然直接/间接效应依赖跨世界的反事实假设，解释时要格外谨慎。
""",
    },
    # ---------------------------------------------------------------- 14
    {
        "slug": "variable-selection-causal",
        "title": "因果推断中的变量选择：目标不是预测结局",
        "importance": "high",
        "importance_rationale": "第 18.1、18.2 节明确指出变量选择在因果推断与预测中目标不同，18.5 节坦承这是一个困难问题；是实践中最高频的困惑来源。",
        "one_liner": "选变量不看「能不能预测结局」，而看它在 DAG 上的位置——调整对撞节点和强工具变量会主动放大偏倚。",
        "intents": [
            "为因果分析选择要调整的协变量",
            "判断某个变量该不该纳入调整集合",
            "理解为什么数据驱动的变量选择会伤害因果估计",
            "区分预测建模与因果推断的变量选择标准",
        ],
        "keywords": ["变量选择", "variable selection", "调整集合", "adjustment set", "对撞节点", "collider", "工具变量误调", "混杂选择", "高维数据", "confounder selection"],
        "also_read": ["cap.what-if.causal-dag-identification", "cap.what-if.bias-structure-diagnosis", "cap.what-if.doubly-robust-estimation"],
        "destination": "router",
        "location": "第 18.1 节 The different goals of variable selection；18.2 Variables that induce or amplify bias；18.3 Causal inference and machine learning；18.5 Variable selection is a difficult problem",
        "tags": ["causal-inference", "variable-selection", "practice"],
        "description": (
            "当用户问「该把哪些变量放进模型」、或想用逐步回归/LASSO 选混杂时用。\n"
            "因果推断的变量选择目标是阻断后门路径，不是提高结局预测精度；\n"
            "条件于对撞节点或强工具变量反而会放大偏倚与方差。\n"
            "触发信号：该调整哪些变量 / 变量选择 / 逐步回归选混杂 / LASSO 选变量 / "
            "这个变量要不要放进模型 / 调整集合 / 高维协变量怎么选。\n"
            "不适用于：已经用 DAG 定好调整集合的场景（直接走因果图识别）。"
        ),
        "card": """
## R — 原文

结构定位：第 18.1 节 "The different goals of variable selection"；18.2 "Variables that induce or amplify bias"；18.5 "Variable selection is a difficult problem"。

## I — 自述

预测建模选变量的标准是"它对预测结局有没有用"。因果推断选变量的标准是"它在 DAG 上的位置是什么"。这两者经常冲突：

- **对撞节点（collider）**：它是治疗与结局的共同结果。它往往**能很好地预测结局**，所以任何以预测为目标的算法都会把它选进来；但条件于它会**打开**一条非因果路径，凭空造出偏倚。
- **强工具变量**：它强烈预测治疗，但对结局无直接效应。调整它会放大偏倚并大幅抬高方差（第 18.2 节）。
- **中介**：它也能预测结局，但调整它会切断总效应的一部分。

所以"用 LASSO 从 200 个变量里筛出混杂"是一个**类别错误**：LASSO 优化的是预测，它恰恰会优先挑出对撞节点和中介。

第 18.5 节作者很坦率：这是一个困难问题，没有万能算法。可靠的做法仍是基于领域知识画 DAG，再配合对高维 nuisance 模型的正则化（此时应选双重稳健估计量，让正则化的偏差不直接污染效应估计）。

## A1 — 书中案例

- **第 18.2 节 "Variables that induce or amplify bias"**：作者给出"调整了反而更糟"的变量类型清单——这正是本书反直觉结论最集中的一节。
- **第 18.3 节**：讨论机器学习进入因果推断时的正确位置——用于拟合 nuisance 模型，而不是用于选混杂。
- **第 18.5 节 "Variable selection is a difficult problem"**：作者没有给出银弹，而是说明为什么这个问题在实践中必须结合领域知识。

## A2 — 未来触发

场景：
1. 用户有几十上百个协变量，不知道调整哪些。
2. 用户打算用逐步回归或 LASSO 筛混杂。
3. 用户问"这个变量要不要放进模型"。
4. 用户担心"调整太多"或"调整太少"。

语言信号：变量选择 / variable selection / 该调整哪些变量 / 逐步回归 / stepwise / LASSO 选混杂 / 调整集合 / adjustment set / 高维协变量。

与相邻能力区分：本能力处理"**怎么选**"；一旦用 DAG 确定了调整集合，估计方法走 IP 加权或标准化；若维度高到必须用 ML，走双重稳健估计。

## E — 执行步骤

1. 先画 DAG，按结构分类每个候选变量：共同原因（要调）、中介（总效应下不调）、对撞节点（绝不调）、工具变量（不调）。
2. **不要用结局关联度筛选。** 用预测选变量等于系统性引入对撞节点与中介。
3. 若维度确实很高且无法逐一判断：把可变变量交给双重稳健机器学习估计量拟合 nuisance 模型，并用交叉拟合。
4. 对"不确定是否为混杂"的变量：报告调整与不调整两套结果，作为敏感性分析，而不是默默选一个。
5. 检查调整后的正值性——加入过多变量会让每层样本枯竭。
6. 完成标准：每一个被纳入的变量都能说出它在 DAG 上的位置与纳入理由。

## B — 边界

- **不要以"它与结局显著相关"为纳入理由。**
- **不要条件于对撞节点**，包括那些"看起来很像混杂"的入院指标、检测与否、存活状态等。
- **不要调整强工具变量**——会放大偏倚与方差（第 18.2 节）。
- **加入变量不是免费的**：每层样本变少会威胁正值性。
- 第 18.5 节提醒：这个问题没有全自动解法，领域知识不可省略。
""",
    },
]


def main() -> None:
    CARDS.mkdir(parents=True, exist_ok=True)
    BOOKDIR.mkdir(parents=True, exist_ok=True)

    capabilities = []
    for c in CAPS:
        cid = f"cap.what-if.{c['slug']}"
        header = (
            f"<!-- capability_id: {cid} | revision: 1 | status: active -->\n"
            f"<!-- 来源: Causal Inference: What If (Hernan & Robins, 2020) / {c['location']} -->\n\n"
        )
        (CARDS / f"{c['slug']}.md").write_text(
            header + c["card"].strip() + "\n", encoding="utf-8"
        )
        promoted = c["destination"] == "promoted"
        capabilities.append({
            "capability_id": cid,
            "revision": 1,
            "status": "active",
            "aliases": [],
            "supersedes": [],
            "merged_into": None,
            "split_into": [],
            "slug": c["slug"],
            "title": c["title"],
            "importance": c["importance"],
            "importance_rationale": c["importance_rationale"],
            "one_liner": c["one_liner"],
            "intents": c["intents"],
            "keywords": c["keywords"],
            # router_table 把 also_read 的每一项拼成 references/capabilities/<slug>.md，
            # 因此这里必须是 slug，不能是 capability_id。
            "also_read": [s.removeprefix("cap.what-if.") for s in c["also_read"]],
            "card": f"cards/{c['slug']}.md",
            "frontmatter": {"description": c["description"].strip(), "tags": c["tags"]},
            "source_evidence": [{"source_id": "src-main-book", "location": c["location"]}],
            "promotion": {
                "destination": c["destination"],
                "gate": ({k: True for k in ("independent_intent", "independent_contract", "independent_run",
                                           "independent_reuse", "independent_eval")}
                         if promoted else
                         {"independent_intent": False, "independent_contract": True, "independent_run": True,
                          "independent_reuse": False, "independent_eval": True}),
                "notes": ("晋级为独立 Skill：具备独立意图、独立契约与独立评测，可被直接触发。"
                          if promoted else
                          "保留为来源路由入口内的能力卡：与相邻能力共享意图入口，经路由入口可达。"),
            },
        })

    router_name = "causal-inference-what-if"
    bundle = {
        "schema_version": 1,
        "bundle_id": "bundle.causal-inference-what-if",
        "book": BOOK,
        "entry": {
            "name": "causal-inference-what-if",
            "title": "因果推断：What If（Hernán & Robins）",
            "description": (
                "Hernán & Robins《Causal Inference: What If》蒸馏出的因果推断能力集，覆盖目标试验模拟、"
                "因果图识别、偏倚结构诊断，以及 IP 加权 / g-formula / G 方法等估计路径。\n"
                "触发：设计或审查观察性研究、判断该调整哪些变量、诊断偏倚类型、选择并实施因果估计方法、"
                "解读 ITT / per-protocol / LATE 等 estimand 的含义。\n"
                "不触发：纯预测建模、统计软件操作教程、与因果推断无关的通用数据分析。"
            ),
            "core_principles": [
                "识别先于估计：先问「在给定假设下这个效应能否被数据唯一确定」，再问用什么方法把它算出来。",
                "干预必须定义明确：说不出可执行操作的「效应」没有单一答案，一致性条件首先就过不了。",
                "按因果图的结构认偏倚，不按名字认偏倚：共同原因是混杂，条件于共同结果是选择偏倚，变量测错是测量偏倚。",
                "目标试验先行：拿到观察性数据先写清 eligibility、治疗策略、时间零点、结局与因果对比，再选估计方法。",
                "同一个 estimand 有多条算法路径：g-formula 建在结局上，IP 加权建在治疗上，G-estimation 建在效应上。",
                "治疗一旦随时间变化并改变自身的混杂因子，传统回归无论怎么调整都有偏，只能用 G 方法。",
                "效应修饰依赖尺度，交互要求干预可被联合施加——两者不是一回事。",
            ],
            "out_of_scope": [
                "纯预测 / 预后建模（不问干预效应）",
                "统计软件操作、代码调试与包用法教学",
                "与因果推断无关的通用数据清洗与可视化",
                "哲学层面的因果本体论讨论（本书明确声明不做）",
                "本书未覆盖的主题：干扰（interference / spillover）、贝叶斯因果推断、网络实验设计",
            ],
            "stop_conditions": [
                "干预写不出可执行的操作时停止估计，先回到问题定义（目标试验模拟）。",
                "正值性结构性违反（某类患者从不接受某种治疗）时，该亚群的效应不可识别，不要硬估。",
                "可交换性无法论证时应转向敏感性分析或工具变量，并明确报告未测混杂的存在。",
                "路由表与能力索引都无法命中的意图，明确说明超出本书范围，不要硬套某张能力卡。",
            ],
        },
        "router_entry": {
            "name": router_name,
            "title": "因果推断：What If — 能力路由入口",
            "description": "全书 14 个能力的统一入口，含未晋级能力卡与索引。",
        },
        "promotion_budget": 8,
        "capabilities": capabilities,
    }

    (BUNDLE / "verified.yaml").write_text(
        yaml.safe_dump(bundle, allow_unicode=True, sort_keys=False, width=120), encoding="utf-8"
    )
    (BUNDLE / "destinations.json").write_text(json.dumps({
        "bundle_id": bundle["bundle_id"],
        "destinations": {
            c["capability_id"]: ({"promoted_to": c["slug"]}
                                 if c["promotion"]["destination"] == "promoted"
                                 else {"served_by": router_name})
            for c in capabilities
        },
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    n_promoted = sum(1 for c in CAPS if c["destination"] == "promoted")
    print(f"[ok] bundle: {BUNDLE}")
    print(f"[ok] {len(CAPS)} 个能力（晋级 {n_promoted}，路由 {len(CAPS) - n_promoted}），入口数 {1 + n_promoted}")


if __name__ == "__main__":
    main()

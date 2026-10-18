# 因果推断：What If · 中文版（what-if-cn）

《Causal Inference: What If》（Miguel A. Hernán & James M. Robins，Chapman & Hall/CRC）的中文翻译站，附带把全书蒸馏出来的一组 Skill。

**在线阅读**：<https://zhangkaicr.github.io/what-if-cn/>

## 一、中文翻译（阅读站）

- 原书三部分结构：无模型的因果推断（1–10 章）/ 基于模型的因果推断（11–18 章）/ 时变处理的因果推断（19–23 章）
- 原书图表按原样保留（从 PDF 原位裁切，165 张图/表 + 封面）
- 译文之外补充必要的背景知识与译者注
- 明暗主题切换、站内全文搜索（按 `/` 聚焦）

**翻译进度**：当前已完成 11 / 24 篇（导言，第 2、3、6、8、14、16、18、20、21、22 章），其余 13 章为占位页——标注「翻译进行中」并附原书小节结构，站内无死链，可正常跳转阅读。

## 二、蒸馏出的 Skill（`skills/`）

用 cangjie-skill 把全书方法论蒸馏为 **14 个原子能力**，编译成 compact pack：

**7 个独立 Skill（可直接触发）**

| Skill | 一句话 |
|---|---|
| `target-trial-emulation` | 拿到观察性数据先写目标试验方案，再碰数据 |
| `causal-dag-identification` | 画因果图，用后门准则挑调整集合 |
| `bias-structure-diagnosis` | 按图的结构认偏倚，不按名字认偏倚 |
| `selection-bias-immortal-time` | 时间零点一错，全盘皆错 |
| `standardization-gformula` | 把结局模型铺到整个人群上 |
| `ip-weighting-msm` | 造一个治疗与混杂无关的伪人群 |
| `time-varying-gmethods` | 当治疗会改变它自己的混杂因子 |

**1 个路由入口** `causal-inference-what-if/`：先读路由表，按意图加载 1 张能力卡。另 7 个能力保留在入口内——可识别性三条件、G-estimation 与结构嵌套模型、双重稳健估计、工具变量、效应修饰与交互、因果中介、因果变量选择。

面向读者的精华长文见 `_cangjie/books/what-if/DIGEST.md`；蒸馏过程的审计轨迹（候选池、三重验证、Capability Bundle、能力卡原文）在 `_cangjie/books/what-if/`。

## 免责声明

翻译仅供个人学习交流，版权归原作者所有；引用请以英文原版为准（作者网站免费提供电子版）。

## 相关项目

- 因果森林知识库：<https://zhangkaicr.github.io/causal-forest-hub/>
- mlr3book 中文版：<https://zhangkaicr.github.io/mlr3book-cn/>

# PIPELINE_STATE — Causal Inference: What If

> 断点续跑用。每完成一个阶段更新本文件。

| 阶段 | 状态 | 产物 |
|---|---|---|
| 0 整书理解 | ✅ 完成 | `BOOK_OVERVIEW.md` |
| 1 并行提取 | ⚠️ 降级串行 | 见下方说明 |
| 1.5 三重验证 | ✅ 完成 | `verified.md`（候选全部通过或归入 rejected） |
| 1.6 晋级门 | ✅ 完成 | `.cangjie/capabilities/verified.yaml` 的 `promotion.destination` |
| 2 RIA++ 能力卡 | ✅ 完成 | `.cangjie/capabilities/cards/*.md`（14 张） |
| 3 Zettelkasten 链接 | ✅ 完成 | `also_read` + `GLOSSARY.md` |
| 4 压力测试 | ⚠️ 部分 | 触发信号与边界已写入 A2/B 段；darwin 格式评测用例未生成 |
| 5 编译与交付 | ✅ 完成 | `skills/`（pack，8 个入口）、`DIGEST.md` |

## 执行说明

**阶段 1 降级原因**：本环境在批量并发 sub-agent 时触发 API 频率限制（HTTP 429），5 个 extractor 无法并行。按 `methodology/02-stage1-parallel-extract.md` 的降级方案，改由主 agent **串行**执行 5 个 extractor 的判断逻辑，产出格式不变。

**阶段 4 说明**：每个晋级能力的触发评测（含兄弟诱饵）以 A2「语言信号 + 相邻能力区分」与 B「边界/反场景」承载；`test-prompts.json` 尚未生成，后续可用 darwin-skill 补齐。

## 关键决策记录

| 决策 | 选择 | 理由 |
|---|---|---|
| 输出模式 | `pack` | 14 个能力中 7 个具备独立意图与独立契约，晋级为独立 Skill；其余 7 个保留在来源路由入口 |
| 入口预算 | 8（1 路由 + 7 晋级） | 正好等于 `promotion_budget`，无需 `--allow-over-budget` |
| 书名元数据 | `Causal Inference - What If` | 原名含 `: `，会破坏生成 SKILL.md 的 YAML frontmatter；原名保留在 `BOOK_OVERVIEW.md` 与能力卡来源标注 |
| 编译产物位置 | `what-if-cn/skills/` | 与翻译站点同仓库发布 |

## 能力清单

**晋级（7）**：target-trial-emulation · causal-dag-identification · bias-structure-diagnosis · selection-bias-immortal-time · standardization-gformula · ip-weighting-msm · time-varying-gmethods

**路由（7）**：identifiability-conditions · g-estimation-snm · doubly-robust-estimation · instrumental-variable · effect-modification-interaction · causal-mediation · variable-selection-causal

---
decision_id: PDR-{{DATE}}-{{TOPIC_SLUG}}
title: {{TITLE}}
status: deliberating # deliberating | executing | validated | falsified
created_date: {{DATE}}
review_date: {{REVIEW_DATE}}
tags:
  - decision
  - pdr
---

# 个人决策记录 (Personal Decision Record)

> 💡 **核心设计**：本文件通过“事前验尸”与“预设证伪线”，杜绝人类天然的“事后诸葛亮偏见 (Hindsight Bias)”。

---

## 阶段一：事前审慎推演 (Before Decision)

### 1. 决策背景与核心命题 (Context & Framing)
- 待解决的具体问题：`{{PROBLEM_STATEMENT}}`
- 当前掌握的核心信息与渠道参数：`{{INFO_SOURCES}}`

### 2. 备选方案权衡 (Alternatives Evaluated)
| 方案 | 潜在收益 | 显性成本与时间锁定 | 隐性机会成本 | 最大回撤风险 |
| :--- | :--- | :--- | :--- | :--- |
| **方案 A (采纳)** |  |  |  |  |
| **方案 B (备选)** |  |  |  |  |

### 3. 三大核心前提假设 (Core Assumptions)
> 如果以下任何一条被现实推翻，本决定的合理性将瞬间归零：
1. 假设一：`{{ASSUMPTION_1}}`
2. 假设二：`{{ASSUMPTION_2}}`
3. 假设三：`{{ASSUMPTION_3}}`

### 4. 事前验尸分析 (Pre-Mortem)
> 假设时间来到一年后的今天，该决策彻底崩盘溃败。站在未来的废墟上回望，最可能死于哪 3 个原因？
1. 死因一：`{{FAILURE_REASON_1}}`
2. 死因二：`{{FAILURE_REASON_2}}`
3. 死因三：`{{FAILURE_REASON_3}}`

### 5. 证伪标准与强制止损线 (Falsification Criteria & Kill Switch)
> 预先设定客观的触发红线。当出现以下指标时，禁止进行主观借口辩解，必须执行无条件止损：
- **客观指标**：`{{METRIC_OR_EVENT}}`
- **止损触发线 (Kill Switch)**：`{{KILL_SWITCH_CONDITION}}`

---

## 阶段二：决定落子锁定 (Lock-in)
- **最终决定**：`{{FINAL_DECISION}}`
- **做决定的当下心理倾向与直觉自省**：`{{EMOTIONAL_STATE_AUDIT}}`
- **底稿锁定哈希/日期**：`{{LOCK_IN_DATE}}`（通过 Git Commit 永久固化历史事实底稿）

---

## 阶段三：到达期限的事后硬核复盘 (Post-Mortem Review at Review_Date)

> 💡 到达 `review_date` 时，外部 Agent 自动调出当年的阶段一底稿，拿客观现实与假设进行冷酷碰撞。

1. **现实结果与假设比对**：
   - 假设一是否被证实：`[是 / 否]` - 具体事实：`{{FACT_1}}`
   - 假设二是否被证实：`[是 / 否]` - 具体事实：`{{FACT_2}}`
   - 假设三是否被证实：`[是 / 否]` - 具体事实：`{{FACT_3}}`
2. **归因分离（能力 vs 运气）**：
   - 如果成功：是决策逻辑正确带来的必然，还是外部随机运气的盲盒红利？
   - 如果失败：是决策前提漏洞，还是遭遇不可抗力的小概率黑天鹅？
3. **沉淀元规律**：
   - 发现的自身认知偏差：`{{NEW_COGNITIVE_BIAS}}`（同步更新至 `personal_bias_registry.md`）
   - 最终判定：`status: validated / falsified`
   - 归档去向：移入 `vault/L3_archive/`

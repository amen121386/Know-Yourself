# 协议 04：记忆蒸馏与认知偏差提炼协议 (Memory Distillation Pipeline)

> 目的：解决“本地文件无序堆积导致上下文腐败 (Context Rot)”的工程悖论，实现“活到老、学到老”的终身演进。

---

## 一、 核心法则：用“元规律”取代“流水账”

随着系统运行时间增加，成百上千篇笔记塞入 Context 会引发模型的**注意力稀释（Lost-in-the-Middle）**。
真正的系统自我进化，不是堆积文章，而是**通过定期蒸馏，提炼关于自身的元规律**：

```
[L2 温记忆：具体决策记录 PDR] 
        ↓ (每季度/每半年执行一次蒸馏工作流)
[提炼归纳：沉淀至 L1 的 personal_bias_registry.md]
        ↓ (完结的原始记录冷冻归档)
[L3 冷数据：历史归档区]
```

---

## 二、 蒸馏产物：《个人认知偏差注册表 (personal_bias_registry.md)》

系统在 `vault/L1_atlas/personal_bias_registry.md` 中维护一份不断自我校准的**个人认知弱点索引**，其结构如下：

```markdown
# 个人认知偏差与行为漏洞注册表

### 1. 压力态下的系统性缺陷 (Stress-Induced Bias)
- [已证伪记录] 案例：2026年某项决策表明，当宿主感到现实竞争压力时，极易退行回“狂买课程/狂囤工具”的心理舒适区；
- [干预对策] 未来检测到类似焦虑时，立即强制要求交付“7天极简实操成果”。

### 2. 收益高估与执行力过载 (Optimism Bias)
- [已证伪记录] 宿主倾向于把一天的精力设想为 10 小时高效状态，忽略了下午意志力崩塌的客观规律；
- [干预对策] 制定排期时，默认在宿主预估的时间上增加 50% 的缓冲冗余。

### 3. 沉没成本与割肉障碍 (Sunk Cost Fallacy)
- [已证伪记录] 针对已经明显证伪的尝试，因前期投入而推迟止损达数月；
- [干预对策] 严格按 PDR 中预设的止损线（Kill_Switch）触发强制熔断提醒。
```

---

## 三、 归档与生命周期流转 (Lifecycle Transition)
1. 当一项决策在 `vault/L2_decisions/` 中到达 `Review_Date` 并完成事后复盘后，状态更新为 `validated`（验证通过）或 `falsified`（被现实证伪）；
2. 提取其核心教训写入 `personal_bias_registry.md`；
3. 将该 PDR 文件由 `vault/L2_decisions/` 移入 `vault/L3_archive/`，不再参与日常 Context 消耗。

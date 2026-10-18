# AI Agent 技能与能力清单 (Skills & Plugins Registry)

> **维护法则**：  
> 记录大模型/智能体挂载的专属 Skill（技能插件）、Prompt 流程与脚本工具。实测验证可用后打上 `[FACT]`。

---

## 1. 技能总览表 (Skill Overview)

| 技能名称 | 类型 | 适用环境 / 框架 | 触发场景 / 作用 | 实测状态 | 更新日期 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **fact-verification** | Rule/Prompt | Universal (Claude/Gemini/Cursor) | 强制任务实测通过后才能打勾并声明事实核销 | `[FACT]` 稳定运行 | 2026-10-01 |
| **auto-sync-os** | Workflow Hook | Universal (Agent Workflow) | 自动将部署成功的工具写回 OS 知识库 | `[FACT]` 稳定运行 | 2026-10-01 |
| *[示例占位]* | Skill | Antigravity / Cursor | 新增技能时在此登记 | 待实测 | - |

---

## 2. 技能维护原则
- 技能必须具备确定性的输入与输出契约；
- 如技能涉及本地执行权限，需在对应规则中声明安全边界。

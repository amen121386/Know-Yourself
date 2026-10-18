#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Know Yourself OS - Vault Initializer
自动化初始化本地个人数据主权仓库 (vault/) 目录结构与初始模板。
"""

import sys
import shutil
from pathlib import Path

# Windows GBK 兼容处理
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def init_vault():
    root = Path(__file__).resolve().parent.parent
    vault_dir = root / "vault"
    templates_dir = root / "templates"

    subdirs = ["L1_atlas", "L2_decisions", "L3_archive", "inbox"]
    for sub in subdirs:
        p = vault_dir / sub
        p.mkdir(parents=True, exist_ok=True)
        gitkeep = p / ".gitkeep"
        if not gitkeep.exists():
            gitkeep.touch()

    # Seed L1 template copy if it doesn't exist
    l1_target = vault_dir / "L1_atlas" / "L1_situational_atlas.md"
    l1_source = templates_dir / "L1_situational_atlas.md"
    if not l1_target.exists() and l1_source.exists():
        shutil.copy(l1_source, l1_target)
        print(f"[*] Initialized L1 Atlas: {l1_target}")

    # Seed personal bias registry if it doesn't exist
    bias_target = vault_dir / "L1_atlas" / "personal_bias_registry.md"
    if not bias_target.exists():
        bias_content = """# 个人认知偏差与行为漏洞注册表 (Personal Bias Registry)

> 本文件存放从历史决策复盘（PDR）与真实经历中提炼出的元规律。
> 供外部 Agent 在每次辅助推演前强制审阅，主动对抗自身盲区。

---

### 1. 压力与焦虑下的系统性退行 (Stress Bias)
- [待填充]

### 2. 收益与执行力的乐观高估偏差 (Planning Fallacy)
- [待填充]

### 3. 沉没成本与割肉障碍 (Sunk Cost Fallacy)
- [待填充]
"""
        bias_target.write_text(bias_content, encoding="utf-8")
        print(f"[*] Initialized Personal Bias Registry: {bias_target}")

    print("\n[OK] Know Yourself 本地外脑仓库 (vault/) 初始化完成！")
    print("     - L1 热记忆: vault/L1_atlas/")
    print("     - L2 温记忆: vault/L2_decisions/")
    print("     - L3 冷数据: vault/L3_archive/")
    print("     - 外部 Agent 写入缓冲: vault/inbox/")

if __name__ == "__main__":
    init_vault()

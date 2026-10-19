#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Know-Yourself OS - Vault Initializer (Zero-Dependency)
一键初始化或重置本地数据主权目录 (vault/) 与基础骨架模板。
"""

import sys
import shutil
import argparse
from pathlib import Path

# Windows GBK 终端编码兼容处理
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def init_vault(force=False):
    root = Path(__file__).resolve().parent.parent
    vault_dir = root / "vault"
    templates_dir = root / "templates"
    examples_dir = root / "examples"

    # 1. 确保核心子目录与 .gitkeep 存在
    subdirs = ["L1_atlas", "L2_decisions", "L3_archive", "inbox"]
    for sub in subdirs:
        p = vault_dir / sub
        p.mkdir(parents=True, exist_ok=True)
        gitkeep = p / ".gitkeep"
        if not gitkeep.exists():
            gitkeep.touch()

    vault_gitkeep = vault_dir / ".gitkeep"
    if not vault_gitkeep.exists():
        vault_gitkeep.touch()

    # 2. 初始化 L1 Atlas 境遇全景图
    atlas_target = vault_dir / "L1_atlas" / "situational_atlas.md"
    atlas_source = templates_dir / "L1_situational_atlas.md"
    if (not atlas_target.exists() or force) and atlas_source.exists():
        shutil.copy(atlas_source, atlas_target)
        print(f"[*] 写入 L1 活跃境遇快照: {atlas_target}")

    # 3. 初始化个人认知偏差注册表
    bias_target = vault_dir / "L1_atlas" / "bias_registry.md"
    bias_source = templates_dir / "personal_bias_registry.md"
    if (not bias_target.exists() or force) and bias_source.exists():
        shutil.copy(bias_source, bias_target)
        print(f"[*] 写入个人认知偏差库: {bias_target}")

    # 4. 初始化全局状态索引 brain_index.json
    index_target = vault_dir / "brain_index.json"
    index_source = examples_dir / "sample_brain_index.json"
    if (not index_target.exists() or force) and index_source.exists():
        shutil.copy(index_source, index_target)
        print(f"[*] 写入全局状态索引: {index_target}")

    # 5. 初始化示例 PDR 决策记录
    demo_pdr_target = vault_dir / "L2_decisions" / "PDR-20260401-001.md"
    demo_pdr_source = examples_dir / "PDR-20260401-001.md"
    if (not demo_pdr_target.exists() or force) and demo_pdr_source.exists():
        shutil.copy(demo_pdr_source, demo_pdr_target)
        print(f"[*] 写入首个演练决策记录: {demo_pdr_target}")

    print("\n[OK] Know-Yourself 本地外脑 (vault/) 初始化完成！")
    print(f"     - 存储根路径: {vault_dir}")
    print("     - 热记忆 (L1 Atlas): vault/L1_atlas/")
    print("     - 温记忆 (L2 PDRs):  vault/L2_decisions/")
    print("     - 冷记忆 (L3 Arch):  vault/L3_archive/")
    print("     - Agent写入缓冲池:  vault/inbox/")
    print("提示：现在可直接双击打开仓库根目录的 Know-Yourself.html 开启可视化工作台！\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Know-Yourself 本地外脑初始化工具")
    parser.add_argument("--force", action="store_true", help="强制覆盖重置 vault 内的基础模板与索引")
    args = parser.parse_args()
    init_vault(force=args.force)

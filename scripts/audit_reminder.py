#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Know Yourself OS - Decision Review Auditor
扫描 vault/L2_decisions/ 目录下已到达复盘日期 (review_date) 的决策记录，提醒进行事后硬核复盘。
"""

import sys
import re
from datetime import datetime, date
from pathlib import Path

# Windows GBK 兼容处理
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def parse_frontmatter(content):
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    if not m:
        return {}
    fm = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip().strip("'\"")
    return fm

def check_audits():
    root = Path(__file__).resolve().parent.parent
    l2_dir = root / "vault" / "L2_decisions"
    
    if not l2_dir.exists():
        print("[-] 未找到 vault/L2_decisions 目录，请先运行 init_vault.py 初始化。")
        return

    today = date.today()
    due_list = []
    active_count = 0

    for file_path in l2_dir.glob("*.md"):
        if file_path.name.startswith("."):
            continue
        try:
            content = file_path.read_text(encoding="utf-8")
        except Exception:
            continue
        
        fm = parse_frontmatter(content)
        review_date_str = fm.get("review_date")
        status = fm.get("status", "executing")

        if status in ["executing", "deliberating"] and review_date_str:
            active_count += 1
            try:
                review_date = datetime.strptime(review_date_str, "%Y-%m-%d").date()
                if review_date <= today:
                    due_list.append((file_path.name, fm.get("title", file_path.stem), review_date_str, status))
            except ValueError:
                pass

    print(f"\n==================================================")
    print(f" Know Yourself 决策看板审计 (今日: {today})")
    print(f"==================================================")
    print(f"[*] 活跃监测中决策总数: {active_count}")

    if not due_list:
        print("[OK] 暂无到期需要事后复盘的决策记录。所有推进项均在观察期内。")
    else:
        print(f"\n[WARN] 发现 {len(due_list)} 项决策已到达预设复盘日期！请立即执行阶段三事后复盘：\n")
        for fname, title, rdate, st in due_list:
            print(f"  - 决策文件: vault/L2_decisions/{fname}")
            print(f"    标题: {title}")
            print(f"    预设复盘日: {rdate} (状态: {st})")
            print(f"    操作建议: 请挂载 templates/PDR_decision_record.md 第三大步骤，开展假设碰撞并提炼元规律。\n")

if __name__ == "__main__":
    check_audits()

# -*- coding: utf-8 -*-
"""
packs_to_seed.py — 34 域包 → 上游 skills.json 种子条目（包级粒度）

与旧版 cards_to_seed.py（卡级 72 条）不同，本脚本以「域包」为单位生成种子条目：
- skill_name = 包 slug；instruction = SKILL.md 总纲正文 + 完整版指引页脚
- ID 一律走 id_ledger.json 台账（既有者复用，新包取最大序号+1，一编永不变）
- 产物：seed-addition-packs.json + PACK_BUILD_REPORT.json + 台账回写

运行：C:/Python314/python.exe packs_to_seed.py（managed Python 缺 PyYAML）
"""
import json
import re
import time
from pathlib import Path

import yaml

ROOT = Path(r"D:\AlcheMvision\judian-skills")
CATEGORIES = ["drama", "creative", "ecommerce"]
LEDGER_PATH = ROOT / "seed-contribution" / "id_ledger.json"
OUT_PATH = ROOT / "seed-contribution" / "seed-addition-packs.json"
REPORT_PATH = ROOT / "seed-contribution" / "PACK_BUILD_REPORT.json"

FOOTER = """

---

**完整版**：本条目为域包总纲。34 个域包的完整卡片（开源署名层 86 卡 + 书籍重铸层 673 卡）位于
[itsWyatt-K/judian-skills](https://github.com/itsWyatt-K/judian-skills)——技能页 → 安装技能 → GitHub →
填入仓库地址与包路径（如 `skills/{cat}/{name}`）即可安装，Agent 可按总纲名录逐卡深读。
来源与许可见各卡 frontmatter：开源署名层逐卡标注 source/license（MIT/Apache-2.0/CC-BY-4.0/官方文档署名）；
书籍重铸层标注 source_book + attribution（方法论自撰重写，不复制原文表达）。"""


def parse_skill_md(path: Path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n(.*)$", text, re.S)
    if not m:
        raise ValueError(f"frontmatter 解析失败: {path}")
    fm = yaml.safe_load(m.group(1))
    body = m.group(2).strip()
    return fm, body


def main():
    ledger = json.loads(LEDGER_PATH.read_text(encoding="utf-8"))
    id_map = ledger["map"]
    id_base = int(ledger["id_base"])
    max_seq = max((int(v) - id_base for v in id_map.values()), default=0)

    now = int(time.time())
    entries = []
    problems = []
    idx = 0
    by_tag = {}

    for cat in CATEGORIES:
        cat_dir = ROOT / "skills" / cat
        for pack_dir in sorted(p for p in cat_dir.iterdir() if p.is_dir()):
            # 只收域包（有 cards/ 目录）与门房技能；排除工作区残留的旧单卡包目录
            is_domain_pack = (pack_dir / "cards").is_dir()
            is_concierge = pack_dir.name == "scene-recipe-concierge"
            if not (is_domain_pack or is_concierge):
                continue
            skill_md = pack_dir / "SKILL.md"
            if not skill_md.exists():
                problems.append(f"缺 SKILL.md: {pack_dir}")
                continue
            fm, body = parse_skill_md(skill_md)
            name = fm.get("name")
            desc = (fm.get("description") or "").strip()
            if name != pack_dir.name:
                problems.append(f"name 与目录名不一致: {name} != {pack_dir.name}")
            if not desc:
                problems.append(f"description 为空: {pack_dir}")

            if name in id_map:
                sid = id_map[name]
            else:
                max_seq += 1
                sid = str(id_base + max_seq)
                id_map[name] = sid

            idx += 1
            by_tag[cat] = by_tag.get(cat, 0) + 1
            entries.append({
                "skill_id": sid,
                "skill_name": name,
                "description": desc,
                "instruction": body + FOOTER.format(cat=cat, name=name),
                "status": 1,
                "markdown_url": "",
                "create_time": now,
                "update_time": now,
                "source": 3,
                "tag": cat,
                "sort_weight": 200 + idx,
                "is_private": False,
                "like_count": 0,
                "owner_uid": "",
                "effective_user": {
                    "name": "剧典技能库（itsWyatt-K）",
                    "avatar_url": "",
                    "uid": ""
                },
                "showcase_media": [],
                "added_count": 0,
                "extra_info": ""
            })

    out_text = json.dumps(entries, ensure_ascii=False, indent=2)
    OUT_PATH.write_text(out_text, encoding="utf-8")

    ledger["map"] = dict(sorted(id_map.items(), key=lambda kv: int(kv[1])))
    ledger["note_pack_batch"] = (
        "2026-09-21 追加 34 个域包条目（序号 73-106 段）；"
        "旧 72 条卡级条目（序号 1-72 段）已被域包结构取代，编号封存永不复用。"
    )
    LEDGER_PATH.write_text(
        json.dumps(ledger, ensure_ascii=False, indent=2), encoding="utf-8")

    report = {
        "generated_at": now,
        "mode": "pack",
        "entries": len(entries),
        "by_tag": by_tag,
        "instruction_total_kb": round(sum(len(e["instruction"]) for e in entries) / 1024, 1),
        "id_range": [entries[0]["skill_id"], entries[-1]["skill_id"]] if entries else [],
        "problems": problems,
        "output": str(OUT_PATH),
    }
    REPORT_PATH.write_text(
        json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"条目数: {len(entries)}  分类: {by_tag}")
    print(f"instruction 合计: {report['instruction_total_kb']} KB")
    print(f"ID 区间: {report['id_range']}")
    if problems:
        print("问题清单:")
        for p in problems:
            print(f"  - {p}")
        raise SystemExit(1)
    print("校验通过：name/description/ID 分配无问题")


if __name__ == "__main__":
    main()

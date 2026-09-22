#!/usr/bin/env python3
"""presets_check.py — 场景预设对账门禁（提交前必跑）

校验 presets.json：
  1. schema：version==1；presetId 唯一且 kebab-case；name/scene/rationale/source/evidence 合规
  2. 引用：每个 skillId 必须存在于种子快照（默认 seed-snapshot.json）——v1 只引用已上架技能
  3. 预算：每个预设 1-8 个技能（影策每轮激活上限 8），预设内不重复
  4. 策略：v1 强制 source=hand-curated（遥测驱动要等 #590 有数据）

用法：
  python presets_check.py                      # 用仓库内种子快照对账
  python presets_check.py --seeds <path>       # 用上游最新 skills.json 对账（跨仓库漂移检测）

种子快照刷新（上游种子变更时）：
  git -C <open-ai-canvas> show <sha>:backend/internal/skills/seed/skills.json > /tmp/seeds.json
  python presets_check.py --refresh-snapshot /tmp/seeds.json
"""
import argparse
import json
import re
import sys

SCENES = {"drama", "creative", "ecommerce", "social", "others"}
EVIDENCE = {"E1", "E2", "E3", "E4", "E5"}


def load_seed_ids(path):
    data = json.load(open(path, encoding="utf-8"))
    if isinstance(data, dict) and "skills" in data:
        entries = data["skills"]
        if entries and isinstance(entries[0], dict) and "skillId" in entries[0]:
            return {e["skillId"] for e in entries}  # 快照格式
        return {e.get("skill_id") or e.get("id") or e.get("skillId") for e in entries}  # 上游原始格式
    return {e.get("skill_id") or e.get("id") or e.get("skillId") for e in data}


def refresh_snapshot(upstream_path):
    data = json.load(open(upstream_path, encoding="utf-8"))
    entries = data["skills"] if isinstance(data, dict) and "skills" in data else data
    snap = {
        "source": "upstream skills.json refresh",
        "captured": __import__("datetime").date.today().isoformat(),
        "count": len(entries),
        "skills": [
            {"skillId": e.get("skill_id") or e.get("id") or e.get("skillId"),
             "name": e.get("name") or e.get("skill_name"),
             "tag": e.get("tag")}
            for e in entries
        ],
    }
    json.dump(snap, open("seed-snapshot.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("snapshot refreshed:", snap["count"], "skills")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seeds", default="seed-snapshot.json", help="种子清单（快照或上游原始 skills.json）")
    ap.add_argument("--refresh-snapshot", metavar="UPSTREAM_JSON", help="用上游最新 seeds 刷新快照后退出")
    args = ap.parse_args()

    if args.refresh_snapshot:
        refresh_snapshot(args.refresh_snapshot)
        return 0

    seed_ids = load_seed_ids(args.seeds)
    data = json.load(open("presets.json", encoding="utf-8"))
    errors = []

    if data.get("version") != 1:
        errors.append("version 必须为 1")
    presets = data.get("presets", [])
    if not presets:
        errors.append("presets 为空")

    ids = [p.get("presetId", "") for p in presets]
    if len(ids) != len(set(ids)):
        errors.append("presetId 重复")

    for p in presets:
        pid = p.get("presetId", "?")
        if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", pid):
            errors.append(f"{pid}: presetId 必须 kebab-case")
        sids = p.get("skillIds", [])
        if not (1 <= len(sids) <= 8):
            errors.append(f"{pid}: 技能数 {len(sids)} 超出 1-8（激活位上限）")
        if len(set(sids)) != len(sids):
            errors.append(f"{pid}: skillIds 有重复")
        for sid in sids:
            if sid not in seed_ids:
                errors.append(f"{pid}: skillId {sid} 不在种子清单（v1 禁止引用未上架技能）")
        if p.get("scene") not in SCENES:
            errors.append(f"{pid}: scene 必须是 {sorted(SCENES)} 之一")
        if p.get("source") != "hand-curated":
            errors.append(f"{pid}: v1 强制 source=hand-curated")
        if p.get("evidence") not in EVIDENCE:
            errors.append(f"{pid}: evidence 必须是 {sorted(EVIDENCE)}")
        rationale = p.get("rationale", "")
        if not rationale or len(rationale) > 200:
            errors.append(f"{pid}: rationale 为空或超 200 字")

    refs = sum(len(p.get("skillIds", [])) for p in presets)
    covered = len({s for p in presets for s in p.get("skillIds", [])})
    print(f"预设数: {len(presets)} | 引用总数: {refs} | 覆盖技能数: {covered}")
    if errors:
        print("GATE FAIL:")
        for e in errors:
            print(" -", e)
        return 1
    print("GATE PASS：全部预设通过（ID 唯一 / scene 合法 / 引用均已上架 / ≤8 / rationale≤200）")
    return 0


if __name__ == "__main__":
    sys.exit(main())

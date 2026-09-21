# -*- coding: utf-8 -*-
"""probe_loop.py — 验证「检索 → 读取」闭环（方案稿验收标准 ②）
明确要求：先 skill_search，再根据返回去读命中的卡/SKILL.md，不许猜路径。
"""
import json
import pathlib
import sys
import time
import uuid

sys.path.insert(0, r"D:\AlcheMvision\_work_tmp")
import ab_runner as A  # noqa: E402

OUT = pathlib.Path(r"D:\AlcheMvision\资料\14-影策技能生态升级方案\AB运行记录")

SKILLS = [
    "2c5ce559f394b03a3d8f8760d13f470f",  # shortform-drama-playbook（28 卡）
    "51006859912cfa4177edda775b246484",  # h3-video-prompt-suite（11 卡）
    "d56dba4e48594384e23a83aaebc1c9db",  # consumer-psychology（41 卡）
]

PROMPT = """我要写一条 3 分钟以内反转短剧的分镜。请严格按下面两步做，不要跳步：

第一步：调用 skill_search，关键词用「反转 结构 钩子」。
第二步：根据 skill_search 返回的内容，用 skill_read_file 去读它给出的路径——
       如果返回的是 cards/… 路径就直接读那张卡；如果是 SKILL.md 就看返回的 cards 索引挑一张读。
       不要自己猜路径，不要读返回之外的东西。

读完后只回答两件事：① 你检索到了什么（path 与 score）；② 你读了哪张卡、它讲了什么要点（三句话以内）。"""


def main():
    A.login()
    canvas_id, _ = A.create_canvas("PROBE-loop-%s" % time.strftime("%m%d-%H%M"))
    payload = {
        "canvasId": canvas_id,
        "prompt": PROMPT,
        "channelId": "CHANNEL_000020",
        "channelModelKey": "step-5-preview-intl",
        "permissionMode": "read_only",
        "contextScope": ["canvas"],
        "skillIds": SKILLS,
        "budget": {"maxCredits": 12000},
        "idempotencyKey": "loop-%s" % uuid.uuid4().hex[:10],
    }
    r = A.api("POST", "/api/agent/runs", payload, timeout=30)
    run = (r.get("data") or {}).get("run") or {}
    rid = run.get("id")
    if not rid:
        print("创建失败:", json.dumps(r, ensure_ascii=False)[:400])
        return
    print("run:", rid)
    final = A.poll(rid, max_wait=600)
    ev = A.fetch_events(rid)
    ans = A.extract_answer(ev)
    stem = "probe_loop_%s" % rid[:8]
    (OUT / (stem + ".events.txt")).write_text(ev, encoding="utf-8")
    (OUT / (stem + ".answer.md")).write_text(ans or "(未提取到答案)", encoding="utf-8")
    (OUT / (stem + ".meta.json")).write_text(json.dumps(
        {"arm": "probe_loop", "skills": SKILLS, "run_id": rid,
         "status": final.get("status"), "answer_len": len(ans),
         "tool_failed": ev.count("tool_failed")}, ensure_ascii=False, indent=2),
        encoding="utf-8")
    print("完成 status=%s 答案长度=%d tool_failed=%d -> %s"
          % (final.get("status"), len(ans), ev.count("tool_failed"), stem))


if __name__ == "__main__":
    main()

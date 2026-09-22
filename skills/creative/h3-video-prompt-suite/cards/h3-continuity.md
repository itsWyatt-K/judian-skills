---
name: h3-continuity
description: 当用户说"接不上 / 跳了 / 转场生硬"时调用。关键触发：接不上 / 跳了 / 转场生硬。工位边界：本技能只做H3 跨视频衔接策略，不产出完整分镜表与成片流程；后者由上游市场技能『叙事短片导演分镜』等负责，两者接力不抢戏。
source_book: MiniMax H3 官方文档与社区规范（2026-08 核验）
source_chapter: "首尾输入与参考输入 / 跨视频衔接公式"
tags: [h3, continuity, 衔接, 首尾帧, 变形桥, 转场, AI生成友好]
layer_confidence: "candidate"
pack: MiniMax H3 提示词规范
core_stance: ""  # TODO: 待补写
skill_type: "framework"  # TODO: 复核
consult_tier: "B（琥珀区·公开书籍方法论）"  # TODO: 复核
verify_state: raw
card_type: book
publish_tier: tier-attrib
source_repo: "MiniMax H3 官方技能文档（即梦 Dreamina 官方 skills 语料，raw-materials/MiniMax-H3-skills）"
source_license: "MiniMax 官方文档（署名引用）"
upstream_defer: ["叙事短片导演分镜"]
first_seen: 2026-08-14
source_card: MiniMax H3 提示词规范/h3-continuity
evidence: E4

---

## R — 原文 (Reading)

H3 的输入分两类且**不得混在同一请求**：`first_frame`/`last_frame` 属图生视频；`reference_image`/`reference_video`/`reference_audio` 属 reference-to-video。连接首尾画面时，首尾输入之间有明确"变形桥梁"时衔接效果最好，桥梁可以是颜色、光线、建筑或主体姿势。跨视频衔接公式：`[视频1] + [转场] + 连接到[视频2] + [转场逻辑]`，参考输入分别给视频 1 与视频 2，提示词形如 "Connect Video 1 to Video 2 in 8 seconds…"。

## I — 方法论骨架 (Interpretation)

每个镜头在 shot-prompts.json 里必须带一个 `衔接策略` 字段，二选一：

1. **首尾帧衔接**（强约束，用于同场景连续动作）：
   - 上一镜的尾帧 = 下一镜的首帧（同一张图，物理保证连续）。
   - 适用：动作接力（起身→走位）、同机位推拉、对白正反打的轴线保持。
   - 注意：用了 first_frame/last_frame 就不能再带 reference_image，角色一致性只能靠提示词文字描述兜底——所以首尾帧方案要求资产卡的视觉锚点抄进保留关系段。
2. **变形桥衔接**（弱约束，用于跨场景/跨时空）：
   - 选一个跨镜头保持的锚：颜色（红伞→红门）、光线（同一束逆光）、建筑（同一面墙）、姿势（同一背影）。
   - 提示词写明桥梁："保留上一镜的红色元素作为转场桥梁，连接到…"。
   - 适用：转场、回忆切入、漫剧分格过渡。

**选哪个**：同场景连续动作→首尾帧；跨场景→变形桥；拿不准→变形桥（不锁死画面，容错高）。

## A1 — 书中的应用 (Past Application)

- **同场景接力**：镜头 3 角色摔门，镜头 4 门外反应——镜头 3 尾帧作镜头 4 首帧，门的位置物理连续，无跳轴感。
- **跨时空变形桥**：现实办公室冷蓝光 → 回忆老家暖黄光，桥梁选"主体姿势"（同一个托腮动作），提示词写"保留托腮姿势，光线由冷蓝渐变为暖黄，连接到回忆场景"。

## A2 — 触发场景 (Future Trigger)

- 阶 ⑨：每生成一镜，自动为它与上一镜之间填衔接策略字段。
- 阶 ⑩ 衔接轴会审：逐对相邻镜头检查——策略是否写明、桥梁锚是否真实存在于两镜、首尾帧方案是否违规混用参考素材。
- 语言信号："接不上 / 跳了 / 转场生硬"。

## E — 可执行步骤 (Execution)

1. **判类型**：下一镜与上一镜是否同场景连续动作？是→首尾帧；否→变形桥。
   *完成标准*：策略二选一并记录理由。
2. **首尾帧分支**：导出上一镜尾帧 → 设为下一镜 first_frame；检查下一镜请求未携带 reference_*；把资产卡视觉锚点抄入保留关系段。
   *完成标准*：无输入类型混用。
3. **变形桥分支**：从颜色/光线/建筑/姿势里选一个在两镜中都存在的锚 → 写进提示词（"保留 X 作为桥梁，连接到…"）。
   *完成标准*：桥梁锚在两镜画面里都可被指出。
4. **登记**：把策略写进 shot-prompts.json 该镜的 `衔接策略` 字段。
   *完成标准*：字段非空，会审衔接轴可读。

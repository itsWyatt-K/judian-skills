---
name: h3-asset-binding
description: "当用户说\"换镜头变脸 / 角色不一致 / 画风漂移\"时调用。关键触发：换镜头变脸 / 角色不一致 / 画风漂移。工位边界：本技能只做H3 素材角色绑定，不产出完整分镜表与成片流程；后者由上游市场技能『叙事短片导演分镜』等负责，两者接力不抢戏。"
tags: ["h3", "asset-binding", "reference-image", "角色一致性", "全能参考", "AI生成友好"]
metadata:
  version: 1.0.0
  source: MiniMax H3 官方技能文档（即梦 Dreamina 官方 skills 语料，raw-materials/MiniMax-H3-skills）
  license: MiniMax 官方文档（署名引用）
  attribution: "Methodology distilled from a public source (open-source project, official model documentation, or published book) with attribution; only the methodology is distilled and no original expression is reproduced."
---

## R — 原文 (Reading)

H3 的 reference-to-video 支持 `reference_image`/`reference_video`/`reference_audio` 三类参考素材；提示词内用 `<Subject1>`、`<Picture1>` 等别名引用。全能参考控制允许同时给多份参考图（角色/场景/道具），模型在生成时保留参考图的身份特征。注意：参考素材与首尾帧（first_frame/last_frame）分属两类输入，不得混在同一请求。角色资产卡的视觉锚点（脸型/发型/服装/配色）由 ip-character-bible 定义，画风规范字段由 ip-style-decoupling 解耦——换画风不重写人物。

## I — 方法论骨架 (Interpretation)

资产绑定三步：

1. **资产卡 → 参考图**：assets.json 里每张角色卡/场景卡/道具卡对应一张参考图（角色定妆照/场景概念图/道具特写）。参考图质量决定一致性上限：角色参考图必须正脸、光线均匀、无遮挡。
2. **参考图 → 素材别名**：在提示词素材定义段声明——`<Subject1> = 角色A定妆照（reference_image）`、`<Picture1> = 客厅场景图（reference_image）`。一镜内别名唯一。
3. **别名 → 保留关系**：在保留关系段写"保留 <Subject1> 的脸型/发型/服装"——文字侧保险，与参考图双保险。漫剧/真人风格差异只写在画风规范字段（如"2D 国漫平涂风格"），不改人物描述。

**一致性失效排查序**：先查参考图质量（是否正脸/清晰）→ 再查保留关系段是否抄全视觉锚点 → 最后查是否违规混用首尾帧。

## A1 — 书中的应用 (Past Application)

- **双角色同框**：`<Subject1>`=角色A、`<Subject2>`=角色B，保留关系段分别声明两人锚点；生成时两人身份不互串。
- **漫剧改真人**：同一份角色卡，画风规范字段从"2D 国漫平涂"改为"真人实拍质感"，人物描述不动——ip-style-decoupling 的画风解耦在 H3 侧的落地。

## A2 — 触发场景 (Future Trigger)

- 阶 ⑧→⑨ 交接：资产卡确认后，逐张绑定为素材别名，产出绑定清单（assets.json 增补 alias 字段）。
- 阶 ⑩ 衔接轴：检查角色资产跨镜一致（别名是否全程指向同一参考图）。
- 语言信号："换镜头变脸 / 角色不一致 / 画风漂移"。

## E — 可执行步骤 (Execution)

1. **核对参考图**：每个角色/场景/道具是否有合格参考图？角色图必须正脸清晰；缺图→先补图再绑定。
   *完成标准*：assets.json 每项含 reference_image 路径。
2. **分配别名**：按出场顺序给资产分配 `<Subject1..n>`/`<Picture1..n>`，写入 assets.json 的 alias 字段；全片别名映射唯一且不变。
   *完成标准*：别名映射表生成。
3. **写进提示词**：每镜素材定义段声明本镜用到的别名；保留关系段抄资产卡视觉锚点。
   *完成标准*：抽任一镜，别名与 assets.json 一致。
4. **画风检查**：漫剧/真人风格只出现在画风规范字段，人物描述无风格词污染。
   *完成标准*：换画风无需改人物段。

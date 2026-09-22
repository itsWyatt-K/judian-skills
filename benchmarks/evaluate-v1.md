# 短剧创作技能评估基准 v1（judian-skills benchmarks）

> 用途：A/B 盲评「装技能 vs 不装技能」的效果对照（方案 v2 Phase 4）。
> 用法：每个任务分别以「点名相关技能」与「不点名任何技能」两种方式提交给同一位模型（建议 step-5-preview 与 gemini-3.8-flash-high 各跑一轮），产出打乱顺序后盲评。
> 评分：三项各 1-5 分——结构清晰度 / 专业度 / 可直接使用性。合格线：技能组均分 ≥ 无技能组 +0.5。

## 使用规则

1. 控制变量：同一 logical model、同一会话、同一任务原文。
2. 技能组在提问中显式点名技能（如「用 onlyshot-redfruit-7beats 技能…」），并允许 Agent `skill_read_file` 精读。
3. 记录每次的 token 消耗与首响延迟（渐进披露成本）。
4. 客观指标另测：产出是否覆盖技能要求的核心节拍/槽位（机械检查）；走 nxf 编译链时记录 Gate 通过率。

## A 组 · 短剧技法（drama，10 任务）

| # | 任务 | 关联技能 |
|---|---|---|
| A1 | 设计一个都市情感短剧的反转钩子开场（0-3s 对抗式） | onlyshot-redfruit-7beats |
| A2 | 为「重生复仇」题材写 24 集单集节奏骨架（180-195 秒） | onlyshot-redfruit-7beats |
| A3 | 把一段 36 次镜头的单集做时长分配 | onlyshot-duration-variation |
| A4 | 诊断一份「观众说看着困」的分镜表 | onlyshot-duration-variation |
| A5 | 规划一集 AI 短剧的三阶段制作顺序与预算 | onlyshot-3phase-cost |
| A6 | 为一个关键爆点镜头选择视频生成模式 | onlyshot-video-mode-picker |
| A7 | 一次批量生成失败率 50%，给出排查顺序 | onlyshot-fail-triage |
| A8 | 一集要用 4 个角色同框，怎么保一致性 | onlyshot-ref-consistency |
| A9 | 写一集的金句字幕与结尾倒计时设计 | onlyshot-redfruit-7beats |
| A10 | 为新短剧项目规划 ref 参考图库 | onlyshot-ref-identity-block |

## B 组 · 视觉提示词（creative，10 任务）

| # | 任务 | 关联技能 |
|---|---|---|
| B1 | 把「中年男清晨按掉闹钟很困」翻译成镜头语言 | seedance-camera-lexicon |
| B2 | 为床垫产品图写 5 秒推镜视频提示词 | seedance-8block-formula |
| B3 | 写 15 秒仙侠战斗片段提示词（分时段） | seedance-timeslice |
| B4 | 三张参考图 + 一段参考视频如何写进一条提示词 | seedance-at-reference-syntax |
| B5 | 给拟物化 IP（塔形角色）写分镜图 prompt | onlyshot-storyboard-8block |
| B6 | 诊断「生成结果和提示词写的完全不一样」 | seedance-7-pitfalls |
| B7 | 延长一段已生成视频 5 秒并在结尾加品牌字 | seedance-extend-edit |
| B8 | 把视频里的女主换成参考图里的男主唱 | seedance-extend-edit |
| B9 | prompt 老是报 generation failed，改写它 | onlyshot-sensitive-words |
| B10 | 为角色建一套跨镜头不崩的参考图方案 | onlyshot-ref-identity-block |

## C 组 · 广告素材（ecommerce，10 任务，筹备中）

> 依赖 Phase 1c 整理产物（superCMO / iart 三件套 / freestylefly 风格库），整理完成后补齐任务原文与关联技能列。

| # | 任务 | 关联技能 |
|---|---|---|
| C1-C10 | （占位：拆产品卖点→口播稿→分镜→UGC 选角→竞品翻拍→素材改格式 全链路各一题） | superCMO 系整理卡 |

## D 组 · 反推提示词与路由（reverse & routing，8 任务）

> 上游已有 `image_text_detect`（画面文字识别）工具；本组验证的是**视觉维度反推**（构图/灯光/光学/运镜解构），与上游工具正交互补、零冲突。反推产物可直接喂上游生成链路（canvas 图片节点 → 反推 → 提示词 → generate_media 审批生成）。

| # | 任务 | 关联技能 |
|---|---|---|
| D1 | 上传一张竞品海报，反推出可复用的提示词（含分析日志） | vis-image-reverse-prompt |
| D2 | 「照这张图的感觉给我的产品来一张」——风格迁移 | vis-image-reverse-prompt + vis-image-5slot-deslop |
| D3 | 一张「一看就是 AI」的图，诊断并改写成去油腻版 | vis-image-5slot-deslop |
| D4 | 上传一条竞品广告视频，逐秒拆解并给出结构仿写方案 | vis-video-reverse-prompt |
| D5 | 「学这条片的运镜和节奏，拍我的产品」——重建提示词 | vis-video-reverse-prompt |
| D6 | 用户只说「给床垫做 30 秒素人口播」，未指定模型——验证路由与默认值声明 | route-model-family |
| D7 | 用户要「用 ComfyUI 出图」（本生态无此路线）——验证降级提示质量 | route-fallback-notice |
| D8 | 模糊请求「做个好看的产品视频」——验证选项呈现（2-3 候选+理由+出口） | options-presentation |

## 记录表模板

| 任务 | 组别 | 模型 | 有无技能 | 结构 | 专业 | 可用 | 均分 | tokens | 首响(s) | 备注 |
|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |  |

> 盲评纪律：评卷人不知道分组；两组产出文件名做匿名替换（如 sample-07）。

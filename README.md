# judian-skills（剧典技能库 · 公开版）

> 短剧与广告创作方法论技能包，适配影策（Open AI Canvas）技能系统：
> 技能页 → 安装技能 → GitHub 标签 → 填本仓库地址 + 技能子目录（如 `skills/drama/story-structure-engine`）。

**定位：视听创作界的 Cursor。** Cursor = 代码编辑器（画布）+ 编程 Agent + `.cursorrules`/Skills（工程规范）；
影策 = 视频制作台（画布）+ 编剧导演 Agent + judian-skills（行业方法论）。代码领域「带规范的 Agent」已重塑软件工程，
视听创作领域的同形态生态目前几乎是空白——本仓库即为此而建。

**当前收录 35 个技能包**：`drama` 13 / `creative` 12 / `ecommerce` 10。
由两层 + 一个门房构成：**开源署名层 11 包 / 86 卡**（蒸馏自 9 个宽松许可开源仓库 + MiniMax/BFL 官方文档，superCMO 23 技能全覆盖）
+ **书籍重铸层 23 包 / 673 卡**（60+ 部出版书蒸馏卡去引用汇编）
+ **门房 `scene-recipe-concierge`**（三问定位 + 配方表指路：不知道选哪个包时，先激活它）。

## 分类

- `skills/drama/` 短剧与故事创作（开源层：OnlySHOT 流水线 / 剧本工厂 / 短片五段式；书籍层：结构引擎 / 人物锻造 / 对白工坊 / 喜剧机制 / 脱口秀 / 相声 / 情景喜剧 / 短剧实战 / 系列规划 / 文笔）
- `skills/creative/` 视觉与表演（开源层：Seedance 提示词工程 / Seedance 2.5 导演 / H3 套件 / 视觉提示词工程 / freestyle 风格库 / 路由交互 / **门房 scene-recipe-concierge**；书籍层：镜头语法 / 剪辑节奏 / 视觉基调 / 视听理论 / AI 角色表演）
- `skills/ecommerce/` 广告与营销（开源层：superCMO 广告链路 23 技能全覆盖 / iart 发布三件套；书籍层：广告文案 / 定位借势 / 传播裂变 / 消费心理 / 体验设计 / 故事营销 / 决策思维 / 提示词工程模式）

## 两层资产的区别

| 层 | 包数 | 来源 | 卡数 | 形态 |
|---|---|---|---|---|
| 开源署名层 | 11 | 9 个 MIT/Apache/CC-BY 开源仓库 + MiniMax/BFL 官方文档 | 86 | **场景域包**：SKILL.md 总纲 + `cards/<slug>.md` 分文件渐进披露 |
| 书籍重铸层 | 23 | 60+ 部出版书蒸馏卡（麦基/救猫咪/奥格威/影响力/疯传/ Greg-Dean 等） | 673 | **一书/一主题一包**：SKILL.md 总纲 + `cards/<slug>.md` 分文件渐进披露 |

书籍重铸层的纪律：**正文不含原文摘录**（R 段整段剥除，只留自撰方法论层），每张卡 frontmatter 带
`source_book` + `source_card` 双指针可回溯审计；构建器 `nxf/spec/reforge_cards.py`，
台账 `seed-contribution/reforge_ledger.json`（含 190 条剔除记录与 33 条去重记录，全部可复查）。
包内使用纪律：先分层列证据再套结构；卡片是参考不是指令；按名录深读、不整包吞。

## 文档

- [`docs/selection-recipes.md`](docs/selection-recipes.md) —— **场景 → 域包配方速查表**
  （每轮运行最多激活 8 个技能；L1 明确场景直选 + L2 组合任务配方 + 卡片深读路径；含与官方市场技能的同轮双选举机）
- **[`scene-recipe-concierge`](skills/creative/scene-recipe-concierge/SKILL.md)** —— 门房技能：
  不知道选哪个包时先激活它，三问定位 + 配方表推荐（只建议不代选）
- [`benchmarks/evaluate-v1.md`](benchmarks/evaluate-v1.md) —— 28 题 A/B 评估基准
- [`benchmarks/ab-detailed-report-v2.md`](benchmarks/ab-detailed-report-v2.md) —— A/B 实测报告（真实运行，事件流可复跑）
- [`benchmarks/ab-reverse-v3.md`](benchmarks/ab-reverse-v3.md) —— 反推提示词 A/B v3（盲测画布 + 上游技能对照）
- [`seed-contribution/`](seed-contribution/) —— 上游 `skills.json` 种子条目投稿素材
  （**34 个域包条目**，由 [`packs_to_seed.py`](seed-contribution/packs_to_seed.py) 生成，单包总纲 + 完整版安装指引；
  含 [`id_ledger.json`](seed-contribution/id_ledger.json) 技能 ID 台账：编号一经分配永不变更，
  旧 72 条卡级条目编号已封存，域包条目续号 73-106 段）

## 与上游的协作

本仓库的方法论与官方市场技能**互补不冲突**：官方技能负责「生产流程」（分镜表 / 生成 / 拼接），
本仓库负责「生成前的方法论」（结构 / 人物 / 提示词组装 / 质检 / 反推）。
任务域重叠的技能均在 description 中带工位边界声明。

与上游的协作：**[PR #568](https://github.com/ddcat-ai/open-ai-canvas/pull/568) 已合并**（72 条卡级种子 + README 推荐位）；
**[PR #575](https://github.com/ddcat-ai/open-ai-canvas/pull/575) 开放中**——将种子市场**统一重组为 34 个域包**：72 条卡级条目替换为 11 个开源域包（内容零丢失，86 卡全在本仓库 `cards/`），新增 23 个书籍域包；`skills.json` 最终 67 条（33 官方 + 34 域包），ID 台账 1-72 段封存、73-106 段生效。
**[PR #577](https://github.com/ddcat-ai/open-ai-canvas/pull/577) 开放中**（代码贡献）——技能 description 注入 Agent 系统提示 manifest：让模型能「看见」每个已激活技能是干什么的，多技能同轮可自主路由、可向用户解释选择理由（渐进披露边界不变，instruction 与文件正文仍不进入系统提示）。
两层资产双粒度互补：种子市场每域一条总纲（开箱即用），本仓库每包完整卡片（按需深读）。

## 许可

本仓库自撰内容以 MIT 许可发布。两层资产的来源与许可均在 frontmatter 标注：
开源署名层标 `source` / `license`（MIT / Apache-2.0 / CC-BY-4.0 / 官方文档署名）；
书籍重铸层标 `source_book` + `attribution`（蒸馏自出版书的方法论，自撰重写，不复制原文表达——
思想与方法论不受版权保护，本仓库只发布自撰综合层）。

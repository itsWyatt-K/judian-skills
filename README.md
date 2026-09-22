# judian-skills（剧典技能库 · 公开版）

> 短剧与广告创作方法论技能包，适配影策（Open AI Canvas）技能系统：
> 技能页 → 安装技能 → GitHub 标签 → 填本仓库地址 + 技能子目录（如 `skills/drama/story-structure-playbook`）。

## 这个仓库是什么

一批**创作方法论技能包**，装在影策里给 Agent 用。每个包 = 一份总纲（SKILL.md，含卡片名录与输出契约）
+ 若干张方法论卡（`cards/<slug>.md`，按需深读，不整包塞进上下文）。

它不生产画面，也不替代影策的生成链路；它负责**生成之前的判断**——结构怎么搭、人物怎么立、
提示词怎么组装、什么算合格。

## 当前状态（v2.0.0 · 2026-09-22）

**已提交 35 个包**：34 个域包（759 张卡）+ 门房 `scene-recipe-concierge`。
分层：开源署名层 11 包 / 86 卡 + 书籍重铸层 23 包 / 673 卡。

v2.0.0 做了一次**可用性改造**（不是内容扩充）：

1. **补卡路径断链** —— 影策生成通道的挑卡算法要求卡路径出现在总纲文本里，否则直接淘汰。
   改造前 759 张卡中列了完整路径的是 0 张；改造后 34/34 个包在各自专业任务下都能选出卡。
2. **补输出契约** —— 每个包明确「交付什么 / 冲突时听谁 / 用户没说时默认什么 / 怎么自检」。
3. **标注证据等级** —— 每张卡标 `evidence: E4`（出版方法重铸）。
4. **中文化与分类对齐** —— 名称由英文 slug 改为中文，分类对齐影策五分类。

### 还没做到的（如实说明）

- **证据等级全部是 E4，没有 E1**。E4 = 专业方法成立；E1 = 在当前模型上做过真实成片验证。
  我们**没有**做过逐卡实测，所以没有一张卡有资格标 E1。
- **没有证明「装上就提升成片质量」**。现有 A/B 只在云端 Agent 通道测得 79 → 89（见下），
  而用户日常勾选技能的那条生成通道**尚未做同题对照**。
- **工作区还有 86 个单文件技能目录未纳入版本管理**，本仓库只提交了上述 35 个包。

## 两种使用形态

同一个方法论，本仓库提供两种粒度，按场景选：

| 形态 | 位置 | 什么时候用 |
|---|---|---|
| **域包**（35 个） | `skills/drama|creative|ecommerce/` | 需要系统攻一个主题：总纲给你全貌，按名录深读具体某张卡 |
| **单文件技能**（56 个） | `skills/singles/` | 只解决一个具体问题：整个技能就是一个完整方法，装上一个就能用 |

`singles/` 下的 56 个技能是从 759 张卡里挑出的**招牌卡**——判据是「用户带着具体困扰来」
（description 以"当用户说…/当需要…"开头）且卡内自带方法论骨架与产出物。
每张卡原文完整保留，只换了中文名、影策 tag，并补了一段输出契约。
卡内 frontmatter 的 `promoted_from` 字段指向它来自哪张卡，可回溯。

## 演示媒体

`showcase/` 目录有 90 张卡片图（34 张域包图 `pack-<slug>.png` + 56 张单文件技能图 `<slug>.png`），
由 `scripts` 外的本地脚本生成，随仓库版本化，URL 形如
`https://raw.githubusercontent.com/itsWyatt-K/judian-skills/main/showcase/pack-<slug>.png`。

**说明**：这些是**信息卡片图**（技能名 + 一句话能力 + 卡数/关键词），不是 AI 生成的示例成片。
选它而不是 AI 抽卡图，理由是：卡片传递的是这个技能到底能干什么的**真实信息**，
而 AI 示例图与技能方法关联弱、只是装饰，且风格杂乱。示例成片待有真实使用案例后再补。

## 分类

- `skills/drama/` 短剧与故事创作（结构引擎 / 人物锻造 / 对白工坊 / 喜剧机制 / 脱口秀 / 相声 / 情景喜剧 / 短剧实战 / 系列规划 / 文笔 / 镜头语法 / 视听理论 等）
- `skills/creative/` 视觉与表演（Seedance 提示词工程 / Seedance 2.5 导演 / H3 套件 / 视觉提示词工程 / freestyle 风格库 / 路由交互 / 剪辑节奏 / 视觉基调 / AI 角色表演 / **门房**）
- `skills/ecommerce/` 广告与营销（superCMO 广告链路 / iart 发布三件套 / 广告文案 / 定位借势 / 传播裂变 / 消费心理 / 体验设计 / 故事营销 / 决策思维 / 提示词工程模式）

## 两层资产的区别

| 层 | 包数 | 来源 | 卡数 | 形态 |
|---|---|---|---|---|
| 开源署名层 | 11 | 9 个 MIT/Apache/CC-BY 开源仓库 + MiniMax/BFL 官方文档 | 86 | SKILL.md 总纲 + `cards/<slug>.md` 渐进披露 |
| 书籍重铸层 | 23 | 60+ 部出版书蒸馏卡 | 673 | SKILL.md 总纲 + `cards/<slug>.md` 渐进披露 |

书籍重铸层的纪律：**正文不含原文摘录**（只留自撰方法论层），每张卡 frontmatter 带
`source_book` + `source_card` 双指针可回溯审计；台账 `seed-contribution/reforge_ledger.json`
（含剔除与去重记录，可复查）。

## A/B 实测记录（含结论，不只列文件名）

| 报告 | 规模 | 结论 |
|---|---|---|
| [`ab-pilot-report-v1.md`](benchmarks/ab-pilot-report-v1.md) | 单任务两组 | 试点，技能组胜 |
| [`ab-full-report-v1.md`](benchmarks/ab-full-report-v1.md) | 28 任务 × 2 条件 = 56 次真实运行 | **无法判定**（方法论缺陷，详见报告） |
| [`ab-detailed-report-v2.md`](benchmarks/ab-detailed-report-v2.md) | 三方对照（含上游现有技能） | 见报告 |
| [`ab-reverse-v3.md`](benchmarks/ab-reverse-v3.md) | 9 次真实运行，step-5，盲测画布 | 见报告 |
| [`AB黄金测试-盲评记录.md`](benchmarks/AB黄金测试-盲评记录.md) | 3 任务 × 2 臂，step-5 | 基线 79 → 实验 89（+10） |

**黄金测试那 +10 分的边界必须说清**：它走的是**云端 Agent 通道**（`POST /api/agent/runs`），
而用户日常用的是**生成通道**（生成面板勾选技能、内容拼进提示词）。两条通道取卡方式不同，
前者能读到卡，后者在 v2.0.0 之前一张卡都拿不到（见上「补卡路径断链」）。
所以这 +10 分**不能直接推论到用户可感的生成通道**——那条通道的同题对照尚未做。

另有一份负结果记录：三次自由跑实测，模型**没有自发调用**检索工具（调用次数 0/0/0），
说明「能力可用」与「会被使用」是两件事。见 [`benchmarks/README.md`](benchmarks/README.md)。

## 文档

- [`docs/PACK-UPGRADE-CONTRACT.md`](docs/PACK-UPGRADE-CONTRACT.md) —— v2.0.0 改造规范、动机、实测证据与验收标准
- [`docs/selection-recipes.md`](docs/selection-recipes.md) —— 场景 → 域包配方速查表（每轮最多激活 8 个技能）
- [`scene-recipe-concierge`](skills/creative/scene-recipe-concierge/SKILL.md) —— 门房技能：不知道选哪个包时先激活它，三问定位 + 配方表推荐（只建议不代选）
- [`seed-contribution/`](seed-contribution/) —— 上游 `skills.json` 种子投稿素材（35 条域包条目，由 `packs_to_seed.py` 生成；`id_ledger.json` 为 ID 台账，编号一经分配永不变更）

## 与上游的协作

官方市场技能负责「生产流程」（分镜表 / 生成 / 拼接），本仓库负责「生成前的方法论」
（结构 / 人物 / 提示词组装 / 质检 / 反推）。任务域重叠的技能均在 description 中带工位边界声明。

- **[PR #568](https://github.com/ddcat-ai/open-ai-canvas/pull/568) 已合并** —— 72 条卡级种子 + README 推荐位
- **[PR #575](https://github.com/ddcat-ai/open-ai-canvas/pull/575) 开放中** —— 种子市场统一重组为 34 个域包，`skills.json` 最终 67 条，ID 台账 1-72 段封存、73-106 段生效
- **[PR #577](https://github.com/ddcat-ai/open-ai-canvas/pull/577) 开放中** —— 技能 description 注入 Agent 系统提示 manifest，让模型能「看见」每个已激活技能是干什么的

## 许可

本仓库自撰内容以 MIT 许可发布。来源与许可均在 frontmatter 标注：
开源署名层标 `source` / `license`；书籍重铸层标 `source_book` + `attribution`
（出版书方法论的自撰重写，不复制原文表达）。

# judian-skills（剧典技能库 · 公开版）

> 短剧与广告创作方法论技能包，适配影策（Open AI Canvas）技能系统：
> 技能页 → 安装技能 → GitHub 标签 → 填本仓库地址 + 技能子目录（如 `skills/drama/onlyshot-3phase-cost`）。

**当前收录 70 个技能包**：`drama` 14 / `creative` 44 / `ecommerce` 12。

## 分类

- `skills/drama/` 短剧技法（节奏校准 / 时长配额 / 失败分诊 / 一致性 / 审核词）
- `skills/creative/` 视觉提示词（Seedance 组装 / Seedance 2.5 / MiniMax H3 官方规范 / 视觉反推 / 路由与交互）
- `skills/ecommerce/` 广告素材（superCMO 口播链路 / iart 发布片与卡点 / 产品图）

## 文档

- [`docs/selection-recipes.md`](docs/selection-recipes.md) —— **场景 → 8 技能配方速查表**
  （每轮运行最多激活 8 个技能；含与官方市场技能的同轮双选举机）
- [`benchmarks/evaluate-v1.md`](benchmarks/evaluate-v1.md) —— 28 题 A/B 评估基准
- [`benchmarks/ab-detailed-report-v2.md`](benchmarks/ab-detailed-report-v2.md) —— A/B 实测报告（真实运行，事件流可复跑）
- [`seed-contribution/`](seed-contribution/) —— 上游 `skills.json` 种子条目投稿素材（70 条）

## 与上游的协作

本仓库的方法论与官方市场技能**互补不冲突**：官方技能负责「生产流程」（分镜表 / 生成 / 拼接），
本仓库负责「生成前的方法论」（节奏校准 / 提示词组装 / 质检 / 反推）。
任务域重叠的技能均在 description 中带工位边界声明。

已向上游提交集成 PR：**[ddcat-ai/open-ai-canvas#568](https://github.com/ddcat-ai/open-ai-canvas/pull/568)**
（新增 70 个种子技能 + README 推荐位）。合入后所有影策实例开箱即用。

## 许可

本仓库自撰内容以 MIT 许可发布；来自第三方开源项目的蒸馏内容在每张卡 frontmatter 中标注
来源与许可（`source_repo` / `source_license` / `source_book`）；MiniMax H3 系列为官方文档署名引用。

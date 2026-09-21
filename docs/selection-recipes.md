# 场景 → 域包配方速查表（每轮激活 ≤8 的选法 · 34 域包版）

> 背景：影策 Agent 每轮运行**最多激活 8 个技能**，且只能读本轮激活的技能。judian-skills 已重组为 **34 个场景域包**（开源署名层 11 包 + 书籍重铸层 23 包，共 769 卡）——一域一包占一个激活位，包内卡片经 `skill_read_file` 渐进披露按需深读。
> 用法：按场景从下表选 1-4 个域包（**不凑数**，激活越多上下文越贵）；「→上游」表示生产环节交给影策官方市场技能（同轮双选，实现「我方方法论 → 上游生产」接力）。
> 域包内选卡：激活包后先读 SKILL.md 总纲，按名录只深读任务需要的卡——不要整包吞。

## L1 · 明确场景直选（一击命中）

| 场景 | 激活域包 | 打法 |
|---|---|---|
| **H3（即梦）视频出片** | `h3-video-prompt-suite` | 官方六段式/首尾帧衔接/资产绑定全在这包；风格片（3D 动画/MV/纸模定格等 9 种）按需深读对应 style 卡 |
| **Seedance 生视频** | `seedance-prompt-engineering` | 8block 公式/参考图语法/运镜词库/七坑自查；官方规范优先于通用方法论 |
| **Seedance 2.5 导演级** | `seedance-25-director-craft` | 模式选择/资产锁表/时序审计/剪辑公式；需多镜头连续性时用 |
| **FLUX 图像/资产图** | `visual-prompt-engineering` | 四层结构/HEX 控色/无负向词/角色一致性；与 `model-routing-interaction` 同轮选 |
| **竞品广告克隆/翻拍** | `supercmo-ad-chain` | 深读 clone-structure + competitor-research + competitor-id；版权边界：结构可仿、表达不可抄 |
| **产品视频/口播广告** | `supercmo-ad-chain` | 深读 hook-patterns + script-budget（每秒 2-3 词）+ spoken-language + product-video-ads |
| **GPT-Image2 信息图/风格图** | `freestyle-style-library` | 模板匹配/提示词块/陷阱清单；pitfalls 卡装负向约束 |
| **写小说/剧本台词** | `prose-craft` 或 `dialogue-workshop` | 前者是叙述文笔，后者是对白专项 |
| **写脱口秀段子** | `standup-craft` | Greg Dean 笑话结构（铺垫/笑点/排练轮） |

## L2 · 组合任务配方（多包同轮）

| # | 任务 | 域包组合（≤8 位） |
|---|---|---|
| 1 | **红果短剧单集**（A/B 实测场景） | `onlyshot-shortform-pipeline`（骨架：7 节点秒级节奏）+ `model-routing-interaction`（入口：模型族+规范准入）+ `visual-tone-design`（骨架：场景五要素）+ **→上游「叙事短片导演分镜」**（生产：节奏落地为分镜表） |
| 2 | **短剧全剧立项/大纲** | `story-structure-engine`（结构坐标系）+ `character-forge`（人物弧光）+ `series-arc-planning`（跨集规划）+ `options-presentation` 卡（含在 model-routing-interaction 包内，模糊请求选项呈现）+ **→上游「故事开发」** |
| 3 | **广告全链路**（调研→概念→脚本→分镜） | `supercmo-ad-chain`（主战：campaign-planning→ad-copy→storyboard-sheets 全链）+ `consumer-psychology`（卖点背后的行为学依据）+ `ad-copywriting`（文案打磨：标题八式/长文案）+ **→上游「顶级波普视觉广告导演」** |
| 4 | **电商大图/系列图** | `visual-prompt-engineering`（四层结构+控色）+ `freestyle-style-library`（模板与陷阱）+ `supercmo-ad-chain`（深读 product-description + product-photo-modes）+ **→上游「系列套图生成」** |
| 5 | **参考片反推/竞品拆解** | `visual-prompt-engineering`（深读 vis-image-reverse-prompt + vis-video-reverse-prompt）+ `supercmo-ad-chain`（深读 clone-structure）+ `model-routing-interaction`（模型族准入）+ **→上游「一图成片-电影广告全能导演」** |
| 6 | **剧本质检/交稿机检** | `factory-script-machine`（工厂机检）+ `dialogue-workshop`（对白诊断）+ `onlyshot-shortform-pipeline`（深读 sensitive-words + fail-triage）+ `visual-tone-design`（词汇层质检） |
| 7 | **生成失败排查** | `onlyshot-shortform-pipeline`（三分诊）+ `model-routing-interaction`（模型族切换+降级提示）+ `seedance-prompt-engineering`（七坑自查）+ `seedance-25-director-craft`（深读 timing-audit + continuity-locks） |
| 8 | **品牌定位/营销策略** | `positioning-strategy`（心智阶梯/找洞）+ `story-marketing`（故事经济学）+ `decision-thinking`（决策模型）+ `viral-contagion`（传播设计） |
| 9 | **喜剧创作**（相声/情景喜剧/漫才） | `comedy-mechanics`（笑点机制）+ `standup-craft`（脱口秀结构）+ `xiangsheng-craft`（相声三翻四抖）+ `sitcom-lab`（情景喜剧结构） |
| 10 | **AI 角色表演**（IP 短片/数字人） | `ai-performance-lab`（表演提示词全家桶：表情/肢体/情绪节拍）+ `character-forge`（人设一致性）+ `visual-tone-design`（视觉基调）+ **→上游视频生成技能** |

## 卡片深读路径（包内怎么选卡）

每包 SKILL.md 总纲都带**卡片名录**（每卡一行一句话索引）。标准动线：

1. 激活包 → Agent 自动读总纲（何时调用/何时不用/名录/工位边界）；
2. 任务命中哪张卡的名录描述 → `skill_read_file` 深读那张卡（每页 12000 字符）；
3. 一轮任务通常只需深读 1-3 张卡，**不整包吞**。

---

## 三条使用纪律

1. **同轮双选实现接力**：需要「我方想清楚 → 上游做出来」的场景，把两侧技能都选上（A/B 融合复测验证：Agent 会主动读双方并正确分工）；
2. **不凑数**：少于 8 位就少选——激活越多上下文越贵；上游官方市场技能与本库域包可同轮混选；
3. **库随便装**：34 个域包可全部装进技能库（库无数量限制），每轮按本表选 ≤8；种子市场条目与仓库包一一对应，装了就长期可用。

## 附：34 域包速览

| 类 | 域包 |
|---|---|
| drama (13) | story-structure-engine / character-forge / dialogue-workshop / comedy-mechanics / standup-craft / xiangsheng-craft / sitcom-lab / prose-craft / series-arc-planning / shortform-drama-playbook / shortfilm-structure / factory-script-machine / onlyshot-shortform-pipeline |
| creative (11) | h3-video-prompt-suite / seedance-prompt-engineering / seedance-25-director-craft / visual-prompt-engineering / freestyle-style-library / model-routing-interaction / shot-grammar / editing-rhythm / visual-tone-design / audiovisual-theory / ai-performance-lab |
| ecommerce (10) | supercmo-ad-chain / ad-copywriting / positioning-strategy / consumer-psychology / story-marketing / viral-contagion / experience-design / decision-thinking / prompt-engineering-patterns / iart-launch-trio |

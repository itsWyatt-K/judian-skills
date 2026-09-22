# 新手场景推荐表（说人话 → 装哪个技能）

> 这份表服务一个具体痛点：**打开技能库面对 120+ 个技能，不知道挂什么**。
> 用法：在最左边的「用户原话」里找到你的场景 → 装上「起步单卡」（一个就能用）→ 需要更深体系时再按「进阶」加域包。
>
> 前置阅读：[`selection-recipes.md`](selection-recipes.md)（域包配方速查表，每轮最多激活 8 个技能）。

## 怎么用（三步）

1. **说人话查表**：不用记任何包名，用你自己的话在下表找场景。
2. **先装起步单卡**：56 个单文件技能（`skills/singles/`）每个只解决一个具体问题，装上就能用——新手一次只装 1 个，别贪多。
3. **不够用再加深**：单卡解决「这一个问题」，域包（34 个）解决「一整套流程」。同轮可以混选（每轮上限 8 个激活位）。

安装方式：种子市场搜技能中文名即装；或 GitHub 装（仓库 `itsWyatt-K/judian-skills`，单卡在 `skills/singles/<分类>/<目录名>/`）。

**诚实声明**：本表所有技能目前都是 **E4 级**——成熟专业方法的重铸，尚未经当前模型逐题实测（E1/E2 级标注要等达尔文评估跑完，见 README「还没做到的」）。单卡是从 759 张方法论卡里按「用户带着具体困扰来」挑出的招牌卡。

## 场景总表（短剧 / 故事 / 画面 / 广告 / 定位 / 运营）

### 写短剧（红果 / 抖音 / 竖屏）

| 用户原话 | 起步单卡（先装这个） | 进阶（不够用时加） |
|---|---|---|
| "开篇留不住人，前三秒秒划" | **短剧开篇八法与付费点**（czks-hook-paywall） | + 域包 `shortform-drama-playbook` |
| "不爽，没有追下一集的欲望" | **爽点与钩子设计**（dxj-audience-hook） | + 域包 `onlyshot-shortform-pipeline`（7 节点秒级节奏） |
| "结尾太平，想再来个反转" | **反转结尾写法**（ssqr-twist-ending） | + 域包 `story-structure-engine` |
| "想写温情收尾但怕糊弄" | **暖式反转回报**（warm-twist-payoff） | — |
| "一集写完不知道有没有戏" | **一场戏有没有戏**（tvd-dramatic-beat） | + 域包 `factory-script-machine`（交稿机检） |

### 故事与剧本通用

| 用户原话 | 起步单卡 | 进阶 |
|---|---|---|
| "主角成长写得假 / 突然想通" | **正向成长弧光**（cca-positive-arc） | + 域包 `story-structure-engine` |
| "写反派起源 / 主角一步步变坏" | **负向弧光与堕落**（cca-negative-arc） | + 域包 `character-forge` |
| "主角不讨喜，观众不进戏" | **主角不讨喜诊断**（save-the-cat-diagnosis） | + **人设反差构建**（persona-contrast-builder） |
| "主角坚定不成长，怎么写" | **平弧：不成长也好看**（cca-flat-arc） | — |
| "确认我的故事是什么类型" | **救猫咪十类型**（save-the-cat-genre-ten-types） | + **救猫咪不变法则**（save-the-cat-laws） |
| "写群像，一群人关系没变化" | **群像变化设计**（wfs-group-change） | + **变化闭环收束**（wfs-change-closure） |
| "试播集既要独立又要勾长线" | **试播集设计**（tvd-pilot-design） | + 域包 `series-arc-planning` |
| "角色跨集人格跳变" | **分集人物一致性**（tvd-episodic-characterization） | — |
| "写完怕落入温情流水套路" | **反套路守门**（wfs-anti-trope-guard） | — |
| "台词尴尬 / 平铺直叙" | **对白节拍设计**（mckee-dialogue-beats） | + **对白欲望先行**（mckee-dialogue-desire） |
| "背景信息不知道怎么交代" | **exposition 藏进动作**（mckee-dialogue-exposition） | + 域包 `dialogue-workshop` |
| "写不讨喜的主角" | **非英雄主角**（kom-non-hero） | + **荒唐目标可信化**（kom-winning） |
| "英雄时刻写得俗" | **表演式英雄主义**（performative-heroism） | — |
| "代际/权力冲突吵架没设计感" | **关系隐喻镜头**（kom-perspective-lens） | — |

### 画面 / 镜头 / 生成提示词

| 用户原话 | 起步单卡 | 进阶 |
|---|---|---|
| "H3（即梦）提示词不会写" | **H3 六段式提示词**（h3-prompt-six-section） | + **H3 参考资产绑定**（h3-asset-binding） |
| "换镜头就变脸 / 画风漂移" | **H3 参考资产绑定**（h3-asset-binding） | + 域包 `h3-video-prompt-suite` |
| "Seedance 提示词不可复现" | **Seedance 八块公式**（seedance-8block-formula） | + 域包 `seedance-prompt-engineering` |
| "一句想法怎么出图" | **生图五槽去油腻模板**（vis-image-5slot-deslop） | + 域包 `visual-prompt-engineering` |
| "画面没电影感 / 基调不对" | **视觉基调七要素**（vis-seven-elements） | + **对比与亲和定调**（vis-contrast-affinity） |
| "同一事件拍成笑还是惨" | **视角四选法**（vis-viewpoint-first） | — |
| "一场戏拆成可执行镜头" | **视频镜头卡十四字段**（vis-video-shot-card） | + 域包 `shot-grammar` |
| "该不该用运动镜头" | **运动镜头选择**（gfl-camera-movement） | — |
| "对话机位左右关系老翻" | **对话机位与屏幕方向**（gfl-screen-direction） | — |

### 角色表演（AI 视频 / 数字人）

| 用户原话 | 起步单卡 | 进阶 |
|---|---|---|
| "AI 角色表演僵硬 / 模式化" | **AI 角色表演分层写法**（ai-acting-master） | + 域包 `ai-performance-lab` |
| "情绪变化写得突兀" | **情绪戏动作节拍**（emotion-action-beats） | — |

### 口播带货 / 广告投放

| 用户原话 | 起步单卡 | 进阶 |
|---|---|---|
| "参数很硬用户无感" | **数据变可感证据**（factual-evidence） | + 域包 `supercmo-ad-chain` |
| "推广文案像商家推销" | **朋友口吻推广文案**（friend-chat-title） | + 域包 `ad-copywriting` |
| "知识付费推广标题没点击" | **知识付费推广标题**（practical-tip-title） | — |
| "社会证明会不会反效果" | **社会证明适用条件**（social-proof-conditions） | — |
| "结果一样却因'看起来轻松'被压价" | **让努力被看见**（effort-visibility-premium） | — |
| "道理都懂就是不动" | **未来的自己具体化**（future-self-vividness） | — |
| "竞对清单过期 / 不知道谁是真竞对" | **双通道竞对发现**（supercmo-competitor-id） | + 域包 `supercmo-ad-chain` |

### 品牌 / 定位 / 策略

| 用户原话 | 起步单卡 | 进阶 |
|---|---|---|
| "品类心智格子被占满了" | **定位心智图**（positioning-mind-mapping） | + 域包 `positioning-strategy` |
| "该不该用老品牌打新品类" | **品牌延伸陷阱**（positioning-line-extension-trap） | — |
| "多个机会押注哪一头" | **职业赛马定位**（positioning-career-horse） | + **双轨分析法**（dual-track-analysis） |
| "品牌目的怎么讲" | **目的型故事**（purpose-told-story） | + 域包 `story-marketing` |

### 内容运营 / 服务流程

| 用户原话 | 起步单卡 | 进阶 |
|---|---|---|
| "内容线规划没章法" | **内容操盘手视角**（cmo-showrunner） | — |
| "服务流程设计没结构" | **工作即戏剧结构**（work-is-theatre-drama-structure） | — |
| "想让顾客带着改变离开" | **把顾客变成作品**（transformation-customer-as-product） | — |
| "方案总被搁置" | **可用性赢得认同**（usability-buy-in） | — |
| "输出风格时好时坏" | **人格系统设定**（personality-system） | — |

### 社媒日常（X / 推文）

| 用户原话 | 起步单卡 | 进阶 |
|---|---|---|
| "面对空白屏幕不会起笔" | **短内容结构选择**（x-short-content-craft） | + **发布前完备检查**（x-five-piece-checklist） |
| "一周发布数据怎么复盘" | **周数据复盘流程**（x-data-review） | — |

## 反模式（新手最常踩的三个坑）

1. **一次装八个**：激活位每轮上限 8 个，但激活越多上下文越贵、模型越容易在方法论之间仲裁失灵。一个具体问题 → 一个单卡，解决完再换。
2. **拿单卡干域包的活**：单卡只讲一个方法点。要「从立项到交稿的完整流程」（如红果短剧单集），直接上 `selection-recipes.md` 的 L2 组合配方。
3. **官方技能和我方技能盲目混挂**：同主题两套方法论（官方是单文件 SOP，我方是多卡体系），模型可能给出不同建议需要仲裁。混挂前先想好你要哪一套当主、哪一套当生产环节（接力用法见 selection-recipes 纪律 1）。

## 附：56 个单卡按场景速查（目录名 → 中文名）

> 装的时候在种子市场搜**中文名**；GitHub 路径是 `skills/singles/<分类>/<目录名>/`。

- **短剧**：czks-hook-paywall（短剧开篇八法与付费点）/ dxj-audience-hook（爽点与钩子设计）/ ssqr-twist-ending（反转结尾写法）/ warm-twist-payoff（暖式反转回报）/ tvd-dramatic-beat（一场戏有没有戏）
- **故事结构**：cca-positive-arc / cca-negative-arc / cca-flat-arc / save-the-cat-diagnosis / save-the-cat-genre-ten-types / save-the-cat-laws / wfs-group-change / wfs-change-closure / wfs-anti-trope-guard / tvd-pilot-design / tvd-episodic-characterization
- **人物对白**：persona-contrast-builder / kom-non-hero / kom-winning / kom-perspective-lens / performative-heroism / mckee-dialogue-beats / mckee-dialogue-desire / mckee-dialogue-exposition
- **生成提示词**：h3-prompt-six-section / h3-asset-binding / seedance-8block-formula / vis-image-5slot-deslop
- **视觉镜头**：vis-seven-elements / vis-contrast-affinity / vis-viewpoint-first / vis-video-shot-card / gfl-camera-movement / gfl-screen-direction
- **表演**：ai-acting-master / emotion-action-beats
- **带货广告**：factual-evidence / friend-chat-title / practical-tip-title / social-proof-conditions / effort-visibility-premium / future-self-vividness / supercmo-competitor-id
- **品牌定位**：positioning-mind-mapping / positioning-line-extension-trap / positioning-career-horse / dual-track-analysis / purpose-told-story
- **运营服务**：cmo-showrunner / work-is-theatre-drama-structure / transformation-customer-as-product / usability-buy-in / personality-system
- **社媒**：x-data-review / x-five-piece-checklist / x-short-content-craft

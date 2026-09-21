---
name: h3-style-brand-promo-video
description: "当用户要做\"品牌宣传片/产品发布短片/官网展示/社交媒体推广\"且提供 LOGO 与产品素材时使用。触发词：品牌宣传片、brand promo、产品发布、官网视频、logo 短片、品牌广告。本卡只提炼官方 skill 的叙事与视觉技法要素。工位边界：本技能只做 H3 提示词规范，不替代上游市场技能的生产流程，后者由上游市场技能『顶级波普视觉广告导演』等负责，两者接力不抢戏。工位边界：本技能只做H3 品牌宣传片风格模板，不产出完整分镜表与成片流程；后者由上游市场技能『顶级波普视觉广告导演』等负责，两者接力不抢戏。"
tags: ["h3", "style", "brand", "promo", "宣传片", "产品发布", "logo", "叙事脊柱"]
metadata:
  version: 1.0.0
  source: MiniMax H3 官方技能文档（即梦 Dreamina 官方 skills 语料，raw-materials/MiniMax-H3-skills）
  license: MiniMax 官方文档（署名引用）
  attribution: "Methodology distilled from a public source (open-source project, official model documentation, or published book) with attribution; only the methodology is distilled and no original expression is reproduced."
---

## R — 风格定义（Reading）

品牌宣传片 = 突出产品功能、使用场景、行动号召的短广告（通常 15-30s）。核心纪律是**资产真实**（LOGO/产品图必须来自已验证来源，绝不重绘仿制）+ **故事产品专属**（用真实功能叙事，不用抽象特效掩盖薄弱产品）。

适用边界：
- ✅ 新品发布、官网展示、社媒推广、有授权素材的品牌片
- ❌ 缺少授权素材时仿造品牌标识、虚构产品功能、长篇剧情片

## O — 视觉技法要素（技法萃取）

### 1. 叙事脊柱（按产品类型选）
- AI/SaaS：意图→思考→能力→执行→输出→证明→LOGO
- 实体产品：英雄展示→交互→功能特写→场景→结果→LOGO
- 服务/公司：背景→流程→证据→成果→承诺→LOGO
- 图像主导：真实影像→视觉母题→利益点→情绪回报→LOGO

### 2. 精确节拍（帧意识）
- 15s 建议 5-8 节拍，30s 建议 8-12 节拍
- 每节拍定义：时间/帧范围、视觉主导、产品证明、文案停留、色彩状态、转场、动作意图（铺垫/承诺/冲击/制动）
- 相邻动作自然衔接时可 6-12 帧重叠

### 3. 动效语言（可控强度）
- 让产品动作/光标/光线/几何驱动转场
- 2-5 个色彩状态，每节拍一主动作
- 2-3 个高能峰值 + 安静制动时刻
- 保持 LOGO/文案安全空间清晰可读

### 4. 资产真实纪律
- LOGO/产品界面/包装/字体/色彩系统必须来自已验证或用户授权来源
- 程序化图形只作非写实动效层（遮罩/渐变/粒子/转场几何）
- 绝不重绘或近似品牌标识

### 5. 调性与禁止项
- 调性：confident / clear / on-brand / premium
- 禁止：虚假 HUD、装饰文字墙、未验证指标、全片单一缓动、仿制 LOGO

## A — 与 H3 六段式映射
- `subject_definitions`：真实产品锚（注明来源资产 ID）；无虚构角色则不写角色段
- `detailed_description`：按节拍写产品动作+转场，每节拍一主事件
- `overall_mood`：confident / on-brand
- `overall_soundscape`：品牌安全纯音乐/UI 音效（H3 原生音频优先）；`non_diegetic_music` 写品牌调性

## S — 自写示例片段（原创）
> subject_definitions: <Subject 1> the verified product (matte black earbuds), centered, brand blue accent; <Picture 1> official product render.
> detailed_description: [Shot 1] At 00:00 hero shot of earbuds rotating slowly; at 00:04 UI mockup slides in showing pairing; at 00:08 logo lockup with safe space.
> overall_mood: confident, clear, on-brand.

## H — 红线
- 品牌资产必须真实来源，仿制 LOGO = 一票否决
- 故事必须产品专属，抽象特效掩盖薄弱叙事 = 失败
- 文案/LOGO 安全空间必须可读，不可被动效遮挡

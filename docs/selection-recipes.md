# 场景 → 8 技能配方速查表（每轮激活 ≤8 的选法）

> 背景：影策 Agent 每轮运行**最多激活 8 个技能**（skillIds maxItems=8），且**只能读本轮激活的技能**——技能库（已安装）可以装很多，但每轮要用必须入选。上游市场技能同样受此限。
> 用法：按场景从下表选一行（不足 8 个就少选，不凑数）；「→上游」表示该场景的产出环节交给上游市场技能（同轮双选，实现我方方法论→上游生产的接力）。

## 1. 红果短剧单集节奏（A/B 实测场景）

| # | 技能 | 角色 |
|---|---|---|
| 1 | route-model-family | 入口：定模型族 |
| 2 | model-spec-priority | 入口：官方规范准入 |
| 3 | onlyshot-redfruit-7beats | 骨架：7 节点秒级节奏 |
| 4 | onlyshot-duration-variation | 骨架：时长配额 |
| 5 | vis-video-scene-formula | 骨架：场景五要素 |
| 6 | seedance-7-pitfalls | 质检：提示词七坑 |
| 7 | vocab-audit-substitutes | 质检：词汇层 |
| 8 | **→上游「叙事短片导演分镜」** | 生产：节奏落地为九列分镜表 |

## 2. 短剧全剧立项/大纲

factory-emotion-contract（情绪契约+单元链）/ factory-episode-specs（单集规格）/ factory-ledger（台账）/ onlyshot-redfruit-7beats / options-presentation / route-fallback-notice / model-spec-priority / **→上游「故事开发」**

## 3. 广告 / UGC 投放素材

supercmo-hook-patterns（钩子库）/ supercmo-script-budget（口播预算）/ supercmo-spoken-language / supercmo-ugc-mode-select / iart-launch-arc / iart-ab-batch-variants / vocab-audit-substitutes / **→上游「顶级波普视觉广告导演」或「TikTok网红带货视频」**

## 4. 产品图 / 电商图

supercmo-product-description（产品五要素）/ supercmo-product-photo-modes（十格式）/ freestyle-template-match（风格库匹配）/ freestyle-prompt-blocks / freestyle-pitfalls / vis-image-5slot-deslop / vis-image-reverse-prompt / **→上游「系列套图生成」**

## 5. 参考片反推 / 竞品翻拍

vis-image-reverse-prompt（图反推）/ vis-video-reverse-prompt（视频逐秒拆解）/ supercmo-clone-structure（翻拍版权边界）/ options-presentation / model-spec-priority / vocab-audit-substitutes / seedance-7-pitfalls / **→上游「一图成片-电影广告全能导演」**

## 6. 生视频提示词组装（Seedance/2.5）

model-spec-priority / seedance-8block-formula / seedance-at-reference-syntax / seedance-camera-lexicon / sd25-mode-select / sd25-asset-lock-table / vis-video-universal-rules / vis-video-three-details

## 7. 剧本质检 / 交稿前机检

factory-episode-specs / factory-dialogue-doctor / factory-machine-check / onlyshot-sensitive-words / vocab-audit-substitutes / seedance-7-pitfalls / route-fallback-notice / options-presentation

## 8. 生成失败排查

onlyshot-fail-triage（三分诊）/ onlyshot-sensitive-words / onlyshot-ref-consistency / vocab-audit-substitutes / seedance-7-pitfalls / sd25-timing-audit / sd25-continuity-locks / route-model-family

## 9. H3（即梦）出片

h3-prompt-six-section（官方六段式）/ h3-continuity（首尾帧衔接）/ h3-asset-binding（素材绑定）/ onlyshot-video-mode-picker（4 模选择）/ onlyshot-fail-triage（即梦向分诊）/ onlyshot-sensitive-words / vocab-audit-substitutes / seedance-7-pitfalls

> H3 风格片（3D 动画/品牌片/游戏 intro/手绘/极简产品/MV/拼图解说/纸模定格）按需把对应 `h3-style-*` 换入上表前两位。

---

## 三条使用纪律

1. **同轮双选实现接力**：需要「我方想清楚→上游做出来」的场景，把两侧技能都选上（A/B 融合复测验证：Agent 会主动读双方并正确分工）；
2. **不凑数**：少于 8 个就少选——激活越多上下文越贵，渐进披露下未点名的技能正文不会被读，但元数据仍在上下文；
3. **库随便装**：59 个技能可全部 install/github 装进技能库（库无数量限制），每轮按本表选 ≤8。

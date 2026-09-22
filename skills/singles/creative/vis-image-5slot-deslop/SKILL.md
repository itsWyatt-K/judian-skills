---
name: 生图五槽去油腻模板
description: "把一句想法填成五槽模板直接出图：场景/主体/细节/用途/约束，顺手去油腻。"
tags: ["creative"]
metadata:
  version: 1.0.0
  promoted_from: vis-image-5slot-deslop
  evidence: E4
  source_book: "'visual-skills image 参考库（GitHub: smixs/visual-skills，CC-BY-4.0，署名 Serge Shima）'"
  source_card: "visual-skills 视觉叙事/vis-image-5slot-deslop"
---

# 图像五槽模板与去油腻

## R — 原文要点 (Reading)

来源方法（CC-BY-4.0，整理自 visual-skills image 参考库）：**GPT Image 2.5 五槽模板**——Scene（场景）/ Subject（主体）/ Important Details（重要细节）/ Use Case（用途）/ Constraints（约束）；参数杠杆 `quality: low/medium/high/xhigh/max` 是刻意的保真度旋钮；尺寸为 16 的倍数、最大 3:1、最高 4K（3840×2160）；编辑用两列逻辑（Change 改什么 / Preserve 保留什么 / Constraints 约束）；最多 16 张参考图且每张显式角色。**黄金规则**：动词开头、正向表述、十六进制色值、引号包文字、编辑不重掷（一次一改）。**去油腻（de-slop）**：模型默认先验会产生「一看就是 AI」的结果——禁用增压词（与视频侧同一禁单）；用**拍摄管线**替代形容词（机身+镜头+胶片+灯光设置+后期流程，如「shot on X, 50mm, available light, slight motion blur」）；植入**有位置的瑕疵**（located imperfections：特定位置的污渍/磨损/不对称），真实照片的不完美是定位的而非均匀的。**风格 DNA + 拒绝清单**：生成前用四行锁定强风格（主体处理/光线/色调/质感），生成后拿图对照 DNA 逐行验收。

## I — 方法论骨架 (Interpretation)

1. **五槽即检查表**：空槽=缺指令；约束槽放比例/文字/要避免的工件。
2. **保真度是旋钮不是祈祷**：quality 档位按交付物选，别一律 max。
3. **去油腻三板斧**：禁增压词→拍摄管线→定位瑕疵，三斧替代一切「更真实一点」的祈祷。
4. **风格 DNA 是验收标准**：没有四行 DNA，风格漂移无法判定；有 DNA，返工有依据。
5. **编辑最小作用域**：一次一改，改什么保留什么显式两列。

## A1 — 应用案例 (Past Application)

- 来源方法：UGC 真实感需求 → 拍摄管线（手机镜头+自然光+手持微晃）+ 定位瑕疵（袖口一处起球、杯沿一处水渍）→ 脱离「AI 光」。
- 风格固化：海报风格四行 DNA 写死后，批量出图逐张对照验收，漂移即返工。

## A2 — 触发场景 (Future Trigger)

- 用户说「这图一看就是 AI 画的」「不像参考图」。
- 要按模型写图提示词（Nano Banana / GPT Image 2.5 分流）。
- 批量出图的风格一致性验收。

## E — 可执行步骤 (Execution)

1. **模型分流**：先定 Nano Banana 还是 GPT Image 2.5（决定语法与特性）。
   *完成标准*：模型已定并在输出头部声明。
2. **五槽填空**：Scene/Subject/Details/UseCase/Constraints 逐槽写实。
   *完成标准*：五槽无空槽。
3. **去油腻三斧**：禁增压词→写拍摄管线→植入定位瑕疵。
   *完成标准*：无增压词，管线与瑕疵在位。
4. **DNA 四行**：主体/光线/色调/质感各一行锁定。
   *完成标准*：DNA 四行非空。
5. **编辑两列**：如为编辑任务，Change/Preserve/Constraints 三列写清。
   *完成标准*：两列边界清晰。

## 本技能交付什么

把一句想法填成五槽模板直接出图：场景/主体/细节/用途/约束，顺手去油腻。

### 内容保真优先级

1. **用户明确指定**（题材/风格/禁项/参考职责）；
2. 本技能的专业逻辑自洽；
3. 通用创作规律；
4. 风格与质感装饰。

### 默认决策

- 用户未指定时，按上文方法论骨架的默认分支执行；
- 交付前用一句话说明选了什么。

### 质量门槛

- [ ] 交付物包含上文要求的所有字段；
- [ ] 未把方法论参考当作指令执行，也未据此授权任何工具；
- [ ] 证据等级为 E4，表示"专业上成立"，不表示当前模型已实测验证。

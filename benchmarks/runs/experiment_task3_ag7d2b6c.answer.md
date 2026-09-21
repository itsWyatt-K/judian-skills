已读完 H3 六段式规范、品牌片风格卡、资产绑定与连续性四张卡。下面给结论和成品。

## 一、结论先说

**给你两版可用的东西：**
- **版本 A（单条 15 秒生成）**：纯文本直出，4 个节拍，可直接粘进 H3。适合先看整体气质。
- **版本 B（拆 3 条 5 秒生成）**：露珠特写和产品结尾分开做，可控性和成功率更高。适合正式交付。

**一个硬前提**：品牌片风格卡的铁律是「资产真实」——茶盒如果是真实产品，**必须用实拍图做参考图**，不能让模型凭空画一个"通用茶盒"再手写品牌名，那样 LOGO 和包装几乎一定是错的。你目前画布是空的，没有产品图，所以版本 A 按纯文本写，产品出场只做"材质+形态"描述，不写品牌标识。

---

## 二、15 秒节拍表（版本 A / B 共用）

| 时间 | 节拍 | 视觉主导 | 动作意图 |
|---|---|---|---|
| 00:00–00:03.5 | 茶山晨雾 | 大景，层叠茶垄+薄雾 | 铺垫 |
| 00:03.5–00:08 | 指尖掠芽、露珠滚落 | 微距特写，浅景深 | 情绪核心 |
| 00:08–00:12 | 露珠落篮、手移向下一芽 | 跟随手部，节奏连贯 | 过渡+呼吸感 |
| 00:12–00:15 | 茶盒升起，受光 | 静态微降机位，居中 | 承诺+制动 |

---

## 三、版本 A：单条 15 秒完整提示词（T2V，三段式）

```
integrated_multimodal_description:
[Shot 1] Morning mist drifts in slow sheets over layered tea terraces on a
green hillside; a girl in an indigo-dyed cotton tea-picking outfit and a
conical straw hat stands waist-deep among the tea rows, the lower half of her
figure veiled in thin fog. Camera: slow crane up, medium amplitude, gentle
speed, gradually revealing the scale of the tea mountain.

[Shot 2] At 00:03.500 Macro close-up: her fingertip brushes a tender tea bud
with two young leaves, the bud trembling, a round dew drop clinging to the
leaf edge then sliding down and falling. Camera: macro push in (zoom), small
amplitude, very slow speed, shallow depth of field holding only the fingertip
and the bud sharp.

[Shot 3] At 00:08.000 The falling dew drop lands in a woven bamboo tea basket,
a faint ripple crossing the surface; her hand moves on to the next bud in an
even, unhurried rhythm. Camera: follow tracking beside her hand, medium
amplitude, steady medium speed.

[Shot 4] At 00:12.000 A matte jade-green tea box rises slowly from the lower
frame into centered composition, fine dewdrops on its surface catching the
first sunlight, a soft sweep of light crossing the lid. Camera: static shot
with a slight pedestal down, small amplitude, slow speed, ending on the box
held cleanly in frame.

overall_soundscape: distant birdsong and light wind through tea leaves, the
faint dry rustle of buds touched by fingertips, one clear water droplet
landing; all kept low and airy, no crowd noise.

non_diegetic_music: solo guqin with a bamboo flute answering in the second
half, slow tempo around 70 BPM, one gentle swell at the product reveal then
immediate thinning to a single sustained note.
```

**这条为什么这么写：**
- 运镜全部按官方三段自然句（motion type + amplitude + speed）展开，不写 "cinematic push" 这种空词——模型对"slow crane up, medium amplitude, gentle speed"的执行确定性远高于"电影感推镜"。
- 4 个节拍正好卡在"单镜 ≤4 段"的红线内；15 秒写 6 段以上，H3 会出现动作打架和跳变。
- 声音两段都写了。这是官方明确要求：**即使静音也要写**，否则模型会自作主张加 BGM。
- 产品出场用 pedestal down（轻微降机位）而不是 zoom，是为了让茶盒"浮现"而不是"被放大"，避免廉价感。

---

## 四、版本 B：拆 3 条生成（推荐用于正式交付）

| 段落 | 时长 | 内容 | 衔接策略 |
|---|---|---|---|
| 镜头 1 | 5s | 晨雾茶山大景 + 少女入画 | 变形桥：**青绿色调 + 逆光雾气**贯穿全片 |
| 镜头 2 | 5s | 指尖掠芽、露珠滚落、落篮 | 首尾帧：镜头 1 尾帧 = 镜头 2 首帧（同场景连续动作） |
| 镜头 3 | 5s | 茶盒升起受光 + 留白收尾 | 变形桥：保留青绿主色 + 同一束侧逆光 |

拆分的好处：露珠这种高难度细节单独占 5 秒，模型算力集中，微距清晰度明显好于 15 秒里分到 4.5 秒。代价是要自己拼片段，且必须保证三条的 **seed 和风格词一致**，否则绿色会漂。

---

## 五、如果你有茶盒实拍图：升级为六段式

拿到真实产品图后，把版本 A 改成 Full-Reference Mode，只动两段：

```
subject_definitions:
<Picture 1> the verified tea box product photo (matte jade-green rigid box,
visible lid seam), single-line reference, not to be redrawn.

summary:
[reference generation] A 15-second Chinese-style tea brand promo; the tea
mountain and tea-picking scenes are text-generated, and the closing product
shot is anchored to <Picture 1> for packaging fidelity.

retention_analysis:
<Picture 1> packaging shape, surface material and color: fully_preserved
across [Shot 4]. Tea-mountain green palette and backlit haze: partially_preserved
across [Shot 1]–[Shot 4].
```

注意两条边界：**首尾帧和 reference_image 不能混在同一个请求里**；`<Picture 1>` 这类参考图锚要单独成行，只有 character_anchor 才内联引用。

---

## 六、哪些参数真正影响成片质量

| 参数 | 影响 | 这条片子的建议 |
|---|---|---|
| **duration** | 15 秒信息密度高但容易糊；H3 限 4–15 整数秒 | 先试版本 A 一条，正式交付用版本 B |
| **aspect_ratio** | 决定构图和裁切，改比例等于重做 | 16:9 走品牌官网/大屏；9:16 走抖音小红书，两者提示词里主体大小要调 |
| **seed** | 同 seed + 同 prompt 结果可复现；换 seed 绿色和雾感全变 | 版本 B 三条锁同一个 seed；镜头 2 露珠不满意时只微调 seed 重抽 |
| **negative_prompt** | 直接决定手部、文字、水印干不干净 | 必填：`deformed hands, extra fingers, wrong finger count, garbled text, watermark, logo artifacts, motion blur, oversaturated` |
| **reference_image** | 产品真实性和一致性的唯一保障 | 有茶盒图就一定要用；没图就只能做"通用茶盒"，不能写品牌名 |
| **风格/材质词具体度** | "国风"这种词模型理解差异极大 | 已拆成 indigo-dyed cotton / conical straw hat / matte jade-green / backlit haze 这类可生成词 |
| **音频支持** | H3 原生音频生成，若模型不支持音频则成片默片 | 需要声音时先在模型目录确认支持音频，别生成完再补 |
| **模型选择** | 不同模型对国风色调、微距细节、多图参考支持不同 | 多图参考必须选支持多图的模型，不能为了迁就模型丢掉参考图 |

最容易踩的三个坑：**① 一段里塞 5 个以上节拍 → 动作跳变；② 手写品牌名/LOGO → 文字必错且违反资产真实红线；③ 同时传首尾帧和参考图 → 请求直接失效。**

---

## 七、下一步

当前画布是空的（`AB-experiment-0921-2135`，0 节点），且本轮是只读模式，我**没有创建任何节点、也没有提交任何生成任务**。

如果你要往下走，告诉我一句就行：
- **"把版本 B 落成分镜表"** → 我建一个分镜脚本节点，三条镜头逐行录入，带衔接策略字段；
- **"先生成镜头 1 看气质"** → 需要你确认画幅（16:9 还是 9:16）和是否接受默认模型；
- **"我有茶盒图"** → 把图放进画布，我改用六段式绑参考图重写产品段。
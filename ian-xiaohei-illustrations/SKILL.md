---
name: ian-xiaohei-illustrations
description: 生成 Tony（邢东尼·品牌教练）风格的中文正文配图。用于中文文章、公众号、帖子、博客、Notion、方法论、流程、结构、状态、隐喻配图，以及小黑替换、怪诞手绘、正文插图、shot list、去标题改图。默认 IP 是 Tony，不是小黑。下次调用先读 references/action-library.md 按卡号取动作。纯白手绘、少量红橙蓝批注。
license: MIT
metadata:
  type: workflow
  version: "1.1"
  ip: Tony
  fork: newnewge
---

# Tony 怪诞正文配图

## 核心定位

为中文文章设计和生成 16:9 横版正文配图。目标不是商业插画、PPT 信息图或可爱卡通，而是把文章里的关键判断、流程、结构、状态或隐喻，变成一张清爽、怪诞、有创意、可读但不说明书的手绘解释图。

默认视觉 IP 是 Tony（邢东尼 · 品牌教练），全面替换原仓库小黑。Tony 是正在认真参与系统运转的教练/工作者，不是吉祥物、贴纸或可爱装饰。每张图默认都要出现 Tony，且他必须承担核心动作。

上游风格与工作流继承 Ian 的 ian-xiaohei-illustrations（MIT）。本 skill 只替换 IP 与相关动作库，画风 DNA 保持纯白手绘。

## 先读这些参考

按任务需要读取，不要一次塞满上下文：

- `references/style-dna.md`：风格 DNA、颜色、文字、禁忌。
- `references/action-library.md`：动作总库（下次调用先读，按主题/卡号路由）。
- `references/tony-ip.md`：Tony IP 外形、性格、动作入口、四人组、失形检查。
- `references/general-actions.md`：通用动作 G01–G14。
- `references/wechat-actions.md`：公众号动作 W01–W10。
- `references/brand-actions.md`：品牌教练坏动作全卡（核心 13 + 增补 8）。
- `references/color-actions.md`：颜色开口指令（坐/瞄/冲/留/静/唯一）。
- `references/persuasion-actions.md`：说服路径 × 态度（打招呼/带进门/铺材料/递谈资）。
- `references/composition-patterns.md`：结构类型、原创隐喻方法、反复刻规则。
- `references/prompt-template.md`：单张生图提示词模板。
- `references/qa-checklist.md`：生成后检查和迭代规则。
- `assets/_my-ip/tony.png`：外形基准图。生成前必须读，锁识别件。
- `_my-ip/tony.png`：仓库根目录 IP 基准，生成前对照。
- `assets/examples/`：只作低频视觉校准，不进入默认生成路径。不要照抄构图。

## 替换指令（相对原仓库）

- 禁止再画小黑：黑色实心豆、白点眼无眼镜、无服装的小怪物。
- 所有小黑占位改为 Tony。
- Tony 识别件缺一不可：光头高光弧、圆框眼镜、圆点眼+细笑+腮红、黑白格纹衬衫、黑裤黑鞋、细线四肢。
- 品牌主题优先用 `tony-ip.md` 里的专属坏动作，不要退回正确教练工坊隐喻。

## 工作流

### 1. 消化正文

先读用户给的正文、链接、Notion、Markdown 或截图。提炼核心观点、认知转折、适合用图的点、只适合留文字的点。

不要平均配图。优先认知锚点：核心判断、两个断点、输入输出闭环、分流、前后对比、一鱼多吃、承接路径、常见坑、角色状态、品牌身份/区隔/禁区。

取动作时先读 `references/action-library.md`，按主题落到 G / W / A / C / P 卡号。用户指定卡号则不准换卡。

### 2. 先出配图策略

若用户只要分析怎么配图，先给 shot list。每张图写清楚：放在哪个段落后、主题、核心意思、结构类型、Tony 在图里做什么（写卡号）、建议元素、建议中文标注词。

默认 4-8 张。短文 1-3 张；长文不要轻易超过 9 张。

### 3. 单张生成

用户明确要求生成时，不要停下来等确认。每张单独生成，不要把多张拼在一张里。

每张图只讲一个核心结构。提示词必须包含：16:9 横版、纯白背景、黑色手绘线稿、少量红橙蓝中文手写批注、大量留白、Tony 作为核心动作主体且识别件完整。禁止 PPT、商业插画、幼稚可爱、复杂架构、左上角类型标题、小黑形象。

不要复刻过往案例构图，除非用户明确要求复刻某张图。每次从当前文章重新发明一个奇怪但成立的隐喻。品牌主题用刻意的坏。

中文标注若后端会出伪汉字：先出无字底图，再用 `_my-ip/overlay.py` 后期叠字。

### 4. 检查与迭代

生成后检查 `references/qa-checklist.md`。出现以下问题优先重生成：Tony 只是装饰或没眼镜没格纹、画成了小黑、画面太满、太像流程图/PPT、中文太多或错字、左上角类型标题、太可爱精致商业、背景不是白底、品牌图没有揭穿感。

### 5. 保存交付

把最终图复制到 `assets/<article-slug>-illustrations/`，按顺序命名 `01-topic-name.png`。保留原始生成文件，除非用户明确要求替换。

## 输出口径

策略输出短而准。生成后交付包含：生成了几张、每张用途与卡号、保存路径、哪些最稳、哪些可选。不要长篇解释风格理论。

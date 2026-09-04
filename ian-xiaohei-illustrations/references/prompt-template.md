# 生图提示词模板

每张图单独生成。根据正文内容替换变量，不要把多张图拼在一起。

## 主模板（通用长版）

```text
Generate one standalone 16:9 horizontal Chinese article illustration.

Visual DNA:
Pure white background. Minimalist black flat monoline line art, thin even outlines, slight hand-drawn touch allowed. Lots of empty white space. Sparse red/orange/blue handwritten Chinese annotations. Clean absurd product-sketch feeling. No gradients, no shadows, no paper texture, no complex background, no commercial vector style, no PPT infographic look, no cute mascot poster, no children's illustration, no realistic UI.

Recurring IP character required:
Tony, a chibi teacher mascot: oversized bald head with one highlight arc, round black-framed glasses, dot eyes, small gentle smile, round blush dots, black-and-white plaid (checkered) shirt as his only texture, black pants and shoes, thin stick limbs, flat coloring. Tony must perform the core conceptual action, not decorate the scene. Make Tony a serious-but-warm low-key coach doing slightly absurd system work.

Theme:
{正文配图主题}

Structure type:
{结构类型：Workflow / 系统局部 / 前后对比 / 角色状态 / 概念隐喻 / 方法分层 / 地图路线 / 小漫画分镜}

Core idea:
{这张图要表达的核心意思}

Composition:
{具体画面：Tony 在哪里、正在做什么、主要物件是什么、信息如何流动}

Suggested elements:
{元素1} / {元素2} / {元素3} / {元素4}

Chinese handwritten labels:
{标注词1} / {标注词2} / {标注词3} / {标注词4} / {可选标注词5}

Color use:
Black for main line art and Tony (plaid shirt in black-white). Orange for main flow/path/arrows. Red only for key warnings/problems/results. Blue only for secondary notes or feedback/system state.

Constraints:
One image explains only one core structure. Keep the main subject around 40%-60% of the canvas. Preserve at least 35% blank white space. Use at most 5-8 short handwritten Chinese labels. Do not write a title in the top-left corner. Do not write the structure type on the image. Do not make it a formal diagram, course slide, or dense explainer. Invent a fresh visual metaphor for this specific article. It should be clear but not instructional, interesting but not childish, strange but clean.
```

## 紧凑版（StepFun step-image-edit-2，≤512 字符）

StepFun 分支 prompt 上限 512 字符，用压缩变体；IP 段与画风段不可再压，压变量段：

```text
16:9 Chinese article illustration, pure white bg, minimalist black flat monoline. IP: Tony, chibi bald teacher, big head, round black glasses, dot eyes, smile, blush dots, black-white plaid shirt, black pants, thin limbs. Tony does the core action: {一句话动作}. {画面物件与信息流，一句}. Orange arrows for flow, red for key problem, blue for note. Short handwritten Chinese labels: {词1} / {词2} / {词3}. 40% blank space, no title, no border.
```

## 群像模板（四人组，可选）

需要团队/分工场景时，将 IP 段替换为：

```text
Recurring IP cast required (black-white flat monoline, dot eyes + smile + blush on all):
1. Tony: bald head with highlight arc, round black glasses, black-white plaid shirt — the core action performer.
2. Jiuzhanggui: long black trench coat, straight hair with bangs, holding a whiteboard.
3. Serena: white blazer, slim proportions, holding a laptop.
4. Ajiu: fluffy curly hair, round glasses, holding a checklist board.
Tony must hold the central action; others support at most one sub-step each.
```

## 图像编辑提示

去掉左上角标题：

```text
Edit the provided image. Remove only the handwritten title "{要删除的文字}" and its underline from the top-left corner. Fill that area with the same clean white background, matching the surrounding blank paper. Preserve everything else exactly: characters, labels, paths, line style, composition, aspect ratio, and image quality. Do not add any new text or objects.
```

增强 IP 参与感：

```text
Regenerate this illustration with the same core meaning and simple layout, but make Tony more central to the conceptual action. Tony (bald head, round glasses, plaid shirt) should be doing the strange work that explains the idea, not standing beside the diagram. Keep it clean, sparse, flat monoline, warm but not cute.
```

修正 IP 失形（没眼镜/没格纹衬衫时）：

```text
Regenerate with the identical composition and meaning. Only fix the character: Tony must be a chibi bald teacher with a highlight arc on his head, round black-framed glasses, dot eyes, gentle smile, blush dots, and a black-and-white plaid shirt. Change nothing else in the image.
```

# Prompt Examples

下面这些 prompt 可以直接复制到 Codex 里使用。

## 按动作库取卡（推荐下次这样调）

```text
Use $ian-xiaohei-illustrations
按 references/action-library.md 取动作。
主题：品牌
阶段：判断者
卡号：A01
为这个观点生成一张 16:9 正文配图：品牌先要回答「你到底是谁」。
```

```text
Use $ian-xiaohei-illustrations
按 references/action-library.md 取动作。
主题：公众号
卡号：W03
给「标题对比度」生成一张图。
```

```text
Use $ian-xiaohei-illustrations
按 references/action-library.md 取动作。
主题：颜色
卡号：C03
用户需要立刻点击，不要画色环。
```

```text
Use $ian-xiaohei-illustrations
按 references/action-library.md 取动作。
主题：说服
阶段：路人
卡号：P01
只打招呼，不要报价。
```

## 只做配图规划

```text
Use $ian-xiaohei-illustrations 先不要生图。
请分析下面这篇文章哪里值得配图，输出 5 张左右的 shot list。
每张图写清楚：
- 放在哪个段落后
- 图的主题
- 核心意思
- 结构类型
- Tony在图里做什么（写卡号）
- 建议元素
- 建议中文标注词

<粘贴文章>
```

## 文章正文配图

```text
Use $ian-xiaohei-illustrations 把下面这篇文章生成 4 张Tony怪诞正文配图。
要求：16:9 横版、纯白背景、黑色手绘线稿、少量红橙蓝中文手写批注。
每张图只讲一个核心结构，不要做 PPT 信息图，不要可爱卡通。
先读 references/action-library.md 取卡。

<粘贴文章>
```

## 长文配图策略

```text
Use $ian-xiaohei-illustrations 给这篇长文做配图策略。
不要平均配图，只挑认知锚点：核心判断、输入输出闭环、前后对比、常见坑、承接路径。
默认 6-8 张，先输出 shot list，不要生成图片。

<粘贴文章>
```

## 单个观点生成一张图

```text
Use $ian-xiaohei-illustrations 为这个观点生成一张 16:9 正文配图：

信任不是喊出来的，而是一块证据一块证据铺过去。

画面要怪诞但清爽，Tony必须承担核心动作。
中文标注最多 5 个，短一点。
```

## 工作流主题

```text
Use $ian-xiaohei-illustrations 为“把一条原始素材加工成流量、信任、转化三种内容”生成一张图。
不要画正式流程图，不要复刻一鱼多吃旧案例。
请重新发明一个新的低科技隐喻，让Tony参与核心动作。
```

## 改图：去掉标题

```text
Use $ian-xiaohei-illustrations 帮我编辑这张图。
去掉左上角的“Workflow / 流程图”标题和下划线，其他内容保持不变。
不要新增任何文字或物件。
```

## 改图：增强Tony参与感

```text
Use $ian-xiaohei-illustrations 这张图方向对，但Tony有点像装饰。
请保持核心意思不变，重生成一版：让Tony成为真正推动结构运转的人。
画面更怪一点，但仍然纯白、清爽、少字。
```

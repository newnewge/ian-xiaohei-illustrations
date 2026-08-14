---
type: skill-integration
doc: 小黑公众号图文 Skill · 集成说明
parent: [[个人空间/工具集]]
status: active
tags: [skill, ai作图, 公众号, 小黑, 沉淀]
source: helloianneo/ian-xiaohei-illustrations
fork: newnewge/ian-xiaohei-illustrations
---

# 小黑公众号图文 Skill · 集成说明

> 把 Ian 的 `ian-xiaohei-illustrations` skill 对接到你的 AI 团队工作流。
> 一份**稳定可复用**的作图沉淀，喂你的所有中文公众号正文。

---

## 🎯 它解决什么问题

公众号写正文时，最大的痛点不是写，而是**配图**：

- 千篇一律的 PPT 信息图
- 卡通但不表达任何认知动作
- AI 生成的图文字错乱、风格飘忽

**小黑 skill 的解法**：把文章里的"认知锚点"翻译成 **16:9 / 纯白手绘 / 小黑承担动作** 的怪诞配图。

---

## 📦 仓库元信息

| 字段 | 值 |
|------|-----|
| 上游 | `helloianneo/ian-xiaohei-illustrations` |
| 本 fork | [`newnewge/ian-xiaohei-illustrations`](https://github.com/newnewge/ian-xiaohei-illustrations) |
| 本地路径 | `skills/ian-xiaohei-illustrations/` |
| 真正安装目录 | `skills/ian-xiaohei-illustrations/ian-xiaohei-illustrations/` |
| 协议 | MIT（沿用上游） |
| 关联工作 | [[poster_extracted.md]]、[[copy_drafts.md]] |

---

## 🔧 一键安装到 Codex / Claude Code Skills

```bash
# 假设你使用 $CODEX_HOME 默认路径
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R ./skills/ian-xiaohei-illustrations/ian-xiaohei-illustrations \
      "${CODEX_HOME:-$HOME/.codex}/skills/"
```

安装后，在对话里说：

```text
Use $ian-xiaohei-illustrations 为这篇中文文章设计并生成 5 张小黑怪诞正文配图。
```

---

## 🧩 与现有工作流的对接点

### 1. 与"分身 3 · 内容创作者"配合

| 流程阶段 | 由谁负责 | 产出 |
|----------|----------|------|
| 写文章 | [[分身3-内容创作者]] | Markdown 正文 |
| **提炼认知锚点** | **小黑 skill** | **shot list（4-8 张）** |
| 生图 | 小黑 skill + 图模型 | 16:9 PNG |
| 复盘沉淀 | [[tpl-AI作图-沉淀生成]] | 设计宪法 / 反馈清单 / 案例精选 |

### 2. 与现有 templates 的关系

```
tpl-AI作图-项目启动 ─┐
tpl-AI作图-里程碑   ─┼── 与 小黑 skill 协同，按需调度
tpl-AI作图-沉淀生成 ─┘
```

> ⚠️ 小黑 skill 是**风格专用工具**，不替代你的通用作图工作流。
> 它只服务一个场景：**公众号正文配图**。

### 3. 输出路径约定

```
workspace/
├── 00-项目/<项目名>/articles/         ← 文章 Markdown
├── 00-项目/<项目名>/illustrations/    ← PNG（按 01-, 02-, 03- 编号）
└── 02-共创记录/<日期>/shot-list.md    ← shot list（先图后图的策略）
```

`.gitignore` 已声明 `generated/` `outputs/`，生成的图片不会污染仓库。

---

## 🚀 三档调用模板（复制即用）

### 模板 1｜只出 shot list（不动图）

适用：文章已写好，先看看哪里值得配图。

```text
Use $ian-xiaohei-illustrations 先不要生图。
请分析下面这篇文章哪里值得配图，输出 5 张左右的 shot list。
每张图写清楚：放在哪段后、主题、核心意思、结构类型、小黑在做什么、建议中文标注词。

【粘贴你的公众号正文】
```

### 模板 2｜直接生成正文配图

适用：图位已确定，要直接出图。

```text
Use $ian-xiaohei-illustrations 把下面这篇文章生成 4 张小黑怪诞正文配图。
要求：16:9 横版、纯白背景、黑色手绘线稿、少量红橙蓝中文手写批注。

【粘贴文章】
输出到：00-项目/2024-08-主理人分享会/illustrations/
```

### 模板 3｜为单个概念补一张图

适用：写完发现某段缺点睛之笔，单独补一张。

```text
Use $ian-xiaohei-illustrations 为下面这句话生成一张正文配图：
"<你的金句>"
画面要怪诞但清爽，小黑必须承担核心动作。
```

### 模板 4｜去标题 / 改图 / 局部重绘

```text
Use $ian-xiaohei-illustrations 帮我编辑这张图：
- 去掉左上角的"<某标题>"
- 保留其他元素
- 重新生成 16:9 PNG
```

---

## 🎨 风格 DNA（速查）

记住这几条，几乎不会跑偏：

| ✅ 必须 | ❌ 禁止 |
|--------|---------|
| 16:9 横版 | 商业插画 / KV / 扁平卡通 |
| 纯白背景，无纸纹 | 米色 / 阴影 / 渐变 |
| 黑色手绘线稿（细线、轻抖） | 粗黑边 / PPT 边框 |
| 大量留白（主体占 40-60%） | 画面塞满 |
| 少量红 / 橙 / 蓝中文手写批注 | 大段文字、复杂标题 |
| 小黑承担核心动作 | 小黑只站角落 / 表情可爱卖萌 |
| 一张图只讲一个认知动作 | 一图讲十个流程 / 一篇说明书 |

> 完整 DNA 见 `references/style-dna.md`、`references/xiaohei-ip.md`、`references/composition-patterns.md`。

---

## 📐 推荐结构类型（按文章选）

来自 `composition-patterns.md`，速查表：

| 结构类型 | 适用段 |
|----------|--------|
| Workflow | 步骤型方法论 |
| 系统局部 | 拆解某个工具的内部 |
| 前后对比 | 转型 / 升级 / 觉醒 |
| 角色状态 | 一个人在不同情境下的状态 |
| 概念隐喻 | 把抽象判断变成物理物件 |
| 方法分层 | 难度分层 / 阶段分层 |
| 地图路线 | 选择路径 / 决策分支 |
| 小漫画分镜 | 转折 / 反转 / 故事性 |

> **原则**：从当前文章**重新发明隐喻**，不要复刻上游示例的物件。

---

## ✅ QA checklist（生成前自检）

来自 `references/qa-checklist.md`：

- [ ] 16:9 横版
- [ ] 纯白背景
- [ ] 小黑在图里**做了事**，不只是站着
- [ ] 中文标注 ≤ 6 个词，错字 ≤ 1 个
- [ ] 不出现 "流程图 / 系统架构图 / 常见坑" 等 PPT 标题
- [ ] 没有复刻上游 8 张示例图的构图或物件
- [ ] 主体留白 40-60%

---

## 🔄 与本次工作的衔接

本次会话里产生的素材，可直接喂给这个小黑 skill：

| 已产出文件 | 如何喂给小黑 |
|------------|--------------|
| `poster_extracted.md`（海报元素提取） | 作为「概念隐喻」类配图的输入，提取"主理人偷偷发光"等关键概念 |
| `copy_drafts.md`（3 篇活动文案） | 选中一篇，作为模板 1 / 2 的输入，让小黑为每篇文章生成 4-6 张配图 |

### 一个跨工具的实战例子

假设你要为 **「主理人，别再偷偷发光」活动** 准备一篇公众号长文：

1. **写文案**：用 `分身3-内容创作者`，选定 `copy_drafts.md` 中第二篇（场景型）
2. **配图规划**：用模板 1，让小黑 skill 先出 5 张 shot list
3. **出图**：用模板 2，让小黑 skill 生成 PNG，存到 `00-项目/2024-08-主理人分享会/illustrations/`
4. **沉淀**：项目收尾时，用 `tpl-AI作图-沉淀生成`，整理出你自己版本的"小黑风格宪法"
5. **反馈**：把生成中出现的错字 / 风格漂移 / 小黑站角落等问题，记录到 `00-团队知识/反馈清单/小黑配图.md`

---

## ⚠️ 已知限制

- **图片里的中文越短越稳定**。标注词超过 6 个，错字概率指数级上升。
- **AI 图像模型可能出现错字 / 幻觉标签**。每张图都要人眼检查中文。
- **不要复刻上游示例的构图**——风格校准 ≠ 构图模板。
- 上游 skill 默认 **Codex 环境**，在 Claude Code / Cursor 里需要把 `$ian-xiaohei-illustrations` 替换成实际能识别的 skill 名称。

---

## 📚 相关资源

- 上游 README：[`helloianneo/ian-xiaohei-illustrations`](https://github.com/helloianneo/ian-xiaohei-illustrations)
- 上游示例 prompt：`skills/ian-xiaohei-illustrations/examples/prompts.md`
- 作者 Ian：[www.ianneo.xyz](https://www.ianneo.xyz) · X: [@ianneo_ai](https://x.com/ianneo_ai)
- 配套 skill：`helloianneo/ian-handdrawn-ppt`（手绘 PPT 版）

---

## 🗂 变更记录

| 版本 | 时间 | 修改 |
|------|------|------|
| v1.0 | 2024-08 | 首次对接，写入 4 个调用模板 + 工作流衔接 |

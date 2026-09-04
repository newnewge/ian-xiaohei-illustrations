---
type: skill-extension
doc: 小黑配图 · 数据源接入
parent: [[README_INTEGRATION]]
status: active
version: 1.0
tags: [skill, 数据源, 广告语, 头脑风暴]
source: helloianneo/ian-xiaohei-illustrations
base_constitution: [[NEWNEWGE风格扩展]]
data_source_index: [[data-sources]]
---

# 小黑配图 · 数据源接入 v1.0

> 把"广告语灵感数据源"接进小黑 skill。
> 让它不只服务"已经有文章"的下游，也能冷启动服务"还没有文章"的**头脑风暴**阶段。
> 沿用 NEWNEWGE 版色盘与 4 件视觉锤，不引入第二种风格语言。

---

## 🎯 为什么要接入广告语数据源

### 默认路径的盲区

`README_INTEGRATION` 里描述的小黑 skill 工作流长这样：

```
文章 → 提炼认知锚点 → 出 shot list → 出图
```

**默认假设**：你已经有一篇写好的文章。

但实际创作里，**50% 的工作发生在"还没写文章"时**：

- 选题立项——"这个角度能不能打动读者？"
- 广告语头脑风暴——"哪句话最上头？"
- 视觉概念预演——"这句话能不能被画出来？"

这三步都**没有文章**做输入。它们需要的是：

```
广告语 → 概念 → 配图（头脑风暴用）
```

### 数据源如何填空

`[[data-sources]]` 已经盘过 12+ 个相关数据源。本文档只接其中**与小黑 skill 直接相关**的 5 个：

- `shibing624/AdvertiseGen`（11 万+ 电商广告）——**文案灵感主源**
- `suolyer/copywriting`（万级通用）——多场景兜底
- `mrzjy/creative-ad-prompts-zh`（千级）——创意思维链 prompt 调试
- `sparanoid/chinese-copywriting-guidelines`（规则）——中文排版合规校验
- `shsfwork/awesome-inspiration`（视觉参考）——设计灵感

接入后，小黑 skill 的工作流变成两条路径：

```
路径 A（已有文章）：   文章       → 认知锚点 → shot list → 图
路径 B（头脑风暴）：   广告语数据 → 概念隐喻 → shot list → 图
                                                 ↓
                                            汇合点：shot list
```

> **核心论点**：接入数据源不是为了"替代文章"，是为了**在文章诞生之前**就让小黑 skill 有事可做。

---

## 🔗 数据源对照表

> 详细字段见 `[[data-sources]]`。这里只列出与小黑 skill 的**对接关系**。

| 数据源 | URL | 类型 | 用法 | 调用优先级 |
|--------|-----|------|------|------------|
| 🔥 `shibing624/AdvertiseGen` | https://huggingface.co/datasets/shibing624/AdvertiseGen | 11 万+ 电商广告 | **文案灵感主源**——随机抽 3-5 条同品类样本，做修辞结构分析 | ⭐⭐⭐ |
| 🔥 `suolyer/copywriting` | https://huggingface.co/datasets/suolyer/copywriting | 万级通用 | 多场景兜底——当 AdvertiseGen 品类缺数据时用 | ⭐⭐ |
| 🧩 `mrzjy/creative-ad-prompts-zh` | https://huggingface.co/datasets/mrzjy/creative-ad-prompts-zh | 千级 | 创意思维链 prompt——调试"广告=设计+文案"的输入格式 | ⭐ |
| ⭐ `sparanoid/chinese-copywriting-guidelines` | https://github.com/sparanoid/chinese-copywriting-guidelines | 规则 | 中文排版合规校验——所有图内文字过这一道 | ⭐⭐⭐ |
| 🧩 `shsfwork/awesome-inspiration` | https://github.com/shsfwork/awesome-inspiration | 视觉参考 | 设计灵感——卡壳时翻一翻 | ⭐ |

### 字段说明（速查）

#### shibing624/AdvertiseGen

| 字段 | 值 |
|------|-----|
| 数据规模 | 训练 114k / 验证 1k / 测试 3k |
| 格式 | JSON（`train.json` 230MB） |
| 任务形态 | 商品 KV → 广告文案 |
| License | CC-BY-4.0 |
| 在小黑 skill 里的角色 | **随机抽样 → 分析修辞 → 反推概念隐喻** |
| 抽样推荐数 | 每次头脑风暴抽 3-5 条 |
| 同品类检索 | 用 `tags` / `category` 字段过滤 |

#### suolyer/copywriting

| 字段 | 值 |
|------|-----|
| 数据规模 | 10K-100K |
| 格式 | JSON（`test.json` 728MB） |
| 在小黑 skill 里的角色 | **多场景兜底**——品类跨界、广告语长尾覆盖 |
| 调用建议 | 当 AdvertiseGen 同品类样本 < 3 条时切换 |

#### mrzjy/creative-ad-prompts-zh

| 字段 | 值 |
|------|-----|
| 数据规模 | 1K-10K |
| 格式 | parquet |
| 在小黑 skill 里的角色 | **prompt 调试**——研究"中文广告创意 prompt"的标准结构 |
| 调用建议 | 调模板 NEW-1 之前看 3-5 条，理解"广告 prompt 的思维链"长什么样 |

#### sparanoid/chinese-copywriting-guidelines

| 字段 | 值 |
|------|-----|
| 类型 | Markdown 规则集（中文排版） |
| Stars | 15,630+ |
| 在小黑 skill 里的角色 | **合规校验器**——生成图里的中文必须过这一道 |
| 校验维度 | 全角/半角标点、中英文间距、数字与单位、专有名词 |
| 调用方式 | 模板 NEW-3（排版合规校验） |

#### shsfwork/awesome-inspiration

| 字段 | 值 |
|------|-----|
| 类型 | Awesome list（landing pages / SaaS / UX） |
| 在小黑 skill 里的角色 | **设计灵感面板**——卡壳时翻一翻 |
| 调用建议 | 头脑风暴前 5 分钟刷一遍，避免闭门造车 |

---

## 🚀 3 档新调用模板（重点）

> 这 3 个模板与 `README_INTEGRATION` 的 4 个模板**互补**：
> - 已有 4 个 → 服务"已有文章"
> - 下面 3 个 → 服务"没有文章"

---

### 模板 NEW-1｜广告语 → 配图

**适用**：头脑风暴阶段，已有商品/服务定位，需要 4 张候选配图。

```text
Use $ian-xiaohei-illustrations（NEWNEWGE 风）配合 shibing624/AdvertiseGen 灵感。
给商品/服务「<你的商品>」生成 4 张 16:9 配图（头脑风暴用）。

要求：
- 先随机抽取 3 条 AdvertiseGen 同品类的样本
- 分析其修辞结构（"卖点 + 场景 + 行动召唤"）
- 把"最打人的一句"转化为可视化隐喻
- 视觉约束：NEWNEWGE 色盘 + 4 件视觉锤
```

**使用流程**：

```
1. 准备：明确商品/服务定位（关键词 5 个以内）
2. 抽样：从 AdvertiseGen 按品类抽 3 条样本
3. 分析：拆每条的「卖点 + 场景 + 行动召唤」
4. 挑选：从 3 条里挑出"最打人的一句"
5. 翻译：把那句"金句"翻成物理物件/场景（概念隐喻）
6. 生成：4 张 16:9 候选图，按 NEWNEWGE 视觉锤出
7. 反馈：选 1 张进 shot list，其余进反馈清单
```

**输出物**：

- 4 张候选 PNG（按 `01-` `02-` `03-` `04-` 编号）
- 1 段文案分析记录（写入 `02-共创记录/<日期>/广告语-概念分析.md`）

---

### 模板 NEW-2｜情绪锚点 × 文案 × 配图

**适用**：做情绪海报、节日海报、态度表达类单图。

```text
Use $ian-xiaohei-illustrations 生成情绪海报。
情绪：<怒/喜/惧/思 之一>
文案主轴：「<一句话金句>」
配图 1 张，16:9。

要求：
- 小黑承担"该情绪下的代表性动作"
- 不超过 4 个中文标注词
- 4 件视觉锤必装
```

**情绪 × 动作参考表**：

| 情绪 | 小黑代表性动作 | 推荐视觉锤短句 |
|------|---------------|---------------|
| 怒 | 砸东西 / 拍桌子 / 攥拳 | 📍认知锚点 · 怒 |
| 喜 | 跳起来 / 张臂 / 仰头笑 | 📍认知锚点 · 喜 |
| 惧 | 后退 / 捂眼 / 缩成一团 | 📍认知锚点 · 惧 |
| 思 | 托腮 / 蹲着想 / 望远方 | 📍认知锚点 · 思 |

**与 NEW-1 的关系**：

- NEW-1 是"多张图 + 多条候选广告语"
- NEW-2 是"1 张图 + 1 句金句 + 1 种情绪"
- 两者可以串联：先 NEW-1 出 4 张候选 → 选定 1 张 → 用 NEW-2 加情绪强化

**输出物**：

- 1 张 PNG（情绪海报）
- 情绪与动作的对应说明（写入图角标短句）

---

### 模板 NEW-3｜排版合规校验

**适用**：生成的图里有中文标注，先做一次排版合规检查。

```text
Use $ian-xiaohei-illustrations + sparanoid/chinese-copywriting-guidelines。
先按我的图返工：
1. 对照规则检查标点（全角/半角/空格）
2. 修正文案中不合规字符
3. 重新生成图，确认文字渲染没问题
```

**校验清单**（按 sparanoid 指南浓缩为小黑 skill 版本）：

| 维度 | 规则 | 在小黑图里的常见问题 |
|------|------|---------------------|
| 中英文间距 | 中文与英文/数字之间加 1 个空格 | "小黑做AI" 应为 "小黑做 AI" |
| 全角标点 | 中文语境用全角（，。！？""''） | "小黑做图, 小黑做图" 应为 "小黑做图，小黑做图" |
| 数字与单位 | 数字与单位之间加空格（"5 张" "16:9"） | "5张" 应为 "5 张" |
| 专有名词 | 品牌/产品名按官方写法（不强行翻译） | "Notion" 不写作 "诺雄" |
| 错别字 | 同音字、形近字高发区校对 | "配图" vs "配图" 已校验 |

**返工动作**：

```
1. 拉出原图的中文标注词
2. 对照 sparanoid 指南逐条检查
3. 列出不合规项（一般 1-3 处）
4. 修正文案
5. 重新生成图（用模板 4｜改图）
6. 再过一遍中文错字自检
```

**输出物**：

- 修订后的 PNG
- 1 张排版问题清单（写入 `02-共创记录/<日期>/排版校验.md`）

---

## 🔄 与已有 4 个模板的协同

| 模板 | 来源 | 输入 | 服务阶段 |
|------|------|------|----------|
| 模板 1｜只出 shot list | `README_INTEGRATION` | 文章 | 已有文章 · 路径 A |
| 模板 2｜直接生成正文配图 | `README_INTEGRATION` | 文章 | 已有文章 · 路径 A |
| 模板 3｜为单个概念补一张图 | `README_INTEGRATION` | 金句 | 已有文章 · 路径 A |
| 模板 4｜去标题 / 改图 / 局部重绘 | `README_INTEGRATION` | 已生成的图 | 已有文章 · 路径 A |
| **模板 NEW-1｜广告语 → 配图** | 本文档 | 商品 + 数据源样本 | **头脑风暴 · 路径 B** |
| **模板 NEW-2｜情绪锚点 × 文案 × 配图** | 本文档 | 情绪 + 金句 | **头脑风暴 · 路径 B** |
| **模板 NEW-3｜排版合规校验** | 本文档 | 已生成的图 | **两条路径共用** |

### 两条路径的汇合点

```
路径 A：  文章 ──→ 模板 1 → shot list ──→ 模板 2 → 图 ──→ 模板 NEW-3 校验
                                                                ↓
路径 B：  广告语 ──→ 模板 NEW-1 ──→ 候选图 ──→ 选定 1 张 ──→ shot list
              │
              └─→ 模板 NEW-2 ──→ 情绪海报 ─────────────────────┘
```

**汇合点 = shot list**：

- 路径 A 的 shot list 来自"文章里的认知锚点"
- 路径 B 的 shot list 来自"广告语分析出的概念隐喻"
- 两份 shot list 在写文章之前可以并行存在，写文章时合并

### 实际用法举例

**场景**：为「主理人，别再偷偷发光」活动做配图准备。

```
第 1 周（头脑风暴 · 路径 B）：
  - 模板 NEW-1 × AdvertiseGen → 出 4 张候选配图
  - 模板 NEW-2 × 情绪"怒" → 出 1 张情绪海报（"别再"的态度表达）
  - 模板 NEW-3 × sparanoid → 校验前 5 张图的排版

第 2 周（写文章 · 路径 A）：
  - 用头脑风暴阶段敲定的概念，写公众号正文
  - 模板 1 → 出 shot list
  - 模板 2 → 出 4-6 张正文配图
  - 模板 NEW-3 → 全部图过一遍排版
```

> **关键**：头脑风暴阶段不依赖文章，所以可以**比文章更早启动**。

---

## 📋 接入检查清单

> 上线前，对照这张清单逐项打勾。

### 数据源接入

- [ ] `shibing624/AdvertiseGen` 已下载或可在线读（推荐本地 `data-sources/advertisegen/`）
- [ ] `suolyer/copywriting` 已下载（兜底用）
- [ ] `sparanoid/chinese-copywriting-guidelines` 已 clone 到 `data-sources/`
- [ ] `mrzjy/creative-ad-prompts-zh` 已下载（可选，调试用）
- [ ] `shsfwork/awesome-inspiration` 已 star（视觉灵感面板）

### 工作流装配

- [ ] `[[templates/tpl-广告语头脑风暴-SOP]]` 已就绪
- [ ] 至少 1 张用 **模板 NEW-1** 跑过的图（含文案分析记录）
- [ ] 至少 1 张用 **模板 NEW-2** 跑过的图（情绪 × 动作对应已记录）
- [ ] 至少 1 张用 **模板 NEW-3** 跑过的图（含排版问题清单）

### 与已有 skill 的衔接

- [ ] `README_INTEGRATION.md` 已加"数据源接入"章节级双链
- [ ] `NEWNEWGE风格扩展.md` 的色盘与视觉锤在 NEW-1/2/3 里被引用
- [ ] `data-sources.md` 的"使用建议"段落已标注"小黑 skill 专用子集"

### 反馈沉淀

- [ ] 新建 `02-团队知识/反馈清单/小黑配图-广告语数据源.md`
- [ ] 记录首批 NEW-1/2/3 跑出来的"踩坑"与"惊喜"

---

## 🗂 关联文档

| 文档 | 关系 |
|------|------|
| `[[README_INTEGRATION]]` | 父本 skill 集成说明（已有 4 个模板） |
| `[[NEWNEWGE风格扩展]]` | 色盘 / 视觉锤 / 签名三态（本扩展继承） |
| `[[data-sources]]` | 顶层数据源清单（本文档是其"小黑 skill 专用子集"） |
| `[[templates/tpl-广告语头脑风暴-SOP]]` | 头脑风暴阶段的 SOP 模板（与 NEW-1 配套） |
| `[[设计宪法v1.0-基准实例]]` | 色盘与视觉锤的最终依据 |
| 上游原作：[helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations) | 父本 skill 上游 |

---

## 🗂 变更记录

| 版本 | 时间 | 修改 |
|------|------|------|
| v1.0 | 2024-08 | 首版：5 个数据源接入 + 3 个新调用模板（NEW-1/2/3）+ 与已有 4 模板协同路径 + 接入检查清单 |

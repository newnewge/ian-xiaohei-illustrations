# NEWNEWGE Fork 说明

> 本仓库为 [`helloianneo/ian-xiaohei-illustrations`](https://github.com/helloianneo/ian-xiaohei-illustrations) 的 fork，仅做本地协作与个人维护之用。

## 对接关系

| 角色 | 仓库 |
|------|------|
| 上游（Upstream） | `helloianneo/ian-xiaohei-illustrations` |
| 本 fork | [`newnewge/ian-xiaohei-illustrations`](https://github.com/newnewge/ian-xiaohei-illustrations) |
| 本地路径 | `./skills/ian-xiaohei-illustrations/` |
| 同步日期 | 2024-08（首次对接） |

## 同步上游

```bash
# 添加 upstream（一次性）
git remote add upstream https://github.com/helloianneo/ian-xiaohei-illustrations.git

# 拉取上游更新
git fetch upstream
git checkout main
git merge upstream/main
```

## 本地协作约定

- 本仓库用于 **个人内容生产与 skill 调度**
- 与上游保持 **同步但不主动 push** 修改到 `main`
- 个人定制改动放 `feature/*` 分支
- 输出资产（生成的 PNG / shot list）放在 `outputs/`（已 gitignore）

## 配套文件

- `../README_INTEGRATION.md`：本仓库如何接入 agently 工作流的使用说明（待补）
- `../examples.md`：在你的公众号里调度的示例（待补）

## 致谢

原始作者 **Ian (伊恩)** — [`@ianneo_ai`](https://x.com/ianneo_ai) · [www.ianneo.xyz](https://www.ianneo.xyz) · 微信 `ianneoxyz`

MIT License，沿用上游。

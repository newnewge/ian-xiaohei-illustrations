# NEWNEWGE Fork 说明

> 本仓库为 [`helloianneo/ian-xiaohei-illustrations`](https://github.com/helloianneo/ian-xiaohei-illustrations) 的 fork，仅做本地协作与个人维护之用。

## 对接关系

| 角色 | 仓库 |
|------|------|
| 上游（Upstream） | `helloianneo/ian-xiaohei-illustrations` |
| 本 fork | [`newnewge/ian-xiaohei-illustrations`](https://github.com/newnewge/ian-xiaohei-illustrations) |
| Skill 目录 | `./ian-xiaohei-illustrations/` |
| IP 基准 | `./_my-ip/tony.png` |

## 下次调用

```
Use $ian-xiaohei-illustrations
按 references/action-library.md 取动作。
主题：{通用 / 公众号 / 品牌 / 颜色 / 说服}
阶段：{路人 / 观众 / 判断者 / 立场者}
卡号：{G14 / W03 / A01 / C03 / P01}
```

总库：`ian-xiaohei-illustrations/references/action-library.md`

| 分卡 | 内容 |
|------|------|
| `general-actions.md` | 通用 G01–G14 |
| `wechat-actions.md` | 公众号 W01–W10 |
| `brand-actions.md` | 品牌坏动作 A01–A13 + B01–B08 |
| `color-actions.md` | 颜色开口 C01–C07 |
| `persuasion-actions.md` | 说服路径 P01–P04 |
| `tony-ip.md` | IP + 四人组锁死 |

四人组锁死：Serena = 女、中分披发、休闲裙；阿久 = 女、长发过肩、圆框眼镜、小西装。Tony 必须占核心动作。

## 同步上游

```bash
git remote add upstream https://github.com/helloianneo/ian-xiaohei-illustrations.git
git fetch upstream
git checkout main
git merge upstream/main
```

个人增量（动作库 / IP）不要在 merge 时丢掉。

## 致谢

原始作者 **Ian (伊恩)** — [`@ianneo_ai`](https://x.com/ianneo_ai) · [www.ianneo.xyz](https://www.ianneo.xyz)

MIT License，沿用上游。

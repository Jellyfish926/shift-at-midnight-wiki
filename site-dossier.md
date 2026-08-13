# 站点档案 — shiftatmidnightwiki.site

> 每轮复盘开工先读这份档案，收尾更新它。审核结果只发邮件，不主动核对就会一直停在「审核中」。
> 最后更新：2026-08-13

| 项 | 值 |
|---|---|
| 游戏词 | Shift At Midnight |
| 仓库 | `Jellyfish926/shift-at-midnight-wiki` |
| 架构 | Python 生成器 `_src/` → 静态 HTML 到 `public/`。**唯一构建入口 `_src/build_all.py`**，不要单独跑 `_content_*.py`（合并要跨文件）。手写页由 `_patch_handwritten.py` 拉齐。 |
| 首次提交 | 2026-07-28 |
| 当前页数 | 34（2026-08-13 加 /monsters/entity/） |
| 内页中位字数 | 约 950 词 |

## 审核状态表

**AdSense 面板 2026-08-13 实测(zsn 账号,入口 adsense.google.com/adsense/u/0/pub-6575082962774479/sites;旧版 /adsense/new/ 路径会误报无权访问)**:本站「正在准备」(8/12 重提已被面板记录,最后更新 8/12 16:34),无新结果;ads.txt=已授权。

> ⚠️ 拒信原文**逐字保存，不要转述** —— 整改要对着原文做。

| 平台 | 状态 | 提交日 | 结果日 | 拒因 | 下次可提日 |
|---|---|---|---|---|---|
| AdSense | 审核中(8/12 重提) | 2026-08-12(首提 2026-07-29) | 待出(约 8/17-8/19 查) | 上轮拒因:低价值内容(后台状态详情;拒信邮件原文未调取) | — |
| 2026-08-13 丰富轮 | 34 | 中位约 950（新页 1527） | 开着 | 成就率全站刷新至 8/13；AdSense 状态未核对（后台在 ywx574708831 账号，需重新登录） |
| Humble Partner | 未提 | — | — | — | — |
| Green Man Gaming | 未提 | — | — | — | — |
| Fanatical | 未提 | — | — | — | — |

**ads.txt**：`google.com, pub-6575082962774479, DIRECT, f08c47fec0942fa0`
—— 2026-08-12 实测线上 HTTP 200、内容正确。AdSense 面板若显示「未找到」，是它还没重新抓，不是代码问题。

## 广告状态

| 项 | 值 |
|---|---|
| AdSense pub-id | pub-6575082962774479（验证码在页面上） |
| Adsterra | **开着** —— 2026-08-12 线上实测 invoke.js 在加载 |
| sandbox token | `allow-scripts allow-popups allow-popups-to-escape-sandbox`（故意不给 `allow-top-navigation*`） |

⚠️ **仓库里有两条互相打架的规矩**：`sites/_lessons.md` 说「AdSense 审核期内绝不上第三方广告网络」，
而 `Ads.tsx:162` / 部分 ads.js 注释说「提审中的正确姿势是正文位交给 Adsterra」。
2026-08-12 用户明确选择「都不关」。**下次改广告开关前先把这两处对齐，别再各写各的。**

## 站点特有的坑

- `/demo/` 曾被 `_merge.py` 并进 `/review/#demo`，`vercel.json` 里有三条 308。
  2026-08-12 把合并规则与三条跳转一起拿掉了 —— **页面与 vercel.json 必须同一次部署**。
- 404 页绝不能有 `adsbygoogle`（过审后 Auto ads 会自动注入，明确违反政策）。已核实无。
- 模板 f-string 里嵌 JS/CSS，字面 `{` `}` 必须写成 `{{` `}}`。改完跑
  `python3 -c "import ast;ast.parse(open('_build.py').read())"` 自检。

## 两个待人工核实的疑点（2026-08-12 发现，未改）

1. `/release-date/` 事实表写「Engine: Unity」，取证时找不到任何原始出处。
   新写的 `/system-requirements/` 因此故意没提引擎。
2. Steam API 把九种语言全部标为 **full audio**，而 `/release-date/` 写的是
   "interface and subtitles"。两者必有一错。

## 历次整改快照（过审那次才对得出是哪个改动起效）

| 日期 | 页数 | 平均/中位字数 | Adsterra | 结果 |
|---|---|---|---|---|
| 2026-07-29 首提 | 44 | 平均 447 | KILL_ALL=false（7/31 曾投放并实测强制跳转，同日关闭） | 审核中 |
| 2026-08-05 合并加厚 | 29 | 平均 925 | 关闭 | 8/11 被拒·低价值内容 |
| 2026-08-12 补页修错 | 33 | 中位约 950 | **开着**（用户本轮决定不关） | 待观察 |

## 复盘记录

见同目录 `reviews/`。

---

## 追记 2026-08-12(第 2 轮收尾)
- **8/12 已在 AdSense 后台重提审核**(勾选「已解决相关问题」→ 申请审核,状态变「正在准备/已请求审核」)。提交时站点快照:33 页 / 平均正文约 1000 词 / 站内查重 max ~6% / 死链 0 / **Adsterra Native Banner 在投(sandbox iframe)**。
- 站主政策(8/12 拍板,skill 已同步改):①提审 AdSense 不关闭任何广告;②被拒整改完成即重提,不设等待期。上表「等待期」相关旧口径作废。

# lessons-inbox(站群经验暂存区 · 暂存于 shift 仓,站群仓建立后迁移)

- 2026-08-12 | 云端 Cowork 会话内改站群 | git 代理只对「会话授权仓库」注入凭证,四个站仓 push 一律 403;实测 `NO_PROXY=github.com git push`(配合用户 fine-grained PAT 存入 credential store)可直连推送成功 → 建议并入 seo-yunying「零、执行协议」数据/部署获取路径,或 seo-jianzhan 部署节。
- 2026-08-12 | shift 站 AdSense 提审(挂着 Adsterra Native Banner)被拒「低价值内容」;同账号 beast 站审核期也开着 Adsterra,已一并关停 | 属「提审期第三方广告零容忍」纪律的实证案例 → 并入 seo-jianzhan references/05 §3 教训库。
- 2026-08-12 | adsense_check.py 的 THIRD_PARTY 检测把 privacy 页披露文案里的 adsterra.com 链接也算命中(并非真实加载)| 关停广告后必须同步改隐私页披露,否则自检永远 BLOCK → 并入 seo-jianzhan「广告与过审自检」注意事项。
- 2026-08-12 | GSC 效果页把「每页行数」切到 500 后,用浏览器 get_page_text 一次抓全 240 个查询,无需导出 CSV | seo-yunying 0.1 路径 1 的具体操作捷径。
- 2026-08-12 | 静态 HTML 站(非 MDX)跑 5-gram 查重时,必须先剔除每页共用的 aside/nav 组件,否则全站互相 6-9% 误报(实测剔除后 max 从 15.4% 降到 5.8%,唯一真超标的是 about↔contact 的政策句式)| → 并入 seo-yunying references/content-depth.md 查重节。


## [已并入 2026-08-13] 2026-08-13 Chrome 登录态抓 GSC 的可复用路径（路 1 首次走通）

**实验条件**：五站复盘。效果页 URL 直接带参数导航：
`performance/search-analytics?resource_id=sc-domain:<域名>&num_of_days=28&breakdown=query|page`。
「每页行数」选择器在自动化下点不动（Wiz 框架），表头排序点击也不生效；但「下一页」按钮可用，
逐页取文本稳定 —— 前 40-60 行足够做补页决策。sitemaps 页同样可直读。

**结论**：GSC 取数走 Chrome 登录态完全可行，单站 3-5 次调用拿齐五个数 + 查询榜 + 页面榜 + sitemap 状态。

**并入**：`seo-yunying` 0.1 节路 1 的操作附注。

## [已并入 2026-08-13] 2026-08-13 设备沙箱里 Next.js build 挂起 —— Next 站构建必须走云端

**实验条件**：sephiria 在 Mac 设备沙箱（无外网）跑 `next build`，10 分钟无 Compiled（疑卡字体/遥测网络请求）；
同源码云容器 npm install + build 全通过。另：设备端后台进程要 `setsid` 起才能跨调用存活，`nohup &` 会被杀。

**结论**：Next.js（含 next/font）的站在无外网环境不可构建；渲染字数验证一律云端做（zip 源码 → stage → npm i → build）。

**并入**：`seo-yunying` 四「量现状」 + 站群仓「已知环境坑」。

## [已并入 2026-08-13] 2026-08-13 AdSense「无权访问」是旧版 URL 路径的误报,不是账号问题(当日已推翻自己上一个结论)

**实验条件**:用 `adsense.google.com/adsense/new/u/0/sites`(旧版 new 路径)访问 → 报「zsn2740784715 似乎无权访问此 AdSense 账号」,u/1 枚举同样失败,当时误判为账号不匹配。
同一登录态改用裸域名 `https://adsense.google.com/` → 正常进入 pub-6575082962774479(就在 zsn 账号下),
sites 列表用 `adsense.google.com/adsense/u/0/pub-<pubid>/sites` 直达,表格需等约 5 秒渲染。

**结论**:AdSense 的「无权访问」页不可作为账号归属的证据 —— 先换裸域名入口重试再下结论;
sites 列表 URL 用带 pub-id 的新版路径。当日五站实测:全部「正在准备」,shift 8/12 重提已被面板记录。

**并入**:`seo-yunying` 五·五 执行注记(替代此前「账号不一致」的错误版本)。

## [已并入 2026-08-13] 2026-08-13 特典物品名必须逐字来自店铺页 —— "Polaris" 是编造名，污染了六个语种

**实验条件**：beast 全站把 Deluxe 附赠剑写作 Polaris（en/de/it/es/fr）/ ポラリス（ja）共 46 处；
对 Steam Deluxe DLC 页与 PS Store JP 核对，官方名 Big Dipper / 北斗星，"Polaris" 无任何官方出处。
en/editions 与 ja/editions 是对的 —— 建站期部分页查了店铺、部分页凭记忆写，编造名随翻译被放大。

**结论**：DLC/特典物品名属「必须逐字复制自店铺页」的事实类；多语言站里一个编造名会被忠实翻译放大 N 倍。

**并入**：`seo-jianzhan` 内页写作纪律 + `seo-yunying` 加厚红线。

# lessons-inbox(站群经验暂存区 · 暂存于 shift 仓,站群仓建立后迁移)

- 2026-08-12 | 云端 Cowork 会话内改站群 | git 代理只对「会话授权仓库」注入凭证,四个站仓 push 一律 403;实测 `NO_PROXY=github.com git push`(配合用户 fine-grained PAT 存入 credential store)可直连推送成功 → 建议并入 seo-yunying「零、执行协议」数据/部署获取路径,或 seo-jianzhan 部署节。
- 2026-08-12 | shift 站 AdSense 提审(挂着 Adsterra Native Banner)被拒「低价值内容」;同账号 beast 站审核期也开着 Adsterra,已一并关停 | 属「提审期第三方广告零容忍」纪律的实证案例 → 并入 seo-jianzhan references/05 §3 教训库。
- 2026-08-12 | adsense_check.py 的 THIRD_PARTY 检测把 privacy 页披露文案里的 adsterra.com 链接也算命中(并非真实加载)| 关停广告后必须同步改隐私页披露,否则自检永远 BLOCK → 并入 seo-jianzhan「广告与过审自检」注意事项。
- 2026-08-12 | GSC 效果页把「每页行数」切到 500 后,用浏览器 get_page_text 一次抓全 240 个查询,无需导出 CSV | seo-yunying 0.1 路径 1 的具体操作捷径。
- 2026-08-12 | 静态 HTML 站(非 MDX)跑 5-gram 查重时,必须先剔除每页共用的 aside/nav 组件,否则全站互相 6-9% 误报(实测剔除后 max 从 15.4% 降到 5.8%,唯一真超标的是 about↔contact 的政策句式)| → 并入 seo-yunying references/content-depth.md 查重节。

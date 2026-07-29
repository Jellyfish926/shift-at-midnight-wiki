#!/usr/bin/env python3
"""页面生成器 — 统一 head/nav/footer/JSON-LD 样板,正文逐页手写。

只负责把重复结构生成一致,不生成内容。跑完用 audit_pages 全站校验。
"""
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "public"   # 只往发布目录写;memory.md 与 _src 不进发布树
BASE = "https://shiftatmidnightwiki.site"


def css_ver() -> str:
    """style.css 的内容哈希 —— 缓存击穿。

    vercel.json 给 style.css 设了 max-age=86400。没有版本号的话,改完 CSS 回访用户
    最多要等 24 小时才看到新样式(线上实测踩过:导航改完线上仍是旧样式)。
    带上内容哈希后,改一次样式 URL 就变一次,长缓存才既安全又有效。
    """
    p = ROOT / "style.css"
    return hashlib.md5(p.read_bytes()).hexdigest()[:8] if p.exists() else "0"


CSS_VER = css_ver()

NAV = [("/monsters/", "Monsters"), ("/achievements/", "Achievements"),
       ("/endings/", "Endings"), ("/crossplay/", "Crossplay"),
       ("/guides/", "Guides"), ("/tools/", "Tools"), ("/faq/", "FAQ")]

# 二级导航:教程阶段五「导航结构:清晰的层级」+ 竞品两行导航。
# 覆盖此前 27 个进不了任何导航、只能靠正文链接触达的页面。
NAV2 = [("/release-date/", "Release date"), ("/platforms/", "Platforms"),
        ("/game-pass/", "Game Pass"), ("/price/", "Price"),
        ("/multiplayer/", "Multiplayer"), ("/nights-and-levels/", "Nights"),
        ("/demo/", "Demo"), ("/mods/", "Mods"), ("/review/", "Review"),
        ("/similar-games/", "Similar games")]

# 出站链接 —— 全部一手核实,不使用未经核实的 URL。
# STEAM_APP: 经 SteamDB app/3722330 核实(Developer Bun Muen / Publisher Kwalee /
#            Release 22 July 2026),与本站事实一致。
# STEAM_DEMO 与 OFFICIAL/X: 取自开发者官网 bunmuen.com 上的真实 <a href> 锚点。
STEAM_APP = "https://store.steampowered.com/app/3722330/Shift_At_Midnight/"
STEAM_DEMO = "https://store.steampowered.com/app/4050060/Shift_At_Midnight_Multiplayer_Demo/"
OFFICIAL_SITE = "https://www.bunmuen.com/"
DEV_X = "https://x.com/BunMuenGames"

FOOTER_FINE = ("Shift At Midnight Wiki is an unofficial fan resource. Shift At Midnight is "
               "developed by Bun Muen and published by Kwalee; all trademarks and game assets "
               "belong to their respective owners. This site is not affiliated with or endorsed "
               "by Kwalee or Bun Muen.")

VERIFIED = "Last verified 28 July 2026 &middot; game version: launch build (22 July 2026)"


def nav_html(active: str) -> str:
    out = []
    for href, label in NAV:
        cur = ' aria-current="page"' if href == active else ""
        out.append(f'      <a href="{href}"{cur}>{label}</a>')
    return "\n".join(out)


def nav2_html(active: str) -> str:
    """二级项收进 <details> 下拉 —— 单行导航,不再另起一行占位。
    用 <details>/<summary> 而非 JS 菜单:无脚本可用、键盘可达、移动端点击即开。"""
    rows = []
    # 一级项也放进抽屉,但只在窄屏显示(.m-only)。
    # 窄屏下一级项不再平铺,头部从 173px 压到约 60px —— 用户从 Google 落到内页,
    # 先看到的应该是内容不是导航。桌面端这 7 条被 CSS 隐藏,不重复渲染。
    for href, label in NAV:
        cur = ' aria-current="page"' if href == active else ""
        rows.append(f'        <a class="m-only" href="{href}"{cur}>{label}</a>')
    rows.append('        <span class="menu-sep" aria-hidden="true"></span>')
    for href, label in NAV2:
        cur = ' aria-current="page"' if href == active else ""
        rows.append(f'        <a href="{href}"{cur}>{label}</a>')
    items = "\n".join(rows)
    return (f'      <details class="more">\n'
            f'        <summary><span class="lbl-d">More</span>'
            f'<span class="lbl-m">Menu</span></summary>\n'
            f'        <div class="more-menu">\n{items}\n'
            f"        </div>\n"
            f"      </details>")


def nav2_flat_html() -> str:
    """页脚用平铺版 —— 页脚不该出现下拉,所有链接直接可见可爬。"""
    return "\n".join(f'      <a href="{href}">{label}</a>' for href, label in NAV2)


def store_block() -> str:
    """出站商店区 —— 教程潜规则④外链 + 竞品的 'Play on Steam' 按钮。
    rel 用 noopener;不加 nofollow:这些是真实、相关、对用户有用的官方链接。"""
    return f"""  <aside class="store" aria-label="Where to get the game">
    <h2>Get Shift At Midnight</h2>
    <p class="store-note">Links go to the official store and developer pages. We take no cut &mdash;
      this site earns from ads, not from sales.</p>
    <div class="store-row">
      <a class="store-btn primary" href="{STEAM_APP}" target="_blank" rel="noopener">Play on Steam</a>
      <a class="store-btn" href="{STEAM_DEMO}" target="_blank" rel="noopener">Free multiplayer demo</a>
      <a class="store-btn" href="{OFFICIAL_SITE}" target="_blank" rel="noopener">Official site</a>
    </div>
  </aside>"""


def crumbs_html(trail: list) -> str:
    """trail = [(href|None, name), ...];最后一项是当前页(无链接)。"""
    parts = ['<a href="/">Home</a>']
    for href, name in trail:
        parts.append("<span>/</span>")
        parts.append(f'<a href="{href}">{name}</a>' if href else name)
    return "".join(parts)


def breadcrumb_ld(trail: list, title: str, url: str) -> str:
    items = [{"name": "Home", "item": f"{BASE}/"}]
    for href, name in trail[:-1]:
        items.append({"name": name, "item": f"{BASE}{href}"})
    items.append({"name": trail[-1][1], "item": url})
    lines = []
    for i, it in enumerate(items, 1):
        lines.append('    { "@type": "ListItem", "position": %d, "name": "%s", "item": "%s" }'
                     % (i, it["name"], it["item"]))
    return ('<script type="application/ld+json">\n{\n'
            '  "@context": "https://schema.org",\n  "@type": "BreadcrumbList",\n'
            '  "itemListElement": [\n' + ",\n".join(lines) + "\n  ]\n}\n</script>")


def render(page: dict) -> str:
    path = page["path"]                       # 如 "monsters/marionette"
    url = f"{BASE}/{path}/"
    active = page.get("active", "/" + path.split("/")[0] + "/")
    extra_ld = ("\n" + page["extra_ld"]) if page.get("extra_ld") else ""
    # 工具页的交互脚本:按页内联,defer 不适用于内联,放 body 末尾即可。
    # 只有工具页会用到,其余 34 页一个字节都不多加。
    page_js = ("\n<script>\n" + page["script"].strip() + "\n</script>") if page.get("script") else ""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{page['title']}</title>
<meta name="description" content="{page['desc']}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta property="og:type" content="article">
<meta property="og:site_name" content="Shift At Midnight Wiki">
<meta property="og:title" content="{page['title']}">
<meta property="og:description" content="{page['desc']}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}/og-image.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{page['og_short']}">
<meta name="twitter:description" content="{page['desc']}">
<meta name="twitter:image" content="{BASE}/og-image.jpg">
<link rel="icon" href="/favicon.ico" sizes="16x16 32x32 48x48">
<link rel="icon" href="/favicon-32.png" type="image/png" sizes="32x32">
<link rel="icon" href="/favicon-192.png" type="image/png" sizes="192x192">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preconnect" href="https://pagead2.googlesyndication.com" crossorigin>
<link rel="preconnect" href="https://www.googletagmanager.com">
<link rel="dns-prefetch" href="https://www.clarity.ms">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Anton&amp;family=Jost:wght@300;400;500&amp;display=swap">
<link rel="stylesheet" href="/style.css?v={CSS_VER}">
<!-- Google AdSense ca-pub-6575082962774479 — 站点验证 + 过审后自动投放 -->
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6575082962774479" crossorigin="anonymous"></script>
{breadcrumb_ld(page['trail'], page['title'], url)}{extra_ld}
<!-- Google tag (gtag.js) — GA4 G-RFHPX1SQ5N -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-RFHPX1SQ5N"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', 'G-RFHPX1SQ5N');
</script>
<!-- Microsoft Clarity xtsrs8l2x5 -->
<script type="text/javascript">
  (function(c,l,a,r,i,t,y){{
      c[a]=c[a]||function(){{(c[a].q=c[a].q||[]).push(arguments)}};
      t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
      y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
  }})(window, document, "clarity", "script", "xtsrs8l2x5");
</script>
</head>
<body>

<header class="site">
  <div class="bar">
    <a class="brand" href="/">Shift At Midnight Wiki</a>
    <nav class="site">
{nav_html(active)}
{nav2_html(active)}
    </nav>
    <a class="steam-cta" href="{STEAM_APP}" target="_blank" rel="noopener">Play on Steam</a>
  </div>
</header>

<main>
<div class="wrap{' wide' if page.get('wide') else ''}">

  <nav class="crumbs" aria-label="Breadcrumb">
    {crumbs_html(page['trail'])}
  </nav>

  <h1>{page['h1']}</h1>
  <p class="lede">{page['lede']}</p>

  <p class="updated">{page.get('updated', VERIFIED)}</p>

{page['body']}

  <aside class="ad-native" hidden aria-label="Sponsored"></aside>

{store_block()}

  <aside class="ad-banner" hidden aria-label="Sponsored"></aside>

</div>
</main>

<footer class="site">
  <div class="bar">
    <nav>
{nav_html('')}
{nav2_flat_html()}
      <a href="/about/">About</a>
      <a href="/contact/">Contact us</a>
      <a href="/privacy/">Privacy policy</a>
    </nav>
    <p class="fine">Official links:
      <a href="{STEAM_APP}" target="_blank" rel="noopener">Steam store page</a> &middot;
      <a href="{OFFICIAL_SITE}" target="_blank" rel="noopener">bunmuen.com</a> &middot;
      <a href="{DEV_X}" target="_blank" rel="noopener">@BunMuenGames</a>
    </p>
    <p class="fine">{FOOTER_FINE}</p>
  </div>
</footer>

<script>
/* 导航「More」下拉:<details> 本身已可用(无脚本也能开合、键盘可达),
   这几行只补两个体验细节 —— 点击外部关闭、Esc 关闭。 */
(function () {{
  var d = document.querySelector('header.site details.more');
  if (!d) return;
  document.addEventListener('click', function (e) {{
    if (d.open && !d.contains(e.target)) d.open = false;
  }});
  document.addEventListener('keydown', function (e) {{
    if (e.key === 'Escape' && d.open) {{ d.open = false; d.querySelector('summary').focus(); }}
  }});
}})();
</script>
<!-- 广告位:真实 Adsterra 代码集中填在 /ads.js,不硬编码进页面 -->
<script src="/ads.js" defer></script>{page_js}
</body>
</html>
"""


def build(pages: list) -> None:
    for page in pages:
        out = ROOT / page["path"] / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(render(page), encoding="utf-8")
        print(f"  ✓ /{page['path']}/")

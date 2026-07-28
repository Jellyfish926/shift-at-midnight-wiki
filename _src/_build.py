#!/usr/bin/env python3
"""页面生成器 — 统一 head/nav/footer/JSON-LD 样板,正文逐页手写。

只负责把重复结构生成一致,不生成内容。跑完用 audit_pages 全站校验。
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "public"   # 只往发布目录写;memory.md 与 _src 不进发布树
BASE = "https://shiftatmidnightwiki.site"

NAV = [("/monsters/", "Monsters"), ("/achievements/", "Achievements"),
       ("/endings/", "Endings"), ("/crossplay/", "Crossplay"),
       ("/guides/", "Guides"), ("/faq/", "FAQ")]

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
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="alternate icon" href="/favicon.ico">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Anton&amp;family=Jost:wght@300;400;500&amp;display=swap">
<link rel="stylesheet" href="/style.css">
{breadcrumb_ld(page['trail'], page['title'], url)}{extra_ld}
<!-- Google tag (gtag.js) — GA4 G-RFHPX1SQ5N -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-RFHPX1SQ5N"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-RFHPX1SQ5N');
</script>
<!-- CLARITY_SLOT: Microsoft Clarity 代码待补 -->
</head>
<body>

<header class="site">
  <div class="bar">
    <a class="brand" href="/">Shift At Midnight Wiki</a>
    <nav class="site">
{nav_html(active)}
    </nav>
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
  <aside class="ad-banner" hidden aria-label="Sponsored"></aside>

</div>
</main>

<footer class="site">
  <div class="bar">
    <nav>
{nav_html('')}
      <a href="/platforms/">Platforms</a>
      <a href="/release-date/">Release date</a>
      <a href="/about/">About</a>
      <a href="/contact/">Contact us</a>
      <a href="/privacy/">Privacy policy</a>
    </nav>
    <p class="fine">{FOOTER_FINE}</p>
  </div>
</footer>

<!-- 广告位:真实 Adsterra 代码集中填在 /ads.js,不硬编码进页面 -->
<script src="/ads.js" defer></script>
</body>
</html>
"""


def build(pages: list) -> None:
    for page in pages:
        out = ROOT / page["path"] / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(render(page), encoding="utf-8")
        print(f"  ✓ /{page['path']}/")

#!/usr/bin/env python3
"""把手写页的 header / footer / 出站商店区 拉齐到 _build.py 的模板。

背景:index.html、achievements/、crossplay/、monsters/、404.html 这 5 个页面正文是手写的,
不由 _build.build() 生成。模板一改它们就漂移(审计 five-pages-outside-build-template)。
这个脚本做外科式替换:只换 header 整块、footer 的 nav+fine 段、并插入 store 区块,
正文一字不动。可反复执行(幂等)。

404 是错误页:按 AdSense 政策不放广告位,也不放商店 CTA。
"""
import re
from pathlib import Path

import _build as B

ROOT = Path(__file__).resolve().parent.parent / "public"

PAGES = {
    "index.html": "/",
    "achievements/index.html": "/achievements/",
    "crossplay/index.html": "/crossplay/",
    "monsters/index.html": "/monsters/",
    "404.html": "",
}


def new_header(active: str) -> str:
    return f"""<header class="site">
  <div class="bar">
    <a class="brand" href="/">Shift At Midnight Wiki</a>
    <nav class="site">
{B.nav_html(active)}
{B.nav2_html(active)}
    </nav>
    <a class="steam-cta" href="{B.STEAM_APP}" target="_blank" rel="noopener">Play on Steam</a>
  </div>
</header>"""


MORE_JS = """<script>
/* 导航「More」下拉:<details> 本身已可用(无脚本也能开合、键盘可达),
   这几行只补两个体验细节 —— 点击外部关闭、Esc 关闭。 */
(function () {
  var d = document.querySelector('header.site details.more');
  if (!d) return;
  document.addEventListener('click', function (e) {
    if (d.open && !d.contains(e.target)) d.open = false;
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && d.open) { d.open = false; d.querySelector('summary').focus(); }
  });
})();
</script>"""

FAVICON_OLD = ('<link rel="icon" href="/favicon.svg" type="image/svg+xml">\n'
               '<link rel="alternate icon" href="/favicon.ico">')
FAVICON_NEW = ('<link rel="icon" href="/favicon.ico" sizes="16x16 32x32 48x48">\n'
               '<link rel="icon" href="/favicon-32.png" type="image/png" sizes="32x32">\n'
               '<link rel="icon" href="/favicon-192.png" type="image/png" sizes="192x192">\n'
               '<link rel="apple-touch-icon" href="/apple-touch-icon.png">')


def new_footer_inner(with_official: bool) -> str:
    official = ""
    if with_official:
        official = (
            f'    <p class="fine">Official links:\n'
            f'      <a href="{B.STEAM_APP}" target="_blank" rel="noopener">Steam store page</a> &middot;\n'
            f'      <a href="{B.OFFICIAL_SITE}" target="_blank" rel="noopener">bunmuen.com</a> &middot;\n'
            f'      <a href="{B.DEV_X}" target="_blank" rel="noopener">@BunMuenGames</a>\n'
            f"    </p>\n"
        )
    return (
        f"    <nav>\n{B.nav_html('')}\n{B.nav2_flat_html()}\n"
        '      <a href="/about/">About</a>\n'
        '      <a href="/contact/">Contact us</a>\n'
        '      <a href="/privacy/">Privacy policy</a>\n'
        "    </nav>\n"
        f"{official}"
        f'    <p class="fine">{B.FOOTER_FINE}</p>'
    )


PRECONNECT_OLD = '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
PRECONNECT_NEW = (
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
    '<link rel="preconnect" href="https://pagead2.googlesyndication.com" crossorigin>\n'
    '<link rel="preconnect" href="https://www.googletagmanager.com">\n'
    '<link rel="dns-prefetch" href="https://www.clarity.ms">'
)


def patch(rel: str, active: str) -> str:
    p = ROOT / rel
    s = p.read_text(encoding="utf-8")
    before = s
    is404 = rel == "404.html"

    # 1) header 整块替换
    s = re.sub(r"<header class=\"site\">.*?</header>", new_header(active), s, count=1, flags=re.S)

    # 2) footer 内层替换(保留 <footer class="site"><div class="bar"> 外壳)
    s = re.sub(
        r'(<footer class="site">\s*<div class="bar">\n).*?(\n  </div>\s*</footer>)',
        lambda m: m.group(1) + new_footer_inner(not is404) + m.group(2),
        s, count=1, flags=re.S,
    )

    # 3) preconnect(幂等)
    if "pagead2.googlesyndication.com" not in s.split("</head>")[0] or "rel=\"preconnect\" href=\"https://pagead2" not in s:
        if PRECONNECT_OLD in s and 'rel="preconnect" href="https://pagead2' not in s:
            s = s.replace(PRECONNECT_OLD, PRECONNECT_NEW, 1)

    # 3b) favicon 换成位图套件(幂等)
    if FAVICON_OLD in s:
        s = s.replace(FAVICON_OLD, FAVICON_NEW, 1)

    # 3c) 下拉菜单脚本(幂等)
    if "details.more" not in s.split("</body>")[0].split("<footer")[-1] and "header.site details.more" not in s:
        s = s.replace("<!-- 广告位:", MORE_JS + "\n<!-- 广告位:", 1)
        if MORE_JS not in s:                      # 404 没有广告位注释块
            s = s.replace("</body>", MORE_JS + "\n</body>", 1)

    # 3d) style.css 缓存击穿版本号(每次跑都刷新成当前哈希)
    s = re.sub(r'href="/style\.css(\?v=[0-9a-f]+)?"', f'href="/style.css?v={B.CSS_VER}"', s)

    # 4) 商店区块:插在 ad-banner 之前(404 跳过)
    if not is404 and 'class="store"' not in s:
        if '<aside class="ad-banner"' in s:
            s = s.replace('  <aside class="ad-banner"', B.store_block() + '\n\n  <aside class="ad-banner"', 1)
        else:  # 没有广告位的手写页,插在 </div>\n</main> 之前
            s = re.sub(r"(\n</div>\n</main>)", "\n" + B.store_block() + r"\1", s, count=1)

    if s != before:
        p.write_text(s, encoding="utf-8")
        return "changed"
    return "unchanged"


if __name__ == "__main__":
    for rel, active in PAGES.items():
        print(f"  {patch(rel, active):9} /{rel}")

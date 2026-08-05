#!/usr/bin/env python3
"""页面合并引擎 —— 43 页 → 28 页。

【为什么要有这个文件】
AdSense 拒信里「低价值内容 / 内容不足」最常见的实物形态,不是页数少,
而是**大量 300~500 词的薄页**:每页都只回答半个问题,读者点进来就走。
本站改造前 43 个正文页平均 447 词,40 页不足 800 词 —— 正是这个形态。

合并不新增一个字,却把平均值从 447 抬到 ~850,同时消掉了几组
真实存在的重复:/guide/ 与 /guides/ 两个索引、/multiplayer/ 与 /guide/co-op/
标题抢词、/guide/story-mode/ 与 /nights-and-levels/ 正文七成重叠。

【设计取舍】
不物理合并 _content_*.py 里的 body 字符串 —— 那些是逐页手写的内容源,
打散重排会让以后维护无从下手。改成在构建期按 MERGES 表组装:
内容源保持「一个主题一个 dict」,产出侧是合并后的厚页。想拆回去只要删表。

被并入页的老 URL 全部由 vercel.json 做 308 永久跳转到 目标页#锚点,
站内链接由 rewrite_links() 全量改写 —— 合并绝不能制造死链。
"""
import re
from pathlib import Path

BASE = "https://shiftatmidnightwiki.site"
ROOT = Path(__file__).resolve().parent.parent / "public"

# ── 合并表 ────────────────────────────────────────────────────────────
# into      : 保留的目标 URL(选搜索意图更宽、URL 更自然的那一个)
# sources   : [(被并入页 path, 锚点 id, 新章节 <h2> 标题), ...] 按顺序追加
# meta      : 目标页需要改写的 title/desc/og_short/h1/lede(合并后页面变了,标题必须跟着变)
MERGES = [
    {
        "into": "multiplayer",
        "sources": [
            ("guide/co-op", "co-op", "Co-op guide: playing with two or three people"),
            ("discord", "find-players", "Where to find other players"),
        ],
        "meta": {
            "title": "Shift At Midnight Multiplayer &amp; Co-op — Players, Proximity Chat, Groups",
            "og_short": "Multiplayer &amp; Co-op",
            "desc": "How many players Shift At Midnight supports, how the 6-player lobby option works, how proximity chat changes the game, and where to find a group.",
            "h1": "Shift At Midnight multiplayer and co-op",
            "lede": "The short answer: <strong>three players by design, up to six since the 23 July patch</strong>. This page covers the player count, how co-op actually plays, and where to find people to play it with.",
        },
    },
    {
        "into": "nights-and-levels",
        "sources": [
            ("guide/story-mode", "story-mode", "Story mode: the 13-shift run"),
            ("guide/endless-mode", "endless-mode", "Endless Mode: what happens after Shift 13"),
        ],
        "meta": {
            "title": "Shift At Midnight Nights, Shifts &amp; Endless Mode Explained",
            "og_short": "Nights &amp; Endless Mode",
            "desc": "Shift At Midnight has 13 story shifts plus an Endless Mode beta that unlocks after you finish them. Here is what changes on each run and what Endless adds.",
            "h1": "Nights, shifts and Endless Mode",
            "lede": "Story mode is <strong>13 shifts</strong>. Endless Mode is a separate beta that unlocks only after you finish them. This page covers both, and the three shifts that actually change the rules.",
        },
    },
    {
        "into": "platforms",
        "sources": [
            ("game-pass", "game-pass", "Xbox Game Pass and PC Game Pass"),
        ],
        "meta": {
            "title": "Shift At Midnight Platforms — PC, Xbox, Game Pass, PS5 &amp; Switch",
            "og_short": "Platforms &amp; Game Pass",
            "desc": "Where you can play Shift At Midnight: Steam, Xbox Series X|S, and Game Pass on day one. Whether PS5, Switch and mobile versions exist, and what Play Anywhere means here.",
            "h1": "Shift At Midnight platforms",
            "lede": "Two places, officially: <strong>Steam and Xbox</strong> &mdash; and it is on Game Pass from day one. Everything else people ask about (PS5, Switch, mobile) is answered below.",
        },
    },
    {
        "into": "review",
        "sources": [
            ("price", "price", "Price: is $9.99 fair for this?"),
            ("demo", "demo", "The free multiplayer demo"),
        ],
        "meta": {
            "title": "Is Shift At Midnight Worth It? Price, Demo and the Data",
            "og_short": "Is it worth it?",
            "desc": "Shift At Midnight is $9.99 with a free multiplayer demo. Steam review data, how long it lasts, and who this game is and is not for.",
            "h1": "Is Shift At Midnight worth it?",
            "lede": "Short version: <strong>there is a free multiplayer demo</strong>, so you do not have to take anyone's word for it &mdash; including ours. Here is the price, the review data, and the honest case against buying it.",
        },
    },
    {
        "into": "employee-package",
        "sources": [
            ("joes-diner-newsletter", "newsletter", "Who writes the Joe&rsquo;s Diner newsletter?"),
        ],
        "meta": {
            "title": "Shift At Midnight Secrets — Employee Package &amp; Joe&rsquo;s Diner Newsletter",
            "og_short": "Secrets &amp; lore",
            "desc": "Two things players keep asking about: what the Employee Package actually is, and who writes the Joe's Diner newsletter you find on shift.",
            "h1": "Employee Package and the Joe&rsquo;s Diner newsletter",
            "lede": "Two small pieces of the store that players keep searching for. Neither changes how you play &mdash; both change how the place reads.",
        },
    },
    {
        "into": "tools",
        "sources": [
            ("tools/crossplay-checker", "crossplay-checker", "Crossplay checker"),
            ("tools/achievement-tracker", "achievement-tracker", "Achievement tracker"),
            ("tools/threat-lookup", "threat-lookup", "Threat lookup"),
        ],
        "meta": {
            "title": "Shift At Midnight Tools — Crossplay, Achievements, Threat Lookup",
            "og_short": "Shift At Midnight Tools",
            "desc": "Three free Shift At Midnight tools on one page: check whether your group can play together, track all 10 achievements, and look up any threat by what you saw.",
            "h1": "Shift At Midnight tools",
            "lede": "Three things this wiki can answer faster than a text page can. <strong>All of them run in your browser</strong> &mdash; nothing is uploaded, nothing needs an account.",
        },
    },
    {
        "into": "guide/beginners",
        "sources": [
            ("guide/store-management", "store-management", "Running the store while something is in the building"),
        ],
        "meta": {
            "title": "Shift At Midnight Beginner&rsquo;s Guide — Your First Shifts, Start to Finish",
            "og_short": "Beginner&rsquo;s guide",
            "desc": "Everything a new Shift At Midnight player needs: what the job actually is, the mistakes that end runs, and how to keep the counter moving while something is inside.",
            "h1": "Shift At Midnight beginner&rsquo;s guide",
            "lede": "This is a job simulator with a horror game hiding inside it. <strong>Most first runs end because the player treats it as the other way round.</strong>",
        },
    },
    {
        "into": "guide/survival",
        "sources": [
            ("guide/weapons", "weapons", "Weapons: what you can buy and what it is for"),
        ],
        "meta": {
            "title": "Shift At Midnight Survival Guide — Traps, Barricades and Weapons",
            "og_short": "Survival &amp; weapons",
            "desc": "How to survive a hunt in Shift At Midnight: barricades, traps, sound discipline, and what each weapon is actually good for.",
            "h1": "Shift At Midnight survival guide",
            "lede": "Surviving a hunt is mostly about <strong>sound and doors</strong>, and only lastly about shooting. Weapons matter &mdash; they are just the fourth thing that matters.",
        },
    },
]

# 纯删除(内容重复,无需搬运正文):老 URL 直接 308 到目标页
DROP_ONLY = {
    "guide": "/guides/",                 # 与 /guides/ 是两个功能相同的索引页
    "guide/release": "/release-date/",   # 早已 301,页面文件是残留
}


def _redirect_map() -> dict:
    """老 URL(带首尾斜杠) -> 新 URL(可带锚点)"""
    m = {f"/{p}/": t for p, t in DROP_ONLY.items()}
    for spec in MERGES:
        for src, anchor, _ in spec["sources"]:
            m[f"/{src}/"] = f"/{spec['into']}/#{anchor}"
    return m


REDIRECTS = _redirect_map()
DROPPED = set(REDIRECTS)                     # 形如 "/discord/"


def _demote(html: str) -> str:
    """被并入页的正文要落在新 <h2> 之下,标题层级整体降一级。
    必须先降 h3 再降 h2,否则 h2 会被连降两级变成 h4。"""
    html = re.sub(r"<(/?)h4\b", r"<\1h5", html)
    html = re.sub(r"<(/?)h3\b", r"<\1h4", html)
    html = re.sub(r"<(/?)h2\b", r"<\1h3", html)
    return html


def apply_merges(pages: list) -> list:
    """按 MERGES 组装,返回实际要产出的页面列表。"""
    idx = {p["path"]: p for p in pages}
    consumed = set(DROP_ONLY)

    for spec in MERGES:
        tgt = idx.get(spec["into"])
        if tgt is None:
            raise KeyError(f"合并目标不存在: {spec['into']}")
        chunks = [tgt["body"]]
        for src_path, anchor, heading in spec["sources"]:
            src = idx.get(src_path)
            if src is None:
                raise KeyError(f"被并入页不存在: {src_path}")
            consumed.add(src_path)
            chunks.append(
                f'\n  <section class="merged" id="{anchor}">\n'
                f'  <h2>{heading}</h2>\n'
                f'{_demote(src["body"])}\n  </section>\n'
            )
            # 交互脚本按顺序拼接(三个工具页各自是 IIFE,不会互相污染全局)
            if src.get("script"):
                tgt["script"] = (tgt.get("script") or "") + "\n" + src["script"]
            if src.get("wide"):
                tgt["wide"] = True
        tgt["body"] = "".join(chunks)
        tgt.update(spec["meta"])

    return [p for p in pages if p["path"] not in consumed]


# ── 站内链接改写 ──────────────────────────────────────────────────────
def rewrite_links(html: str) -> str:
    """把指向已合并页的站内链接改写到 目标页#锚点。

    长 key 先替换 —— 否则 "/guide/" 会先吃掉 "/guide/co-op/" 的前缀。
    只匹配 href="..." 的完整值,不做裸文本替换,避免误伤正文。
    """
    for old in sorted(REDIRECTS, key=len, reverse=True):
        html = html.replace(f'href="{old}"', f'href="{REDIRECTS[old]}"')
        html = html.replace(f'href="{BASE}{old}"', f'href="{BASE}{REDIRECTS[old]}"')
    return html


def rewrite_public_tree() -> int:
    """构建完成后全量改写 public/ 下所有 HTML —— 手写页也要覆盖到。"""
    n = 0
    for p in ROOT.rglob("*.html"):
        s = p.read_text(encoding="utf-8")
        t = rewrite_links(s)
        if t != s:
            p.write_text(t, encoding="utf-8")
            n += 1
    return n


def prune_dropped() -> list:
    """把被合并页留在 public/ 里的产物移出发布树。

    移出而不是删除:本仓库常在「连接文件夹」模式下被工具改动,该模式下 unlink 被禁止
    (Operation not permitted),但同文件系统内的 rename 是允许的。移到 _removed/
    (已 .gitignore)后,git 视之为删除,提交后 Vercel 上就没有这些页了 ——
    留着它们既是重复内容,也让 308 跳转形同虚设。"""
    trash = ROOT.parent / "_removed"
    trash.mkdir(exist_ok=True)
    gone = []
    for old in DROPPED:
        rel = old.strip("/").split("#")[0]
        f = ROOT / rel / "index.html"
        if f.exists():
            f.rename(trash / (rel.replace("/", "__") + ".index.html"))
            gone.append(old)
        try:
            (ROOT / rel).rmdir()      # 只删空目录,有子页面就留着
        except OSError:
            pass
    return sorted(gone)


def write_sitemap(paths: list) -> int:
    """从实际产出的页面列表重建 sitemap —— 手工维护的 sitemap 一定会漂移。"""
    urls = sorted({"/"} | {f"/{p}/" for p in paths})
    body = "\n".join(f"  <url>\n    <loc>{BASE}{u}</loc>\n  </url>" for u in urls)
    (ROOT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{body}\n</urlset>\n", encoding="utf-8")
    return len(urls)

#!/usr/bin/env python3
"""工具页 —— 教程阶段五「页面类型:攻略页、工具页、资讯页」里缺失的第三类。

铁律:所有数据均取自本站已核实并已发布的事实表,不新增任何未经核实的游戏数据。
  · crossplay 兼容矩阵  ← /crossplay/ 的 compatibility table
  · 10 个成就 + 全局解锁率 ← /achievements/ 的成就表
  · 7 个威胁的应对法     ← /monsters/ 的 Quick reference

审计明确点名「不要做」的工具(server status / steam charts / tier list / codes /
steam deck 实测)一个都没做 —— 那些必须编造数据。
"""
from _build import build

# ── 数据(与站内已发布事实一字对应) ──────────────────────────────
ACH = [
    # 全局解锁率:2026-08-05 读自 Steam 官方成就统计页
    # https://steamcommunity.com/stats/3722330/achievements/ —— 这些数字会漂,别抄旧的
    ("First Blood", "Kill your first customer", 96.9, False),
    ("Still Breathing", "Survive your first hunt", 93.8, False),
    ("Silenced", "Kill a Shrieking Doll", 89.8, False),
    ("Freed", "Kill a Demented", 79.8, False),
    ("Relentless", "Finish a hunt within 30 seconds", 45.4, False),
    ("Last Performance", "Kill a Marionette", 41.6, False),
    ("Grave Decision", "Hidden &mdash; no description shown", 33.1, True),
    ("Locked And Loaded", "Purchase all melee weapons &amp; fill out the weapons arsenal", 23.5, False),
    ("True Ending", "Hidden &mdash; no description shown", 16.0, True),
    ("Empty Home", "Hidden &mdash; no description shown", 10.1, True),
]

THREATS = [
    # 六个真实威胁 + 两个「常被当成怪物」的条目 + doppelganger 这个类别。
    # 2026-08-05 按官方补丁与交叉验证过的攻略校正:Jack-in-the-Box 是道具不是敌人;
    # Demented 打不死只能引进陷阱;Norbert 是顾客型 doppelganger 且杀他有后果。
    ("Entities", "killable", "Yes",
     "The baseline threat, and the one you summon yourself &mdash; letting a doppelganger check out "
     "brings it back that night in its real form. Barricades, traps and weapons all work.",
     "Still Breathing (93.8%)", "/guide/survival/",
     "entity, entities, spider, hunt, hunter, creature, basic, common"),
    ("Marionette", "boss", "Yes",
     "Killable, and tougher than an Entity. The music box decides it: hold E to rewind before the "
     "melody plays three times, or it summons the Marionette. The 23 July patch cut its health.",
     "Last Performance (41.6%)", "/monsters/marionette/",
     "music box, melody, puppet, strings, boss, song, tune, dancing, shift 9"),
    ("The Dentist", "unkillable", "Yes",
     "Run. Nothing else works &mdash; it is immune to weapons and traps alike. Head for Sheriff Clyde "
     "and do not stop. Shift 13 only.",
     "&mdash;", "/monsters/the-dentist/",
     "dentist, drill, teeth, mask, cannot kill, unkillable, chase, final, shift 13"),
    ("Shrieking Doll", "killable", "Yes",
     "Fragile &mdash; a few shots do it. The real cost is the noise, which is what pulls everything "
     "else onto you. Turns up during hunts, usually alongside Entities.",
     "Silenced (89.8%)", "/monsters/shrieking-doll/",
     "doll, scream, shriek, screaming, porcelain, loud, noise, crawler, small"),
    ("Demented", "trap", "Yes",
     "It freezes while you look at it &mdash; and it cannot be damaged while you look at it either. "
     "The confirmed solution is to break line of sight in a direction that walks it into a trap.",
     "Freed (79.8%)", "/monsters/demented/",
     "demented, stare, look, freeze, weeping angel, trap, deformed, twisted"),
    ("Rakes", "killable", "Yes",
     "Endless and post-story modes only, added on 29 July 2026. They come out of the forest and go "
     "for your customers rather than for you. Intercept before one reaches the store.",
     "&mdash;", "/monsters/",
     "rake, rakes, forest, endless, red glow, customer, scream, new enemy, post story"),
    ("Jack-in-the-Box", "object", "No",
     "Not an enemy &mdash; an object. It is the music box that decides the Marionette encounter. "
     "Hold E to rewind it before the melody plays three times. The 23 July patch made it louder.",
     "&mdash;", "/monsters/jack-in-the-box/",
     "jack in the box, crank, wind, toy, clown, spring, music, box, rewind"),
    ("Norbert", "customer", "No",
     "A customer, not a monster &mdash; a gnome whose ID genuinely scans as fake. Let him finish and "
     "he leaves for the shift. Shoot him and he keeps coming back in disguises.",
     "&mdash;", "/monsters/norbert/",
     "norbert, fake id, gnome, harmless, friendly, scanner, false positive, spare"),
    ("Doppelgangers", "identify", "Yes",
     "Identification, not combat. They copy a real customer's appearance, voice and story &mdash; "
     "the scanner tells you a document is fake, not that the person is hostile.",
     "First Blood (96.9%)", "/guide/doppelgangers/",
     "doppelganger, copy, imposter, twin, duplicate, same customer, id, scanner, lookalike"),
]

# Steam 与 Game Pass 生态是两个隔离的匹配池 —— 出自 /crossplay/ 的兼容表
PLATFORMS = [
    ("steam", "Steam (Windows)", "steam"),
    ("xbox", "Xbox Series X|S", "xbox"),
    ("gamepass", "PC Game Pass", "xbox"),
    ("msstore", "Microsoft Store (bought)", "xbox"),
]


def ach_rows() -> str:
    out = []
    for i, (name, req, pct, hidden) in enumerate(ACH):
        h = ' data-hidden="1"' if hidden else ""
        out.append(
            f'    <label class="tool-check">\n'
            f'      <input type="checkbox" data-ach="{i}" data-pct="{pct}"{h}>\n'
            f'      <span class="lbl"><span class="t">{name}</span>\n'
            f'        <span class="d">{req} &middot; {pct}% of players have this</span></span>\n'
            f"    </label>"
        )
    return "\n".join(out)


def threat_rows() -> str:
    out = []
    for name, kind, hostile, counter, ach, href, keys in THREATS:
        out.append(
            f'    <article class="threat" data-keys="{name.lower()}, {keys}" data-kind="{kind}">\n'
            f'      <h3><a href="{href}">{name}</a></h3>\n'
            f'      <p class="meta">Hostile: {hostile} &middot; Achievement: {ach}</p>\n'
            f"      <p>{counter}</p>\n"
            f"    </article>"
        )
    return "\n".join(out)


def plat_options() -> str:
    return "\n".join(
        f'        <option value="{pid}" data-pool="{pool}">{label}</option>'
        for pid, label, pool in PLATFORMS
    )


TOOLS_LD = """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ItemList",
  "name": "Shift At Midnight tools",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Crossplay compatibility checker", "url": "https://shiftatmidnightwiki.site/tools/crossplay-checker/" },
    { "@type": "ListItem", "position": 2, "name": "Achievement tracker", "url": "https://shiftatmidnightwiki.site/tools/achievement-tracker/" },
    { "@type": "ListItem", "position": 3, "name": "Threat lookup", "url": "https://shiftatmidnightwiki.site/tools/threat-lookup/" }
  ]
}
</script>"""


PAGES = [

# ── /tools/ 索引 ────────────────────────────────────────────────
{
 "path": "tools", "active": "/tools/",
 "title": "Shift At Midnight Tools — Crossplay, Achievements, Threats",
 "og_short": "Shift At Midnight Tools",
 "desc": "Three free tools for Shift At Midnight: check whether your group can play together, track all 10 achievements, and look up any threat by what you saw.",
 "trail": [(None, "Tools")],
 "h1": "Shift At Midnight tools",
 "lede": "Three things this wiki can answer faster than a text page can. <strong>All of them run in your browser</strong> &mdash; nothing is uploaded, nothing needs an account.",
 "extra_ld": TOOLS_LD,
 "body": """
  <div class="term tip">
    <div class="term-h">What these are built from</div>
    <p>Every tool here is driven by the same verified data as the written pages &mdash; the compatibility
      matrix from <a href="/crossplay/">crossplay</a>, the global unlock rates from
      <a href="/achievements/">achievements</a>, and the counterplay table from
      <a href="/monsters/">monsters</a>. <strong>No tool here invents data.</strong> Where a requirement
      is unverified &mdash; notably the three hidden achievements &mdash; the tool says so instead of guessing.</p>
  </div>

  <h2>The tools</h2>
  <div class="grid two">
    <a class="card" href="/tools/#crossplay-checker"><b>Crossplay checker</b><span>Pick where each of you bought the game. Get a yes/no and the cheapest fix if the answer is no.</span></a>
    <a class="card" href="/tools/#achievement-tracker"><b>Achievement tracker</b><span>Tick off all 10. Saves in your browser, and tells you which one is statistically your easiest next.</span></a>
    <a class="card" href="/tools/#threat-lookup"><b>Threat lookup</b><span>Search by what you actually saw &mdash; &ldquo;music box&rdquo;, &ldquo;screaming&rdquo;, &ldquo;fake ID&rdquo; &mdash; not by a name you do not know yet.</span></a>
  </div>

  <h2>Why not a tier list or a server status page</h2>
  <p>Other wikis for this game run tier lists, live player counts and Steam Deck verdicts. We do not,
    because none of those can be produced honestly right now: the game has one difficulty curve and no
    competitive mode, so a &ldquo;tier list&rdquo; would be invented; and a live status widget would be
    reporting a number we cannot verify. When there is something real to measure, we will build it.</p>
"""},

# ── /tools/crossplay-checker/ ───────────────────────────────────
{
 "path": "tools/crossplay-checker", "active": "/tools/",
 "title": "Shift At Midnight Crossplay Checker — Can You Play Together?",
 "og_short": "Crossplay Checker",
 "desc": "Pick where each player bought Shift At Midnight and find out instantly whether you can play together — plus the cheapest fix when the answer is no.",
 "trail": [("/tools/", "Tools"), (None, "Crossplay checker")],
 "h1": "Can you play Shift At Midnight together?",
 "lede": "Shift At Midnight has <strong>partial crossplay</strong>, and the split does not follow PC-vs-console &mdash; it follows <em>where you bought it</em>. Pick each player's store below.",
 "body": """
  <div class="tool">
    <div class="row">
      <div class="field">
        <label for="p1">Player 1 bought it on</label>
        <select id="p1">
%(opts)s
        </select>
      </div>
      <div class="field">
        <label for="p2">Player 2 bought it on</label>
        <select id="p2">
%(opts)s
        </select>
      </div>
      <div class="field">
        <label for="p3">Player 3 (optional)</label>
        <select id="p3">
          <option value="">&mdash; only two of us &mdash;</option>
%(opts)s
        </select>
      </div>
    </div>
    <div class="tool-out" id="out" role="status" aria-live="polite">
      <b>Pick a store for each player</b>
      <p>The answer updates as you choose.</p>
    </div>
    <noscript>
      <p class="noscript-note">This checker needs JavaScript. The same answer in one sentence:
        <strong>Steam players can only play with other Steam players.</strong> Xbox console, PC Game Pass
        and Microsoft Store copies all share one pool and can play with each other. Full table on the
        <a href="/crossplay/">crossplay page</a>.</p>
    </noscript>
  </div>

  <h2>The rule behind the answer</h2>
  <p>There are two matchmaking pools, not four. <strong>Steam is one pool by itself.</strong> Xbox Series X|S,
    PC Game Pass and a bought Microsoft Store copy are the second pool &mdash; they interoperate because of
    Xbox Play Anywhere. Nothing crosses between the two.</p>
  <table class="data">
    <thead><tr><th>Your platform</th><th>Can play with</th><th>Cannot play with</th></tr></thead>
    <tbody>
      <tr><td>Steam (Windows)</td><td>Steam only</td><td>Xbox console, PC Game Pass, Microsoft Store</td></tr>
      <tr><td>Xbox Series X|S</td><td>Xbox + PC Game Pass</td><td>Steam</td></tr>
      <tr><td>PC Game Pass</td><td>Xbox + PC Game Pass</td><td>Steam</td></tr>
      <tr><td>Microsoft Store (bought)</td><td>Xbox + PC Game Pass</td><td>Steam</td></tr>
    </tbody>
  </table>
  <p>The developer has said full crossplay and a server browser are planned, but they are
    <strong>not in the launch build</strong>. Until that ships, the table above is the whole story.
    Background and sourcing on the <a href="/crossplay/">crossplay page</a>.</p>

  <h2>If the answer is no</h2>
  <p>The cheapest fix is almost always <strong>PC Game Pass</strong> rather than buying a second copy:
    it puts a Steam-side player into the Xbox pool for the price of a month's subscription instead of
    another $9.99. See <a href="/platforms/#game-pass">Game Pass</a> and <a href="/review/#price">price</a>.</p>
""" % {"opts": plat_options()},
 "script": """
(function () {
  "use strict";
  var sel = [document.getElementById("p1"), document.getElementById("p2"), document.getElementById("p3")];
  var out = document.getElementById("out");
  if (!out || !sel[0]) return;

  function poolOf(s) {
    if (!s || !s.value) return null;
    return s.options[s.selectedIndex].getAttribute("data-pool");
  }
  function nameOf(s) { return s.options[s.selectedIndex].text; }

  function render() {
    var picked = sel.filter(function (s) { return s && s.value; });
    if (picked.length < 2) {
      out.className = "tool-out";
      out.innerHTML = "<b>Pick a store for each player</b><p>The answer updates as you choose.</p>";
      return;
    }
    var pools = picked.map(poolOf);
    var same = pools.every(function (p) { return p === pools[0]; });
    if (same) {
      out.className = "tool-out ok";
      out.innerHTML = "<b>Yes \\u2014 you can play together</b><p>All " + picked.length +
        " of you are in the same matchmaking pool, so you can join each other directly.</p>";
      return;
    }
    var steamers = picked.filter(function (s) { return poolOf(s) === "steam"; });
    var others = picked.filter(function (s) { return poolOf(s) === "xbox"; });
    var few = steamers.length <= others.length ? steamers : others;
    var fewIsSteam = few === steamers;
    var who = few.map(function (s) { return nameOf(s); }).join(" and ");
    var fix = fewIsSteam
      ? "The cheapest fix is for the Steam side (" + who + ") to get <strong>PC Game Pass</strong> \\u2014 " +
        "a month's subscription rather than a second $9.99 copy. That moves them into the Xbox pool."
      : "The cheapest fix is for the Game Pass / Xbox side (" + who + ") to also own it on " +
        "<strong>Steam</strong>, since a Game Pass copy cannot reach the Steam pool at all.";
    out.className = "tool-out bad";
    out.innerHTML = "<b>No \\u2014 not in the launch build</b>" +
      "<p>Steam is its own matchmaking pool. Xbox console, PC Game Pass and Microsoft Store copies share " +
      "a second pool. Nothing crosses between them.</p><p>" + fix + "</p>";
  }

  sel.forEach(function (s) { if (s) s.addEventListener("change", render); });
  render();
})();
"""},

# ── /tools/achievement-tracker/ ─────────────────────────────────
{
 "path": "tools/achievement-tracker", "active": "/tools/",
 "title": "Shift At Midnight Achievement Tracker — All 10, Saved Locally",
 "og_short": "Achievement Tracker",
 "desc": "Tick off all 10 Shift At Midnight achievements. Progress saves in your browser and the tracker shows which achievement is statistically your easiest next one.",
 "trail": [("/tools/", "Tools"), (None, "Achievement tracker")],
 "h1": "Achievement tracker",
 "lede": "All 10 achievements, ordered by how many players have them. <strong>Your ticks save in this browser only</strong> &mdash; no account, nothing sent anywhere.",
 "body": """
  <div class="tool">
    <div class="bar-track" role="img" aria-label="Completion progress"><div class="bar-fill" id="fill"></div></div>
    <p class="meta" id="count">0 of 10 &middot; 0%%</p>

%(rows)s

    <div class="tool-out" id="next" role="status" aria-live="polite">
      <b>Your easiest next one</b>
      <p>Tick what you already have and this will name the achievement the largest share of players
        unlock next.</p>
    </div>
    <div class="row" style="margin-top:16px">
      <button type="button" id="reset" class="ghost">Reset progress</button>
    </div>
    <noscript>
      <p class="noscript-note">Ticking and saving need JavaScript, but the full list with requirements and
        global unlock rates is on the <a href="/achievements/">achievements page</a> and works without it.</p>
    </noscript>
  </div>

  <h2>What the percentages mean</h2>
  <p>These are Steam global unlock rates &mdash; the share of everyone who owns the game that has the
    achievement. They are a difficulty proxy, not a guide: <strong>First Blood sits at 96.9%%</strong>
    because it unlocks for killing your first customer, which nearly everyone does by accident.</p>
  <p>The three hidden achievements &mdash; Grave Decision (33.1%%), True Ending (16.0%%) and
    Empty Home (10.1%%) &mdash; <strong>do not show their requirements in-game, and we have not verified
    them.</strong> We list what the rates imply on the <a href="/endings/">endings page</a> rather than
    publishing a guess as fact.</p>
""" % {"rows": ach_rows()},
 "script": """
(function () {
  "use strict";
  var KEY = "sam-ach-v1";
  var boxes = [].slice.call(document.querySelectorAll('input[data-ach]'));
  var fill = document.getElementById("fill");
  var count = document.getElementById("count");
  var next = document.getElementById("next");
  var reset = document.getElementById("reset");
  if (!boxes.length || !fill) return;

  function load() {
    var raw = null;
    try { raw = localStorage.getItem(KEY); } catch (e) { return; }
    if (!raw) return;
    var done = raw.split(",");
    boxes.forEach(function (b) {
      if (done.indexOf(b.getAttribute("data-ach")) > -1) b.checked = true;
    });
  }
  function save() {
    var done = boxes.filter(function (b) { return b.checked; })
                    .map(function (b) { return b.getAttribute("data-ach"); });
    try { localStorage.setItem(KEY, done.join(",")); } catch (e) {}
  }
  function render() {
    var got = boxes.filter(function (b) { return b.checked; });
    var pct = Math.round(got.length / boxes.length * 100);
    fill.style.width = pct + "%";
    count.textContent = got.length + " of " + boxes.length + " \\u00b7 " + pct + "%";

    var left = boxes.filter(function (b) { return !b.checked; });
    if (!left.length) {
      next.className = "tool-out ok";
      next.innerHTML = "<b>All 10 \\u2014 done</b><p>Including the three hidden ones. " +
        "That puts you past the 10.1% of players who have Empty Home.</p>";
      return;
    }
    left.sort(function (a, b) {
      return parseFloat(b.getAttribute("data-pct")) - parseFloat(a.getAttribute("data-pct"));
    });
    var top = left[0];
    var label = top.parentNode.querySelector(".t").textContent;
    var pctOf = top.getAttribute("data-pct");
    var hidden = top.getAttribute("data-hidden") === "1";
    var note = hidden
      ? "<p>This one is hidden \\u2014 the game does not show its requirement, and we have not verified it. " +
        "What the unlock rate implies is on the <a href='/endings/'>endings page</a>.</p>"
      : "<p>" + pctOf + "% of all players have it, which makes it the most-unlocked achievement you are " +
        "still missing.</p>";
    next.className = "tool-out warn";
    next.innerHTML = "<b>" + label + "</b>" + note;
  }

  boxes.forEach(function (b) {
    b.addEventListener("change", function () { save(); render(); });
  });
  if (reset) reset.addEventListener("click", function () {
    boxes.forEach(function (b) { b.checked = false; });
    save(); render();
  });
  load(); render();
})();
"""},

# ── /tools/threat-lookup/ ───────────────────────────────────────
{
 "path": "tools/threat-lookup", "active": "/tools/",
 "title": "Shift At Midnight Threat Lookup — Search By What You Saw",
 "og_short": "Threat Lookup",
 "desc": "Type what you saw — a music box, screaming, a fake ID on Night 2 — and get the one correct response for that Shift At Midnight threat.",
 "trail": [("/tools/", "Tools"), (None, "Threat lookup")],
 "h1": "What is chasing me?",
 "lede": "You do not always know the name of the thing in the room with you. <strong>Search by what you actually saw or heard</strong> &mdash; a music box, screaming, a fake ID &mdash; and get the one response that works.",
 "body": """
  <div class="tool">
    <div class="field">
      <label for="q">What did you see or hear?</label>
      <input type="search" id="q" placeholder="music box, screaming, fake ID, drill&hellip;"
             autocomplete="off" spellcheck="false">
    </div>
    <p class="meta" id="hits" role="status" aria-live="polite">Showing all 7 threats</p>
  </div>

  <div id="results">
%(rows)s
  </div>

  <noscript>
    <p class="noscript-note">Filtering needs JavaScript &mdash; but every threat is listed above in full,
      and each links to its own page. The same table is on the <a href="/monsters/">monsters page</a>.</p>
  </noscript>

  <h2>The two mistakes that kill people</h2>
  <div class="term warn">
    <div class="term-h">Attacking the Dentist</div>
    <p>It is the only threat in the game that cannot be fought. If you try, you die. Running is not a
      fallback here &mdash; it is the entire counterplay. See <a href="/monsters/the-dentist/">the Dentist</a>.</p>
  </div>
  <div class="term warn">
    <div class="term-h">Killing Norbert</div>
    <p>Norbert scans as a fake ID on Night 2 and is <strong>completely harmless</strong>. The scanner tells
      you a document is fake &mdash; not that the customer is hostile. See <a href="/monsters/norbert/">Norbert</a>.</p>
  </div>
""" % {"rows": threat_rows()},
 "script": """
(function () {
  "use strict";
  var q = document.getElementById("q");
  var hits = document.getElementById("hits");
  var cards = [].slice.call(document.querySelectorAll(".threat"));
  if (!q || !cards.length) return;

  function run() {
    var term = q.value.trim().toLowerCase();
    var shown = 0;
    cards.forEach(function (c) {
      var hay = c.getAttribute("data-keys") + " " + c.textContent.toLowerCase();
      var ok = !term || hay.indexOf(term) > -1;
      c.hidden = !ok;
      if (ok) shown++;
    });
    if (!term) {
      hits.textContent = "Showing all " + cards.length + " threats";
    } else if (shown === 0) {
      hits.textContent = "Nothing matches \\u201c" + q.value.trim() +
        "\\u201d \\u2014 try what you saw or heard, like \\u201cmusic box\\u201d or \\u201cfake ID\\u201d.";
    } else {
      hits.textContent = shown + (shown === 1 ? " match" : " matches");
    }
  }
  q.addEventListener("input", run);
  run();
})();
"""},

# ── /guide/ 索引:修掉线上 404 ───────────────────────────────────
{
 "path": "guide", "active": "/guides/",
 "title": "Shift At Midnight Guides Index — All Walkthroughs",
 "og_short": "Guides Index",
 "desc": "Every Shift At Midnight guide in one place: beginners, doppelgangers, survival, co-op, weapons, store management, story mode and endless mode.",
 "trail": [(None, "Guide index")],
 "h1": "Guide index",
 "lede": "Every guide on this wiki. If you landed here from a link, the main hub with descriptions is <a href=\"/guides/\">the guides page</a>.",
 "body": """
  <h2>All guides</h2>
  <div class="grid two">
    <a class="card" href="/guide/beginners/"><b>Beginners</b><span>Your first shift, and the three things nobody tells you.</span></a>
    <a class="card" href="/guide/doppelgangers/"><b>Doppelgangers</b><span>Identification, not combat &mdash; the actual game.</span></a>
    <a class="card" href="/guide/survival/"><b>Survival</b><span>Boarding up, traps, and hiding when it goes wrong.</span></a>
    <a class="card" href="/multiplayer/#co-op"><b>Co-op</b><span>Playing with 2&ndash;3 people and proximity chat.</span></a>
    <a class="card" href="/guide/survival/#weapons"><b>Weapons</b><span>What you can buy and what it is actually for.</span></a>
    <a class="card" href="/guide/beginners/#store-management"><b>Store management</b><span>Running the counter while something is in the building.</span></a>
    <a class="card" href="/nights-and-levels/#story-mode"><b>Story mode</b><span>The scripted run and how it differs from endless.</span></a>
    <a class="card" href="/nights-and-levels/#endless-mode"><b>Endless mode</b><span>The free Q4 2026 addition.</span></a>
  </div>

  <h2>Tools</h2>
  <div class="grid two">
    <a class="card" href="/tools/#crossplay-checker"><b>Crossplay checker</b><span>Can your group play together?</span></a>
    <a class="card" href="/tools/#achievement-tracker"><b>Achievement tracker</b><span>All 10, saved in your browser.</span></a>
    <a class="card" href="/tools/#threat-lookup"><b>Threat lookup</b><span>Search by what you saw.</span></a>
  </div>
"""},
]

if __name__ == "__main__":
    print("生成工具页 + guide 索引:")
    build(PAGES)

#!/usr/bin/env python3
"""/tools/completion-tracker/ —— 100% 完成度追踪器。

铁律与其他工具页一致:**一条都不编**。每个可勾选条目都必须在本站已发布的页面里
有对应出处,条目文案是那页事实的压缩,`src` 就是那页的 URL。站内没有页可追溯的
东西(武器清单、收集品、兑换码、47 个 doppelganger 的完整名单)一律不收,并在
正文里明写「本站只收录了 N 条」而不是「全部」。

数据来源对照:
  ACHIEVEMENTS  ← achievements.json(Steam 公开成就页,scripts/fetch_achievements.py 抓)
                  + /endings/(三个隐藏成就的条件)
  ENDINGS       ← /endings/
  MILESTONES    ← /nights-and-levels/、/demo/、/multiplayer/
  BESTIARY      ← /monsters/ 与六个怪物子页
  COUNTER/TELLS ← /guide/doppelgangers/
  NAMED         ← /guide/doppelgangers/(该页只点名 5 个)
"""
import json as _json
import pathlib as _pathlib

from _build import build

_ACH_FILE = _pathlib.Path(__file__).resolve().parent.parent / "achievements.json"
_ACH_CAPTURED = "2026-09-07"
if _ACH_FILE.exists():
    _ACH_CAPTURED = _json.loads(_ACH_FILE.read_text()).get("captured", _ACH_CAPTURED)

# ── 条目表 ────────────────────────────────────────────────────────────
# (id, 名称, 一句话怎么达成, 来源页 URL)
# id 一经发布不可改动、不可重排 —— 进度码是按本表顺序压的位图,改顺序会让所有旧码错位。

ACHIEVEMENTS = [
    ("ach-first-blood", "First Blood",
     "Kill your first customer. 96.7% of players have it &mdash; usually by mistake.", "/achievements/"),
    ("ach-still-breathing", "Still Breathing",
     "Survive your first hunt, which starts when you let a doppelganger check out.", "/achievements/"),
    ("ach-silenced", "Silenced",
     "Kill a Shrieking Doll. It is fragile; the cost is the noise you make doing it.", "/monsters/shrieking-doll/"),
    ("ach-freed", "Freed",
     "Kill a Demented &mdash; break line of sight in a direction that walks it into a trap.", "/monsters/demented/"),
    ("ach-relentless", "Relentless",
     "Finish a hunt within 30 seconds. Be armed and equipped before it starts.", "/guide/survival/#weapons"),
    ("ach-last-performance", "Last Performance",
     "Kill a Marionette. The 23 July patch cut its health, which made this realistic.", "/monsters/marionette/"),
    ("ach-grave-decision", "Grave Decision",
     "Hidden. Unlocks on the ending where you call Sheriff Clyde after Shift 12.", "/endings/"),
    ("ach-locked-and-loaded", "Locked And Loaded",
     "Purchase all melee weapons and fill out the weapons arsenal. A budgeting problem, not a skill one.",
     "/guide/survival/#weapons"),
    ("ach-true-ending", "True Ending",
     "Hidden. Unlocks on the ending where you do not call Clyde and finish Shift 13 with $250 or more.",
     "/endings/"),
    ("ach-empty-home", "Empty Home",
     "Hidden. Unlocks on the ending where you do not call Clyde and finish under $250.", "/endings/"),
]

ENDINGS = [
    ("end-grave-decision", "Grave Decision ending",
     "Call Sheriff Clyde after Shift 12. Money is irrelevant on this branch: your pet lives, Clyde dies.",
     "/endings/"),
    ("end-true-ending", "True Ending",
     "Do not call Clyde, and hold at least $250 when Shift 13 ends. Pet and Clyde both survive.",
     "/endings/"),
    ("end-empty-home", "Empty Home ending",
     "Do not call Clyde and finish Shift 13 under $250. Clyde lives; you cannot pay for the surgery.",
     "/endings/"),
]

MILESTONES = [
    ("run-finish-story", "Finish all 13 story shifts",
     "Story Mode is 13 procedurally generated shifts. There is no night-by-night route to follow.",
     "/nights-and-levels/"),
    ("run-shift-9", "Get through the Shift 9 music-box beat without summoning the Marionette",
     "From Shift 9 a N.E.T. email warns you. Find the box and hold E to rewind before the melody plays three times.",
     "/monsters/jack-in-the-box/"),
    ("run-shift-12", "Reach the post-Shift-12 decision about Sheriff Clyde",
     "This is the fork that decides which of the three endings you get.", "/endings/"),
    ("run-endless", "Unlock the Endless Mode beta",
     "It has been in the game since launch day and unlocks once you finish Story Mode.",
     "/nights-and-levels/#endless-mode"),
    ("run-six-player", "Play a shift in a six-player lobby",
     "Lobby size became selectable up to six in the 23 July patch. The developer calls it a party mode, not the intended experience.",
     "/multiplayer/"),
    ("run-proximity", "Play a full shift in co-op with proximity chat",
     "The mechanic the co-op is built around &mdash; and the reason a floor watcher can talk without breaking the counter.",
     "/multiplayer/"),
    ("run-demo", "Play the three pre-scripted shifts of the free demo",
     "A separate free Steam app. Scripted, not generated, so it previews the loop rather than the experience.",
     "/demo/"),
]

BESTIARY = [
    ("mon-entity", "Entity",
     "The baseline hunter, and the one you summon yourself by waving a doppelganger through. Barricades, traps and weapons all work.",
     "/monsters/entity/"),
    ("mon-shrieking-doll", "Shrieking Doll",
     "A low crawler during hunts. Dies to a few shots; the noise is what pulls everything else onto you.",
     "/monsters/shrieking-doll/"),
    ("mon-demented", "Demented",
     "Frozen while you look at it &mdash; and invulnerable while you look at it. Walk it into a trap instead.",
     "/monsters/demented/"),
    ("mon-marionette", "Marionette",
     "The Shift 9 encounter. Killable, and tougher than an Entity.", "/monsters/marionette/"),
    ("mon-dentist", "The Dentist",
     "Shift 13 only, and the only threat with no counterplay: run at Sheriff Clyde and do not stop.",
     "/monsters/the-dentist/"),
    ("mon-rake", "Rake",
     "Endless and post-story only, added 29 July 2026. Follow the screaming and intercept it before it reaches a customer.",
     "/monsters/rake/"),
    ("mon-jack-in-the-box", "Jack-in-the-Box",
     "Not an enemy &mdash; the wind-up music box that decides the Marionette encounter. Rewind it by hand at least once.",
     "/monsters/jack-in-the-box/"),
    ("mon-norbert", "Norbert",
     "Not a monster &mdash; a customer whose ID genuinely scans as fake. Let him finish his purchase and leave.",
     "/monsters/norbert/"),
    ("mon-doppelganger", "Doppelganger",
     "A category rather than a creature. Catch one at the counter before it completes a purchase.",
     "/guide/doppelgangers/"),
]

COUNTER = [
    ("tool-id-scan", "Run an ID through the scanner",
     "It answers exactly one question: is this document what it claims to be?", "/guide/doppelgangers/"),
    ("tool-net-search", "Search the N.E.T. database by hand",
     "You can type a name in yourself without a document. Most new players never touch it.",
     "/guide/doppelgangers/"),
    ("tool-description-box", "Catch someone out with the description box",
     "Registered appearance, occupation, personal details and shopping habits &mdash; there to be contradicted.",
     "/guide/doppelgangers/"),
    ("tool-anomaly-lens", "Use the Anomaly Lens",
     "One of the five checks the counter gives you.", "/guide/doppelgangers/"),
    ("tool-plate-records", "Check vehicle and plate records",
     "A later unlock, and the only check that concerns something outside the building.",
     "/guide/doppelgangers/"),
]

TELLS = [
    ("tell-identity", "Name or personal details do not match the ID",
     "The strongest version: the database reports that the real person is dead.", "/guide/doppelgangers/"),
    ("tell-occupation", "Stated occupation contradicts the record",
     "Ask what they do, then read what the file says they do.", "/guide/doppelgangers/"),
    ("tell-habits", "Habits or purchases do not line up with the file",
     "Compare the shopping habits on record against what is on the counter.", "/guide/doppelgangers/"),
    ("tell-appearance", "Appearance or clothing contradicts the file",
     "Build, features, photo versus the person standing there &mdash; scar placement catches copies.",
     "/guide/doppelgangers/"),
    ("tell-behaviour", "Behaviour is abnormal",
     "The vaguest tell and the one that improves fastest: you cannot see abnormal until you have watched a lot of normal.",
     "/guide/doppelgangers/"),
    ("tell-emotion", "The emotion readout does not match the words",
     "A reading that contradicts what the person is saying is a tell on its own.", "/guide/doppelgangers/"),
    ("tell-plate", "The plate does not match the vehicle's registered owner",
     "The one check that happens away from the till.", "/guide/doppelgangers/"),
]

NAMED = [
    ("dop-nathan-calloway", "Nathan Calloway",
     "The database says the real Nathan is dead.", "/guide/doppelgangers/"),
    ("dop-natasha-lin", "Natasha Lin",
     "Describes working a morning shift at a place that only opens at night.", "/guide/doppelgangers/"),
    ("dop-agnes-wells", "Agnes Wells",
     "The real Agnes Wells is three years old.", "/guide/doppelgangers/"),
    ("dop-ray-rowland", "Ray Rowland",
     "His neck is far too long.", "/guide/doppelgangers/"),
    ("dop-net-pongsak", "Net Pongsak",
     "He is floating.", "/guide/doppelgangers/"),
]

# (分组 id, 标题, 一句话说明, 条目表)
GROUPS = [
    ("achievements", "Achievements",
     'All 10 Steam achievements. This is the complete set &mdash; Steam lists 10 and we track 10, read on '
     f'<strong>{_ACH_CAPTURED}</strong>. Three of them are hidden in-game.', ACHIEVEMENTS),
    ("endings", "Endings",
     "Three outcomes, decided by two variables. They are mutually exclusive inside one run, so this "
     "category takes a minimum of three completed playthroughs.", ENDINGS),
    ("milestones", "Run milestones",
     "The fixed beats of a run, plus the modes that sit either side of it. Everything else in Story Mode "
     "is procedurally generated, so there is nothing else here that is the same for two players.", MILESTONES),
    ("bestiary", "Bestiary",
     "Every named threat on this wiki &mdash; including the two that people search for as monsters and are "
     "not: one is an object, one is a customer.", BESTIARY),
    ("counter", "Counter toolkit",
     "The five checks the job gives you. Not tracked by the game; tick one when you have actually caught "
     "something with it.", COUNTER),
    ("tells", "The seven categories of tell",
     "Catch a doppelganger by each kind of contradiction. Also not tracked by the game.", TELLS),
    ("named", "Named doppelgangers documented here",
     "<strong>5 of a reported 47.</strong> DualShockers has documented 47 named doppelgangers; this wiki "
     "names five, so this category is deliberately partial and always will be until we can verify more.",
     NAMED),
]

ALL_IDS = [row[0] for g in GROUPS for row in g[3]]
TOTAL = len(ALL_IDS)
assert len(set(ALL_IDS)) == TOTAL, "条目 id 重复"


def _rows(items) -> str:
    out = []
    for iid, name, how, src in items:
        out.append(
            f'      <label class="tool-check">\n'
            f'        <input type="checkbox" data-id="{iid}">\n'
            f'        <span class="lbl"><span class="t"><a href="{src}">{name}</a></span>\n'
            f'          <span class="d">{how}</span></span>\n'
            f"      </label>"
        )
    return "\n".join(out)


def _groups_html() -> str:
    out = []
    for gid, title, note, items in GROUPS:
        out.append(
            f'  <section class="tool" id="g-{gid}" data-group="{gid}">\n'
            f'    <div class="cat-h">\n'
            f"      <h3>{title}</h3>\n"
            f'      <p class="meta" data-cat-count>0 / {len(items)}</p>\n'
            f"    </div>\n"
            f'    <div class="bar-track" role="img" aria-label="{title} progress">'
            f'<div class="bar-fill" data-cat-fill></div></div>\n'
            f'    <p class="cat-note">{note}</p>\n'
            f"{_rows(items)}\n"
            f"  </section>"
        )
    return "\n".join(out)


BODY = """
  <div class="tool" id="summary">
    <div class="cat-h">
      <h2 id="progress">Your completion</h2>
      <p class="meta" id="total-count">0 of %(total)d &middot; 0%%</p>
    </div>
    <div class="bar-track" role="img" aria-label="Total completion progress"><div class="bar-fill" id="total-fill"></div></div>
    <p class="cat-note">%(total)d tick boxes across %(groups)d categories, every one of them traceable to a page
      on this wiki. Ticks save in <strong>this browser only</strong> &mdash; no account, nothing uploaded.</p>
    <div class="row" style="margin-top:16px">
      <button type="button" id="export">Export progress code</button>
      <button type="button" id="import" class="ghost">Import a code</button>
      <button type="button" id="reset" class="ghost">Reset everything</button>
    </div>
    <div class="code-box" id="code-box" hidden>
      <label for="code">Progress code</label>
      <textarea id="code" rows="3" spellcheck="false" autocomplete="off"></textarea>
      <div class="row" style="margin:12px 0 0">
        <button type="button" id="apply">Load this code</button>
        <button type="button" id="copy" class="ghost">Copy</button>
        <button type="button" id="close-code" class="ghost">Close</button>
      </div>
    </div>
    <div class="tool-out" id="msg" role="status" aria-live="polite">
      <b>Nothing ticked yet</b>
      <p>Start anywhere. The bar above and each category bar update as you go.</p>
    </div>
    <noscript>
      <p class="noscript-note">Ticking, saving and the progress code all need JavaScript &mdash; but the full
        checklist below is plain HTML, so you can read it, print it, or follow the links without it.</p>
    </noscript>
  </div>

  <h2>The checklist</h2>
%(groups_html)s

  <h2>How to use this, and where the list comes from</h2>
  <p>Tick a box and it is remembered in this browser under a single key. Nothing is sent anywhere, there is
    no account, and closing the tab loses nothing. The trade-off is that browser storage is
    per-device: your phone and your desktop keep separate lists, and clearing site data wipes it. That is
    what the <strong>progress code</strong> is for. Export produces a short string that encodes exactly which
    boxes are ticked &mdash; paste it into the same box on another device, hit <em>Load this code</em>, and the
    two match. The code is a base64 bitmap of this page's fixed item order: no name, no account,
    nothing identifying.</p>
  <p>The list is assembled from this wiki's own pages. The ten achievements come from the Steam achievement stats page, re-read on <strong>%(captured)s</strong>
    and refreshed weekly by this site's build &mdash; the full list with unlock rates is on
    <a href="/achievements/">achievements</a>. The three endings, and the conditions that separate them, come
    from <a href="/endings/">endings</a>. The bestiary entries are the named threats on
    <a href="/monsters/">monsters</a>. The counter toolkit,
    the seven categories of tell and the five named doppelgangers all come from
    <a href="/guide/doppelgangers/">identifying doppelgangers</a>. Every item name is a link back to the page
    it came from, so you can check any line against its source.</p>

  <h2>Where this list is knowingly incomplete</h2>
  <p>A tracker that pretends to be exhaustive is worse than one that admits its edges.</p>
  <ul>
    <li><strong>Named doppelgangers: 5 of a reported 47.</strong> DualShockers documented 47; this wiki names
      five, because listing all of them in advance replaces the game with a lookup table &mdash; and because we
      have not verified the rest. See <a href="/guide/doppelgangers/">the identification guide</a>.</li>
    <li><strong>Weapons: no per-weapon list exists here.</strong> Locked And Loaded asks you to buy every melee
      weapon, but no published list of those weapons or their prices could be verified, so there is one tick
      box for the achievement and none for individual weapons. See
      <a href="/guide/survival/#weapons">weapons</a>.</li>
    <li><strong>No collectibles, no codes.</strong> There is no documented collectible system, and no official
      console commands or cheat codes exist &mdash; lists of "item IDs" for this game are not traceable to
      the developer. See <a href="/cheats/">cheats and console commands</a>.</li>
    <li><strong>No per-night checklist.</strong> Shifts are procedurally generated, so a night-by-night list
      would describe one person's run. Only the fixed beats are in the milestones category. See
      <a href="/nights-and-levels/">nights and shifts</a>.</li>
    <li><strong>Endless Mode is still a beta.</strong> The finished version is a free Q4 2026 update. If it
      adds achievements or named threats, they get added here with a date on them.</li>
  </ul>
  <p>New to the game and unsure where to begin? <a href="/start-here/">Start here</a> orders the pages by what
    you need first. If you would rather track only the ten achievements with their global unlock rates
    attached, the older <a href="/tools/#achievement-tracker">achievement tracker</a> does exactly that.</p>
""" % {"total": TOTAL, "groups": len(GROUPS), "groups_html": _groups_html(), "captured": _ACH_CAPTURED}


SCRIPT = """
(function () {
  "use strict";
  var KEY = "sam-completion-v1";
  var PREFIX = "SAM1-";
  var boxes = [].slice.call(document.querySelectorAll('#main-tracker input[data-id]'));
  if (!boxes.length) return;

  var totalFill = document.getElementById("total-fill");
  var totalCount = document.getElementById("total-count");
  var msg = document.getElementById("msg");
  var codeBox = document.getElementById("code-box");
  var codeArea = document.getElementById("code");
  var groups = [].slice.call(document.querySelectorAll('section[data-group]'));

  /* 名称本身是链接,但它在 <label> 里 —— 不拦截的话点链接会顺带勾掉这一条。 */
  [].slice.call(document.querySelectorAll('.tool-check .t a')).forEach(function (a) {
    a.addEventListener("click", function (e) { e.stopPropagation(); });
  });

  function checkedIds() {
    return boxes.filter(function (b) { return b.checked; })
                .map(function (b) { return b.getAttribute("data-id"); });
  }
  function save() {
    try { localStorage.setItem(KEY, checkedIds().join(",")); } catch (e) {}
  }
  function load() {
    var raw = null;
    try { raw = localStorage.getItem(KEY); } catch (e) { return; }
    if (!raw) return;
    var done = raw.split(",");
    boxes.forEach(function (b) {
      if (done.indexOf(b.getAttribute("data-id")) > -1) b.checked = true;
    });
  }

  /* ── 进度码:按本页固定条目顺序压成位图 → base64 ── */
  function encode() {
    var bits = boxes.map(function (b) { return b.checked ? "1" : "0"; }).join("");
    while (bits.length % 8) bits += "0";
    var s = "";
    for (var i = 0; i < bits.length; i += 8) s += String.fromCharCode(parseInt(bits.substr(i, 8), 2));
    return PREFIX + btoa(s).replace(/=+$/, "");
  }
  function decode(code) {
    var c = String(code).trim().replace(/\\s+/g, "");
    if (c.indexOf(PREFIX) === 0) c = c.slice(PREFIX.length);
    if (!c) return null;
    if (!/^[A-Za-z0-9+/=]+$/.test(c)) return null;
    while (c.length % 4) c += "=";
    var raw;
    try { raw = atob(c); } catch (e) { return null; }
    var bits = "";
    for (var i = 0; i < raw.length; i++) {
      bits += ("0000000" + raw.charCodeAt(i).toString(2)).slice(-8);
    }
    if (bits.length < boxes.length) return null;
    return bits;
  }
  function applyCode(code) {
    var bits = decode(code);
    if (!bits) {
      say("bad", "That code did not read",
          "A progress code looks like <code>SAM1-\\u2026</code> and comes from the Export button on this page. " +
          "Nothing was changed.");
      return;
    }
    boxes.forEach(function (b, i) { b.checked = bits.charAt(i) === "1"; });
    save(); render();
    say("ok", "Code loaded", "Your ticks now match that code. It is saved in this browser too.");
  }
  function say(cls, title, text) {
    msg.className = "tool-out" + (cls ? " " + cls : "");
    msg.innerHTML = "<b>" + title + "</b><p>" + text + "</p>";
  }

  function render() {
    var got = 0;
    groups.forEach(function (g) {
      var gb = [].slice.call(g.querySelectorAll("input[data-id]"));
      var n = gb.filter(function (b) { return b.checked; }).length;
      got += n;
      var pct = Math.round(n / gb.length * 100);
      g.querySelector("[data-cat-fill]").style.width = pct + "%";
      g.querySelector("[data-cat-count]").textContent = n + " / " + gb.length;
    });
    var pct = Math.round(got / boxes.length * 100);
    totalFill.style.width = pct + "%";
    totalCount.textContent = got + " of " + boxes.length + " \\u00b7 " + pct + "%";
  }

  boxes.forEach(function (b) {
    b.addEventListener("change", function () { save(); render(); });
  });

  document.getElementById("export").addEventListener("click", function () {
    codeBox.hidden = false;
    codeArea.value = encode();
    codeArea.focus();
    codeArea.select();
    say("ok", "Here is your progress code",
        "Copy it and paste it into this box on your other device, then press Load this code.");
  });
  document.getElementById("import").addEventListener("click", function () {
    codeBox.hidden = false;
    codeArea.value = "";
    codeArea.focus();
    say("", "Paste a progress code",
        "Then press Load this code. It replaces every tick on this page with the ones in the code.");
  });
  document.getElementById("apply").addEventListener("click", function () {
    applyCode(codeArea.value);
  });
  document.getElementById("copy").addEventListener("click", function () {
    codeArea.select();
    var ok = false;
    try { ok = document.execCommand("copy"); } catch (e) {}
    if (!ok && navigator.clipboard) { navigator.clipboard.writeText(codeArea.value); ok = true; }
    say(ok ? "ok" : "warn", ok ? "Copied" : "Copy it by hand",
        ok ? "The code is on your clipboard." : "Your browser blocked the copy \\u2014 select the text and copy it yourself.");
  });
  document.getElementById("close-code").addEventListener("click", function () {
    codeBox.hidden = true;
  });
  document.getElementById("reset").addEventListener("click", function () {
    if (!window.confirm("Clear every tick on this page? This cannot be undone, and any progress code you have not saved will be lost.")) return;
    boxes.forEach(function (b) { b.checked = false; });
    save(); render();
    say("warn", "Everything cleared", "All " + boxes.length + " boxes are unticked again.");
  });

  load(); render();
})();
"""


PAGES = [
{
 "path": "tools/completion-tracker", "active": "/tools/",
 "title": "Shift At Midnight 100% Completion Tracker — 46 Checkboxes, Saved Locally",
 "og_short": "Completion Tracker",
 "desc": ("Tick off every Shift At Midnight achievement, ending, threat and run milestone this wiki has "
          "verified. Progress saves in your browser, and an export code moves it between devices."),
 "trail": [("/tools/", "Tools"), (None, "Completion tracker")],
 "h1": "Shift At Midnight 100% completion tracker",
 "lede": ("Every achievement, ending, named threat and fixed story beat this wiki can source, in one "
          "checklist. <strong>Your ticks save in this browser</strong> &mdash; and an export code carries them "
          "to another device without an account."),
 "extra_ld": """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "Complete everything in Shift At Midnight",
  "description": "A checklist of every Shift At Midnight achievement, ending, named threat and fixed story beat documented on this wiki.",
  "step": [
    { "@type": "HowToStep", "name": "Finish the 13 story shifts", "url": "https://shiftatmidnightwiki.site/nights-and-levels/" },
    { "@type": "HowToStep", "name": "Collect all three endings", "url": "https://shiftatmidnightwiki.site/endings/" },
    { "@type": "HowToStep", "name": "Unlock all 10 achievements", "url": "https://shiftatmidnightwiki.site/achievements/" },
    { "@type": "HowToStep", "name": "Meet every named threat", "url": "https://shiftatmidnightwiki.site/monsters/" }
  ]
}
</script>""",
 "body": '<div id="main-tracker">\n' + BODY + "\n</div>",
 "script": SCRIPT,
},
]

if __name__ == "__main__":
    print(f"生成完成度追踪器({TOTAL} 条 / {len(GROUPS)} 类):")
    build(PAGES)

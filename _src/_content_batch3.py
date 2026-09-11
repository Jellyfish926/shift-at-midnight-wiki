#!/usr/bin/env python3
"""2026-09-11 第三批新增页 —— 站内素材重组型,三页,不新增事实。

本容器出不了外网,所有陈述只汇总自本仓已产出的 public/ 页面,不引入新来源。

/glossary/          A-Z 术语表,汇总各页出现的系统/敌人/机制专有名词
/monsters/compare/   七个敌人的对比表 + 「遇到哪个该怎么办」
/start-here/         新手到进阶的阅读顺序,结尾 FAQ 全部链回站内出处
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))

M = [("/monsters/", "Monsters")]

PAGES = [
{
 "path": "glossary",
 "active": "/guides/",
 "title": "Shift At Midnight Glossary: Every Term, A to Z",
 "og_short": "Glossary of terms",
 "desc": "Every Shift At Midnight term explained in one place — doppelganger tells, the N.E.T. database, the Hunt, Endless Mode and more — each linked to the full page.",
 "trail": [(None, "Glossary")],
 "h1": "Shift At Midnight glossary",
 "lede": "This wiki uses a lot of terms the game itself never stops to define &mdash; the <strong>N.E.T. database</strong>, a <strong>Hunt</strong>, the difference between <strong>Story</strong> and <strong>Post-Story Endless</strong>. This page collects every one of them in a single A-Z list, each with a short definition and a link to the page that covers it in full. Nothing here is a new claim &mdash; every entry is compiled from a page this wiki has already published.",
 "updated": "Last verified 11 September 2026 &middot; game version: 29 July 2026 patch",
 "body": """
  <div class="tags">
    <span class="tag">39 terms</span>
    <span class="tag">Compiled from on-site pages</span>
    <span class="tag amber">No new facts introduced</span>
  </div>

  <h2>How to use this list</h2>
  <p>Each entry is one or two sentences plus a link to the page that covers it properly. Definitions here are deliberately thin &mdash; anything unverified stays on the linked page, not duplicated here.</p>

  <h2>A&ndash;Z</h2>

  <h3>A</h3>
  <p><strong>Achievements.</strong> Ten Steam achievements, three hidden until unlocked, running 96.9% down to 10.1%. See <a href="/achievements/">the achievements page</a>.</p>

  <h3>B</h3>
  <p><strong>Barricade.</strong> Wooden boards over doors and windows that slow the <a href="/monsters/entity/">Entity</a> during a Hunt. See the <a href="/guide/survival/">survival guide</a>.</p>
  <p><strong>BepInEx.</strong> The unofficial modding framework the community scene is built on &mdash; there is no Steam Workshop. See <a href="/mods/">mods</a>.</p>
  <p><strong>Blood Moon.</strong> A guaranteed-Hunt shift: blood rain falls and the Entity comes regardless of your counter work. See the <a href="/monsters/entity/">Entity page</a>.</p>
  <p><strong>Bun Muen.</strong> The solo developer who built Shift At Midnight, credited alone on Steam and the original itch.io page. See <a href="/credits/">credits</a>.</p>

  <h3>C</h3>
  <p><strong>Cheats / trainers.</strong> No official console commands; third-party trainers exist from providers like WeMod and PLITCH, unverified here. See <a href="/cheats/">cheats</a>.</p>
  <p><strong>Controller support.</strong> None on PC &mdash; every field in Steam's declaration reads false; Xbox is controller-only by contrast. See <a href="/controls/">controls</a>.</p>
  <p><strong>Crossplay.</strong> Partial: Xbox console and PC Game Pass share one pool, Steam is separate. See <a href="/crossplay/">crossplay</a>.</p>

  <h3>D</h3>
  <p><strong>Demented.</strong> Freezes only while you look directly at it, not killable by gunfire &mdash; break your gaze and lead it into a trap. See the <a href="/monsters/demented/">Demented page</a>.</p>
  <p><strong>The Dentist.</strong> The final shift's threat, confirmed immune to firearms and melee; only Sheriff Clyde ends the encounter. See <a href="/monsters/the-dentist/">the Dentist</a>.</p>
  <p><strong>Demo.</strong> A free build, still listed as of 12 August 2026 &mdash; three pre-scripted shifts against the full game's 13 random ones. See <a href="/demo/">demo</a>.</p>
  <p><strong>Doppelganger.</strong> A customer wearing a real person's identity that you catch via scanner and database before the purchase completes &mdash; the core loop of every shift. See <a href="/guide/doppelgangers/">the doppelganger guide</a>.</p>

  <h3>E</h3>
  <p><strong>Employee Package.</strong> A physical launch giveaway item; this wiki covers giveaway-phishing risk under the same page. See <a href="/employee-package/">Employee Package</a>.</p>
  <p><strong>Endings.</strong> Three outcomes &mdash; Grave Decision, True Ending, Empty Home &mdash; decided by two variables at Shift 13. See <a href="/endings/">endings</a>.</p>
  <p><strong>Endless Mode.</strong> An open-beta mode that unlocks only after finishing Story Mode's 13 shifts. See <a href="/nights-and-levels/">nights &amp; Endless Mode</a>.</p>
  <p><strong>Entity.</strong> The true form of a doppelganger that completes its purchase &mdash; blind, and tracks sound including proximity voice chat. See <a href="/monsters/entity/">the Entity</a>.</p>
  <p><strong>EULA.</strong> Kwalee's licence agreement; its anti-modification clause is why trainers are against the terms. See <a href="/cheats/">cheats</a>.</p>

  <h3>G</h3>
  <p><strong>Grave Decision.</strong> The most common of the three endings, at 33.1% global unlock. See <a href="/endings/">endings</a>.</p>

  <h3>H</h3>
  <p><strong>Hunt.</strong> Triggered by a missed doppelganger or a Blood Moon shift &mdash; survival is mostly sound and doors, weapons last. See <a href="/guide/survival/">the survival guide</a>.</p>

  <h3>I</h3>
  <p><strong>itch.io prototype.</strong> The free singleplayer build the game started as, carrying its own composer credit and a "no generative AI" disclosure. See <a href="/credits/">credits</a>.</p>

  <h3>J</h3>
  <p><strong>Jack-in-the-Box.</strong> An item, not a monster &mdash; a random spawn that summons the <a href="/monsters/marionette/">Marionette</a>. See <a href="/monsters/jack-in-the-box/">Jack-in-the-Box</a>.</p>

  <h3>K</h3>
  <p><strong>Kwalee.</strong> The publisher; distribution and storefront presence, not development &mdash; Bun Muen built the game alone. See <a href="/credits/">credits</a>.</p>

  <h3>L</h3>
  <p><strong>Languages.</strong> Nine, confirmed on both Steam and Xbox. Whether every one has full voice audio or interface/subtitles only is unresolved &mdash; sources on this wiki disagree. See <a href="/languages/">languages</a>.</p>

  <h3>M</h3>
  <p><strong>Marionette.</strong> From Shift 9 &mdash; hold E on the music box to rewind it before the melody finishes three times. See <a href="/monsters/marionette/">the Marionette</a>.</p>
  <p><strong>Mods.</strong> No official Workshop or tools; a working BepInEx community scene exists, including a player-count mod. See <a href="/mods/">mods</a>.</p>

  <h3>N</h3>
  <p><strong>N.E.T. database.</strong> The system you cross-check a customer's ID against &mdash; the mechanical core of every shift. See <a href="/guide/doppelgangers/">the doppelganger guide</a>.</p>
  <p><strong>Norbert.</strong> Not actually lethal &mdash; sparing him ends it cleanly, killing him triggers repeated non-lethal pranks. See <a href="/monsters/norbert/">Norbert</a>.</p>

  <h3>P</h3>
  <p><strong>Patience meter.</strong> The ID-check time-pressure mechanic the 29 July 2026 patch removed entirely. See <a href="/guide/doppelgangers/">the doppelganger guide</a>.</p>
  <p><strong>Post-Story.</strong> The state after finishing all 13 Story shifts &mdash; unlocks Endless Mode and the <a href="/monsters/rake/">Rake</a>. See <a href="/nights-and-levels/">nights &amp; Endless Mode</a>.</p>
  <p><strong>Proximity chat.</strong> Distance-based voice &mdash; a mechanic, not just convenience, since the Entity tracks it. See <a href="/multiplayer/">multiplayer</a>.</p>

  <h3>Q</h3>
  <p><strong>Quota.</strong> The sales target each shift is measured against. See <a href="/guide/beginners/">the beginner's guide</a>.</p>

  <h3>R</h3>
  <p><strong>Rake.</strong> A fast, forest-spawning threat added 29 July 2026, exclusive to Post-Story Endless Mode. See <a href="/monsters/rake/">the Rake</a>.</p>

  <h3>S</h3>
  <p><strong>Sheriff Clyde.</strong> The only way to end an encounter with the Dentist, and one of the two variables deciding your ending. See <a href="/monsters/the-dentist/">the Dentist</a> and <a href="/endings/">endings</a>.</p>
  <p><strong>Shrieking Doll.</strong> The most fragile threat and easiest monster achievement (89.8% Silenced). See <a href="/monsters/shrieking-doll/">Shrieking Doll</a>.</p>
  <p><strong>Steam Deck.</strong> Rated <strong>Playable</strong>, not Verified. See <a href="/system-requirements/">system requirements</a>.</p>
  <p><strong>Steam Input.</strong> Valve's controller-translation layer; the game's own support flag is declared false. See <a href="/controls/">controls</a>.</p>

  <h3>T</h3>
  <p><strong>Trap.</strong> A placeable countermeasure that, with weapons and barricades, helps end a Hunt. See <a href="/guide/survival/">the survival guide</a>.</p>

  <h3>W</h3>
  <p><strong>Weapons arsenal.</strong> The purchasable loadout tied to the Locked And Loaded achievement (23.5% unlock). See <a href="/guide/survival/">the survival guide</a>.</p>

  <h3>X</h3>
  <p><strong>Xbox Play Anywhere.</strong> Links one purchase across Xbox and Windows &mdash; shares saves, not input method. See <a href="/platforms/">platforms</a>.</p>

  <h2>Quick answers</h2>
  <div class="faq">
    <details>
      <summary>Is this list complete?</summary>
      <div class="a"><p>It covers every term this wiki uses across its own pages as of 11 September 2026. If the game adds new mechanics, they will get their own page first and a glossary entry after.</p></div>
    </details>
    <details>
      <summary>Where do I go for the full explanation of a term?</summary>
      <div class="a"><p>Every entry links to the page that covers it properly &mdash; this list is a lookup, not a replacement for those pages.</p></div>
    </details>
    <details>
      <summary>Why isn't every letter of the alphabet represented?</summary>
      <div class="a"><p>Because this is a list of terms this wiki actually uses, not a filled template &mdash; some letters (F, O, U, V, Y, Z) simply have no matching term on the site yet.</p></div>
    </details>
  </div>

  <div class="grid two">
    <a class="card" href="/start-here/"><b>Start here</b><span>A suggested reading order through the whole wiki, beginner to advanced.</span></a>
    <a class="card" href="/monsters/compare/"><b>Compare all threats</b><span>Every monster's trigger, kill method and achievement rate in one table.</span></a>
    <a class="card" href="/faq/"><b>FAQ</b><span>Direct question-and-answer format instead of a term list.</span></a>
    <a class="card" href="/monsters/"><b>Full bestiary</b><span>Every named threat with its own page.</span></a>
  </div>
""",
},
{
 "path": "monsters/compare",
 "active": "/guides/",
 "title": "Shift At Midnight Monsters Compared: Which Ones Can You Kill?",
 "og_short": "All monsters compared",
 "desc": "All seven Shift At Midnight threats compared in one table — when each appears, whether it can be killed, the counter that works, and its achievement unlock rate.",
 "trail": M + [(None, "Compare all threats")],
 "h1": "Every Shift At Midnight threat, compared",
 "lede": "Seven named threats appear across this wiki's bestiary, each with its own page and its own counter. Read individually, it is easy to lose track of which ones you can actually shoot, which one you can only outsmart, and which one is off-limits until you finish Story Mode. This page puts all seven side by side, with figures pulled straight from <a href=\"/achievements/\">the achievements page</a> and each monster's own page &mdash; nothing recalculated, nothing new claimed.",
 "updated": "Last verified 11 September 2026 &middot; game version: 29 July 2026 patch",
 "body": """
  <div class="tags">
    <span class="tag">7 threats compared</span>
    <span class="tag amber">Figures from on-site pages only</span>
    <span class="tag red">The Dentist: cannot be killed</span>
  </div>

  <h2>The comparison table</h2>
  <p>"Achievement" unlock rates are the global percentage from <a href="/achievements/">the achievements page</a> as of this check, not each monster page's own copy &mdash; a couple of monster pages carry a slightly older snapshot of the same figure, so this table uses the single freshest source rather than mixing two.</p>

  <table class="facts">
    <tr><th>Marionette</th><td>From Shift 9, Story Mode. <strong>Killable</strong> &mdash; hold E on the music box to rewind it before the melody finishes three times. Achievement: Last Performance, 41.6%. Details: <a href="/monsters/marionette/">Marionette page</a>.</td></tr>
    <tr><th>Entity</th><td>End of any shift where a doppelganger's purchase completed, or any Blood Moon shift. <strong>Killable</strong> &mdash; weapons, traps and barricades all contribute; it is blind and tracks sound. Achievement: Still Breathing (survive), 93.8%. Details: <a href="/monsters/entity/">Entity page</a>.</td></tr>
    <tr><th>Demented</th><td>Appears during regular shifts. <strong>Not killable by gunfire</strong> &mdash; freezes only while you look directly at it; the confirmed counter is breaking your gaze and leading it into a trap. Achievement: Freed, 79.8%. Details: <a href="/monsters/demented/">Demented page</a>.</td></tr>
    <tr><th>Shrieking Doll</th><td>Appears during regular shifts. <strong>Killable</strong> &mdash; the most fragile threat in the game, a few shots. Achievement: Silenced, 89.8%, the easiest monster achievement. Details: <a href="/monsters/shrieking-doll/">Shrieking Doll page</a>.</td></tr>
    <tr><th>The Dentist</th><td>Shift 13 only, the final story shift. <strong>Cannot be killed</strong> &mdash; firearms and melee are confirmed ineffective; only Sheriff Clyde ends the encounter, in a cutscene. No achievement of its own. Details: <a href="/monsters/the-dentist/">Dentist page</a>.</td></tr>
    <tr><th>Norbert</th><td>A doppelganger-category customer, not a hostile monster. <strong>Not lethal</strong> either way &mdash; sparing him ends it cleanly; killing him triggers repeated non-lethal pranks for the rest of the shift. No dedicated achievement. Details: <a href="/monsters/norbert/">Norbert page</a>.</td></tr>
    <tr><th>Rake</th><td>Post-Story Endless Mode only, added 29 July 2026. <strong>Killable</strong> &mdash; the developer's own instruction is to shoot it before it reaches the playable area. No dedicated achievement (predates its addition). Details: <a href="/monsters/rake/">Rake page</a>.</td></tr>
  </table>

  <p class="src">Jack-in-the-Box is deliberately left out of the table above: this wiki's <a href="/monsters/jack-in-the-box/">own page</a> treats it as an item that summons the Marionette, not a threat with its own kill method or achievement.</p>

  <h2>What actually matters: three groups, not seven</h2>
  <p>Seven entries in a bestiary read like seven different fights to learn. In practice they split into three groups, and which group a threat falls into decides how you should be spending your attention.</p>

  <h3>Group 1 &mdash; shoot it: Entity, Marionette, Shrieking Doll, Rake</h3>
  <p>Four of the seven have a direct, confirmed kill method involving weapons or a specific interaction under time pressure. These are the ones where the <a href="/guide/survival/">survival guide's</a> advice about weapons actually applies &mdash; buy the arsenal, know your ammo, and treat the Marionette's music-box timer and the Rake's shoot-before-it-arrives instruction as the two cases where a delay is punished more than usual.</p>

  <h3>Group 2 &mdash; outsmart it: Demented</h3>
  <p>The Demented is the one exception to "shoot the problem." Gunfire does not work on it; the confirmed solution is behavioural &mdash; break your gaze, lead it somewhere with a trap already set. Treating it like Group 1 and trying to shoot your way out is the single most common mismatch between what a player expects from a horror-game monster and what this specific one requires.</p>

  <h3>Group 3 &mdash; there is no fight: The Dentist, Norbert</h3>
  <p>These two do not resolve through combat at all, for opposite reasons. The Dentist is confirmed immune to everything except a scripted Sheriff Clyde intervention, so any strategy built around damaging it is wasted effort on the final shift. Norbert is not a combat encounter in the first place &mdash; the choice is social (spare or kill), and killing him is confirmed to make your remaining shift <em>harder</em>, not easier, through repeated harassment. Both are covered in more decision-focused detail on <a href="/monsters/norbert/">Norbert's own page</a> and the <a href="/endings/">endings page</a>, since the Dentist's outcome is one of the two variables that decides your ending.</p>

  <h2>Story Mode vs. Post-Story Endless</h2>
  <p>Only one threat on this list is gated by mode rather than by shift number: the <a href="/monsters/rake/">Rake</a> exists exclusively in Post-Story Endless Mode, which itself only unlocks after finishing all 13 Story shifts. A player who has never touched Endless will never encounter one, no matter how their Story run went. Every other threat on this table can appear within the 13-shift Story campaign; the <a href="/nights-and-levels/">nights &amp; Endless Mode page</a> covers exactly which shifts guarantee which encounters, including Blood Moon shifts that force an Entity Hunt regardless of your counter performance.</p>

  <h2>Which one should worry you most, by playstyle</h2>
  <p>If you play solo, the Entity is the one to prepare for first &mdash; it is both the most frequent (any missed doppelganger triggers it) and the one the <a href="/guide/survival/">survival guide</a> spends the most space on, since sound and barricades matter more than weapons alone. If you play co-op, the Demented is worth flagging to your team specifically, because a squadmate who has not read this comparison will likely default to shooting it, and that default does not work. If you are Post-Story and running Endless for the achievement grind, the Rake is the newest variable and the one with the thinnest official documentation &mdash; see its own page for exactly what is confirmed versus reported.</p>

  <h2>Quick answers</h2>
  <div class="faq">
    <details>
      <summary>Which monster is impossible to kill?</summary>
      <div class="a"><p>The Dentist. Firearms and melee are confirmed ineffective against it; the only resolution is Sheriff Clyde's intervention in a scripted cutscene. See the <a href="/monsters/the-dentist/">Dentist page</a>.</p></div>
    </details>
    <details>
      <summary>Which monster has the lowest achievement unlock rate?</summary>
      <div class="a"><p>Of the ones with a dedicated achievement, Last Performance (kill a Marionette) is lowest at 41.6%, per <a href="/achievements/">the achievements page</a>. The Dentist and Rake have no dedicated achievement to compare.</p></div>
    </details>
    <details>
      <summary>Is the Rake harder than the other monsters?</summary>
      <div class="a"><p>Unverified &mdash; there is no achievement-rate figure for it to compare against the others, and most of its reported behaviour beyond the developer's own one-sentence description is secondary and unconfirmed. See the <a href="/monsters/rake/">Rake page</a> for exactly what is and isn't sourced.</p></div>
    </details>
  </div>

  <div class="grid two">
    <a class="card danger" href="/monsters/"><b>Full bestiary</b><span>Every threat's own page, in more depth than this comparison.</span></a>
    <a class="card" href="/guide/survival/"><b>Survival guide</b><span>Sound, barricades and weapons — the mechanics behind Group 1's kill methods.</span></a>
    <a class="card" href="/endings/"><b>Endings</b><span>How the Dentist's outcome factors into which of the three endings you get.</span></a>
    <a class="card" href="/glossary/"><b>Glossary</b><span>Every term on this page, defined in one place.</span></a>
  </div>
""",
},
{
 "path": "start-here",
 "active": "/guides/",
 "title": "Where to Start: A Shift At Midnight Reading Order",
 "og_short": "Where to start on this wiki",
 "desc": "New to Shift At Midnight? A suggested reading order through this wiki's guides, monster pages and mechanics pages, from first shift to Endless Mode.",
 "trail": [(None, "Start here")],
 "h1": "Where to start on this wiki",
 "lede": "This wiki has grown to more than 35 pages, and none of them tell you in what order to read them. If you just bought the game, or you are stuck on your first Hunt, this page is a suggested path through the site &mdash; beginner first, advanced last &mdash; with one line on why each step matters before you click through.",
 "updated": "Last verified 11 September 2026 &middot; game version: 29 July 2026 patch",
 "body": """
  <div class="tags">
    <span class="tag">8-step reading order</span>
    <span class="tag">Beginner to advanced</span>
  </div>

  <h2>Before you launch the game</h2>
  <ol>
    <li><strong><a href="/release-date/">Release date &amp; the basics</a>.</strong> Confirms you are looking at the current game, not an outdated May listing left over from before its two delays &mdash; a five-minute read that prevents every other page from confusing you with dates that no longer apply.</li>
    <li><strong><a href="/platforms/">Platforms</a>.</strong> Steam, Xbox, and Game Pass from day one &mdash; worth confirming before you buy on the wrong storefront, especially if you are trying to play with a specific friend (see step 6).</li>
    <li><strong><a href="/system-requirements/">System requirements</a>.</strong> A GTX 1050 Ti minimum and a Steam Deck rating of Playable, not Verified &mdash; check this before install, not after a crash sends you to <a href="/troubleshooting/">troubleshooting</a> later.</li>
  </ol>

  <h2>Your first shift</h2>
  <ol start="4">
    <li><strong><a href="/guide/beginners/">Beginner's guide</a>.</strong> The single most important reframe on this wiki: this is a job simulator with a horror game hiding inside it, and most failed first runs come from playing it the other way round. Read this before your first shift, not after a bad one.</li>
    <li><strong><a href="/guide/doppelgangers/">Doppelganger guide</a>.</strong> The actual job &mdash; reading an ID, cross-checking the N.E.T. database, and deciding whether the person in front of you is real. This is where the patience-meter removal (29 July patch) matters most, and where the <a href="/glossary/">glossary</a> earns its keep if a term here is unfamiliar.</li>
  </ol>

  <h2>When something goes wrong</h2>
  <ol start="6">
    <li><strong><a href="/guide/survival/">Survival guide</a>.</strong> What to do once a Hunt has started &mdash; sound and doors first, weapons fourth despite being what most players reach for first. Read this before you need it, because a Hunt does not pause for you to alt-tab to a guide.</li>
    <li><strong><a href="/monsters/compare/">Compare all threats</a>, then the individual monster pages.</strong> Once survival mechanics make sense generally, the comparison page sorts all seven threats into three response types &mdash; shoot it, outsmart it, or accept there is no fight &mdash; before you go deep on any single monster's own page.</li>
  </ol>

  <h2>Playing with other people</h2>
  <p>If you are playing solo, skip to the next section. If not: <a href="/multiplayer/">multiplayer &amp; co-op</a> covers lobby size (three by design, six since the 23 July patch) and why proximity chat is a mechanic, not just convenience, given the Entity tracks sound. If your group spans storefronts, read <a href="/crossplay/">crossplay</a> before anyone buys anything &mdash; Xbox and PC Game Pass share a pool, Steam does not, and that is not something a refund fixes after the fact.</p>

  <h2>Going deeper</h2>
  <ol start="8">
    <li><strong><a href="/achievements/">Achievements</a> and <a href="/endings/">endings</a>.</strong> Once the core loop is comfortable, these two pages cover the completion curve (96.9% down to 10.1%) and the two variables &mdash; the Sheriff Clyde call and your Shift 13 savings &mdash; that decide which of the three endings you get.</li>
  </ol>
  <p>If you would rather work from a checklist than a reading order, the <a href="/tools/completion-tracker/">100% completion tracker</a> puts every achievement, ending, named threat and fixed story beat on this wiki into 46 tick boxes that save in your browser.</p>
  <p>After that, <a href="/nights-and-levels/">nights &amp; Endless Mode</a> explains what changes once Story Mode's 13 shifts are behind you, including the Post-Story-only <a href="/monsters/rake/">Rake</a>. If you are chasing every corner of the game rather than just finishing it, <a href="/mods/">mods</a> and <a href="/updates/">updates</a> round things out; if something breaks along the way, <a href="/troubleshooting/">troubleshooting</a> separates the fixes that are confirmed from the reports this wiki could not verify.</p>

  <h2>What this order deliberately skips</h2>
  <p>A few pages are useful but not part of the critical path, so they are left off the numbered list above rather than forced in: <a href="/credits/">credits</a> (who made it), <a href="/languages/">languages</a>, <a href="/controls/">controls</a>, <a href="/cheats/">cheats</a>, <a href="/employee-package/">Employee Package</a>, <a href="/demo/">the free demo</a>, <a href="/review/">the review page</a>, and <a href="/similar-games/">similar games</a> are all reference material you reach for when a specific question comes up, not steps you need before your next shift.</p>

  <h2>Quick answers</h2>
  <div class="faq">
    <details>
      <summary>I just want to survive my first Hunt. What's the minimum I should read?</summary>
      <div class="a"><p>Steps 4, 5 and 6 above &mdash; the <a href="/guide/beginners/">beginner's guide</a>, the <a href="/guide/doppelgangers/">doppelganger guide</a>, and the <a href="/guide/survival/">survival guide</a>. That covers the job, the mistake that triggers a Hunt, and what to do once one starts.</p></div>
    </details>
    <details>
      <summary>Do I need to read the monster pages before playing?</summary>
      <div class="a"><p>No. The <a href="/monsters/compare/">comparison page</a> is enough going in; the individual monster pages are more useful after you have actually met each one and want the specific counter confirmed.</p></div>
    </details>
    <details>
      <summary>I'm playing with friends on different platforms. Where do I start?</summary>
      <div class="a"><p>Read <a href="/crossplay/">crossplay</a> before anyone buys the game. Steam and Xbox/PC Game Pass players are in separate pools, and that decides which storefront your group should buy on.</p></div>
    </details>
    <details>
      <summary>What changed most recently that this order should account for?</summary>
      <div class="a"><p>The <a href="/updates/">updates page</a> tracks this: as of its last check, the 29 July 2026 patch was still the newest documented change, and it is the one referenced throughout this order, since it removed the patience meter and added the Rake. We have not been able to confirm the contents of anything newer.</p></div>
    </details>
    <details>
      <summary>Where do I look up a term I don't recognize?</summary>
      <div class="a"><p>The <a href="/glossary/">glossary</a> &mdash; every term used across this reading order is defined there in one place, each linked back to its full page.</p></div>
    </details>
  </div>

  <div class="grid two">
    <a class="card" href="/guide/beginners/"><b>Step 1: Beginner's guide</b><span>The single most important reframe before your first shift.</span></a>
    <a class="card" href="/glossary/"><b>Glossary</b><span>Every term in this reading order, defined and linked.</span></a>
    <a class="card" href="/monsters/compare/"><b>Compare all threats</b><span>All seven monsters sorted into three response types.</span></a>
    <a class="card" href="/faq/"><b>FAQ</b><span>Specific questions, answered directly, if you'd rather not read in order.</span></a>
  </div>
""",
},
]

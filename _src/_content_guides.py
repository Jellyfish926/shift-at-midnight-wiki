#!/usr/bin/env python3
"""攻略页 + Trends 查询词页正文。覆盖 Trends 全部 17 个相关查询。"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _build import build

G = [("/guides/", "Guides")]

FAQ_LD = """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Is Shift At Midnight crossplay?",
      "acceptedAnswer": { "@type": "Answer", "text": "Partially. Xbox console and PC Game Pass players share one pool through Xbox Play Anywhere. The Steam version connects only to other Steam players." } },
    { "@type": "Question", "name": "Is Shift At Midnight on Game Pass?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes, day one on both Xbox console and PC Game Pass. It is also an Xbox Play Anywhere title." } },
    { "@type": "Question", "name": "How many players can play Shift At Midnight?",
      "acceptedAnswer": { "@type": "Answer", "text": "Up to three players in online co-op with proximity chat. A full single-player mode is also available." } },
    { "@type": "Question", "name": "How much does Shift At Midnight cost?",
      "acceptedAnswer": { "@type": "Answer", "text": "9.99 USD at launch with a 10% introductory discount. It is also included with Xbox Game Pass." } },
    { "@type": "Question", "name": "Does Shift At Midnight have mods?",
      "acceptedAnswer": { "@type": "Answer", "text": "No official mod support or Steam Workshop integration has been announced as of 28 July 2026." } },
    { "@type": "Question", "name": "How many achievements does Shift At Midnight have?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ten. Three of them are hidden: Grave Decision, True Ending and Empty Home." } },
    { "@type": "Question", "name": "Is Shift At Midnight on PS5?",
      "acceptedAnswer": { "@type": "Answer", "text": "No. There is no PlayStation 5 or PS4 version of Shift At Midnight and none has been announced. It is available on PC via Steam and the Microsoft Store, and on Xbox Series X|S." } },
    { "@type": "Question", "name": "Is Shift At Midnight available on mobile or the App Store?",
      "acceptedAnswer": { "@type": "Answer", "text": "No. There is no iOS or Android version of Shift At Midnight. It is a PC and Xbox title only." } },
    { "@type": "Question", "name": "When did Shift At Midnight come out?",
      "acceptedAnswer": { "@type": "Answer", "text": "Shift At Midnight released on 22 July 2026, after being delayed twice from its original 28 May 2026 date." } },
    { "@type": "Question", "name": "Is Shift At Midnight free?",
      "acceptedAnswer": { "@type": "Answer", "text": "The game costs 9.99 USD to buy, but it is included at no extra cost with Xbox Game Pass on both console and PC." } },
    { "@type": "Question", "name": "Who developed Shift At Midnight?",
      "acceptedAnswer": { "@type": "Answer", "text": "It was built by solo developer Bun Muen and published by Kwalee. It released on 22 July 2026." } }
  ]
}
</script>"""

PAGES = [
{
 "path": "guides", "active": "/guides/",
 "title": "All Shift At Midnight Guides — Complete Wiki Index",
 "og_short": "All Shift At Midnight Guides",
 "desc": "Every Shift At Midnight guide in one index: beginners, doppelganger identification, survival, co-op roles, weapons, quotas, story mode and the Q4 2026 roadmap.",
 "trail": [(None, "Guides")],
 "h1": "All Shift At Midnight guides",
 "lede": "Everything on this wiki, organised by what you are actually trying to do. If you have just installed the game, start with the beginner's guide. If something specific killed you, go straight to the <a href=\"/monsters/\">bestiary</a>.",
 "body": """
  <h2>Start here</h2>
  <div class="grid two">
    <a class="card" href="/guide/beginners/"><b>Beginner's guide</b><span>Your first three shifts, and the three things nobody tells you.</span></a>
    <a class="card" href="/guide/doppelgangers/"><b>Spotting doppelgangers</b><span>What the ID scanner does and does not tell you.</span></a>
  </div>

  <h2>Surviving the night</h2>
  <div class="grid two">
    <a class="card" href="/guide/survival/"><b>Traps, barricades &amp; hiding</b><span>When identification has already failed.</span></a>
    <a class="card" href="/guide/weapons/"><b>Weapons arsenal</b><span>Completing it is a 20.6% achievement.</span></a>
    <a class="card danger" href="/monsters/"><b>Bestiary</b><span>Every named threat &mdash; and the one you cannot fight.</span></a>
    <a class="card" href="/achievements/"><b>All 10 achievements</b><span>Full list with global unlock rates.</span></a>
  </div>

  <h2>Running the store</h2>
  <div class="grid two">
    <a class="card" href="/guide/store-management/"><b>Quotas &amp; restocking</b><span>The job you still have to do while being hunted.</span></a>
    <a class="card" href="/guide/co-op/"><b>Co-op &amp; proximity chat</b><span>How three players should split roles.</span></a>
  </div>

  <h2>Modes &amp; content</h2>
  <div class="grid two">
    <a class="card" href="/guide/story-mode/"><b>Story Mode</b><span>The shift structure and where the endings sit.</span></a>
    <a class="card" href="/guide/endless-mode/"><b>Endless Mode &amp; roadmap</b><span>The free Q4 2026 update.</span></a>
    <a class="card" href="/endings/"><b>All endings</b><span>What the three hidden achievements imply.</span></a>
    <a class="card" href="/release-date/"><b>Release date</b><span>Out now &mdash; 22 July 2026, after two delays.</span></a>
  </div>

  <h2>Platform &amp; availability</h2>

  <div class="grid two">
    <a class="card" href="/platforms/"><b>All platforms</b><span>PS5, mobile, App Store, Switch &mdash; the honest answers.</span></a>
    <a class="card" href="/demo/"><b>The demo</b><span>What it contained, and whether it still matters.</span></a>
    <a class="card" href="/nights-and-levels/"><b>Nights &amp; levels</b><span>Is night three the last one? No.</span></a>
    <a class="card" href="/employee-package/"><b>Employee Package</b><span>The merch bundle, and why you cannot buy it.</span></a>
  </div>

  <h2>Before you buy</h2>
  <div class="grid two">
    <a class="card" href="/crossplay/"><b>Crossplay</b><span>Steam players cannot play with Game Pass players. Read this first.</span></a>
    <a class="card" href="/multiplayer/"><b>Multiplayer</b><span>Player count, hosting, getting a session going.</span></a>
    <a class="card" href="/price/"><b>Price</b><span>What it costs and whether Game Pass makes that moot.</span></a>
    <a class="card" href="/review/"><b>Is it worth it?</b><span>What the reception and the achievement data suggest.</span></a>
    <a class="card" href="/similar-games/"><b>Games like it</b><span>Where to go next, split by what you actually liked.</span></a>
  </div>
"""},
{
 "path": "guide/beginners", "active": "/guides/",
 "title": "Shift At Midnight Beginner's Guide — Surviving Your First Shifts",
 "og_short": "Shift At Midnight Beginner's Guide",
 "desc": "A beginner's guide to Shift At Midnight that starts with the mistake 96.6% of players make: treating the ID scanner as a threat detector.",
 "trail": G + [(None, "Beginner's guide")],
 "h1": "Beginner's guide",
 "lede": "The fastest way to understand this game is to understand one number: <strong>96.6% of all players have killed a customer</strong>. That is the most common achievement in the game. It is not a badge of skill &mdash; it is the game documenting a mistake almost everyone makes.",
 "body": """
  <h2>The three things nobody tells you</h2>

  <h3>1. The ID scanner reports on documents, not on danger</h3>
  <p>Your ID verification computer tells you whether a document is authentic. That is its entire function. It does not tell you whether the holder intends to hurt you, and treating it as a threat detector is the single most expensive misunderstanding available.</p>
  <p>The game proves this to you twice, from opposite directions. <a href="/monsters/norbert/">Norbert</a> arrives on Night 2 with a fake ID and is completely harmless. <a href="/monsters/the-dentist/">The Dentist</a> is eight feet tall, lethal, and does not appear on the computer at all.</p>

  <h3>2. Not everything can be fought</h3>
  <p>Reaching for a weapon is a reflex the game builds and then punishes. There is an entity in this game against which <strong>no weapon, trap or barricade is effective</strong>. Against the Dentist, running is not the cowardly option &mdash; it is the only option that exists.</p>

  <h3>3. The store keeps running</h3>
  <p>Horror is not a pause button here. You still have a quota, shelves still empty, and customers still arrive while something is loose in the building. Players who treat every scare as a reason to abandon the counter fail the shift on numbers rather than on death.</p>

  <div class="term tip">
    <div class="term-h">Your first three shifts</div>
    <ol>
      <li><strong>Night 1 &mdash; learn the counter.</strong> Serve people, scan IDs, watch what a normal interaction looks like. You cannot spot an anomaly until you know the baseline.</li>
      <li><strong>Night 2 &mdash; meet Norbert.</strong> He will scan as fake. Do not kill him. This is the lesson.</li>
      <li><strong>Night 3 &mdash; buy a weapon.</strong> Have it equipped <em>before</em> a hunt starts, not during one.</li>
    </ol>
  </div>

  <h2>What the achievement curve tells you to expect</h2>
  <p>The first four achievements are held by 75&ndash;97% of players, and they arrive on their own if you keep playing: killing a customer, surviving a hunt, killing a <a href="/monsters/shrieking-doll/">Shrieking Doll</a>, killing a <a href="/monsters/demented/">Demented</a>. Do not chase them.</p>
  <p>The cliff is at <em>Relentless</em> (40.1%) and <a href="/monsters/marionette/">Last Performance</a> (35.1%). Those need you to know something in advance. Everything below them needs deliberate effort. See <a href="/achievements/">the full list</a>.</p>

  <h2>Money</h2>
  <p>You will want to spend everything on restocking, because the quota is immediate and the arsenal is not. Resist a little. <em>Locked And Loaded</em> &mdash; purchasing every melee weapon &mdash; sits at 20.6%, and the reason it is that low is that people spend their earnings shift-to-shift and never bank. See the <a href="/guide/weapons/">weapons guide</a>.</p>

  <h2>If you are playing with friends</h2>
  <p>Check <a href="/crossplay/">the crossplay page before anyone buys</a>. Steam players cannot play with Game Pass players. This catches groups out constantly.</p>

  <div class="grid two">
    <a class="card" href="/guide/doppelgangers/"><b>Doppelganger identification</b><span>The actual tells, once you know the scanner is not one.</span></a>
    <a class="card danger" href="/monsters/"><b>Bestiary</b><span>Know what is coming before it arrives.</span></a>
  </div>
"""},
{
 "path": "guide/doppelgangers", "active": "/guides/",
 "title": "Shift At Midnight Doppelgangers — How to Identify Them",
 "og_short": "Shift At Midnight Doppelgangers",
 "desc": "Doppelgangers mimic appearance, voice, mannerisms and backstory. The ID scanner only verifies documents — here is what identification actually rests on.",
 "trail": G + [(None, "Doppelgangers")],
 "h1": "Identifying doppelgangers",
 "lede": "Doppelgangers are the most common enemy in the game and the only one you handle with <strong>judgement rather than combat</strong>. They copy a human's look, voice, mannerisms and background well enough to walk in and ask for cigarettes.",
 "body": """
  <div class="term warn">
    <div class="term-h">The core problem</div>
    <p>Your ID verification computer answers exactly one question: <em>is this document authentic?</em> It does not answer <em>is this person human?</em> and it does not answer <em>is this person going to hurt me?</em> Everything difficult about this game lives in that gap.</p>
  </div>

  <h2>The two counterexamples that define the rule</h2>
  <p>Before building any identification habit, internalise these two:</p>
  <ul>
    <li><a href="/monsters/norbert/"><strong>Norbert</strong></a> &mdash; fake ID, openly not what he claims, <strong>harmless</strong>. Arrives Night 2.</li>
    <li><a href="/monsters/the-dentist/"><strong>The Dentist</strong></a> &mdash; <strong>does not register on the computer at all</strong>, and is lethal.</li>
  </ul>
  <p>Any rule of the form "scanner says X, therefore do Y" is broken by one of these. The scanner is one input among several, and it is not the decisive one.</p>

  <h2>What identification actually rests on</h2>
  <p>Doppelgangers mimic four things: <strong>appearance, voice, mannerisms and background</strong>. Mimicry is imitation, and imitation has seams. The practical skill is knowing the baseline well enough to notice when something is off &mdash; which is why Night 1 is best spent simply watching normal customers behave normally.</p>
  <p>Behaviour is generally more informative than paperwork. Norbert stepping around the counter is a behavioural anomaly the game shows you deliberately. A customer whose stated background does not match how they act is giving you more signal than a document ever will.</p>

  <div class="term tip">
    <div class="term-h">Cross-reference, do not single-source</div>
    <p>The reliable method is layering: what the document says, what the person says, and how the person behaves. One anomaly is noise. Two that point the same direction is a decision. Acting on a single flag &mdash; in either direction &mdash; is how you end up in the 96.6% who have killed a customer.</p>
  </div>

  <h2>The cost of being wrong</h2>
  <p>Being wrong toward mercy lets something through your door. Being wrong toward suspicion kills a paying customer &mdash; the game tracks this with its own achievement, and the three rare hidden achievements (<em>Grave Decision</em> 26.0%, <em>True Ending</em> 13.4%, <em>Empty Home</em> 7.0%) may well relate to how you handled these calls. That last point is <a href="/endings/">inference, and we label it as such</a>.</p>

  <h2>In co-op</h2>
  <p>Three players can genuinely split this. One works the counter and the scanner, one watches the floor for behavioural anomalies, one keeps the store running. With <a href="/guide/co-op/">proximity chat</a> the floor watcher can flag something quietly without the person at the counter breaking eye contact. Three people all crowding the same customer sees less, not more.</p>

  <div class="grid two">
    <a class="card" href="/guide/beginners/"><b>Beginner's guide</b><span>The three things nobody tells you.</span></a>
    <a class="card danger" href="/monsters/"><b>Bestiary</b><span>The threats that are not doppelgangers.</span></a>
  </div>
"""},
{
 "path": "guide/survival", "active": "/guides/",
 "title": "Shift At Midnight Survival Guide — Traps, Barricades &amp; Hiding",
 "og_short": "Shift At Midnight Survival Guide",
 "desc": "When identification has failed and something is loose in the store: barricading, trap placement, hiding, and the one entity none of it works against.",
 "trail": G + [(None, "Survival")],
 "h1": "Traps, barricades &amp; hiding",
 "lede": "This is the toolkit for after the counter has failed. Something is loose in the building, the shift is still running, and you need the store to survive until dawn.",
 "body": """
  <div class="term warn">
    <div class="term-h">The exception, stated first</div>
    <p>None of this works on <a href="/monsters/the-dentist/">the Dentist</a>. No weapon, trap or barricade is effective against him. If that is what is in your store, stop reading and run.</p>
  </div>

  <h2>Barricading</h2>
  <p>Barricades buy time and shape movement. A gas station is a small building with a limited number of ways through it, which means blocking the right door does not just delay a threat &mdash; it forces it onto a path you chose.</p>
  <p>The mistake is barricading reactively, sealing yourself into a room with one exit. A barricade that removes your own escape route has converted a chase into a corner. Block to <em>redirect</em>, not to hide behind.</p>

  <h2>Traps</h2>
  <p>Traps are placement, and placement is prediction. They pay off where a threat has to go rather than where it happens to be, which means the value comes from knowing the store's chokepoints before the night gets bad. Laying traps while being chased is close to useless.</p>

  <h2>Hiding</h2>
  <p>Hiding is a reset, not a solution. It breaks contact so you can get back to a shift that is still running &mdash; the quota does not pause because you are under a counter. Use it to buy the seconds you need to move somewhere useful.</p>

  <div class="term tip">
    <div class="term-h">Learn the layout on a quiet night</div>
    <p>Every skill on this page depends on knowing the building &mdash; which aisles connect, where the loops are, which corners are dead ends. Spend an early, calm shift walking the store deliberately. Map knowledge is the one asset that works against everything, including the entity you cannot fight.</p>
  </div>

  <h2>Escalation nights</h2>
  <p>Some shifts escalate into sustained assault rather than individual customers at the counter, and the balance moves from interrogation to survival. We are still verifying the exact trigger conditions, so we are not publishing a mechanism we cannot confirm. What is clear from play is that these are the nights this page's toolkit exists for.</p>

  <h2>Weapons are a separate question</h2>
  <p>Killing things and surviving things are different problems. See the <a href="/guide/weapons/">weapons arsenal</a> &mdash; and note that buying every melee weapon is its own achievement at 20.6%.</p>

  <div class="grid two">
    <a class="card" href="/guide/weapons/"><b>Weapons arsenal</b><span>What to have equipped before the hunt starts.</span></a>
    <a class="card" href="/guide/co-op/"><b>Co-op roles</b><span>Three players, three jobs.</span></a>
  </div>
"""},
{
 "path": "guide/co-op", "active": "/guides/",
 "title": "Shift At Midnight Co-op Guide — 3 Players &amp; Proximity Chat",
 "og_short": "Shift At Midnight Co-op Guide",
 "desc": "How three players should split roles in Shift At Midnight, why proximity chat is a mechanic rather than a feature, and why running Discord over the top hurts you.",
 "trail": G + [(None, "Co-op")],
 "h1": "Co-op &amp; proximity chat",
 "lede": "Up to <strong>three players</strong>, online, with <strong>proximity chat</strong>. That second detail is not a convenience feature &mdash; it is a mechanic, and treating it as one is the difference between a co-ordinated crew and three people panicking in separate aisles.",
 "body": """
  <div class="term warn">
    <div class="term-h">Check this before anyone buys</div>
    <p>Steam players <strong>cannot</strong> play with Xbox or PC Game Pass players. Xbox console and PC Game Pass share one pool via Play Anywhere; Steam is isolated. See <a href="/crossplay/">crossplay</a> &mdash; this catches groups out constantly.</p>
  </div>

  <h2>Proximity chat is positional data</h2>
  <p>Voices get quieter with distance. That means every sound your teammates make is telling you where they are, and the game expects you to shout across the store. A scream that is suddenly loud is a teammate who is suddenly close, and that is information you get for free.</p>
  <p>This is why running Discord over the top hurts you. It flattens distance to zero, removes the cue the design depends on, and makes it much harder to tell where someone is when things go wrong. Use the in-game chat.</p>

  <h2>Three roles</h2>
  <ul>
    <li><strong>Counter.</strong> Works customers and the ID scanner. Does not leave for noises.</li>
    <li><strong>Floor.</strong> Watches behaviour, restocks, spots anomalies the scanner cannot see. The one who notices <a href="/monsters/norbert/">someone stepping around the counter</a>.</li>
    <li><strong>Response.</strong> Weapon equipped, handles hunts, owns time-critical objects.</li>
  </ul>
  <p>The failure mode is all three converging on whatever made the last noise. A <a href="/monsters/shrieking-doll/">Shrieking Doll</a> screams specifically to pull attention &mdash; three people answering that call is three people not doing their jobs.</p>

  <div class="term tip">
    <div class="term-h">The music box is a co-op problem</div>
    <p>On a <a href="/monsters/marionette/">Marionette</a> night, one player owns the <a href="/monsters/jack-in-the-box/">music box</a> for the whole encounter and calls the melody count aloud. Three people half-watching a box that has to be wound is how groups end up facing the Marionette with no counterplay &mdash; which is why only 35.1% have ever killed one.</p>
  </div>

  <h2>Solo is a real option</h2>
  <p>There is a full single-player mode, and several achievements &mdash; including the ending-related ones &mdash; do not require a group. Solo trades co-ordination for control: nobody else kills a customer you were still assessing.</p>

  <div class="grid two">
    <a class="card" href="/crossplay/"><b>Crossplay</b><span>Who can actually play with whom.</span></a>
    <a class="card" href="/multiplayer/"><b>Multiplayer setup</b><span>Player count and getting a session going.</span></a>
  </div>
"""},
{
 "path": "guide/weapons", "active": "/guides/",
 "title": "Shift At Midnight Weapons — Arsenal &amp; Locked And Loaded",
 "og_short": "Shift At Midnight Weapons Guide",
 "desc": "Buying every melee weapon unlocks Locked And Loaded, held by only 20.6% of players. Why it is low, how to bank for it, and what weapons cannot solve.",
 "trail": G + [(None, "Weapons")],
 "h1": "Weapons arsenal",
 "lede": "Purchasing every melee weapon and filling out the arsenal unlocks <strong>Locked And Loaded</strong> &mdash; held by only <strong>20.6%</strong> of players. It is not a difficulty problem. It is a budgeting problem.",
 "body": """
  <div class="tags">
    <span class="tag amber">Achievement: Locked And Loaded</span>
    <span class="tag">20.6% of players</span>
  </div>

  <h2>Why only one in five players has it</h2>
  <p>Money in this game has an immediate use and a deferred one. Restocking keeps your quota healthy tonight. Weapons pay off on a night that may not come. Under pressure, players spend on the immediate thing every time &mdash; and the arsenal never gets finished.</p>
  <p>The fix is to decide early that some fraction of every shift's earnings is untouchable and goes to the arsenal. Deciding to chase this at hour twenty means grinding shifts purely for money, which is much less fun than banking a little as you go.</p>

  <h2>Have it equipped before the hunt</h2>
  <p>The habit that separates comfortable players from scrambling ones: buy and equip before a hunt starts. <em>Relentless</em> &mdash; finish a hunt within 30 seconds, 40.1% &mdash; is close to impossible if the first ten seconds are spent shopping.</p>

  <div class="term tip">
    <div class="term-h">Best target for Relentless</div>
    <p>A <a href="/monsters/shrieking-doll/">Shrieking Doll</a>. It comes to you rather than hiding, so the clock is not spent searching. Do not attempt it on a <a href="/monsters/marionette/">Marionette</a> night, and never on a <a href="/monsters/the-dentist/">Dentist</a> night &mdash; that one cannot be killed at all.</p>
  </div>

  <h2>What weapons do not solve</h2>
  <ul>
    <li><strong>The Dentist.</strong> No weapon works. Running is the entire answer.</li>
    <li><strong>Doppelgangers.</strong> The problem is identification, not damage. A weapon applied to the wrong customer is the 96.6% achievement.</li>
    <li><strong>The Marionette.</strong> Decided by the <a href="/monsters/jack-in-the-box/">music box</a> before the fight. Arriving armed but unprepared does not help.</li>
  </ul>

  <h2>What we have not confirmed</h2>
  <p>We are not publishing a weapon tier list, damage values or per-monster recommendations, because we cannot verify them yet. Confident-sounding numbers for this game are circulating without sourcing. When we have data we can stand behind, it goes here with the date.</p>

  <div class="grid two">
    <a class="card" href="/achievements/"><b>All achievements</b><span>Where Locked And Loaded sits.</span></a>
    <a class="card" href="/guide/store-management/"><b>Quotas &amp; money</b><span>Where the budget comes from.</span></a>
  </div>
"""},
{
 "path": "guide/store-management", "active": "/guides/",
 "title": "Shift At Midnight Store Management — Quotas &amp; Restocking",
 "og_short": "Shift At Midnight Store Management",
 "desc": "The horror does not pause your quota. How to keep the gas station running — restocking, queue handling and budgeting — while something is loose in the building.",
 "trail": G + [(None, "Store management")],
 "h1": "Quotas &amp; restocking",
 "lede": "The part of Shift At Midnight that guides skip: <strong>you still have a job</strong>. Shelves empty, customers queue, and the quota does not care that something came through the door.",
 "body": """
  <h2>The quota is the real timer</h2>
  <p>Death is the dramatic failure. Missing quota is the common one. Every minute spent hiding, barricading or investigating is a minute not spent serving, and shifts are lost on numbers far more often than players expect.</p>
  <p>Practically this means threats have a budget. Breaking contact and getting back to the counter is usually correct; a fully cleared store with an unmet quota is a failed shift.</p>

  <h2>Restocking</h2>
  <p>Restocking is predictable work, which makes it the right thing to do during calm stretches &mdash; and the wrong thing to be doing when something is developing. Front-load it early in a shift while the store is quiet.</p>

  <div class="term tip">
    <div class="term-h">In co-op, restocking is the floor role's job</div>
    <p>It puts a player in the aisles with a reason to be looking around &mdash; which is exactly where behavioural anomalies get spotted. The <a href="/guide/co-op/">floor role</a> restocks and watches at the same time.</p>
  </div>

  <h2>Queue pressure is the design</h2>
  <p>A queue creates time pressure on the one decision the game cares about: is this person human? Rushing produces the 96.6% outcome &mdash; killing a customer &mdash; or the opposite error of waving through something you should have caught. The queue is not an obstacle to the horror; it is the mechanism that generates it.</p>

  <h2>Budgeting</h2>
  <p>Money splits between restocking (immediate, keeps quota healthy) and the <a href="/guide/weapons/">weapons arsenal</a> (deferred, and its own 20.6% achievement). Bank a fixed slice every shift rather than deciding to chase the arsenal later.</p>

  <div class="grid two">
    <a class="card" href="/guide/weapons/"><b>Weapons arsenal</b><span>The other half of the budget.</span></a>
    <a class="card" href="/guide/doppelgangers/"><b>Doppelganger identification</b><span>The decision the queue is pressuring.</span></a>
  </div>
"""},
{
 "path": "guide/story-mode", "active": "/guides/",
 "title": "Shift At Midnight Story Mode — Shifts &amp; Structure",
 "og_short": "Shift At Midnight Story Mode",
 "desc": "How Story Mode is structured in Shift At Midnight, what randomly generated shifts mean for guides, and where the three hidden ending achievements sit.",
 "trail": G + [(None, "Story Mode")],
 "h1": "Story Mode",
 "lede": "Shifts are <strong>randomly generated</strong>, which changes what a guide can honestly promise you. There is no fixed night-by-night script to memorise &mdash; what carries over is knowledge of the threats and the systems.",
 "body": """
  <h2>Randomly generated shifts</h2>
  <p>The game builds shifts procedurally rather than running a fixed sequence. Any guide that hands you a night-by-night walkthrough is describing one person's run, not yours.</p>
  <p>What transfers is threat knowledge: recognising a <a href="/monsters/shrieking-doll/">Shrieking Doll</a> by its scream, knowing the <a href="/monsters/jack-in-the-box/">music box</a> is a countdown, knowing <a href="/monsters/the-dentist/">the Dentist</a> cannot be fought. Those are true on every seed.</p>

  <div class="term tip">
    <div class="term-h">Norbert is the exception</div>
    <p><a href="/monsters/norbert/">Norbert</a> is consistently reported as a <strong>Night 2</strong> arrival &mdash; a fixed beat in a procedural structure, which fits his role as a deliberate teaching moment placed early enough to matter.</p>
  </div>

  <h2>Where the endings sit</h2>
  <p>Three achievements are hidden and rare: <em>Grave Decision</em> (26.0%), <em>True Ending</em> (13.4%) and <em>Empty Home</em> (7.0%). Their separation suggests distinct outcomes rather than one sequence. Full discussion on <a href="/endings/">the endings page</a>, with fact and inference clearly separated.</p>
  <p>Because shifts are procedural but endings are rare, the likely lever is <em>how you played</em> rather than <em>which nights you got</em> &mdash; the run-level decisions, not the seed.</p>

  <h2>Solo or co-op</h2>
  <p>Story Mode works either way. Solo gives you full control of every judgement call, which matters if you are hunting the hidden achievements &mdash; nobody else kills a customer you were still assessing.</p>

  <div class="grid two">
    <a class="card" href="/endings/"><b>All endings</b><span>What the hidden achievements imply.</span></a>
    <a class="card" href="/guide/endless-mode/"><b>Endless Mode</b><span>The free Q4 2026 update.</span></a>
  </div>
"""},
{
 "path": "guide/endless-mode", "active": "/guides/",
 "title": "Shift At Midnight Endless Mode &amp; 2026 Roadmap",
 "og_short": "Shift At Midnight Endless Mode",
 "desc": "Endless Mode is a free update planned for Q4 2026. What has actually been confirmed, and what people are incorrectly claiming is on the roadmap.",
 "trail": G + [(None, "Endless Mode")],
 "h1": "Endless Mode &amp; roadmap",
 "lede": "One thing is on the published roadmap: a <strong>free Endless Mode update in Q4 2026</strong>. That is the confirmed list. Everything else circulating as &ldquo;upcoming&rdquo; is not something we can verify.",
 "body": """
  <h2>What is confirmed</h2>
  <table class="facts">
    <tr><th>Update</th><td>Endless Mode</td></tr>
    <tr><th>Cost</th><td>Free</td></tr>
    <tr><th>Timing</th><td>Q4 2026</td></tr>
    <tr><th>Source</th><td>Official store listing</td></tr>
  </table>

  <div class="term warn">
    <div class="term-h">What is not confirmed</div>
    <p>Steam crossplay is <strong>not</strong> on any roadmap we can verify. Neither is official mod support, additional platforms, or new named monsters. If you have read otherwise, check whether the claim has a source attached &mdash; a lot of it does not. See <a href="/crossplay/">crossplay</a> and <a href="/mods/">mods</a>.</p>
  </div>

  <h2>Why an endless mode makes sense here</h2>
  <p>The core loop &mdash; a shift, a quota, customers who may not be customers &mdash; is naturally repeatable, and <a href="/guide/story-mode/">shifts are already procedurally generated</a>. An endless variant is a small step from what exists: remove the narrative frame and let shifts continue until you fail.</p>
  <p>It also addresses the achievement curve. The bottom four achievements need deliberate attempts, and an endless mode gives you a place to farm attempts without restarting a story run.</p>

  <h2>What we will do when it ships</h2>
  <p>Update this page with the actual patch notes and date, and revise the <a href="/achievements/">achievements page</a> if the update adds any. We will not pre-write speculative content for an update that does not exist yet.</p>

  <div class="grid two">
    <a class="card" href="/guide/story-mode/"><b>Story Mode</b><span>The structure Endless Mode is derived from.</span></a>
    <a class="card" href="/guide/release/"><b>Release &amp; platforms</b><span>Where the game is available now.</span></a>
  </div>
"""},
{
 "path": "guide/release", "active": "/guides/",
 "title": "Shift At Midnight Release Date, Platforms &amp; Where to Buy",
 "og_short": "Shift At Midnight Release &amp; Platforms",
 "desc": "Shift At Midnight released 22 July 2026 on Steam, Xbox Series X|S and Microsoft Store, day one on Game Pass. Which version to buy depends on your friends.",
 "trail": G + [(None, "Release &amp; platforms")],
 "h1": "Release date &amp; platforms",
 "lede": "Released <strong>22 July 2026</strong> on Steam, Xbox Series X|S and the Microsoft Store, day one on Xbox Game Pass. Which version you should buy is genuinely not obvious &mdash; it depends on where your friends are.",
 "body": """
  <table class="facts">
    <tr><th>Released</th><td>22 July 2026</td></tr>
    <tr><th>Developer</th><td>Bun Muen (solo)</td></tr>
    <tr><th>Publisher</th><td>Kwalee</td></tr>
    <tr><th>Platforms</th><td>Steam (Windows 10/11 64-bit), Xbox Series X|S, Microsoft Store</td></tr>
    <tr><th>Game Pass</th><td>Day one &mdash; console and PC</td></tr>
    <tr><th>Play Anywhere</th><td>Yes</td></tr>
    <tr><th>Price</th><td>$9.99 USD, 10% introductory discount</td></tr>
    <tr><th>Players</th><td>1&ndash;3, online co-op with proximity chat</td></tr>
    <tr><th>Steam languages</th><td>English, French, German, Spanish (Spain), Japanese, Russian, Simplified Chinese, Traditional Chinese, Portuguese (Brazil)</td></tr>
    <tr><th>Achievements</th><td>10</td></tr>
    <tr><th>Content</th><td>Steam notes "plenty of gore and blood"</td></tr>
  </table>

  <div class="term warn">
    <div class="term-h">Which version to buy</div>
    <p>This is the decision that matters, and it is not about features. <strong>Steam players cannot play with Xbox or PC Game Pass players.</strong> Xbox console and PC Game Pass share a pool through Play Anywhere. Decide as a group before anyone spends money &mdash; see <a href="/crossplay/">crossplay</a>.</p>
  </div>

  <h2>Game Pass changes the maths</h2>
  <p>If anyone in your group has Game Pass, the game is free for them, and it launched there day one on both console and PC. For a $9.99 co-op game, "one of us already has it included" often decides the whole platform question. See <a href="/game-pass/">Game Pass &amp; Play Anywhere</a>.</p>

  <h2>Play Anywhere</h2>
  <p>One Microsoft Store purchase covers both the Xbox console and Windows versions, with shared saves. If you want to play on a console and a PC, that is the version that does it in one purchase.</p>

  <div class="grid two">
    <a class="card" href="/crossplay/"><b>Crossplay</b><span>Read before buying.</span></a>
    <a class="card" href="/price/"><b>Price</b><span>What it costs and whether that matters.</span></a>
  </div>
"""},
{
 "path": "multiplayer", "active": "/guides/",
 "title": "Shift At Midnight Multiplayer — Player Count &amp; Crossplay",
 "og_short": "Shift At Midnight Multiplayer",
 "desc": "Shift At Midnight supports up to 3 players in online co-op with proximity chat. Platform compatibility is the thing that stops most groups playing together.",
 "trail": [(None, "Multiplayer")],
 "h1": "Multiplayer",
 "lede": "<strong>Up to three players</strong>, online co-op, with <strong>proximity chat</strong>. There is also a full single-player mode. The thing that most often stops a group playing together is not the player cap &mdash; it is which store they bought it from.",
 "body": """
  <table class="facts">
    <tr><th>Max players</th><td>3</td></tr>
    <tr><th>Mode</th><td>Online co-op</td></tr>
    <tr><th>Voice</th><td>Proximity chat</td></tr>
    <tr><th>Single-player</th><td>Yes, full mode</td></tr>
    <tr><th>Crossplay</th><td>Xbox + PC Game Pass only &mdash; <a href="/crossplay/">Steam isolated</a></td></tr>
  </table>

  <div class="term warn">
    <div class="term-h">The three-player cap is a hard limit</div>
    <p>If your group is four people, one is sitting out. The game is built around three roles in a small building, and the design does not stretch. Plan accordingly before you organise a night.</p>
  </div>

  <h2>Getting everyone into a session</h2>
  <p>Everyone must be on the same side of the platform line. Steam players connect only to Steam players; Xbox console and PC Game Pass players share one pool via Play Anywhere. Mixed groups cannot play together, and this is the single most common reason a planned session does not happen. Sort it <em>before</em> anyone buys.</p>

  <h2>Proximity chat is a mechanic</h2>
  <p>Voices fade with distance, so every noise your teammates make carries positional information. Running Discord over the top removes that and makes co-ordination worse, not better. Use the in-game chat &mdash; see the <a href="/guide/co-op/">co-op guide</a> for role splitting.</p>

  <h2>Is solo worth it?</h2>
  <p>Yes, and it is not a lesser mode. Solo gives you complete control of every judgement call at the counter, which matters if you are chasing the <a href="/endings/">hidden ending achievements</a>. Co-op is more chaotic and funnier; solo is tenser and more deliberate.</p>

  <div class="grid two">
    <a class="card" href="/crossplay/"><b>Crossplay</b><span>Exactly who can play with whom.</span></a>
    <a class="card" href="/guide/co-op/"><b>Co-op roles</b><span>How three players should split the work.</span></a>
  </div>
"""},
{
 "path": "game-pass", "active": "/guides/",
 "title": "Is Shift At Midnight on Game Pass? Yes — Day One, Play Anywhere",
 "og_short": "Shift At Midnight on Game Pass",
 "desc": "Shift At Midnight launched day one on Xbox Game Pass for console and PC, and is an Xbox Play Anywhere title. What that gets you versus buying on Steam.",
 "trail": [(None, "Game Pass")],
 "h1": "Shift At Midnight on Game Pass",
 "lede": "<strong>Yes &mdash; day one, on both Xbox console and PC.</strong> It is also an Xbox Play Anywhere title, which means one Microsoft Store purchase covers the Xbox and Windows versions. That detail is also why the crossplay situation is what it is.",
 "body": """
  <table class="facts">
    <tr><th>On Game Pass</th><td>Yes &mdash; day one (22 July 2026)</td></tr>
    <tr><th>Tiers</th><td>Xbox console and PC Game Pass</td></tr>
    <tr><th>Play Anywhere</th><td>Yes</td></tr>
    <tr><th>Buy price</th><td>$9.99 USD if you do not subscribe</td></tr>
    <tr><th>Crossplay pool</th><td>Shares with Xbox console + Microsoft Store</td></tr>
  </table>

  <h2>What Play Anywhere gets you</h2>
  <p>Buy once on the Microsoft Store and you own both the Xbox console and Windows versions, with shared saves. Start a run on PC, continue on the console. For a $9.99 game this is a real convenience, and it is also the technical reason Xbox and PC Game Pass players are in the same multiplayer pool &mdash; both builds talk to the same Microsoft networking layer.</p>

  <div class="term warn">
    <div class="term-h">The trade-off against Steam</div>
    <p>Game Pass and Microsoft Store players <strong>cannot play with Steam players</strong>. If your friends are on Steam, the free Game Pass copy is not usable for playing with them. Full breakdown on <a href="/crossplay/">the crossplay page</a>.</p>
  </div>

  <h2>Achievements differ</h2>
  <p>The Microsoft versions track Xbox achievements; the Steam version tracks Steam achievements. The requirements are the same ten, but our <a href="/achievements/">achievements page</a> quotes Steam global unlock rates because those are the numbers that are publicly readable.</p>

  <h2>If it leaves Game Pass</h2>
  <p>Game Pass catalogues rotate. Nothing has been announced about this title leaving, and we are not going to speculate about a date &mdash; but if you are deep into a run and the possibility bothers you, the Play Anywhere purchase at $9.99 makes your access permanent.</p>

  <div class="grid two">
    <a class="card" href="/crossplay/"><b>Crossplay</b><span>Who you can actually play with.</span></a>
    <a class="card" href="/price/"><b>Price</b><span>What buying it costs instead.</span></a>
  </div>
"""},
{
 "path": "price", "active": "/guides/",
 "title": "Shift At Midnight Price — $9.99 and Whether to Buy It",
 "og_short": "Shift At Midnight Price",
 "desc": "Shift At Midnight is $9.99 USD with a 10% launch discount, and free on Game Pass. Which platform you buy on matters more than the price does.",
 "trail": [(None, "Price")],
 "h1": "Price &amp; editions",
 "lede": "<strong>$9.99 USD</strong>, with a 10% introductory discount at launch, and <strong>free with Xbox Game Pass</strong>. There is one edition. The decision that actually costs people money is not the price &mdash; it is the store.",
 "body": """
  <table class="facts">
    <tr><th>Price</th><td>$9.99 USD (regional pricing varies)</td></tr>
    <tr><th>Launch discount</th><td>10% introductory offer</td></tr>
    <tr><th>Editions</th><td>One &mdash; no deluxe or season pass</td></tr>
    <tr><th>Game Pass</th><td>Included, day one</td></tr>
    <tr><th>Future content</th><td>Endless Mode, Q4 2026 &mdash; free</td></tr>
  </table>

  <div class="term warn">
    <div class="term-h">The expensive mistake is not the price</div>
    <p>It is buying on the wrong store. <strong>Steam players cannot play with Game Pass or Xbox players.</strong> Spending $9.99 on Steam when your friends are on Game Pass means buying it again on the Microsoft Store. Decide as a group first &mdash; <a href="/crossplay/">crossplay</a>.</p>
  </div>

  <h2>No paid DLC announced</h2>
  <p>The only content on the roadmap is Endless Mode in Q4 2026, and it is <strong>free</strong>. No season pass, no deluxe edition, no paid cosmetics have been announced. For a $9.99 game from a solo developer, what you buy is what there is.</p>

  <h2>Is it worth $9.99?</h2>
  <p>The honest framing: this is a three-player co-op horror game with ten achievements and a procedural shift structure. The achievement curve suggests most players get several hours in &mdash; 40.1% reach <em>Relentless</em>, which is not a first-session achievement &mdash; and a meaningful minority push into the rare hidden endings at 7&ndash;13%. See <a href="/review/">is it worth it</a>.</p>
  <p>If you have Game Pass the question does not arise. If you do not, and you have two friends who will play it with you, $9.99 for a co-op night is not a hard sell. If you are buying it to play alone, it is a smaller game than the store page implies.</p>

  <div class="grid two">
    <a class="card" href="/game-pass/"><b>Game Pass</b><span>Free if you subscribe.</span></a>
    <a class="card" href="/review/"><b>Is it worth it?</b><span>What the data suggests.</span></a>
  </div>
"""},
{
 "path": "mods", "active": "/guides/",
 "title": "Shift At Midnight Mods — Is There Mod Support?",
 "og_short": "Shift At Midnight Mods",
 "desc": "No official mod support or Steam Workshop integration has been announced for Shift At Midnight as of 28 July 2026. What that means and what the risks are.",
 "trail": [(None, "Mods")],
 "h1": "Mods",
 "lede": "<strong>There is no official mod support.</strong> No Steam Workshop integration and no modding tools have been announced as of 28 July 2026. That is the honest answer, and it is worth knowing before you go looking.",
 "body": """
  <h2>What is confirmed</h2>
  <table class="facts">
    <tr><th>Steam Workshop</th><td>Not listed</td></tr>
    <tr><th>Official mod tools</th><td>None announced</td></tr>
    <tr><th>Roadmap mention</th><td>None &mdash; roadmap lists only Endless Mode (Q4 2026)</td></tr>
  </table>

  <div class="term warn">
    <div class="term-h">Risks of unofficial mods</div>
    <p>Without official support, anything you find is third-party and unsupported. Three specific problems: it may break with any patch; it may interfere with <strong>achievement tracking</strong>, which matters given three achievements are hidden and rare; and in an online co-op game, modified clients can fail to connect to unmodified ones. If you are chasing <a href="/endings/">True Ending</a> or <a href="/achievements/">Empty Home</a>, an unofficial mod is a bad bet.</p>
  </div>

  <h2>Why a solo developer might not prioritise it</h2>
  <p>Shift At Midnight is built by one person, Bun Muen, published by Kwalee. Mod support is a substantial ongoing commitment &mdash; documented interfaces, stability guarantees across patches, and a support burden when mods break. The announced roadmap points at content (Endless Mode) rather than platform work. That is a reasonable set of priorities and we would not read anything into it.</p>

  <h2>If it changes</h2>
  <p>This page gets updated with the announcement and date. We will not list third-party mods or link to them while there is no official framework &mdash; recommending unsupported binaries for a game whose rare achievements are still unsolved would be irresponsible.</p>

  <div class="grid two">
    <a class="card" href="/guide/endless-mode/"><b>Roadmap</b><span>What is actually coming.</span></a>
    <a class="card" href="/achievements/"><b>Achievements</b><span>What mods could put at risk.</span></a>
  </div>
"""},
{
 "path": "discord", "active": "/guides/",
 "title": "Shift At Midnight Discord &amp; Community — Where Players Gather",
 "og_short": "Shift At Midnight Community",
 "desc": "Where the Shift At Midnight community actually is, why the hidden achievements are still unsolved, and how to contribute useful findings rather than guesses.",
 "trail": [(None, "Community")],
 "h1": "Community &amp; Discord",
 "lede": "A three-player co-op game where <strong>three of ten achievements are still hidden</strong> generates a lot of community activity &mdash; people looking for a third player, and people trying to work out what <em>True Ending</em> actually needs.",
 "body": """
  <div class="term warn">
    <div class="term-h">On links</div>
    <p>We do not publish Discord invite links. Invites expire, get replaced, and are a standard vector for impersonation &mdash; a fan wiki linking to a server that has changed hands is a real risk. Check the official Steam store page and Kwalee's own channels for current official links. If a server claims to be official, verify it from the publisher's side, not from a fan site.</p>
  </div>

  <h2>Why the community matters more than usual here</h2>
  <p>Steam hides the descriptions for <em>Grave Decision</em> (26.0%), <em>True Ending</em> (13.4%) and <em>Empty Home</em> (7.0%). Nobody has an official requirement text. That means the only path to solving them is players correlating their own runs &mdash; which is exactly the kind of thing a community does well and a single guide writer cannot do at all.</p>

  <div class="term tip">
    <div class="term-h">How to contribute something useful</div>
    <p>Log your runs. Who you served, who you killed, what the scanner said, which achievement fired at the end. One run proves nothing; ten logged runs across a few players is how hidden achievements get cracked. Posting "I think it's about karma" without notes attached is how bad guidance spreads &mdash; and a lot of the confident writing about this game's endings traces back to exactly that.</p>
  </div>

  <h2>Finding a third player</h2>
  <p>The cap is three, and the platform split is the constraint. Say which version you are on when you post &mdash; <strong>Steam players cannot play with Xbox or PC Game Pass players</strong>. Half the failed link-ups in any co-op community for this game are people who did not mention their store. See <a href="/crossplay/">crossplay</a>.</p>

  <div class="grid two">
    <a class="card" href="/endings/"><b>Endings</b><span>What is confirmed and what is still open.</span></a>
    <a class="card" href="/multiplayer/"><b>Multiplayer</b><span>Player count and platform compatibility.</span></a>
  </div>
"""},
{
 "path": "review", "active": "/guides/",
 "title": "Is Shift At Midnight Worth It? What the Data Says",
 "og_short": "Is Shift At Midnight Worth It?",
 "desc": "A $9.99 co-op horror game from a solo developer. What the achievement completion curve and the design actually tell you about whether it is worth your time.",
 "trail": [(None, "Is it worth it?")],
 "h1": "Is Shift At Midnight worth it?",
 "lede": "A <strong>$9.99</strong> three-player co-op horror game from a solo developer, free on Game Pass. Rather than tell you it is &ldquo;a must-play&rdquo;, here is what the publicly readable data actually supports.",
 "body": """
  <h2>What the achievement curve says about engagement</h2>
  <p>Completion rates are one of the few honest public signals about whether people stick with a game.</p>
  <ul>
    <li><strong>92.8%</strong> survive their first hunt &mdash; almost nobody bounces off immediately.</li>
    <li><strong>75.3%</strong> kill a <a href="/monsters/demented/">Demented</a> &mdash; three quarters get past the opening.</li>
    <li><strong>40.1%</strong> reach <em>Relentless</em> &mdash; not a first-session achievement. Four in ten players are still engaged well past the tutorial phase.</li>
    <li><strong>13.4% / 7.0%</strong> reach the rare hidden endings &mdash; a real minority is digging.</li>
  </ul>
  <p>For a $9.99 indie release, a 40% figure on a mid-tier skill achievement is a healthy retention signal. It is not a game most people refund after an hour.</p>

  <h2>What it does well</h2>
  <p>The central idea is genuinely good: a horror game where the scary decision is <em>administrative</em>. You are checking ID at a counter, and the tension comes from having authority you are not qualified to exercise. The <a href="/monsters/norbert/">Norbert</a>/<a href="/monsters/the-dentist/">Dentist</a> pairing &mdash; harmless thing that trips your alarm, lethal thing that does not register at all &mdash; is a genuinely elegant piece of design teaching.</p>
  <p><a href="/guide/co-op/">Proximity chat</a> is used as a mechanic rather than a feature. Voices fading with distance is load-bearing.</p>

  <h2>What to be realistic about</h2>
  <ul>
    <li><strong>It is small.</strong> Ten achievements, one mode plus a free one coming in Q4. This is a $9.99 game and it is scoped like one.</li>
    <li><strong>It is better with people.</strong> Solo works and is tenser, but the design's best moments are three people shouting across a gas station.</li>
    <li><strong>The platform split is a genuine annoyance.</strong> <a href="/crossplay/">Steam cannot play with Game Pass</a>, and for a co-op game that is a real cost.</li>
    <li><strong>Gore.</strong> Steam flags "plenty of gore and blood". It is a game about deciding whether to kill the person in front of you.</li>
  </ul>

  <div class="term tip">
    <div class="term-h">Straight answer</div>
    <p>If you have Game Pass and two friends, install it tonight &mdash; it costs you nothing and it is a good three-hour night. If you are buying at $9.99 to play with a group, that is easy value provided <a href="/crossplay/">everyone buys on the same side of the platform line</a>. If you are buying it to play alone, it is a smaller and quieter game than the trailers suggest &mdash; still interesting, but manage expectations.</p>
  </div>

  <div class="grid two">
    <a class="card" href="/price/"><b>Price &amp; editions</b><span>What you get for $9.99.</span></a>
    <a class="card" href="/guide/beginners/"><b>Beginner's guide</b><span>If you have decided to play.</span></a>
  </div>
"""},
{
 "path": "joes-diner-newsletter", "active": "/guides/",
 "title": "Who Writes the Joe's Diner Newsletter? — Shift At Midnight",
 "og_short": "Joe's Diner Newsletter",
 "desc": "One of the most-searched Shift At Midnight questions is who writes the Joe's Diner newsletter. Here is what we can and cannot confirm, without inventing an answer.",
 "trail": [(None, "Joe's Diner newsletter")],
 "h1": "Who writes the Joe's Diner newsletter?",
 "lede": "This is one of the questions people actually type into Google about Shift At Midnight &mdash; a specific piece of in-world text that players notice and want explained. We are going to be straight with you about what is confirmed and what is not.",
 "body": """
  <div class="term warn">
    <div class="term-h">Status: not confirmed</div>
    <p>We do not have a verified in-game answer for who authors the Joe's Diner newsletter, and we are not going to invent one. There is a real difference between &ldquo;here is the answer&rdquo; and &ldquo;here is a plausible-sounding sentence&rdquo;, and a lot of writing about this game's smaller mysteries is the second thing wearing the clothes of the first.</p>
  </div>

  <h2>Why this question exists at all</h2>
  <p>Shift At Midnight puts readable in-world material in front of you while you work. A newsletter from a nearby diner is exactly the kind of object that reads as flavour on the first shift and as a clue on the fifth &mdash; particularly in a game where three achievements are hidden and the community is actively hunting for what triggers them.</p>
  <p>The question is being searched because players suspect it matters. That suspicion is reasonable, and it is not the same as evidence.</p>

  <h2>What we can say</h2>
  <ul>
    <li>The game is built around <strong>reading things carefully</strong> &mdash; IDs, behaviour, readings that disagree with each other. In-world text rewards attention by design.</li>
    <li>Three achievements are hidden: <em>Grave Decision</em> (26.0%), <em>True Ending</em> (13.4%), <em>Empty Home</em> (7.0%). None has a published requirement. See <a href="/endings/">endings</a>.</li>
    <li>Nothing publicly documented connects the newsletter to those achievements. That is an <strong>absence of evidence</strong>, not evidence of absence.</li>
  </ul>

  <div class="term tip">
    <div class="term-h">If you want to actually solve this</div>
    <p>Screenshot the newsletter every run and note which shift it appeared on and what else was different about that night. If the text varies between runs, that is a strong signal it is procedural flavour. If it is identical every time and names someone, that is a much more interesting fact. Nobody has published that comparison &mdash; which is exactly why the question is still open.</p>
    <p>If you have run that comparison, that is a genuinely useful contribution. See <a href="/discord/">community</a>.</p>
  </div>

  <h2>Why we are leaving this page thin</h2>
  <p>Because padding it would be worse than admitting we do not know. When we have a verified answer &mdash; from reproducible player reports or from the developer &mdash; it goes here with the date and the source, and this page gets rewritten properly.</p>

  <div class="grid two">
    <a class="card" href="/endings/"><b>Endings</b><span>The other open questions in this game.</span></a>
    <a class="card" href="/guide/story-mode/"><b>Story Mode</b><span>Why procedural shifts complicate clue-hunting.</span></a>
  </div>
"""},
{
 "path": "faq", "active": "/faq/",
 "title": "Shift At Midnight FAQ — Crossplay, Game Pass, Players &amp; Endings",
 "og_short": "Shift At Midnight FAQ",
 "desc": "Straight answers to the most searched Shift At Midnight questions: crossplay, Game Pass, player count, price, mods, achievements and the hidden endings.",
 "trail": [(None, "FAQ")],
 "h1": "Shift At Midnight FAQ",
 "lede": "The questions people actually search, answered directly. Where the honest answer is &ldquo;not confirmed&rdquo;, we say that instead of guessing.",
 "extra_ld": FAQ_LD,
 "body": """
  <h2>Buying &amp; playing together</h2>
  <div class="faq">
    <details open>
      <summary>Is Shift At Midnight crossplay?</summary>
      <div class="a"><p><strong>Partially.</strong> Xbox console and PC Game Pass players share one pool through Xbox Play Anywhere. The Steam version connects only to other Steam players. Mixed groups cannot play together. <a href="/crossplay/">Full breakdown</a>.</p></div>
    </details>
    <details>
      <summary>Is Shift At Midnight on Game Pass?</summary>
      <div class="a"><p>Yes &mdash; day one, on both Xbox console and PC. It is also an Xbox Play Anywhere title. <a href="/game-pass/">Details</a>.</p></div>
    </details>
    <details>
      <summary>How many players can play together?</summary>
      <div class="a"><p>Up to three, online, with proximity chat. There is also a full single-player mode. <a href="/multiplayer/">More</a>.</p></div>
    </details>
    <details>
      <summary>How much does it cost?</summary>
      <div class="a"><p>$9.99 USD with a 10% introductory discount at launch, and free with Game Pass. One edition, no paid DLC announced. <a href="/price/">More</a>.</p></div>
    </details>
    <details>
      <summary>Is Shift At Midnight on PS5?</summary>
      <div class="a"><p><strong>No.</strong> There is no PlayStation 5 or PS4 version and none has been announced. See <a href="/platforms/">platforms</a>.</p></div>
    </details>
    <details>
      <summary>Is Shift At Midnight on mobile or the App Store?</summary>
      <div class="a"><p><strong>No.</strong> No iOS or Android version exists. Anything using this name in a mobile app store is not this game. See <a href="/platforms/">platforms</a>.</p></div>
    </details>
    <details>
      <summary>Is Shift At Midnight free?</summary>
      <div class="a"><p>Not to buy &mdash; it is $9.99. But it is included with Xbox Game Pass at no extra cost.</p></div>
    </details>
    <details>
      <summary>When did Shift At Midnight come out?</summary>
      <div class="a"><p><strong>22 July 2026</strong>, after being delayed twice from an original 28 May date. See <a href="/release-date/">release date</a>.</p></div>
    </details>
    <details>
      <summary>Is night three the last level?</summary>
      <div class="a"><p>No &mdash; Story Mode continues past it. Shifts are procedurally generated rather than fixed levels. See <a href="/nights-and-levels/">nights &amp; levels</a>.</p></div>
    </details>
    <details>
      <summary>What is the Employee Package?</summary>
      <div class="a"><p>A physical merch bundle Kwalee ran as a giveaway &mdash; not DLC and not for sale. See <a href="/employee-package/">Employee Package</a>.</p></div>
    </details>
    <details>
      <summary>Which platform should I buy it on?</summary>
      <div class="a"><p>Whichever one your friends are on &mdash; that is genuinely the whole answer, because the two pools cannot mix. If anyone in the group has Game Pass, the Microsoft side is usually cheapest overall.</p></div>
    </details>
  </div>

  <h2>Monsters &amp; mechanics</h2>
  <div class="faq">
    <details>
      <summary>How do I beat the Marionette?</summary>
      <div class="a"><p>The <a href="/monsters/jack-in-the-box/">music box</a> decides it. Wind it all the way down and the fight never starts; let the melody play three times without winding and you face it with no real counter. Only 35.1% of players have killed one. <a href="/monsters/marionette/">Full guide</a>.</p></div>
    </details>
    <details>
      <summary>How do I kill the Dentist?</summary>
      <div class="a"><p><strong>You do not.</strong> No weapon, trap or barricade is effective. He is also invisible to the ID verification computer. Running is the entire answer. <a href="/monsters/the-dentist/">More</a>.</p></div>
    </details>
    <details>
      <summary>Should I kill Norbert?</summary>
      <div class="a"><p>No. He scans as a fake ID and is <strong>completely harmless</strong> &mdash; a gnome who turns up on Night 2 to cause chaos. He exists to teach you that the scanner reports on documents, not on danger. <a href="/monsters/norbert/">More</a>.</p></div>
    </details>
    <details>
      <summary>Does the ID scanner tell me who is dangerous?</summary>
      <div class="a"><p>No. It tells you whether a <em>document</em> is authentic. Norbert has a fake ID and is harmless; the Dentist does not appear on it at all and is lethal. <a href="/guide/doppelgangers/">Identification guide</a>.</p></div>
    </details>
  </div>

  <h2>Achievements &amp; endings</h2>
  <div class="faq">
    <details>
      <summary>How many achievements are there?</summary>
      <div class="a"><p>Ten. Three are hidden: <em>Grave Decision</em> (26.0%), <em>True Ending</em> (13.4%) and <em>Empty Home</em> (7.0%). <a href="/achievements/">Full list with rarity</a>.</p></div>
    </details>
    <details>
      <summary>How do I get the true ending?</summary>
      <div class="a"><p><strong>Not confirmed.</strong> The achievement description is hidden and no verified requirement has been published. We are not going to invent one &mdash; <a href="/endings/">here is what the data does and does not support</a>.</p></div>
    </details>
    <details>
      <summary>What is the hardest achievement?</summary>
      <div class="a"><p><em>Empty Home</em> at 7.0%, followed by <em>True Ending</em> at 13.4%. Of the non-hidden ones, <em>Locked And Loaded</em> (buy every melee weapon) at 20.6% is the rarest.</p></div>
    </details>
  </div>

  <h2>Content &amp; updates</h2>
  <div class="faq">
    <details>
      <summary>Does it have mods?</summary>
      <div class="a"><p>No official mod support or Steam Workshop integration as of 28 July 2026. <a href="/mods/">Why, and the risks of unofficial ones</a>.</p></div>
    </details>
    <details>
      <summary>What is coming next?</summary>
      <div class="a"><p>Endless Mode &mdash; a free update planned for Q4 2026. That is the only confirmed item on the roadmap. <a href="/guide/endless-mode/">More</a>.</p></div>
    </details>
    <details>
      <summary>Will Steam get crossplay later?</summary>
      <div class="a"><p>No announcement has been made. Plan your purchases as though the Steam island is permanent.</p></div>
    </details>
    <details>
      <summary>Who made it?</summary>
      <div class="a"><p>Solo developer <strong>Bun Muen</strong>, published by <strong>Kwalee</strong>. Released 22 July 2026.</p></div>
    </details>
  </div>
"""},
]

if __name__ == "__main__":
    print("生成攻略页 + 查询词页:")
    build(PAGES)

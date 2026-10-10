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
      "acceptedAnswer": { "@type": "Answer", "text": "Partially, per the developer. The 10 July 2026 announcement says Xbox and PC Game Pass players will have crossplay, and that Steam players will only be able to play with other Steam players. On the Steam side, the same post previews a Steam-only public server browser, and no later changelog mentions it shipping. No official announcement promises crossplay between Steam and Xbox (all 31 official Steam announcements checked on 10 October 2026). Which pool a bought Microsoft Store copy joins, and how Xbox Play Anywhere relates to matchmaking, is not confirmed by any official statement, and this site has not tested it." } },
    { "@type": "Question", "name": "Is Shift At Midnight on Game Pass?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes, per the developer: the 22 July 2026 launch post says the game is out on Steam, Xbox and Game Pass, and the 10 July 2026 post names Xbox PC Game Pass. Whether it is still in the Game Pass catalogue was not re-checked on 10 October 2026." } },
    { "@type": "Question", "name": "How many players can play Shift At Midnight?",
      "acceptedAnswer": { "@type": "Answer", "text": "Three by design. The 23 July 2026 patch made the lobby cap selectable up to six, but the developer says the game is designed and has always been marketed around a maximum of three players, and does not recommend six for a first playthrough. Single-player is fully supported, and co-op uses proximity chat." } },
    { "@type": "Question", "name": "How much does Shift At Midnight cost?",
      "acceptedAnswer": { "@type": "Answer", "text": "9.99 USD on Steam, with no discount running on 10 October 2026. The Xbox listing showed 9.99 USD on 12 August 2026 and was not re-checked." } },
    { "@type": "Question", "name": "Does Shift At Midnight have mods?",
      "acceptedAnswer": { "@type": "Answer", "text": "There is no Steam Workshop and there are no official modding tools, and the developer has not commented on modding either way. A community scene built on BepInEx does exist: 12 mods were listed on Thunderstore as of 5 August 2026, plus a separate section on Nexus Mods. The best known of them, ShiftMorePlayers, raises the lobby cap well past six and only needs to be installed by the host." } },
    { "@type": "Question", "name": "How many achievements does Shift At Midnight have?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ten. Three of them are hidden: Grave Decision at 35.1 percent, True Ending at 16.0 percent and Empty Home at 10.9 percent, as of 10 October 2026." } },
    { "@type": "Question", "name": "How do you get the true ending in Shift At Midnight?",
      "acceptedAnswer": { "@type": "Answer", "text": "Two conditions. Do not call Sheriff Clyde when the choice appears after Shift 12, and finish Shift 13 with at least 250 dollars in personal savings. Calling Clyde gives the Grave Decision ending instead, and declining with less than 250 dollars gives Empty Home. 16.0 percent of players have the True Ending achievement as of 10 October 2026." } },
    { "@type": "Question", "name": "How do you unlock Endless Mode in Shift At Midnight?",
      "acceptedAnswer": { "@type": "Answer", "text": "Finish Story Mode. Endless Mode shipped as a beta on launch day, 22 July 2026, but unlocks only once the 13-shift story is complete. It is the only mode where Rake enemies appear. The Steam store page says a free, major Endless Mode update is planned for Q4 2026 (read 10 October 2026); no official Steam announcement names Q4 2026 or gives a date for it." } },
    { "@type": "Question", "name": "How many nights are in Shift At Midnight?",
      "acceptedAnswer": { "@type": "Answer", "text": "Story Mode is 13 shifts. Customers and events are procedurally generated, so runs differ. The fixed points are Shift 9, when the Marionette becomes possible, the choice offered after Shift 12, and Shift 13." } },
    { "@type": "Question", "name": "What did the latest Shift At Midnight patch change?",
      "acceptedAnswer": { "@type": "Answer", "text": "The 1 September 2026 patch added 30 new customers to Story Mode and Endless Mode, added the Chainsaw as a purchasable melee weapon (now required for the Locked And Loaded achievement), and added security cameras in Endless Mode. As of 10 October 2026 it is the newest patch on the official Steam announcement feed; the 20 August 2026 patch before it added 15 customers and cloud saves for Steam." } },
    { "@type": "Question", "name": "Is Shift At Midnight on PS5?",
      "acceptedAnswer": { "@type": "Answer", "text": "No. There is no PlayStation 5 or PS4 version of Shift At Midnight and none has been announced. The developer's 22 July 2026 launch post names Steam, Xbox and Game Pass." } },
    { "@type": "Question", "name": "Is Shift At Midnight available on mobile or the App Store?",
      "acceptedAnswer": { "@type": "Answer", "text": "No. There is no iOS or Android version of Shift At Midnight. It is a PC and Xbox title only." } },
    { "@type": "Question", "name": "When did Shift At Midnight come out?",
      "acceptedAnswer": { "@type": "Answer", "text": "Shift At Midnight released on 22 July 2026, after being delayed twice from its original 28 May 2026 date." } },
    { "@type": "Question", "name": "Is Shift At Midnight free?",
      "acceptedAnswer": { "@type": "Answer", "text": "The game costs 9.99 USD on Steam. It was announced for Xbox PC Game Pass at launch (10 July 2026 post); Game Pass catalogue membership was last seen on the Xbox listing on 12 August 2026 and was not re-checked on 10 October 2026. There is also a free multiplayer demo on Steam." } },
    { "@type": "Question", "name": "Who developed Shift At Midnight?",
      "acceptedAnswer": { "@type": "Answer", "text": "It was built by solo developer Bun Muen and published by Kwalee. It released on 22 July 2026." } }
  ]
}
</script>"""

PAGES = [
{
 "path": "guides", "active": "/guides/",
 "published": "2026-08-05",   # 保留改日期行之前的 datePublished(D2 2026-10-10)
 "updated": "Last updated 2026-10-10 &middot; the crossplay card, the patience card re-checked 10 October 2026 against the official Steam announcements &middot; rest of the page last verified 5 August 2026 (29 July 2026 patch) and not re-checked against the 20 August and 1 September 2026 patches (see the updates page)",
 "title": "All Shift At Midnight Guides — Complete Wiki Index",
 "og_short": "All Shift At Midnight Guides",
 "desc": "Every Shift At Midnight guide in one index, ordered by where you are in a run: your first shift, spotting doppelgangers, surviving hunts, the three endings, and Endless Mode.",
 "trail": [(None, "Guides")],
 "h1": "All Shift At Midnight guides",
 "lede": "Everything on this wiki, ordered the way a run actually goes &mdash; the counter first, then telling people apart, then surviving what you let through, then the endings. If something specific just killed you, skip to the <a href=\"/monsters/\">bestiary</a>.",
 "body": """
  <h2>1. Your first shift</h2>
  <p>The job is a gas-station counter job. The horror is what happens when you do the counter job badly. Read the first of these before you start; the other three answer questions that arrive within the hour.</p>
  <div class="grid two">
    <a class="card" href="/guide/beginners/"><b>Beginner&rsquo;s guide</b><span>What the job is, what the quota wants from you, and the mistakes that end first runs. Start here.</span></a>
    <a class="card" href="/nights-and-levels/"><b>Nights, shifts &amp; Endless</b><span>Story mode is 13 procedurally generated shifts. Only three of them change the rules &mdash; read this when you want to know what is fixed and what is rolled.</span></a>
    <a class="card" href="/multiplayer/"><b>Multiplayer &amp; co-op</b><span>Three players by design, six selectable since the 23 July patch, and how to divide the work between them.</span></a>
    <a class="card danger" href="/crossplay/"><b>Crossplay &mdash; read before buying</b><span>Per the developer (10 July 2026), Steam players will only be able to play with other Steam players. Check before anyone pays.</span></a>
  </div>

  <h2>2. Telling people apart</h2>
  <p>This is the actual game; everything else is consequence. A doppelganger you wave through completes its purchase, walks out, and comes back the same night as something that hunts you &mdash; which is why identification and survival are one subject rather than two.</p>
  <div class="grid two">
    <a class="card" href="/guide/doppelgangers/"><b>Identifying doppelgangers</b><span>The seven categories of tell, what the N.E.T. database does that the ID scanner cannot, why Norbert is a trap, and what the patch notes say about the patience timer.</span></a>
    <a class="card" href="/tools/#threat-lookup"><b>Threat lookup</b><span>Search by what you actually saw &mdash; music box, screaming, fake ID &mdash; instead of by a name you do not have yet.</span></a>
  </div>

  <h2>3. Surviving what you let in</h2>
  <p>Seven kinds of threat, and they do not want the same thing. One you summon yourself. One cannot be fought at all. One is not a monster &mdash; it is a wind-up box. One is a customer.</p>
  <div class="grid two">
    <a class="card danger" href="/monsters/"><b>Bestiary</b><span>All seven threats side by side, from the <a href="/monsters/entity/">Entity</a> you summon yourself to the Rakes of Endless Mode.</span></a>
    <a class="card" href="/guide/survival/"><b>Survival &amp; weapons</b><span>Sound discipline, barricades, traps, and what each weapon is for. Read it before the hunt rather than during one.</span></a>
  </div>
  <ul>
    <li><a href="/monsters/shrieking-doll/"><strong>Shrieking Doll</strong></a> &mdash; fragile, hunts by line of sight, dies to a few shots. The sensible target if you want <em>Relentless</em>.</li>
    <li><a href="/monsters/demented/"><strong>Demented</strong></a> &mdash; frozen for as long as you look straight at it. You do not out-shoot this one; you walk it into a trap.</li>
    <li><a href="/monsters/marionette/"><strong>Marionette</strong></a> &mdash; from Shift 9 onward, flagged in advance by a N.E.T. email and decided by a music box.</li>
    <li><a href="/monsters/jack-in-the-box/"><strong>Jack-in-the-Box</strong></a> &mdash; not a monster. It is the music box, and three melodies is the deadline.</li>
    <li><a href="/monsters/norbert/"><strong>Norbert</strong></a> &mdash; not a monster either. A gnome with a fake ID who exists to punish the obvious response.</li>
    <li><a href="/monsters/the-dentist/"><strong>The Dentist</strong></a> &mdash; Shift 13. Immune to weapons and traps. Running is the entire answer.</li>
  </ul>

  <h2>4. Finishing the story</h2>
  <p>Which ending you get is settled by two things, and both are easy to miss if you do not know they exist: a phone call offered to you after Shift 12, and how much money is in your account when Shift 13 ends.</p>
  <div class="grid two">
    <a class="card" href="/endings/"><b>All three endings</b><span>The exact conditions for True Ending, Grave Decision and Empty Home, and the global unlock rate for each.</span></a>
    <a class="card" href="/achievements/"><b>All 10 achievements</b><span>The full list with rarity &mdash; most useful as a map of which parts of the game most players never reach.</span></a>
  </div>

  <h2>5. After the credits</h2>
  <p>Endless Mode unlocks only once the story is finished, and it is not simply more shifts: it has an enemy that story mode never spawns.</p>
  <div class="grid two">
    <a class="card" href="/nights-and-levels/#endless-mode"><b>Endless Mode</b><span>What the beta already contains, what the free Q4 2026 update is meant to add, and where the Rakes come from.</span></a>
    <a class="card" href="/updates/"><b>Patch notes</b><span>Every change since launch. The 29 July patch removed a mechanic and added an enemy &mdash; if you finished before then, some of what you know is out of date.</span></a>
    <a class="card" href="/mods/"><b>Mods</b><span>No Workshop, but an active BepInEx scene &mdash; including the mod that pushes lobbies well past six.</span></a>
    <a class="card" href="/similar-games/"><b>Games like it</b><span>Sorted by which part you liked: the interrogation, the co-op, or the shift itself.</span></a>
  </div>

  <h2>Reference</h2>
  <div class="grid two">
    <a class="card" href="/review/"><b>Is it worth it?</b><span>The price, the free demo, and what nearly 7,000 Steam reviews add up to.</span></a>
    <a class="card" href="/platforms/"><b>Platforms &amp; Game Pass</b><span>PC and Xbox, day one on Game Pass, and the honest answers about PS5, Switch and mobile.</span></a>
    <a class="card" href="/release-date/"><b>Release date</b><span>22 July 2026, and the two delays that came before it.</span></a>
    <a class="card" href="/tools/"><b>Tools</b><span>Crossplay checker, achievement tracker and threat lookup &mdash; all running in your browser.</span></a>
    <a class="card" href="/employee-package/"><b>Secrets &amp; lore</b><span>What the Employee Package actually is, and who writes the Joe&rsquo;s Diner newsletter.</span></a>
    <a class="card" href="/faq/"><b>FAQ</b><span>Short answers to the most-searched questions, each linking to the long one.</span></a>
    <a class="card" href="/system-requirements/"><b>System requirements</b><span>Both Steam spec tiers field for field, the Steam Deck rating and where it comes from, and what the Xbox listing adds.</span></a>
    <a class="card" href="/demo/"><b>The free demo</b><span>Three pre-scripted shifts against 13 generated ones &mdash; and the free itch.io build this game grew out of.</span></a>
    <a class="card" href="/troubleshooting/"><b>Troubleshooting</b><span>Lobby errors, crashes, black screens and no audio: which have official fixes, and which honestly do not.</span></a>
    <a class="card" href="/player-count/"><b>Player count</b><span>Is anyone still playing? The Steam numbers, why the trackers disagree, and the figure we will not repeat.</span></a>
  </div>

  <h2>How this wiki handles sources</h2>
  <p>Specific numbers &mdash; unlock rates, patch dates, lobby caps, the cash threshold on the true ending &mdash; carry a link to where they came from, with the date they were read. Where only one outlet has reported something, the page says so rather than laundering it into fact. And where there is no source at all, there is no page: no night-by-night walkthrough table, no Rake health values, no weapon damage numbers, no Metacritic average, because none of those exist yet. That is why this wiki is shorter than its competitors in a few places, and why the parts that are here can be checked.</p>
"""},
{
 "path": "guide/beginners", "active": "/guides/",
 "published": "2026-08-05",   # 保留改日期行之前的 datePublished(D2 2026-10-10)
 "updated": "Last updated 2026-10-10 &middot; the crossplay sentence, the patience section re-checked 10 October 2026 against the official Steam announcements &middot; rest of the page last verified 5 August 2026 (29 July 2026 patch) and not re-checked against the 20 August and 1 September 2026 patches (see the updates page)",
 "title": "Shift At Midnight Beginner's Guide — Surviving Your First Shifts",
 "og_short": "Shift At Midnight Beginner's Guide",
 "desc": "A beginner's guide to Shift At Midnight that starts with the mistake [[ACH:First Blood]]% of players make: treating the ID scanner as a threat detector.",
 "trail": G + [(None, "Beginner's guide")],
 "h1": "Beginner's guide",
 "lede": "The fastest way to understand this game is to understand one number: <strong>[[ACH:First Blood]]% of all players have killed a customer</strong>. That is the most common achievement in the game. It is not a badge of skill &mdash; it is the game documenting a mistake almost everyone makes.",
 "body": """
  <h2>What the patch notes say about patience</h2>
  <p>The 29 July 2026 announcement says &ldquo;Removed patience in ENDLESS MODE / POST-STORY MODE&rdquo; and the 1 September 2026 announcement says &ldquo;Re-enabled patience for ENDLESS MODE&rdquo;. Neither line mentions Story Mode, and no official announcement says whether Story Mode customers still run down a patience timer. See <a href="/updates/">updates</a>.</p>
  <p>The opening strategy for a new player: <strong>scan everything, read the
    description box, and search the N.E.T. database on anyone who feels off.</strong> The cost of being wrong
    is a hunt. See the
    <a href="/guide/doppelgangers/">identification guide</a> for what to actually look at.</p>

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
  <p>The cliff is at <em>Relentless</em> ([[ACH:Relentless]]%) and <a href="/monsters/marionette/">Last Performance</a> ([[ACH:Last Performance]]%). Those need you to know something in advance. Everything below them needs deliberate effort. See <a href="/achievements/">the full list</a>.</p>

  <h2>Money</h2>
  <p>You will want to spend everything on restocking, because the quota is immediate and the arsenal is not. Resist a little. <em>Locked And Loaded</em> &mdash; purchasing every melee weapon &mdash; sits at [[ACH:Locked And Loaded]]%, and the reason it is that low is that people spend their earnings shift-to-shift and never bank. See the <a href="/guide/survival/#weapons">weapons guide</a>.</p>

  <h2>If you are playing with friends</h2>
  <p>Check <a href="/crossplay/">the crossplay page before anyone buys</a>. Per the developer (10 July 2026), Steam players will only be able to play with other Steam players.</p>

  <div class="grid two">
    <a class="card" href="/guide/doppelgangers/"><b>Doppelganger identification</b><span>The actual tells, once you know the scanner is not one.</span></a>
    <a class="card danger" href="/monsters/"><b>Bestiary</b><span>Know what is coming before it arrives.</span></a>
  </div>
"""},
{
 "path": "guide/doppelgangers", "active": "/guides/",
 "published": "2026-08-05",   # 保留改日期行之前的 datePublished(D2b 2026-10-10)
 "updated": "Last updated 2026-10-10 &middot; patience statements and the doppelganger count note re-checked 10 October 2026 against the official Steam announcements &middot; rest of the page last verified 5 August 2026 (29 July 2026 patch) and not re-checked against the 20 August and 1 September 2026 patches (see the updates page)",
 "title": "Shift At Midnight Doppelgangers — How to Identify Them",
 "og_short": "Shift At Midnight Doppelgangers",
 "desc": "The seven categories of tell, what the N.E.T. database does that the ID scanner cannot, the document checks worth running, and what the patch notes say about patience.",
 "trail": G + [(None, "Doppelgangers")],
 "h1": "Identifying doppelgangers",
 "lede": "This is the job. Something walks in wearing a real person &mdash; face, voice, mannerisms, biography &mdash; and you have a scanner, a database and your own attention. The 29 July 2026 announcement says &ldquo;Removed patience in ENDLESS MODE / POST-STORY MODE&rdquo; and the 1 September 2026 announcement says &ldquo;Re-enabled patience for ENDLESS MODE&rdquo;; neither line mentions Story Mode, so do not assume customers will wait forever.",
 "body": """
  <div class="term warn">
    <div class="term-h">Why this outranks every other skill</div>
    <p>Let a doppelganger finish its purchase and walk out and <strong>it comes back that same night in monster form to hunt you</strong> (<a href="https://gamerant.com/shift-at-midnight-all-monsters/" target="_blank" rel="noopener">Game Rant</a>). Most hunts on the <a href="/guide/survival/">survival page</a> were created here, at the counter, minutes earlier.</p>
  </div>

  <p>The opposite error is cheaper but not free: killing a real customer unlocks <em>First Blood</em>, held by <strong>[[ACH:First Blood]]% of players</strong>. It is the most common achievement in the game, which tells you how hard this call is and how little the game expects perfection.</p>

  <h2>What you have to work with</h2>
  <ul>
    <li><strong>The ID scan.</strong> Run the card and the computer answers exactly one question: is this document what it claims to be?</li>
    <li><strong>The N.E.T. database, searched by hand.</strong> You do not need a document to look someone up; you can type a name in yourself. Most new players never touch it, and it is what catches a good forgery.</li>
    <li><strong>The description box on each file.</strong> Registered appearance, occupation, personal details and shopping habits &mdash; there so you can contradict the person in front of you.</li>
    <li><strong>The Anomaly Lens.</strong></li>
    <li><strong>Vehicle and plate records</strong> once unlocked &mdash; the only check that concerns something outside the building.</li>
  </ul>

  <h2>The seven categories of tell</h2>
  <ol>
    <li><strong>Name or personal details do not match the ID.</strong> The strongest version is the database reporting that the real person is <em>dead</em> &mdash; conclusive even when nothing about the customer looks wrong.</li>
    <li><strong>Stated occupation contradicts the record.</strong> Ask what they do, then read what the file says they do.</li>
    <li><strong>Habits and personal details do not line up.</strong> Compare the purchase habits in the file against what is on the counter.</li>
    <li><strong>Appearance or clothing contradicts the file.</strong> Build, features, what the photo shows versus what is standing there.</li>
    <li><strong>Behaviour is abnormal.</strong> The vaguest category, and the one that improves fastest with practice: you cannot see abnormal until you have watched a lot of normal.</li>
    <li><strong>The emotion readout does not match the words.</strong> A reading that contradicts what the person is saying or doing is a tell on its own.</li>
    <li><strong>The plate does not match the vehicle&rsquo;s registered owner.</strong> A later unlock, and the one check that happens away from the till.</li>
  </ol>
  <p class="src">Categories and systems: <a href="https://www.thegamer.com/shift-at-midnight-spot-doppelganger-guide/" target="_blank" rel="noopener">TheGamer</a>.</p>

  <h2>Work the document first</h2>
  <p><a href="https://www.destructoid.com/all-shift-at-midnight-doppelgangers-and-how-to-identify-them/" target="_blank" rel="noopener">Destructoid</a>&rsquo;s checks come first because they cost seconds:</p>
  <ul>
    <li><strong>Does the ID have a barcode at all?</strong> Some do not. That is the fastest fail available to you.</li>
    <li><strong>Put passports and driving licences through the computer</strong> instead of eyeballing them.</li>
    <li><strong>Interrogate against the document.</strong> Ask date of birth, ask occupation, and compare the photo with the person &mdash; Destructoid singles out <strong>scar placement</strong> as the detail that catches copies.</li>
  </ul>
  <p>The principle underneath all of it: a doppelganger has copied a person, not that person&rsquo;s paperwork. Anywhere the two are supposed to agree is a seam.</p>

  <h2>What the tells look like in practice</h2>
  <p><a href="https://www.dualshockers.com/shift-at-midnight-all-doppelgangers/" target="_blank" rel="noopener">DualShockers has documented 47 named doppelgangers</a>, each with its own tell (its count when we read it for the 5 August 2026 version of this page). That count predates two official patches: the 20 August 2026 announcement says &ldquo;15 new customers added to STORY MODE and ENDLESS MODE&rdquo; and the 1 September 2026 announcement says &ldquo;30 NEW CUSTOMERS added to STORY MODE and ENDLESS MODE&rdquo;. Neither says how many of them are doppelgangers, so the current total is not confirmed. Five, to show the range:</p>
  <ul>
    <li><strong>Nathan Calloway</strong> &mdash; the database says the real Nathan is dead.</li>
    <li><strong>Natasha Lin</strong> &mdash; describes working a morning shift at a place that only opens at night.</li>
    <li><strong>Agnes Wells</strong> &mdash; the real Agnes Wells is three years old.</li>
    <li><strong>Ray Rowland</strong> &mdash; his neck is far too long.</li>
    <li><strong>Net Pongsak</strong> &mdash; he is floating.</li>
  </ul>
  <p>Two are database contradictions you would never see by looking; two would never be flagged by any scan; one is a man hovering above your floor. No single check covers that spread &mdash; layer them.</p>

  <h2>Not all of them queue at the counter</h2>
  <p>Destructoid also names forms that never present a document: a spider-like one, an employee shape with abnormally long limbs, a chameleon type <strong>blended into a storage-room wall</strong>, a duplicate of Sheriff Clyde, corpse forms and infant forms. We have not independently verified each. The consequence is the same either way &mdash; a scanner at the till cannot find something standing in your stockroom, so somebody has to walk the aisles.</p>

  <h2>Norbert: the flag that means nothing</h2>
  <p>Norbert is a customer-type doppelganger, described by DualShockers as a magical, annoying gnome. His ID scans as fake and the system flags him as a Doppelganger. Both readings are correct, and both are a red herring.</p>
  <ul>
    <li><strong>Let him go</strong> and he completes his purchase, leaves, and does not reappear for the rest of the shift.</li>
    <li><strong>Kill him</strong> and he returns in different disguises &mdash; a poisoned lemonade stand, a motorcycle stunt, dressed as a girl &mdash; playing pranks rather than attacking lethally.</li>
  </ul>
  <p><em>Single source, not independently confirmed:</em> the behaviour after killing him is reported only by <a href="https://allthings.how/shift-at-midnight-what-sparing-norbert-does-to-your-shift/" target="_blank" rel="noopener">AllThings.How</a>. The lesson holds either way &mdash; <strong>the flag tells you a document is wrong, not what the holder is going to do.</strong> More on <a href="/monsters/norbert/">Norbert</a>.</p>

  <h2>What the patch notes say about patience</h2>
  <p>The 29 July 2026 announcement says &ldquo;Removed patience in ENDLESS MODE / POST-STORY MODE&rdquo; and the 1 September 2026 announcement says &ldquo;Re-enabled patience for ENDLESS MODE&rdquo;. Neither line mentions Story Mode, and no official announcement says whether Story Mode customers still run down a patience timer. See <a href="/updates/">patch notes</a>.</p>

  <h2>With two or three players</h2>
  <p>Split roles instead of crowding the till: one on the scanner and database, one watching the aisles for the things that never come to the counter, one keeping the store running so the shift does not fail on numbers. Proximity chat lets the floor watcher speak quietly without the counter breaking eye contact. See <a href="/multiplayer/#co-op">co-op roles</a>.</p>

  <h2>What this page leaves out</h2>
  <p>The full DualShockers list of names, because reading them in advance replaces the game with a lookup table. And any schedule of who turns up on which night: customers and events are <a href="/nights-and-levels/">procedurally generated</a>, so such a list describes one playthrough, not the game.</p>

  <div class="grid two">
    <a class="card" href="/guide/survival/"><b>Survival &amp; weapons</b><span>For when this page has already failed and something is loose in the building.</span></a>
    <a class="card danger" href="/monsters/"><b>Bestiary</b><span>What comes back after you wave one through.</span></a>
  </div>
"""},
{
 "path": "guide/survival", "active": "/guides/",
 "published": "2026-08-05",   # 保留改日期行之前的 datePublished(D2b 2026-10-10)
 "updated": "Last updated 2026-10-10 &middot; the Chainsaw / Locked And Loaded statement re-checked 10 October 2026 against the 1 September 2026 Steam announcement &middot; rest of the page last verified 5 August 2026 (29 July 2026 patch) and not re-checked against the 20 August and 1 September 2026 patches (see the updates page)",
 "title": "Shift At Midnight Survival Guide — Traps, Barricades &amp; Hiding",
 "og_short": "Shift At Midnight Survival Guide",
 "desc": "When identification has failed and something is loose in the store: sound discipline, barricading, trap placement, and how each of the six threats has to be handled differently.",
 "trail": G + [(None, "Survival")],
 "h1": "Traps, barricades &amp; hiding",
 "lede": "This is the toolkit for after the counter has failed. Something is loose in the building, the shift is still running, and the store has to survive until dawn.",
 "body": """
  <div class="term warn">
    <div class="term-h">The exception, stated first</div>
    <p>None of this works on <a href="/monsters/the-dentist/">the Dentist</a>, who arrives on <strong>Shift 13</strong>: immune to your weapons, and traps do not stop him. The only published route through that encounter is to run at Sheriff Clyde without hiding and without looking back, until the cutscene takes over. <em>Single source, not independently confirmed.</em></p>
  </div>

  <h2>Hunts are something you caused</h2>
  <p>They are not weather. Let a doppelganger complete its purchase and walk out and <strong>it returns that same night as a monster</strong> (<a href="https://gamerant.com/shift-at-midnight-all-monsters/" target="_blank" rel="noopener">Game Rant</a>), so everything below is the bill for a decision made at the counter &mdash; see <a href="/guide/doppelgangers/">identifying doppelgangers</a>. <em>Still Breathing</em>, for surviving your first hunt, sits at <strong>[[ACH:Still Breathing]]%</strong>; <em>Relentless</em>, for finishing one inside 30 seconds, sits at <strong>[[ACH:Relentless]]%</strong>. That gap is this page&rsquo;s subject: surviving is normal, ending it fast is a plan.</p>

  <h2>Sound is the first thing to control</h2>
  <p>Noise gives away your position, so silence is a defensive tool before any barricade is &mdash; and a gun is the loudest thing you own, which is why a <a href="/monsters/shrieking-doll/">Shrieking Doll</a> shot at the wrong moment can cost more than it saves. <em>Both points are single-sourced and not independently confirmed.</em> Sound works for you too: since the <a href="https://steamdb.info/patchnotes/24354120/" target="_blank" rel="noopener">23 July patch</a> the <a href="/monsters/jack-in-the-box/">Jack-in-the-Box</a> is much louder, turning the search for it into a listening problem, and in Endless Mode a screaming customer means a Rake has spawned.</p>

  <h2>Barricades, traps and hiding</h2>
  <p><strong>Barricades</strong> buy time and shape movement. The station is small with few ways through it, so the right door does not just delay a threat &mdash; it forces it onto a path you chose. Barricading reactively into a room with one exit converts a chase into a corner: block to redirect, not to hide behind.</p>
  <p><strong>Traps</strong> are prediction: they pay off where a threat has to go, not where it happens to be, so the value comes from knowing the chokepoints before the night turns bad. Laying them mid-chase is useless. They are also the only published answer to a <a href="/monsters/demented/">Demented</a>, which cannot be shot down.</p>
  <p><strong>Hiding</strong> is a reset, not a solution: it breaks contact so you can get back to a shift that is still running. The quota does not pause because you are under a counter.</p>

  <h2>They do not all want the same thing</h2>
  <ul>
    <li><strong>Entities</strong> &mdash; the default hunters, and what you get for letting a doppelganger leave. Barricades, traps and weapons all work; they get harder as the run goes on.</li>
    <li><strong><a href="/monsters/shrieking-doll/">Shrieking Doll</a></strong> &mdash; small, crawls low, finds you by line of sight, dies to a few shots. An interruption rather than a threat, but a noisy one to remove. <em>Single source.</em></li>
    <li><strong><a href="/monsters/demented/">Demented</a></strong> &mdash; cannot move while you look straight at it. Hold the stare, back it toward a trap, then break eye contact. Not rare, whatever you have read: <strong>[[ACH:Freed]]%</strong> of players have killed one.</li>
    <li><strong><a href="/monsters/marionette/">Marionette</a></strong> &mdash; from <strong>Shift 9</strong> onward, flagged in advance by a N.E.T. email. When the music box starts, find it and <strong>hold E to rewind before the melody plays three times</strong>; it appears in the break room, a storage room, the bathroom or a shelf aisle. It can be killed, and the 23 July HP cut makes that a real option with a stocked arsenal and a second player.</li>
    <li><strong>Rakes</strong> &mdash; Endless and post-story only. They come out of the forest and go for your customers rather than you: follow the screaming, look for red light at the treeline, kill it before it reaches the building. <em>Beyond &ldquo;they exist and emerge from the forests&rdquo;, single-sourced.</em> See <a href="/nights-and-levels/#endless-mode">Endless Mode</a>.</li>
    <li><strong><a href="/monsters/the-dentist/">The Dentist</a></strong> &mdash; see the top of this page.</li>
  </ul>

  <div class="term tip">
    <div class="term-h">Learn the layout on a quiet night</div>
    <p>Every skill here depends on knowing the building: which aisles connect, where the loops are, which corners are dead ends. Map knowledge is the one asset that works against everything, including the entity you cannot fight.</p>
  </div>

  <p>Everything above is about not needing to shoot. The rest is what you can buy for when you do.</p>
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
  <p>No official post describes roles for co-op. The split below is our own suggestion, not an official system and not something we can source. It assumes the three players the developer says the game &ldquo;is designed and has always been marketed around&rdquo;.</p>

  <div class="tablewrap">
  <table class="data">
    <thead><tr><th>Role</th><th>Main job</th><th>Rule to hold</th></tr></thead>
    <tbody>
      <tr><td><strong>Counter</strong></td><td>Serves customers and runs the <a href="/guide/doppelgangers/">scanner and database</a></td><td>Does not leave for noises</td></tr>
      <tr><td><strong>Floor</strong></td><td>Watches behaviour, restocks, spots what the scanner misses</td><td>Calls out anyone <a href="/monsters/norbert/">stepping around the counter</a></td></tr>
      <tr><td><strong>Response</strong></td><td>Carries the weapon and handles hunts</td><td>Owns time-critical objects</td></tr>
    </tbody>
  </table>
  </div>

  <p>On a <a href="/monsters/marionette/">Marionette</a> night, according to our <a href="/monsters/jack-in-the-box/">Jack-in-the-Box page</a>, which cites Game Rant&rsquo;s music box guide, three complete melodies from the wind-up music box summon the Marionette, and holding E to rewind the box before that third pass stops the encounter. That page also suggests giving one player the box for the whole encounter; in the split above, also our suggestion, that is the Response role.</p>
"""},
{
 "path": "guide/weapons", "active": "/guides/",
 "title": "Shift At Midnight Weapons — Arsenal &amp; Locked And Loaded",
 "og_short": "Shift At Midnight Weapons Guide",
 "desc": "Buying every melee weapon unlocks Locked And Loaded, held by only [[ACH:Locked And Loaded]]% of players. Why it is low, how to bank for it, and what weapons cannot solve.",
 "trail": G + [(None, "Weapons")],
 "h1": "Weapons arsenal",
 "lede": "Purchasing every melee weapon and filling out the arsenal unlocks <strong>Locked And Loaded</strong> &mdash; held by only <strong>[[ACH:Locked And Loaded]]%</strong> of players. It is not a difficulty problem. It is a budgeting problem.",
 "body": """
  <div class="tags">
    <span class="tag amber">Achievement: Locked And Loaded</span>
    <span class="tag">[[ACH:Locked And Loaded]]% of players</span>
  </div>

  <h2>Melee is the achievement; the guns are insurance</h2>
  <p><em>Locked And Loaded</em> is specific: <strong>purchase all melee weapons and fill out the weapons arsenal</strong>. At <strong>[[ACH:Locked And Loaded]]%</strong> it is a budgeting problem, not a difficulty one: restocking pays tonight, the arsenal pays on a night that may never come, and under pressure people buy the immediate thing. Decide early that a fixed slice of each shift&rsquo;s takings is untouchable.</p>
  <p>Firearms sit outside that achievement, and there are now two of them: the <a href="https://store.steampowered.com/news/app/3722330/view/695394018676179340" target="_blank" rel="noopener">29 July patch</a> added a second purchasable gun alongside the one the game shipped with. They are also the loudest tools you own, which is the argument for melee on a night you would rather not be found &mdash; see sound discipline above. Full change list: <a href="/updates/">patch notes</a>.</p>

  <h2>Have it equipped before the hunt</h2>
  <p>Buy and equip before a hunt starts, not during one: <em>Relentless</em> &mdash; finish a hunt within 30 seconds, <strong>[[ACH:Relentless]]%</strong> &mdash; is close to impossible if the first ten seconds go on shopping. The target to attempt it on is a <a href="/monsters/shrieking-doll/">Shrieking Doll</a>, which comes to you rather than hiding. Never on a <a href="/monsters/the-dentist/">Dentist</a> night, which cannot be won at all.</p>

  <h2>What a weapon does not solve</h2>
  <ul>
    <li><strong>The Dentist.</strong> No weapon works. Running is the entire answer.</li>
    <li><strong>Doppelgangers.</strong> The problem is identification, not damage &mdash; a weapon applied to the wrong customer is the [[ACH:First Blood]]% achievement. See <a href="/guide/doppelgangers/">identifying doppelgangers</a>.</li>
    <li><strong>An unwound music box.</strong> Whether you fight a <a href="/monsters/marionette/">Marionette</a> at all is settled by the <a href="/monsters/jack-in-the-box/">box</a>, not your loadout. A weapon helps once the fight starts &mdash; the 23 July patch cut its HP &mdash; but arriving armed does not substitute for winding.</li>
  </ul>

  <p>We do not publish a weapon tier list, damage values or per-monster recommendations. The developer has named one melee weapon, the Chainsaw (&ldquo;now required for the LOCKED AND LOADED achievement&rdquo;, 1 September 2026 announcement); the rest of the list and the prices are not published, and the confident numbers circulating for this game are unsourced.</p>

  <div class="grid two">
    <a class="card" href="/achievements/"><b>All achievements</b><span>Where Locked And Loaded sits in the completion curve.</span></a>
    <a class="card" href="/guide/beginners/#store-management"><b>Quotas &amp; money</b><span>Where the budget for all of this comes from.</span></a>
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
    <p>It puts a player in the aisles with a reason to be looking around &mdash; which is exactly where behavioural anomalies get spotted. The <a href="/multiplayer/#co-op">floor role</a> restocks and watches at the same time.</p>
  </div>

  <h2>Queue pressure is the design</h2>
  <p>A queue creates time pressure on the one decision the game cares about: is this person human? Rushing produces the [[ACH:First Blood]]% outcome &mdash; killing a customer &mdash; or the opposite error of waving through something you should have caught. The queue is not an obstacle to the horror; it is the mechanism that generates it.</p>

  <h2>Budgeting</h2>
  <p>Money splits between restocking (immediate, keeps quota healthy) and the <a href="/guide/survival/#weapons">weapons arsenal</a> (deferred, and its own [[ACH:Locked And Loaded]]% achievement). Bank a fixed slice every shift rather than deciding to chase the arsenal later.</p>

  <div class="grid two">
    <a class="card" href="/guide/survival/#weapons"><b>Weapons arsenal</b><span>The other half of the budget.</span></a>
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
  <p>Three achievements are hidden and rare: <em>Grave Decision</em> ([[ACH:Grave Decision]]%), <em>True Ending</em> (16.0%) and <em>Empty Home</em> ([[ACH:Empty Home]]%). They are three separate endings, not milestones on one path. Full discussion on <a href="/endings/">the endings page</a>, with fact and inference clearly separated.</p>
  <p>Because shifts are procedural but endings are rare, the likely lever is <em>how you played</em> rather than <em>which nights you got</em> &mdash; the run-level decisions, not the seed.</p>

  <h2>Solo or co-op</h2>
  <p>Story Mode works either way. Solo gives you full control of every judgement call, which matters if you are hunting the hidden achievements &mdash; nobody else kills a customer you were still assessing.</p>

  <div class="grid two">
    <a class="card" href="/endings/"><b>All endings</b><span>What the hidden achievements imply.</span></a>
    <a class="card" href="/nights-and-levels/#endless-mode"><b>Endless Mode</b><span>The free Q4 2026 update.</span></a>
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
    <tr><th>Beta</th><td>In the game since launch day, 22 July 2026 &mdash; unlocks after Story Mode</td></tr>
    <tr><th>Full version</th><td>Free update planned for Q4 2026</td></tr>
    <tr><th>Cost</th><td>Free &mdash; both the beta and the update</td></tr>
    <tr><th>Source</th><td>Official store listing and the developer&rsquo;s site</td></tr>
  </table>

  <p><strong>The beta is already in the game</strong>, and this is the thing most pages get wrong. It shipped
    on launch day and unlocks once the 13-shift story is finished &mdash; the developer&rsquo;s own site
    describes it as &ldquo;infinite nights, only unlockable after completing story mode&rdquo; and calls it
    &ldquo;an unfinished gamemode, hence the beta&rdquo;, with continuous updates promised over time. What is
    scheduled for Q4 2026 is the <em>finished</em> version of that mode, not its first appearance. It is also
    the only mode where Rakes appear &mdash; see the section above.</p>

  <div class="term warn">
    <div class="term-h">What is not confirmed</div>
    <p>Steam crossplay is <strong>not</strong> on any roadmap we can verify, and neither is official mod support or an additional platform. If you have read otherwise, check whether the claim has a source attached &mdash; a lot of it does not. See <a href="/crossplay/">crossplay</a> and <a href="/mods/">mods</a>.</p>
  </div>

  <h2>Why an endless mode makes sense here</h2>
  <p>The core loop &mdash; a shift, a quota, customers who may not be customers &mdash; is naturally repeatable, and <a href="/nights-and-levels/#story-mode">shifts are already procedurally generated</a>. An endless variant is a small step from what exists: remove the narrative frame and let shifts continue until you fail.</p>
  <p>It also addresses the achievement curve. The bottom four achievements need deliberate attempts, and an endless mode gives you a place to farm attempts without restarting a story run.</p>

  <h2>What we will do when the full version ships</h2>
  <p>Update this page with the actual patch notes and date, and revise the <a href="/achievements/">achievements page</a> if the update adds any. What is in the game today is the beta; we are not going to pre-write speculative content for the parts of the finished mode that have not shipped.</p>

  <div class="grid two">
    <a class="card" href="/nights-and-levels/#story-mode"><b>Story Mode</b><span>The structure Endless Mode is derived from.</span></a>
    <a class="card" href="/release-date/"><b>Release &amp; platforms</b><span>Where the game is available now.</span></a>
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
    <tr><th>Price</th><td>$9.99 USD (10% launch discount ended 29 July 2026)</td></tr>
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
  <p>If anyone in your group has Game Pass, the game is free for them, and it launched there day one on both console and PC. For a $9.99 co-op game, "one of us already has it included" often decides the whole platform question. See <a href="/platforms/#game-pass">Game Pass &amp; Play Anywhere</a>.</p>

  <h2>Play Anywhere</h2>
  <p>One Microsoft Store purchase covers both the Xbox console and Windows versions, with shared saves. If you want to play on a console and a PC, that is the version that does it in one purchase.</p>

  <div class="grid two">
    <a class="card" href="/crossplay/"><b>Crossplay</b><span>Read before buying.</span></a>
    <a class="card" href="/review/#price"><b>Price</b><span>What it costs and whether that matters.</span></a>
  </div>
"""},
{
 "path": "multiplayer", "active": "/guides/", "published": "2026-08-05",
 "title": "Shift At Midnight Multiplayer — Player Count &amp; Crossplay",
 "og_short": "Shift At Midnight Multiplayer",
 "desc": "Shift At Midnight supports up to 3 players in online co-op with proximity chat. Platform compatibility is the thing that stops most groups playing together.",
 "trail": [(None, "Multiplayer")],
 "h1": "Multiplayer",
 "lede": "<strong>Up to three players</strong>, online co-op, with <strong>proximity chat</strong>. There is also a full single-player mode. The thing that most often stops a group playing together is not the player cap &mdash; it is which store they bought it from.",
 "updated": "Last verified 10 October 2026 &middot; game version: 1 September 2026 patch",
 "body": """
  <table class="facts">
    <tr><th>Players</th><td>1 to 3 by design; lobbies up to 6 since 23 July 2026</td></tr>
    <tr><th>Co-op type</th><td>Online co-op (Steam store category)</td></tr>
    <tr><th>Local or split-screen</th><td>Not listed on the Steam store page</td></tr>
    <tr><th>Remote Play Together</th><td>Not listed on the Steam store page</td></tr>
    <tr><th>Voice</th><td>Proximity chat, built in</td></tr>
    <tr><th>Single-player</th><td>Yes</td></tr>
  </table>

  <h2>How many players can join one lobby?</h2>
  <p>Three is the designed size. The Steam store page describes the game as &ldquo;An online co-op detective horror for up to 3 players&rdquo;, and the launch post says &ldquo;Play solo or with up to 2 extra friends&rdquo;. One day after launch, the 23 July 2026 patch let the host pick a higher cap. The changelog reads: &ldquo;When creating a lobby, you can now select a max player count of 6 players.&rdquo;</p>

  <div class="tablewrap">
  <table class="data">
    <thead><tr><th>Lobby size</th><th>Supported?</th><th>What the developer says</th></tr></thead>
    <tbody>
      <tr><td><strong>1 (solo)</strong></td><td>Yes</td><td>Listed as Single-player on Steam</td></tr>
      <tr><td><strong>2&ndash;3</strong></td><td>Yes</td><td>The size the game is designed around</td></tr>
      <tr><td><strong>4&ndash;6</strong></td><td>Yes, host option</td><td>Outside the intended design; not for a first playthrough</td></tr>
      <tr><td><strong>7 or more</strong></td><td>Not stated</td><td>The patch note names 6 as the selectable maximum and says nothing above it; see <a href="/mods/">mods</a></td></tr>
    </tbody>
  </table>
  </div>

  <p>Bun Muen was blunt about the six-player option in that same patch note. The game &ldquo;is designed and has always been marketed around a maximum of 3 players&rdquo;, and a bigger lobby &ldquo;will likely become too chaotic, and is not recommended for your first playthrough&rdquo;. The changelog was posted on Steam, and we could not confirm the option on the Xbox versions (checked 10 October 2026).</p>

  <h2>How do you host a game with friends?</h2>
  <p>The host creates a lobby from the game and chooses the maximum player count at that point. That much is stated in the 23 July 2026 patch note. No official post documents the invite steps or menu names, so we do not list them here. Our <a href="/troubleshooting/">troubleshooting page</a> covers what to check when a friend cannot see or join your lobby.</p>
  <p>Two official statements matter before anyone tries to join. On stores, the developer&rsquo;s 10 July 2026 announcement says Steam players will only be able to play with other Steam players, and that Xbox and PC Game Pass players will have crossplay. We have not tested either, and the <a href="/crossplay/">crossplay page</a> sets out what is on the record. On branches, the launch-day &ldquo;network-issues-patch&rdquo; beta fix came with this instruction: &ldquo;Everyone you play with must also follow these instructions&rdquo;.</p>
  <p>A Steam-only public server browser was announced on 10 July 2026 for launch or shortly after. No later changelog mentions it shipping, so its status is not confirmed as of 10 October 2026.</p>

  <h2>How does voice chat work?</h2>
  <p>The game has built-in proximity chat. The store page puts it plainly: &ldquo;proximity chat enhances the experience&rdquo;, and the 22 July 2026 launch post lists &ldquo;proximity chat&rdquo; among the things to expect. The 20 August 2026 patch added individual volume sliders for each player. The 23 July 2026 patch also removed the profanity filter.</p>

  <h2>Can you try co-op before buying?</h2>
  <p>Yes. A free &ldquo;Shift At Midnight Multiplayer Demo&rdquo; has been on Steam since 29 September 2025, and Steam lists it as Online Co-op. It is a separate app from the full game, and Steam lists it as free. Our <a href="/demo/">demo page</a> lists what it includes.</p>

  <h2>Is solo worth playing?</h2>
  <p>Solo is an officially supported way to play. Steam lists the game under Single-player as well as Online Co-op, and the launch post says &ldquo;Play solo or with up to 2 extra friends&rdquo;. The store page does lean toward groups, saying &ldquo;Multiplayer is where the game thrives&rdquo;. No official statement compares how solo and co-op play, so we do not rank them. If you are playing alone for the story, the <a href="/endings/">endings page</a> sets out the three outcomes. For live numbers on how many people are playing, see <a href="/player-count/">player count</a>.</p>
"""},
{
 "path": "game-pass", "active": "/guides/",
 "title": "Is Shift At Midnight on Game Pass? Yes — Day One, Play Anywhere",
 "og_short": "Shift At Midnight on Game Pass",
 "desc": "Shift At Midnight launched day one on Xbox Game Pass for console and PC, and is an Xbox Play Anywhere title. What that gets you versus buying on Steam.",
 "trail": [(None, "Game Pass")],
 "h1": "Shift At Midnight on Game Pass",
 "lede": "<strong>Yes &mdash; day one, on both Xbox console and PC.</strong> It is also an Xbox Play Anywhere title, which means one Microsoft Store purchase covers the Xbox and Windows versions. That detail is also why the crossplay situation is what it is.",
 "updated": "Last verified 10 October 2026 &middot; game version: 1 September 2026 patch",
 "body": """
  <p><strong>Yes at launch.</strong> The launch announcement on 22 July 2026 reads &ldquo;OUT NOW on Steam, Xbox &amp; Game Pass&rdquo;, and the earlier release-date post names &ldquo;Xbox PC Gamepass&rdquo; as well. The Xbox store listing showed the game as included with PC Game Pass and Xbox Game Pass Ultimate when it was last verified on 12 August 2026 against that listing. That listing was not re-checked on 10 October 2026.</p>

  <table class="facts">
    <tr><th>On Game Pass at launch</th><td>Yes &mdash; 22 July 2026</td></tr>
    <tr><th>Versions named by the developer</th><td>Xbox and Xbox PC Game Pass</td></tr>
    <tr><th>In the catalogue</th><td>Included with PC Game Pass and Xbox Game Pass Ultimate, last verified 12 August 2026 against the Xbox store listing; not re-checked on 10 October 2026</td></tr>
    <tr><th>Xbox price</th><td>$9.99, last verified 12 August 2026 against the Xbox store listing; not re-checked on 10 October 2026</td></tr>
    <tr><th>Steam price for comparison</th><td>$9.99 USD (10 October 2026)</td></tr>
    <tr><th>Crossplay, per the developer</th><td>&ldquo;Xbox and PC Gamepass players will have crossplay&rdquo; (10 July 2026); not tested by us</td></tr>
  </table>

  <p>The last row quotes the 10 July 2026 release-date announcement. The same announcement says &ldquo;Steam players will only be able to play with other Steam players.&rdquo; The <a href="/crossplay/">crossplay page</a> has the full matrix, and <a href="/multiplayer/">multiplayer</a> explains how lobbies work once you are on the same side.</p>
"""},
{
 "path": "price", "active": "/guides/",
 "title": "Shift At Midnight Price — $9.99 and Whether to Buy It",
 "og_short": "Shift At Midnight Price",
 "desc": "Shift At Midnight is $9.99 USD with a 10% launch discount, and free on Game Pass. Which platform you buy on matters more than the price does.",
 "trail": [(None, "Price")],
 "h1": "Price &amp; editions",
 "lede": "<strong>$9.99 USD</strong> on Steam, with no discount on 10 October 2026. It was announced for Xbox PC Game Pass at launch; current catalogue status was not re-checked. There is one edition. The decision that actually costs people money is not the price &mdash; it is the store.",
 "body": """
  <table class="facts">
    <tr><th>Price</th><td>$9.99 USD (regional pricing varies)</td></tr>
    <tr><th>Launch discount</th><td>Announced by the developer on 8 June 2026; the end date is not stated in any official announcement. No discount on Steam on 10 October 2026</td></tr>
    <tr><th>Editions</th><td>One &mdash; no deluxe or season pass</td></tr>
    <tr><th>Game Pass</th><td>On Game Pass at launch, per the developer (22 July 2026); current catalogue status not re-checked on 10 October 2026</td></tr>
    <tr><th>Future content</th><td>Endless Mode, Q4 2026 &mdash; free</td></tr>
  </table>

  <div class="term warn">
    <div class="term-h">The expensive mistake is not the price</div>
    <p>It is buying on the wrong store. <strong>Per the developer, Steam players will only play with other Steam players.</strong> Which pool a Microsoft Store copy joins is not confirmed by any official statement. Decide as a group first &mdash; <a href="/crossplay/">crossplay</a>.</p>
  </div>

  <h2>No paid DLC announced</h2>
  <p>The only content on the roadmap is Endless Mode in Q4 2026, and it is <strong>free</strong>. No season pass, no deluxe edition, no paid cosmetics have been announced. For a $9.99 game from a solo developer, what you buy is what there is.</p>

  <h2>Is it worth $9.99?</h2>
  <p>The honest framing: this is a three-player co-op horror game with ten achievements and a procedural shift structure. The achievement curve suggests most players get several hours in &mdash; [[ACH:Relentless]]% reach <em>Relentless</em>, which is not a first-session achievement &mdash; and a meaningful minority push into the rare hidden endings at 10&ndash;16%. See <a href="/review/">is it worth it</a>.</p>
  <p>If you already play it through Game Pass the question does not arise. If you do not, and you have two friends who will play it with you, $9.99 for a co-op night is not a hard sell. If you are buying it to play alone, it is a smaller game than the store page implies.</p>

  <div class="grid two">
    <a class="card" href="/platforms/#game-pass"><b>Game Pass</b><span>What the developer and the Xbox listing say.</span></a>
    <a class="card" href="/review/"><b>Is it worth it?</b><span>What the data suggests.</span></a>
  </div>
"""},
{
 "path": "mods", "active": "/guides/",
 "published": "2026-08-05",   # 保留改日期行之前的 datePublished(D2 2026-10-10)
 "updated": "Last updated 2026-10-10 &middot; the crossplay sentence re-checked 10 October 2026 against the developer&rsquo;s 10 July 2026 Steam announcement &middot; rest of the page last verified 5 August 2026 (29 July 2026 patch) and not re-checked against the 20 August and 1 September 2026 patches (see the updates page)",
 "title": "Shift At Midnight Mods — Workshop, BepInEx &amp; ShiftMorePlayers",
 "og_short": "Shift At Midnight Mods",
 "desc": "No Steam Workshop and no official tools — but there is a working BepInEx scene: 12 mods on Thunderstore, a Nexus section, and ShiftMorePlayers, which pushes lobbies past six.",
 "trail": [(None, "Mods")],
 "h1": "Shift At Midnight mods",
 "lede": "<strong>There is no Steam Workshop and there are no official modding tools.</strong> There is a working community scene built on BepInEx &mdash; small, but real &mdash; and one of its mods answers the question most people arrive here with: can more than six of us play at once?",
 "body": """
  <h2>Official support: none, in either direction</h2>

  <table class="facts">
    <tr><th>Steam Workshop</th><td>Not among the categories on the <a href="https://store.steampowered.com/app/3722330/Shift_At_Midnight/" target="_blank" rel="noopener">Steam store page</a></td></tr>
    <tr><th>Official mod tools or API</th><td>None announced</td></tr>
    <tr><th>Developer statement on modding</th><td>None &mdash; neither endorsed nor discouraged</td></tr>
    <tr><th>Xbox and Microsoft Store builds</th><td>Not applicable &mdash; everything below is a PC plugin</td></tr>
  </table>

  <p>The third row is the one that matters. Bun Muen has never publicly commented on modding in either direction. Nothing here has been blessed and nothing has been forbidden, which in practice means every mod on this page is unsupported: a broken save, a failed lobby or a plugin that stops loading after a patch is nobody&rsquo;s obligation to fix.</p>

  <p>The announced roadmap is content rather than platform work &mdash; the full release of <a href="/nights-and-levels/#endless-mode">Endless Mode</a> plus more customers, traps, weapons and monsters in a free update planned for Q4 2026. Modding tools are not on it.</p>

  <h2>Where the scene actually lives</h2>

  <p><a href="https://thunderstore.io/c/shift-at-midnight/" target="_blank" rel="noopener">Thunderstore</a> hosts &ldquo;The Shift At Midnight Mod Database&rdquo; and is the main platform, with <strong>12 mods listed as of 5 August 2026</strong>. <a href="https://www.nexusmods.com/games/shiftatmidnight/mods" target="_blank" rel="noopener">Nexus Mods</a> runs a separate section for the game, and it is where the most-wanted mod lives rather than on Thunderstore &mdash; so check both before concluding something does not exist.</p>

  <p>Calibrate your expectations against the download counts. The busiest Thunderstore entries are <strong>ModSettingsMenu (486), ShiftAtMidnightLocalizationAPI (468) and ShiftAtMidnightHostMenu (432)</strong>. Those are three-figure numbers for a game that <a href="https://steamdb.info/app/3722330/charts/" target="_blank" rel="noopener">peaked at 12,556 concurrent players</a> on 23 July, so this is a scene of a few hundred people that is two weeks old. Notice what those three mods are, too: a settings menu, a localisation API, a host menu. That is plumbing, not content. Nobody is shipping new monsters or new maps yet because the libraries you would build them on are still being written.</p>

  <h2>What you need before installing anything</h2>

  <p>Shift At Midnight is a Unity game compiled with <strong>IL2CPP, 64-bit</strong>. That single fact decides your whole toolchain:</p>

  <ul>
    <li><strong>BepInExPack IL2CPP</strong> is the prerequisite &mdash; not the Mono build of BepInEx. Installing the wrong pack is the most common reason a mod appears to do nothing at all.</li>
    <li>Some mods, including the lobby-size one below, need <strong>BepInEx 6 IL2CPP bleeding-edge</strong> rather than a stable release.</li>
    <li>The listings assume a manager rather than hand-dropped DLLs. <strong>GaleModManager</strong> is the one the Thunderstore pages are written around.</li>
    <li>Stay on the current game build. Two patches landed in the first fortnight and both touched surfaces mods hook into &mdash; see <a href="/updates/">patch notes</a>.</li>
  </ul>

  <h2>ShiftMorePlayers, and the honest version of &ldquo;250 players&rdquo;</h2>

  <p>The base game is <a href="/multiplayer/">designed around three players</a> and has offered a selectable cap of six since the <a href="https://steamdb.info/patchnotes/24354120/" target="_blank" rel="noopener">23 July patch</a>. <a href="https://www.nexusmods.com/shiftatmidnight/mods/3" target="_blank" rel="noopener">ShiftMorePlayers</a> replaces the CREATE LOBBY dropdown with a range of <strong>2 to 250</strong>, defaulting to 8.</p>

  <p>The number that matters is not 250. The mod&rsquo;s own author publishes the working figures: <strong>recommended 8, safe ceiling around 10</strong>, and past that, chaos &mdash; object interaction and monster targeting start breaking down. Read it as an eight-player version of the game with a slider that goes further than it should, and it will not disappoint you.</p>

  <div class="term tip">
    <div class="term-h">Only the host needs it</div>
    <p>This is what makes the mod usable for an ordinary group: <strong>friends running the vanilla game can join a modded host</strong>. One person installs BepInEx 6 IL2CPP and the mod, keeps their Steam copy current, and hosts. Nobody else changes anything.</p>
  </div>

  <p>Even unmodded, the developer warned that six-player lobbies &ldquo;may become chaotic&rdquo; and advised against them for a first playthrough. Everything that argument says about six, it says louder about eight. Finish the <a href="/nights-and-levels/">13-shift story</a> at three, then open it up.</p>

  <h2>The risks, specifically</h2>

  <ul>
    <li><strong>Patches break plugins.</strong> Two shipped in fourteen days and the second added an enemy and rebalanced the game. A scene this size will not always have a fix out the same day.</li>
    <li><strong>Achievements: unknown, and we will not pretend otherwise.</strong> No source states whether BepInEx plugins affect Steam achievement unlocks in this game &mdash; the developer has not commented and the mod pages do not address it. If you are going for <a href="/endings/">True Ending</a> (16.0%) or <em>Empty Home</em> ([[ACH:Empty Home]]%), do that run on a clean install and keep modded lobbies as a separate hobby. See <a href="/achievements/">all 10 achievements</a>.</li>
    <li><strong>Client compatibility is per-mod.</strong> ShiftMorePlayers explicitly supports vanilla clients; do not assume the next mod does. The host&rsquo;s mod list defines the session, so read each page.</li>
    <li><strong>Nothing is vetted.</strong> No Workshop means no platform-level review of what you are running. Use the game&rsquo;s own Thunderstore and Nexus pages rather than reuploads.</li>
    <li><strong>PC only.</strong> There is no equivalent for the Xbox or Microsoft Store builds, so a modded lobby cannot include a console <a href="/platforms/#game-pass">Game Pass</a> player &mdash; which is already true unmodded, because <a href="/crossplay/">the developer says Steam players will only play with other Steam players</a>.</li>
  </ul>

  <h2>What this page will not do</h2>

  <p>No click-by-click install walkthrough &mdash; it would be documenting a bleeding-edge BepInEx build that changes underneath it, and every mod page carries its own current prerequisites. No rankings of mods we cannot test. What is above is what can be checked against primary sources: that official support does not exist, where the scene is, how large it is, and what its flagship mod does according to the person who wrote it.</p>

  <div class="grid two">
    <a class="card" href="/multiplayer/"><b>Multiplayer</b><span>The unmodded lobby cap, and why the developer is not keen on six.</span></a>
    <a class="card" href="/updates/"><b>Patch notes</b><span>Every change since launch &mdash; the thing that breaks plugins.</span></a>
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
  <p>The official Discord server is the developer&rsquo;s own suggestion. Bun Muen&rsquo;s recent patch notes on Steam end by asking players to join it, and each of those notes carries the invite link. We do not copy invite links here; the 1 September 2026 patch note on the <a href="https://store.steampowered.com/app/3722330/Shift_At_Midnight/" target="_blank" rel="noopener">Steam store page</a> carries one.</p>

  <p>Two official statements apply to any group you find. The developer has said Steam players will only be able to play with other Steam players, and the 23 July 2026 patch note says the host selects the maximum player count when creating a lobby. Our <a href="/guide/beginners/">beginner&rsquo;s guide</a> covers the first shifts.</p>

  <div class="grid two">
    <a class="card" href="/crossplay/"><b>Crossplay</b><span>Exactly who can play with whom.</span></a>
    <a class="card" href="/troubleshooting/"><b>Troubleshooting</b><span>When a friend cannot join your lobby.</span></a>
  </div>
"""},
{
 "path": "review", "active": "/guides/",
 "published": "2026-08-05",   # 保留改日期行之前的 datePublished(D2 2026-10-10)
 "updated": "Last updated 2026-10-10 &middot; price, launch-discount, Game Pass and crossplay statements re-checked 10 October 2026 against the official Steam announcements and Steam store data &middot; rest of the page last verified 5 August 2026 (29 July 2026 patch) and not re-checked against the 20 August and 1 September 2026 patches (see the updates page)",
 "title": "Is Shift At Midnight Worth It? What the Data Says",
 "og_short": "Is Shift At Midnight Worth It?",
 "desc": "A $9.99 co-op horror game from a solo developer. What the achievement completion curve and the design actually tell you about whether it is worth your time.",
 "trail": [(None, "Is it worth it?")],
 "h1": "Is Shift At Midnight worth it?",
 "lede": "A <strong>$9.99</strong> three-player co-op horror game from a solo developer. Rather than tell you it is &ldquo;a must-play&rdquo;, here is what the publicly readable data actually supports.",
 "body": """
  <h2>What the achievement curve says about engagement</h2>
  <p>Completion rates are one of the few honest public signals about whether people stick with a game.</p>
  <ul>
    <li><strong>[[ACH:Still Breathing]]%</strong> survive their first hunt &mdash; almost nobody bounces off immediately.</li>
    <li><strong>[[ACH:Freed]]%</strong> kill a <a href="/monsters/demented/">Demented</a> &mdash; most players get past the opening.</li>
    <li><strong>[[ACH:Relentless]]%</strong> reach <em>Relentless</em> &mdash; not a first-session achievement. Four in ten players are still engaged well past the tutorial phase.</li>
    <li><strong>16.0% / [[ACH:Empty Home]]%</strong> reach the rare hidden endings &mdash; a real minority is digging.</li>
  </ul>
  <p>For a $9.99 indie release, a 40% figure on a mid-tier skill achievement is a healthy retention signal. It is not a game most people refund after an hour.</p>

  <h2>What the Steam review score actually says</h2>
  <p>Read from the Steam store page on <strong>12 August 2026</strong>: overall <strong>Very Positive</strong>, from <strong>7,114</strong> reviews. By language, English sits at <strong>94% of 3,363</strong> reviews, Simplified Chinese at Mostly Positive from 2,014, and Russian at Very Positive from 672.</p>
  <p>The shape over time is the more useful half. GameRant counted more than 800 reviews at 90% positive on 23 July, the day after launch. Going from there to over seven thousand in three weeks describes a game that kept selling after the launch-week coverage moved on.</p>
  <p>The aggregators do not agree on the number, though. One tracker reported 8.2K reviews at 88% positive on 11 August 2026 &mdash; a day earlier than our reading, and higher. We quote the store page because it is the primary source; why the trackers diverge, and which figures are safe to repeat, is on <a href="/player-count/">player count</a>.</p>
  <p>What no review score tells you is whether the parts <em>you</em> care about work, which is what the rest of this page is for. And if you would rather not take a number's word for any of it, there is a <a href="/demo/">free demo</a>.</p>

  <h2>What it does well</h2>
  <p>The central idea is genuinely good: a horror game where the scary decision is <em>administrative</em>. You are checking ID at a counter, and the tension comes from having authority you are not qualified to exercise. The <a href="/monsters/norbert/">Norbert</a>/<a href="/monsters/the-dentist/">Dentist</a> pairing &mdash; harmless thing that trips your alarm, lethal thing that does not register at all &mdash; is a genuinely elegant piece of design teaching.</p>
  <p><a href="/multiplayer/#co-op">Proximity chat</a> is used as a mechanic rather than a feature. Voices fading with distance is load-bearing.</p>

  <h2>What to be realistic about</h2>
  <ul>
    <li><strong>It is small.</strong> Ten achievements, one mode plus a free one coming in Q4. This is a $9.99 game and it is scoped like one.</li>
    <li><strong>It is better with people.</strong> Solo works and is tenser, but the design's best moments are three people shouting across a gas station.</li>
    <li><strong>The platform split is a genuine annoyance.</strong> <a href="/crossplay/">Per the developer, Steam players will only play with other Steam players</a>, and for a co-op game that is a real cost.</li>
    <li><strong>Gore.</strong> Steam flags "plenty of gore and blood". It is a game about deciding whether to kill the person in front of you.</li>
  </ul>

  <div class="term tip">
    <div class="term-h">Straight answer</div>
    <p>If you already have it through Game Pass and two friends are on the same side, install it tonight &mdash; it is a good three-hour night (Game Pass catalogue status was last read on 12 August 2026 and not re-checked on 10 October 2026). If you are buying at $9.99 to play with a group, that is easy value provided <a href="/crossplay/">everyone buys on the same side of the platform line</a>. If you are buying it to play alone, it is a smaller and quieter game than the trailers suggest &mdash; still interesting, but manage expectations.</p>
  </div>

  <div class="grid two">
    <a class="card" href="/review/#price"><b>Price &amp; editions</b><span>What you get for $9.99.</span></a>
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
    <li>Three achievements are hidden: <em>Grave Decision</em> ([[ACH:Grave Decision]]%), <em>True Ending</em> (16.0%), <em>Empty Home</em> ([[ACH:Empty Home]]%). None has an official requirement text, though the conditions are now documented. See <a href="/endings/">endings</a>.</li>
    <li>Nothing publicly documented connects the newsletter to those achievements. That is an <strong>absence of evidence</strong>, not evidence of absence.</li>
  </ul>

  <div class="term tip">
    <div class="term-h">If you want to actually solve this</div>
    <p>Screenshot the newsletter every run and note which shift it appeared on and what else was different about that night. If the text varies between runs, that is a strong signal it is procedural flavour. If it is identical every time and names someone, that is a much more interesting fact. Nobody has published that comparison &mdash; which is exactly why the question is still open.</p>
    <p>If you have run that comparison, that is a genuinely useful contribution. See <a href="/multiplayer/#find-players">community</a>.</p>
  </div>

  <h2>Why we are leaving this page thin</h2>
  <p>Because padding it would be worse than admitting we do not know. When we have a verified answer &mdash; from reproducible player reports or from the developer &mdash; it goes here with the date and the source, and this page gets rewritten properly.</p>

  <div class="grid two">
    <a class="card" href="/endings/"><b>Endings</b><span>The other open questions in this game.</span></a>
    <a class="card" href="/nights-and-levels/#story-mode"><b>Story Mode</b><span>Why procedural shifts complicate clue-hunting.</span></a>
  </div>
"""},
{
 "path": "faq", "active": "/faq/",
 "updated": "Last updated 2026-10-10 &middot; crossplay, Game Pass, price, patch, patience, Q4 2026 update and achievement unlock-rate statements re-checked 10 October 2026 against the official Steam announcements, store data and achievement stats &middot; Xbox store details are as read on 12 August 2026 and were not re-checked &middot; rest of the page last verified 5 August 2026 (29 July 2026 patch) &middot; latest patch: 1 September 2026",
 "published": "2026-08-05",
 "title": "Shift At Midnight FAQ — Crossplay, Players, Endings &amp; Mods",
 "og_short": "Shift At Midnight FAQ",
 "desc": "Straight answers to the most searched Shift At Midnight questions: crossplay, player count, the three endings, Endless Mode, mods, and what the latest patch changed.",
 "trail": [(None, "FAQ")],
 "h1": "Shift At Midnight FAQ",
 "lede": "The questions people actually search, answered directly. Where the honest answer is &ldquo;not confirmed&rdquo;, we say that instead of guessing.",
 "extra_ld": FAQ_LD,
 "body": """
  <h2>Buying &amp; playing together</h2>
  <div class="faq">
    <details open>
      <summary>Is Shift At Midnight crossplay?</summary>
      <div class="a"><p><strong>Partially, per the developer.</strong> The 10 July 2026 announcement says Xbox and PC Game Pass players will have crossplay, and that Steam players will only be able to play with other Steam players. On the Steam side, the same post previews a Steam-only public server browser, and no later changelog mentions it shipping. No official announcement promises crossplay between Steam and Xbox (all 31 official Steam announcements checked on 10 October 2026). Which pool a bought Microsoft Store copy joins, and how Xbox Play Anywhere relates to matchmaking, is not confirmed by any official statement, and this site has not tested it. <a href="/crossplay/">Full breakdown</a>.</p></div>
    </details>
    <details>
      <summary>My friends are on Game Pass and I bought it on Steam. What are my options?</summary>
      <div class="a"><p>If your group is split between Steam and Xbox or PC Game Pass, the developer&rsquo;s 10 July 2026 announcement says Steam players will only be able to play with other Steam players, and no later official post changes that (all 31 official Steam announcements checked on 10 October 2026). Which pool a copy bought on the Microsoft Store joins is not confirmed by any official statement, and we have not tested any combination. We do not name a cheapest fix; see the <a href="/crossplay/">crossplay page</a> for what is on the record, or <a href="/tools/#crossplay-checker">check your group here</a>.</p></div>
    </details>
    <details>
      <summary>Is Shift At Midnight on Game Pass?</summary>
      <div class="a"><p>Yes, per the developer. The 22 July 2026 launch post says the game is &ldquo;OUT NOW on Steam, Xbox &amp; Game Pass&rdquo;, and the 10 July 2026 post says it would be available on &ldquo;Steam, Xbox and Xbox PC Gamepass&rdquo;. Whether it is still in the Game Pass catalogue was not re-checked on 10 October 2026. The Xbox store listing read on 12 August 2026 carried an Xbox Play Anywhere label; we did not re-check it. <a href="/platforms/#game-pass">Details</a>.</p></div>
    </details>
    <details>
      <summary>How many players can play together?</summary>
      <div class="a"><p><strong>Three by design, six if you want it.</strong> The <a href="https://steamdb.info/patchnotes/24354120/" target="_blank" rel="noopener">23 July patch</a> made the lobby cap selectable up to six, but the developer says the game &ldquo;is designed and has always been marketed around a maximum of 3 players&rdquo;, that larger lobbies may become chaotic, and that six is not recommended for a first playthrough. Single-player is fully supported. <a href="/multiplayer/">More</a>.</p></div>
    </details>
    <details>
      <summary>How much does it cost?</summary>
      <div class="a"><p>$9.99 USD on Steam, with no discount running on 10 October 2026. The Xbox listing showed $9.99 on 12 August 2026 and was not re-checked. No paid DLC has been announced. <a href="/review/#price">More</a>.</p></div>
    </details>
    <details>
      <summary>Is Shift At Midnight on PS5?</summary>
      <div class="a"><p><strong>No.</strong> There is no PlayStation 5 or PS4 version and none has been announced. See <a href="/platforms/">platforms</a>.</p></div>
    </details>
    <details>
      <summary>Is Shift At Midnight on mobile or the App Store?</summary>
      <div class="a"><p><strong>No.</strong> No iOS or Android version exists. Anything using this name in a mobile app store is not this game.</p></div>
    </details>
    <details>
      <summary>Is Shift At Midnight free?</summary>
      <div class="a"><p>Not to buy &mdash; it is $9.99 on Steam. It was announced for Xbox PC Game Pass at launch (10 July 2026 post). Game Pass catalogue membership was last seen on the Xbox listing on 12 August 2026 and was not re-checked on 10 October 2026. There is a free multiplayer demo on Steam. <a href="/demo/">About the demo</a>.</p></div>
    </details>
    <details>
      <summary>When did Shift At Midnight come out?</summary>
      <div class="a"><p><strong>22 July 2026</strong>, after two delays from an original 28 May date. See <a href="/release-date/">release date</a>.</p></div>
    </details>
  </div>

  <h2>Monsters &amp; mechanics</h2>
  <div class="faq">
    <details>
      <summary>How many nights are there?</summary>
      <div class="a"><p><strong>Story Mode is 13 shifts</strong>, procedurally generated, so no two runs match. The fixed points are Shift 9 (the Marionette becomes possible), the choice offered after Shift 12, and Shift 13. See <a href="/nights-and-levels/">nights &amp; shifts</a>.</p></div>
    </details>
    <details>
      <summary>How do I beat the Marionette?</summary>
      <div class="a"><p>Find the <a href="/monsters/jack-in-the-box/">music box</a> and <strong>hold E to rewind it before the melody plays three times</strong>. It spawns in the break room, a storage room, the bathroom or a shelf aisle, and the 23 July patch made it much louder to find by ear. It can also be killed outright &mdash; the same patch cut its HP &mdash; though only 44.0% of players have (Steam global achievement stats, 10 October 2026). <a href="/monsters/marionette/">Full guide</a>.</p></div>
    </details>
    <details>
      <summary>How do I kill the Dentist?</summary>
      <div class="a"><p><strong>You do not.</strong> He appears on Shift 13, no weapon or trap is effective, and running until Sheriff Clyde intervenes is the entire answer. <a href="/monsters/the-dentist/">More</a>.</p></div>
    </details>
    <details>
      <summary>What is a Rake?</summary>
      <div class="a"><p>An enemy added in the <a href="https://store.steampowered.com/news/app/3722330/view/695394018676179340" target="_blank" rel="noopener">29 July patch</a> that emerges from the forests around the station. It only exists in <strong>Endless and post-story modes</strong> &mdash; Story Mode never spawns one. <a href="/nights-and-levels/#endless-mode">More</a>.</p></div>
    </details>
    <details>
      <summary>Do customers still run out of patience while I check their ID?</summary>
      <div class="a"><p><strong>It depends on the mode, going by the patch notes.</strong> The 29 July 2026 announcement says &ldquo;Removed patience in ENDLESS MODE / POST-STORY MODE&rdquo;, and the 1 September 2026 announcement says &ldquo;Re-enabled patience for ENDLESS MODE&rdquo;. Neither line mentions Story Mode, and no official announcement says patience was removed there. <a href="/guide/doppelgangers/">Identification guide</a>.</p></div>
    </details>
    <details>
      <summary>Should I kill Norbert?</summary>
      <div class="a"><p>No. He scans as a fake ID, is flagged as a doppelganger, and is harmless &mdash; a gnome who exists to teach you the flag reports on documents, not intent. <a href="/monsters/norbert/">More</a>.</p></div>
    </details>
    <details>
      <summary>What happens if I let a doppelganger go?</summary>
      <div class="a"><p>It completes its purchase, leaves, and <strong>comes back that same night in monster form to hunt you</strong>. That is where most hunts come from. <a href="/guide/survival/">Survival guide</a>.</p></div>
    </details>
  </div>

  <h2>Achievements &amp; endings</h2>
  <div class="faq">
    <details>
      <summary>How many achievements are there?</summary>
      <div class="a"><p>Ten. Three are hidden: <em>Grave Decision</em> (35.1%), <em>True Ending</em> (16.0%) and <em>Empty Home</em> (10.9%), as of 10 October 2026. <a href="/achievements/">Full list with rarity</a>.</p></div>
    </details>
    <details>
      <summary>How do I get the true ending?</summary>
      <div class="a"><p>Two conditions: <strong>do not call Sheriff Clyde</strong> when the choice appears after Shift 12, and <strong>finish Shift 13 with at least $250 saved</strong>. Calling Clyde gives <em>Grave Decision</em> instead; declining with under $250 gives <em>Empty Home</em>. <a href="/endings/">All three endings</a>.</p></div>
    </details>
    <details>
      <summary>What is the hardest achievement?</summary>
      <div class="a"><p><em>Empty Home</em> at 10.9%, then <em>True Ending</em> at 16.0%. Of the non-hidden ones, <em>Locked And Loaded</em> &mdash; buy every melee weapon &mdash; is rarest at 21.5%. All three figures are Steam global unlock rates read on 10 October 2026.</p></div>
    </details>
  </div>

  <h2>Content &amp; updates</h2>
  <div class="faq">
    <details>
      <summary>Does it have mods or Steam Workshop?</summary>
      <div class="a"><p><strong>No Workshop, no official tools</strong>, and no comment from the developer either way. There is an active BepInEx scene: 12 mods on Thunderstore as of 5 August 2026 plus a Nexus section, including one that raises the lobby cap far past six &mdash; only the host installs it. <a href="/mods/">Full rundown and the risks</a>.</p></div>
    </details>
    <details>
      <summary>How do I unlock Endless Mode?</summary>
      <div class="a"><p><strong>Finish Story Mode.</strong> Endless Mode shipped as a beta on launch day but unlocks only once the 13-shift story is complete. It is the only place Rakes appear. <a href="/nights-and-levels/#endless-mode">More</a>.</p></div>
    </details>
    <details>
      <summary>What did the latest patch change?</summary>
      <div class="a"><p>The 1 September 2026 patch added 30 new customers to Story Mode and Endless Mode, added the Chainsaw as a purchasable melee weapon (now required for the Locked And Loaded achievement), and added security cameras in Endless Mode. As of 10 October 2026 it is the newest patch on the official Steam announcement feed; the 20 August 2026 patch before it added 15 customers and cloud saves for Steam. <a href="/updates/">All patch notes</a>.</p></div>
    </details>
    <details>
      <summary>What is coming next?</summary>
      <div class="a"><p>The Steam store page states: &ldquo;A free, major ENDLESS MODE update is planned for Q4 2026, with exclusive customers, weapons, traps, monsters and more.&rdquo; (read 10 October 2026). None of the 31 official Steam announcements names Q4 2026 or gives a date for it. <a href="/updates/">Patch notes</a>.</p></div>
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

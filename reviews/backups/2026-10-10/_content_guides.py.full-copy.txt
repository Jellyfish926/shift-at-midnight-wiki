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
      "acceptedAnswer": { "@type": "Answer", "text": "Partially. Xbox console and PC Game Pass players share one pool through Xbox Play Anywhere. The Steam version connects only to other Steam players. Full crossplay and a server browser are promised in a post-release update, with no date given." } },
    { "@type": "Question", "name": "Is Shift At Midnight on Game Pass?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes, day one on both Xbox console and PC Game Pass. It is also an Xbox Play Anywhere title." } },
    { "@type": "Question", "name": "How many players can play Shift At Midnight?",
      "acceptedAnswer": { "@type": "Answer", "text": "Three by design. The 23 July 2026 patch made the lobby cap selectable up to six, but the developer says the game is designed and has always been marketed around a maximum of three players, and does not recommend six for a first playthrough. Single-player is fully supported, and co-op uses proximity chat." } },
    { "@type": "Question", "name": "How much does Shift At Midnight cost?",
      "acceptedAnswer": { "@type": "Answer", "text": "9.99 USD. The 10% launch discount ended on 29 July 2026. It is also included with Xbox Game Pass." } },
    { "@type": "Question", "name": "Does Shift At Midnight have mods?",
      "acceptedAnswer": { "@type": "Answer", "text": "There is no Steam Workshop and there are no official modding tools, and the developer has not commented on modding either way. A community scene built on BepInEx does exist: 12 mods were listed on Thunderstore as of 5 August 2026, plus a separate section on Nexus Mods. The best known of them, ShiftMorePlayers, raises the lobby cap well past six and only needs to be installed by the host." } },
    { "@type": "Question", "name": "How many achievements does Shift At Midnight have?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ten. Three of them are hidden: Grave Decision at 33.1 percent, True Ending at 16.0 percent and Empty Home at 10.1 percent." } },
    { "@type": "Question", "name": "How do you get the true ending in Shift At Midnight?",
      "acceptedAnswer": { "@type": "Answer", "text": "Two conditions. Do not call Sheriff Clyde when the choice appears after Shift 12, and finish Shift 13 with at least 250 dollars in personal savings. Calling Clyde gives the Grave Decision ending instead, and declining with less than 250 dollars gives Empty Home. 16.0 percent of players have the True Ending achievement." } },
    { "@type": "Question", "name": "How do you unlock Endless Mode in Shift At Midnight?",
      "acceptedAnswer": { "@type": "Answer", "text": "Finish Story Mode. Endless Mode shipped as a beta on launch day, 22 July 2026, but unlocks only once the 13-shift story is complete. It is the only mode where Rake enemies appear. A full version is planned for a free update in Q4 2026." } },
    { "@type": "Question", "name": "How many nights are in Shift At Midnight?",
      "acceptedAnswer": { "@type": "Answer", "text": "Story Mode is 13 shifts. Customers and events are procedurally generated, so runs differ. The fixed points are Shift 9, when the Marionette becomes possible, the choice offered after Shift 12, and Shift 13." } },
    { "@type": "Question", "name": "What did the latest Shift At Midnight patch change?",
      "acceptedAnswer": { "@type": "Answer", "text": "The 29 July 2026 patch added Rake enemies to endless and post-story modes, added a second purchasable firearm, and removed the customer patience mechanic, so verifying IDs is no longer timed. As of 13 August 2026 it is still the newest update." } },
    { "@type": "Question", "name": "Is Shift At Midnight on PS5?",
      "acceptedAnswer": { "@type": "Answer", "text": "No. There is no PlayStation 5 or PS4 version of Shift At Midnight and none has been announced. It is available on PC via Steam and the Microsoft Store, and on Xbox Series X|S." } },
    { "@type": "Question", "name": "Is Shift At Midnight available on mobile or the App Store?",
      "acceptedAnswer": { "@type": "Answer", "text": "No. There is no iOS or Android version of Shift At Midnight. It is a PC and Xbox title only." } },
    { "@type": "Question", "name": "When did Shift At Midnight come out?",
      "acceptedAnswer": { "@type": "Answer", "text": "Shift At Midnight released on 22 July 2026, after being delayed twice from its original 28 May 2026 date." } },
    { "@type": "Question", "name": "Is Shift At Midnight free?",
      "acceptedAnswer": { "@type": "Answer", "text": "The game costs 9.99 USD to buy, but it is included at no extra cost with Xbox Game Pass on both console and PC. There is also a free multiplayer demo on Steam." } },
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
    <a class="card danger" href="/crossplay/"><b>Crossplay &mdash; read before buying</b><span>Steam players and Game Pass players cannot play together. Finding this out after everyone has paid is the most expensive mistake on this wiki.</span></a>
  </div>

  <h2>2. Telling people apart</h2>
  <p>This is the actual game; everything else is consequence. A doppelganger you wave through completes its purchase, walks out, and comes back the same night as something that hunts you &mdash; which is why identification and survival are one subject rather than two.</p>
  <div class="grid two">
    <a class="card" href="/guide/doppelgangers/"><b>Identifying doppelgangers</b><span>The seven categories of tell, what the N.E.T. database does that the ID scanner cannot, why Norbert is a trap, and what changed when the patience timer was removed.</span></a>
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
 "title": "Shift At Midnight Beginner's Guide — Surviving Your First Shifts",
 "og_short": "Shift At Midnight Beginner's Guide",
 "desc": "A beginner's guide to Shift At Midnight that starts with the mistake 96.9% of players make: treating the ID scanner as a threat detector.",
 "trail": G + [(None, "Beginner's guide")],
 "h1": "Beginner's guide",
 "lede": "The fastest way to understand this game is to understand one number: <strong>96.9% of all players have killed a customer</strong>. That is the most common achievement in the game. It is not a badge of skill &mdash; it is the game documenting a mistake almost everyone makes.",
 "body": """
  <h2>The game got easier on 29 July, and it matters most for you</h2>
  <p>The <a href="/updates/">29 July 2026 patch removed the patience mechanic</a>. Before it, a customer
    standing at your counter was running down a meter while you checked their documents, which meant every
    verification was a race. That pressure is gone. If you learned this game from a video recorded in the
    first week &mdash; and most of the ones with the biggest view counts were &mdash; you are being taught to
    rush a check that you are now allowed to take your time over.</p>
  <p>For a new player this changes the correct opening strategy outright: <strong>scan everything, read the
    description box, and search the N.E.T. database on anyone who feels off.</strong> The cost of being slow
    is now close to zero, and the cost of being wrong is a hunt. See the
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
  <p>The cliff is at <em>Relentless</em> (45.4%) and <a href="/monsters/marionette/">Last Performance</a> (41.6%). Those need you to know something in advance. Everything below them needs deliberate effort. See <a href="/achievements/">the full list</a>.</p>

  <h2>Money</h2>
  <p>You will want to spend everything on restocking, because the quota is immediate and the arsenal is not. Resist a little. <em>Locked And Loaded</em> &mdash; purchasing every melee weapon &mdash; sits at 23.5%, and the reason it is that low is that people spend their earnings shift-to-shift and never bank. See the <a href="/guide/survival/#weapons">weapons guide</a>.</p>

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
 "desc": "The seven categories of tell, what the N.E.T. database does that the ID scanner cannot, the document checks worth running, and why the 29 July patch changed how you should verify.",
 "trail": G + [(None, "Doppelgangers")],
 "h1": "Identifying doppelgangers",
 "lede": "This is the job. Something walks in wearing a real person &mdash; face, voice, mannerisms, biography &mdash; and you have a scanner, a database and your own attention. The <a href=\"https://store.steampowered.com/news/app/3722330/view/695394018676179340\" target=\"_blank\" rel=\"noopener\">29 July patch removed the patience mechanic</a>, so you now have one more thing: time.",
 "body": """
  <div class="term warn">
    <div class="term-h">Why this outranks every other skill</div>
    <p>Let a doppelganger finish its purchase and walk out and <strong>it comes back that same night in monster form to hunt you</strong> (<a href="https://gamerant.com/shift-at-midnight-all-monsters/" target="_blank" rel="noopener">Game Rant</a>). Most hunts on the <a href="/guide/survival/">survival page</a> were created here, at the counter, minutes earlier.</p>
  </div>

  <p>The opposite error is cheaper but not free: killing a real customer unlocks <em>First Blood</em>, held by <strong>96.9% of players</strong>. It is the most common achievement in the game, which tells you how hard this call is and how little the game expects perfection.</p>

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
  <p><a href="https://www.dualshockers.com/shift-at-midnight-all-doppelgangers/" target="_blank" rel="noopener">DualShockers has documented 47 named doppelgangers</a>, each with its own tell. Five, to show the range:</p>
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

  <h2>What the 29 July patch changed here</h2>
  <p>Before it, customers ran down a patience meter while you verified them, so rushing a scan was a defensible choice. <strong>That mechanic is gone.</strong> Nothing now argues against typing the name into the database, asking a second question, or stepping away from the counter to read a file. Instincts formed in the game&rsquo;s first week are more hurried than they need to be. See <a href="/updates/">patch notes</a>.</p>

  <h2>With two or three players</h2>
  <p>Split roles instead of crowding the till: one on the scanner and database, one watching the aisles for the things that never come to the counter, one keeping the store running so the shift does not fail on numbers. Proximity chat lets the floor watcher speak quietly without the counter breaking eye contact. See <a href="/multiplayer/#co-op">co-op roles</a>.</p>

  <h2>What this page leaves out</h2>
  <p>All 47 names, because reading them in advance replaces the game with a lookup table. And any schedule of who turns up on which night: customers and events are <a href="/nights-and-levels/">procedurally generated</a>, so such a list describes one playthrough, not the game.</p>

  <div class="grid two">
    <a class="card" href="/guide/survival/"><b>Survival &amp; weapons</b><span>For when this page has already failed and something is loose in the building.</span></a>
    <a class="card danger" href="/monsters/"><b>Bestiary</b><span>What comes back after you wave one through.</span></a>
  </div>
"""},
{
 "path": "guide/survival", "active": "/guides/",
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
  <p>They are not weather. Let a doppelganger complete its purchase and walk out and <strong>it returns that same night as a monster</strong> (<a href="https://gamerant.com/shift-at-midnight-all-monsters/" target="_blank" rel="noopener">Game Rant</a>), so everything below is the bill for a decision made at the counter &mdash; see <a href="/guide/doppelgangers/">identifying doppelgangers</a>. <em>Still Breathing</em>, for surviving your first hunt, sits at <strong>93.8%</strong>; <em>Relentless</em>, for finishing one inside 30 seconds, sits at <strong>45.4%</strong>. That gap is this page&rsquo;s subject: surviving is normal, ending it fast is a plan.</p>

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
    <li><strong><a href="/monsters/demented/">Demented</a></strong> &mdash; cannot move while you look straight at it. Hold the stare, back it toward a trap, then break eye contact. Not rare, whatever you have read: <strong>79.8%</strong> of players have killed one.</li>
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
    <p>On a <a href="/monsters/marionette/">Marionette</a> night, one player owns the <a href="/monsters/jack-in-the-box/">music box</a> for the whole encounter and calls the melody count aloud. Three people half-watching a box that has to be wound is how groups end up facing the Marionette with no counterplay &mdash; which is why only 41.6% have ever killed one.</p>
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
 "desc": "Buying every melee weapon unlocks Locked And Loaded, held by only 23.5% of players. Why it is low, how to bank for it, and what weapons cannot solve.",
 "trail": G + [(None, "Weapons")],
 "h1": "Weapons arsenal",
 "lede": "Purchasing every melee weapon and filling out the arsenal unlocks <strong>Locked And Loaded</strong> &mdash; held by only <strong>23.5%</strong> of players. It is not a difficulty problem. It is a budgeting problem.",
 "body": """
  <div class="tags">
    <span class="tag amber">Achievement: Locked And Loaded</span>
    <span class="tag">23.5% of players</span>
  </div>

  <h2>Melee is the achievement; the guns are insurance</h2>
  <p><em>Locked And Loaded</em> is specific: <strong>purchase all melee weapons and fill out the weapons arsenal</strong>. At <strong>23.5%</strong> it is a budgeting problem, not a difficulty one: restocking pays tonight, the arsenal pays on a night that may never come, and under pressure people buy the immediate thing. Decide early that a fixed slice of each shift&rsquo;s takings is untouchable.</p>
  <p>Firearms sit outside that achievement, and there are now two of them: the <a href="https://store.steampowered.com/news/app/3722330/view/695394018676179340" target="_blank" rel="noopener">29 July patch</a> added a second purchasable gun alongside the one the game shipped with. They are also the loudest tools you own, which is the argument for melee on a night you would rather not be found &mdash; see sound discipline above. Full change list: <a href="/updates/">patch notes</a>.</p>

  <h2>Have it equipped before the hunt</h2>
  <p>Buy and equip before a hunt starts, not during one: <em>Relentless</em> &mdash; finish a hunt within 30 seconds, <strong>45.4%</strong> &mdash; is close to impossible if the first ten seconds go on shopping. The target to attempt it on is a <a href="/monsters/shrieking-doll/">Shrieking Doll</a>, which comes to you rather than hiding. Never on a <a href="/monsters/the-dentist/">Dentist</a> night, which cannot be won at all.</p>

  <h2>What a weapon does not solve</h2>
  <ul>
    <li><strong>The Dentist.</strong> No weapon works. Running is the entire answer.</li>
    <li><strong>Doppelgangers.</strong> The problem is identification, not damage &mdash; a weapon applied to the wrong customer is the 96.9% achievement. See <a href="/guide/doppelgangers/">identifying doppelgangers</a>.</li>
    <li><strong>An unwound music box.</strong> Whether you fight a <a href="/monsters/marionette/">Marionette</a> at all is settled by the <a href="/monsters/jack-in-the-box/">box</a>, not your loadout. A weapon helps once the fight starts &mdash; the 23 July patch cut its HP &mdash; but arriving armed does not substitute for winding.</li>
  </ul>

  <p>We do not publish a weapon tier list, damage values or per-monster recommendations. There is no published list of the melee weapons or their prices, and the confident numbers circulating for this game are unsourced.</p>

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
  <p>A queue creates time pressure on the one decision the game cares about: is this person human? Rushing produces the 96.9% outcome &mdash; killing a customer &mdash; or the opposite error of waving through something you should have caught. The queue is not an obstacle to the horror; it is the mechanism that generates it.</p>

  <h2>Budgeting</h2>
  <p>Money splits between restocking (immediate, keeps quota healthy) and the <a href="/guide/survival/#weapons">weapons arsenal</a> (deferred, and its own 23.5% achievement). Bank a fixed slice every shift rather than deciding to chase the arsenal later.</p>

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
  <p>Three achievements are hidden and rare: <em>Grave Decision</em> (33.1%), <em>True Ending</em> (16.0%) and <em>Empty Home</em> (10.1%). They are three separate endings, not milestones on one path. Full discussion on <a href="/endings/">the endings page</a>, with fact and inference clearly separated.</p>
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
 "path": "multiplayer", "active": "/guides/",
 "title": "Shift At Midnight Multiplayer — Player Count &amp; Crossplay",
 "og_short": "Shift At Midnight Multiplayer",
 "desc": "Shift At Midnight supports up to 3 players in online co-op with proximity chat. Platform compatibility is the thing that stops most groups playing together.",
 "trail": [(None, "Multiplayer")],
 "h1": "Multiplayer",
 "lede": "<strong>Up to three players</strong>, online co-op, with <strong>proximity chat</strong>. There is also a full single-player mode. The thing that most often stops a group playing together is not the player cap &mdash; it is which store they bought it from.",
 "body": """
  <table class="facts">
    <tr><th>Max players</th><td>3 by design &mdash; 6 selectable since the 23 July 2026 patch</td></tr>
    <tr><th>Mode</th><td>Online co-op</td></tr>
    <tr><th>Voice</th><td>Proximity chat</td></tr>
    <tr><th>Single-player</th><td>Yes, full mode</td></tr>
    <tr><th>Crossplay</th><td>Xbox + PC Game Pass only &mdash; <a href="/crossplay/">Steam isolated</a></td></tr>
  </table>

  <div class="term warn">
    <div class="term-h">Six is possible. Three is what the game was built for.</div>
    <p>The <a href="https://steamdb.info/patchnotes/24354120/" target="_blank" rel="noopener">23 July 2026 patch</a> made the lobby cap selectable up to six, so a group of four is not shut out. The developer was unusually direct about what that option is, though: the game &ldquo;is designed and has always been marketed around a maximum of 3 players&rdquo;, larger lobbies &ldquo;may become chaotic&rdquo;, and six is not recommended for a first playthrough. Treat six as a party mode and three as the game.</p>
  </div>

  <h2>Getting everyone into a session</h2>
  <p>Everyone must be on the same side of the platform line. Steam players connect only to Steam players; Xbox console and PC Game Pass players share one pool via Play Anywhere. Mixed groups cannot play together, and this is the single most common reason a planned session does not happen. Sort it <em>before</em> anyone buys.</p>
  <p>If everyone is on the same store and you still cannot see each other, the next two suspects are a mismatched Steam beta branch and a stalled update &mdash; both are covered on <a href="/troubleshooting/">troubleshooting</a>.</p>

  <h2>Proximity chat is a mechanic</h2>
  <p>Voices fade with distance, so every noise your teammates make carries positional information. Running Discord over the top removes that and makes co-ordination worse, not better. Use the in-game chat &mdash; see the <a href="/multiplayer/#co-op">co-op guide</a> for role splitting.</p>

  <h2>Is solo worth it?</h2>
  <p>Yes, and it is not a lesser mode. Solo gives you complete control of every judgement call at the counter, which matters if you are chasing the <a href="/endings/">hidden ending achievements</a>. Co-op is more chaotic and funnier; solo is tenser and more deliberate.</p>

  <div class="grid two">
    <a class="card" href="/crossplay/"><b>Crossplay</b><span>Exactly who can play with whom.</span></a>
    <a class="card" href="/multiplayer/#co-op"><b>Co-op roles</b><span>How three players should split the work.</span></a>
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
    <a class="card" href="/review/#price"><b>Price</b><span>What buying it costs instead.</span></a>
  </div>
"""},
{
 "path": "price", "active": "/guides/",
 "title": "Shift At Midnight Price — $9.99 and Whether to Buy It",
 "og_short": "Shift At Midnight Price",
 "desc": "Shift At Midnight is $9.99 USD with a 10% launch discount, and free on Game Pass. Which platform you buy on matters more than the price does.",
 "trail": [(None, "Price")],
 "h1": "Price &amp; editions",
 "lede": "<strong>$9.99 USD</strong> &mdash; the 10% launch discount ended on 29 July 2026 &mdash; and <strong>free with Xbox Game Pass</strong>. There is one edition. The decision that actually costs people money is not the price &mdash; it is the store.",
 "body": """
  <table class="facts">
    <tr><th>Price</th><td>$9.99 USD (regional pricing varies)</td></tr>
    <tr><th>Launch discount</th><td>10% introductory offer &mdash; ended 29 July 2026</td></tr>
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
  <p>The honest framing: this is a three-player co-op horror game with ten achievements and a procedural shift structure. The achievement curve suggests most players get several hours in &mdash; 45.4% reach <em>Relentless</em>, which is not a first-session achievement &mdash; and a meaningful minority push into the rare hidden endings at 10&ndash;16%. See <a href="/review/">is it worth it</a>.</p>
  <p>If you have Game Pass the question does not arise. If you do not, and you have two friends who will play it with you, $9.99 for a co-op night is not a hard sell. If you are buying it to play alone, it is a smaller game than the store page implies.</p>

  <div class="grid two">
    <a class="card" href="/platforms/#game-pass"><b>Game Pass</b><span>Free if you subscribe.</span></a>
    <a class="card" href="/review/"><b>Is it worth it?</b><span>What the data suggests.</span></a>
  </div>
"""},
{
 "path": "mods", "active": "/guides/",
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
    <li><strong>Achievements: unknown, and we will not pretend otherwise.</strong> No source states whether BepInEx plugins affect Steam achievement unlocks in this game &mdash; the developer has not commented and the mod pages do not address it. If you are going for <a href="/endings/">True Ending</a> (16.0%) or <em>Empty Home</em> (10.1%), do that run on a clean install and keep modded lobbies as a separate hobby. See <a href="/achievements/">all 10 achievements</a>.</li>
    <li><strong>Client compatibility is per-mod.</strong> ShiftMorePlayers explicitly supports vanilla clients; do not assume the next mod does. The host&rsquo;s mod list defines the session, so read each page.</li>
    <li><strong>Nothing is vetted.</strong> No Workshop means no platform-level review of what you are running. Use the game&rsquo;s own Thunderstore and Nexus pages rather than reuploads.</li>
    <li><strong>PC only.</strong> There is no equivalent for the Xbox or Microsoft Store builds, so a modded lobby cannot include a console <a href="/platforms/#game-pass">Game Pass</a> player &mdash; which is already true unmodded, because <a href="/crossplay/">Steam and Game Pass do not share a player pool</a>.</li>
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
  <div class="term warn">
    <div class="term-h">On links</div>
    <p>We do not publish Discord invite links. Invites expire, get replaced, and are a standard vector for impersonation &mdash; a fan wiki linking to a server that has changed hands is a real risk. Check the official Steam store page and Kwalee's own channels for current official links. If a server claims to be official, verify it from the publisher's side, not from a fan site.</p>
  </div>

  <h2>Why the community matters more than usual here</h2>
  <p>Steam still hides the descriptions for <em>Grave Decision</em> (33.1%), <em>True Ending</em> (16.0%) and <em>Empty Home</em> (10.1%), and there is no official requirement text for any of them &mdash; the conditions now on <a href="/endings/">the endings page</a> were worked out by players and written up by outlets, not published by the developer. That is what a community is for, and it is why logged runs beat confident guesses.</p>

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
    <li><strong>93.8%</strong> survive their first hunt &mdash; almost nobody bounces off immediately.</li>
    <li><strong>79.8%</strong> kill a <a href="/monsters/demented/">Demented</a> &mdash; three quarters get past the opening.</li>
    <li><strong>45.4%</strong> reach <em>Relentless</em> &mdash; not a first-session achievement. Four in ten players are still engaged well past the tutorial phase.</li>
    <li><strong>16.0% / 10.1%</strong> reach the rare hidden endings &mdash; a real minority is digging.</li>
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
    <li><strong>The platform split is a genuine annoyance.</strong> <a href="/crossplay/">Steam cannot play with Game Pass</a>, and for a co-op game that is a real cost.</li>
    <li><strong>Gore.</strong> Steam flags "plenty of gore and blood". It is a game about deciding whether to kill the person in front of you.</li>
  </ul>

  <div class="term tip">
    <div class="term-h">Straight answer</div>
    <p>If you have Game Pass and two friends, install it tonight &mdash; it costs you nothing and it is a good three-hour night. If you are buying at $9.99 to play with a group, that is easy value provided <a href="/crossplay/">everyone buys on the same side of the platform line</a>. If you are buying it to play alone, it is a smaller and quieter game than the trailers suggest &mdash; still interesting, but manage expectations.</p>
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
    <li>Three achievements are hidden: <em>Grave Decision</em> (33.1%), <em>True Ending</em> (16.0%), <em>Empty Home</em> (10.1%). None has an official requirement text, though the conditions are now documented. See <a href="/endings/">endings</a>.</li>
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
      <div class="a"><p><strong>Partially.</strong> Xbox console and PC Game Pass players share one pool through Xbox Play Anywhere. The Steam version connects only to other Steam players. Full crossplay and a server browser are promised in a post-release update, with no date given; the browser is still not live as of 5 August 2026. <a href="/crossplay/">Full breakdown</a>.</p></div>
    </details>
    <details>
      <summary>My friends are on Game Pass and I bought it on Steam. What are my options?</summary>
      <div class="a"><p>One of you has to own it on the other side; there is no workaround. It is included with Game Pass on both console and PC, so the cheapest fix is usually the Steam player picking it up there. <a href="/tools/#crossplay-checker">Check your group here</a>.</p></div>
    </details>
    <details>
      <summary>Is Shift At Midnight on Game Pass?</summary>
      <div class="a"><p>Yes &mdash; day one, on both Xbox console and PC. It is also an Xbox Play Anywhere title with cloud saves. <a href="/platforms/#game-pass">Details</a>.</p></div>
    </details>
    <details>
      <summary>How many players can play together?</summary>
      <div class="a"><p><strong>Three by design, six if you want it.</strong> The <a href="https://steamdb.info/patchnotes/24354120/" target="_blank" rel="noopener">23 July patch</a> made the lobby cap selectable up to six, but the developer says the game &ldquo;is designed and has always been marketed around a maximum of 3 players&rdquo;, that larger lobbies may become chaotic, and that six is not recommended for a first playthrough. Single-player is fully supported. <a href="/multiplayer/">More</a>.</p></div>
    </details>
    <details>
      <summary>How much does it cost?</summary>
      <div class="a"><p>$9.99 USD on Steam and the Xbox store. The 10% launch discount ended on 29 July 2026 and there is no paid DLC. <a href="/review/#price">More</a>.</p></div>
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
      <div class="a"><p>Not to buy &mdash; it is $9.99. It is included with Game Pass at no extra cost, and there is a free multiplayer demo on Steam. <a href="/demo/">About the demo</a>.</p></div>
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
      <div class="a"><p>Find the <a href="/monsters/jack-in-the-box/">music box</a> and <strong>hold E to rewind it before the melody plays three times</strong>. It spawns in the break room, a storage room, the bathroom or a shelf aisle, and the 23 July patch made it much louder to find by ear. It can also be killed outright &mdash; the same patch cut its HP &mdash; though only 41.6% of players have. <a href="/monsters/marionette/">Full guide</a>.</p></div>
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
      <div class="a"><p><strong>No.</strong> The patience mechanic was removed on 29 July 2026, so verification is no longer timed. Habits formed in the first week can be unlearned. <a href="/guide/doppelgangers/">Identification guide</a>.</p></div>
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
      <div class="a"><p>Ten. Three are hidden: <em>Grave Decision</em> (33.1%), <em>True Ending</em> (16.0%) and <em>Empty Home</em> (10.1%). <a href="/achievements/">Full list with rarity</a>.</p></div>
    </details>
    <details>
      <summary>How do I get the true ending?</summary>
      <div class="a"><p>Two conditions: <strong>do not call Sheriff Clyde</strong> when the choice appears after Shift 12, and <strong>finish Shift 13 with at least $250 saved</strong>. Calling Clyde gives <em>Grave Decision</em> instead; declining with under $250 gives <em>Empty Home</em>. <a href="/endings/">All three endings</a>.</p></div>
    </details>
    <details>
      <summary>What is the hardest achievement?</summary>
      <div class="a"><p><em>Empty Home</em> at 10.1%, then <em>True Ending</em> at 16.0%. Of the non-hidden ones, <em>Locked And Loaded</em> &mdash; buy every melee weapon &mdash; is rarest at 23.5%.</p></div>
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
      <div class="a"><p>The 29 July 2026 patch added Rake enemies to endless and post-story modes, added a second purchasable firearm, and removed the patience mechanic. As of 13 August 2026 that is still the newest update. <a href="/updates/">All patch notes</a>.</p></div>
    </details>
    <details>
      <summary>What is coming next?</summary>
      <div class="a"><p>A free update planned for <strong>Q4 2026</strong>: the full release of Endless Mode plus more customers, traps, weapons and monsters.</p></div>
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

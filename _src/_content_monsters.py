#!/usr/bin/env python3
"""怪物页 + 结局页正文。事实来源:Steam 商店页、Steam 全球成就统计、公开攻略交叉核对。
推断一律显式标注,不与事实混写。"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _build import build

M = [("/monsters/", "Monsters")]

PAGES = [
{
 "path": "monsters/marionette",
 "title": "Shift At Midnight Marionette — Shift 9 Music Box &amp; How to Kill It",
 "og_short": "Shift At Midnight Marionette Guide",
 "desc": "The Marionette arrives from Shift 9. Find the music box, hold E to rewind it before the melody plays three times — or fight what it summons. Only 40.0% of players have killed one.",
 "trail": M + [(None, "Marionette")],
 "h1": "Marionette",
 "lede": "The <strong>Shift 9</strong> threat, and the one most players never beat &mdash; only <strong>40.0%</strong> of players have killed a Marionette. The encounter is governed by a wind-up <a href=\"/monsters/jack-in-the-box/\">music box</a> hidden somewhere in the store, and the clock on it is exactly three melodies long.",
 "body": """
  <div class="tags">
    <span class="tag red">Hostile</span>
    <span class="tag amber">From Shift 9</span>
    <span class="tag green">Can be killed</span>
    <span class="tag">40.0% have Last Performance</span>
  </div>

  <table class="facts">
    <tr><th>First appears</th><td>Shift 9 onwards, Story Mode</td></tr>
    <tr><th>Advance warning</th><td>An N.E.T. email flags it before the shift</td></tr>
    <tr><th>Live warning</th><td>A music box starts playing somewhere in the store</td></tr>
    <tr><th>Counterplay</th><td>Reach the box and hold <strong>E</strong> to rewind it before the melody finishes three times</td></tr>
    <tr><th>Can it be killed?</th><td>Yes &mdash; tougher than a standard entity, and its health was reduced on 23 July 2026</td></tr>
    <tr><th>Achievement</th><td><em>Last Performance</em> &mdash; Kill a Marionette</td></tr>
  </table>
  <p class="src">Sources:
    <a href="https://gamerant.com/shift-at-midnight-all-monsters/" target="_blank" rel="noopener">Game Rant monster list</a>,
    <a href="https://gamerant.com/shift-at-midnight-jack-in-the-box-music-box-marionette-location/" target="_blank" rel="noopener">Game Rant music box guide</a>,
    <a href="https://steamcommunity.com/stats/3722330/achievements/" target="_blank" rel="noopener">Steam global achievement stats</a> (read 5 August 2026).</p>

  <h2>How to tell it is coming</h2>

  <p><strong>The long warning is an N.E.T. email.</strong> From Shift 9 the terminal flags the Marionette before the night starts, so you are never ambushed on a first appearance. Treat that email as your cue to buy ammunition and to walk the store once so you know where your traps already are.</p>

  <p><strong>The short warning is the music box itself.</strong> Somewhere in the building a wind-up box audibly starts playing, and that sound is the encounter beginning. The <a href="https://steamdb.info/patchnotes/24354120/" target="_blank" rel="noopener">23 July 2026 patch</a> increased the box&rsquo;s volume, so it is far easier to place by ear than it was at launch. Any launch-day guide calling the box hard to hear is out of date.</p>

  <h2>The three-melody clock</h2>

  <p>Once the box is playing you have until the melody has run three times. Get to it and hold <strong>E</strong> to rewind it before that third pass and the Marionette does not arrive at all. Let the melody complete three times and it does.</p>

  <p>That is why this encounter behaves so differently from the rest of the <a href="/monsters/">bestiary</a>. The <a href="/monsters/shrieking-doll/">Shrieking Doll</a> and the <a href="/monsters/demented/">Demented</a> are problems you solve when they are in front of you; the Marionette is one you solve before it exists, using an object in another room.</p>

  <div class="term warn">
    <div class="term-h">What we cannot confirm</div>
    <p>The confirmed requirement is that the box must not complete three melodies. No reliable source says whether one rewind settles it permanently or whether the box can wind down and restart later in the same shift, so we will not tell you either way. We are also not publishing melody lengths in seconds &mdash; there is no figure we can stand behind.</p>
  </div>

  <h2>Where the box actually spawns</h2>

  <p>The location is randomised per shift. The spawn areas that have been documented are the <strong>break room</strong>, the <strong>storage room</strong>, the <strong>bathroom</strong>, and the <strong>shelving aisles</strong> on the shop floor.</p>

  <p>So a fixed search route is the wrong approach &mdash; do not sweep the store in the same order every time. Walk toward the sound first, then check whichever of those four areas is nearest to where the audio is loudest.</p>

  <h2>If it arrives anyway: the fight</h2>

  <p>The Marionette can be killed. It is noticeably tougher than a standard entity, so this is an ammunition problem &mdash; going in with an empty gun is how a survivable fight becomes a fatal one. Teammates make it substantially easier.</p>

  <p>The 23 July patch <strong>reduced its health</strong>, which is why older advice reads as more dire than the fight now is: any ammo count written before 23 July describes a tougher monster than the one you will meet.</p>

  <div class="term tip">
    <div class="term-h">Lobby size, since 23 July</div>
    <p>Lobbies are now selectable up to <strong>six players</strong>, but the developer stated that the game &ldquo;is designed and has always been marketed around a maximum of 3 players&rdquo;, that larger lobbies &ldquo;may become chaotic&rdquo;, and that six is not recommended for a first playthrough. For this encounter, three is the number that lets one person own the box while the others hold the store. See <a href="/updates/">patch notes</a>.</p>
  </div>

  <h2>Common mistakes</h2>

  <ul>
    <li><strong>Treating it as a combat problem.</strong> Reflexes and a better weapon do not decide this encounter. An object in another room does.</li>
    <li><strong>Finishing the customer at the counter first.</strong> Since the <a href="https://store.steampowered.com/news/app/3722330/view/695394018676179340" target="_blank" rel="noopener">29 July patch</a> removed the patience mechanic, customers no longer run down a timer while you verify them &mdash; so the person at your counter can genuinely wait. The music box cannot.</li>
    <li><strong>Searching by memory instead of by ear.</strong> The spawn is random every shift. Your route from last night tells you nothing.</li>
    <li><strong>Assuming this is the final boss.</strong> It is not. <a href="/monsters/the-dentist/">The Dentist</a> is Shift 13, and nothing you learn here transfers &mdash; that one cannot be fought at all.</li>
  </ul>

  <h2>Which achievement this is tied to</h2>

  <p><em>Last Performance</em> &mdash; Kill a Marionette &mdash; sits at <strong>40.0%</strong>. Put that next to the other two straightforward monster kills: <em>Silenced</em> (Shrieking Doll) at <strong>89.2%</strong> and <em>Freed</em> (Demented) at <strong>78.8%</strong>.</p>

  <p>The gap is not about how often it appears &mdash; it announces itself by email and by sound. Two things separate it. The correct defensive play, rewinding the box, is also the play that denies you the kill, so cautious players never earn it. And it starts at Shift 9 of 13, so reaching it means getting most of the way through Story Mode, while the <a href="/achievements/">achievement curve</a> shows a heavy drop-off well before that. That second reading is ours, drawn from the published rates rather than any developer statement.</p>

  <p>If you want the achievement deliberately, let the melody play its three passes on purpose &mdash; on a shift that is otherwise under control, with ammunition already bought, rather than on a night that is already going badly.</p>

  <h2>What changed in the patches</h2>

  <ul>
    <li><strong>23 July 2026:</strong> Marionette health <strong>reduced</strong>, and Jack-in-the-Box volume <strong>increased</strong>. Both changes push the same way &mdash; the box is easier to find, and the fight is easier to win if you do not find it.</li>
    <li><strong>29 July 2026:</strong> the patience mechanic was removed, so walking away from a half-verified customer to deal with the box no longer costs you at the counter.</li>
  </ul>
  <p class="src">Patch sources: <a href="https://steamdb.info/patchnotes/24354120/" target="_blank" rel="noopener">SteamDB build 24354120</a> and the <a href="https://store.steampowered.com/news/app/3722330/view/695394018676179340" target="_blank" rel="noopener">29 July Steam announcement</a>. Full timeline on <a href="/updates/">updates</a>.</p>

  <div class="grid two">
    <a class="card danger" href="/monsters/jack-in-the-box/"><b>Jack-in-the-Box</b><span>The box itself &mdash; where it spawns and how to handle it.</span></a>
    <a class="card" href="/achievements/"><b>All achievements</b><span>Where Last Performance sits in the completion curve.</span></a>
  </div>
"""},
{
 "path": "monsters/the-dentist",
 "title": "Shift At Midnight The Dentist — The Shift 13 Chase Explained",
 "og_short": "Shift At Midnight The Dentist",
 "desc": "The Dentist arrives on the final shift and cannot be killed — weapons do nothing, traps do not stop him. The only correct play is to run to Sheriff Clyde.",
 "trail": M + [(None, "The Dentist")],
 "h1": "The Dentist",
 "lede": "The final shift&rsquo;s pursuer, and the only threat in the game with no counterplay at all. <strong>Your weapons do nothing to him and traps do not stop him.</strong> You survive Shift 13 by running until Sheriff Clyde ends it in a cutscene &mdash; there is no second method.",
 "body": """
  <div class="tags">
    <span class="tag red">Hostile &mdash; final shift</span>
    <span class="tag red">Cannot be killed</span>
    <span class="tag amber">Shift 13</span>
    <span class="tag">No achievement of its own</span>
  </div>

  <div class="term warn">
    <div class="term-h">Do not try to fight this</div>
    <p>The Dentist is described as <strong>completely immune to your weapons</strong>, and <strong>traps do not stop him</strong>. The only stated option is to keep running until <strong>Sheriff Clyde</strong> deals with him in a cutscene. If your instinct when something comes through the door is to reach for the arsenal, this is the encounter that punishes it.</p>
    <p class="src">Source: <a href="https://gamerant.com/shift-at-midnight-all-monsters/" target="_blank" rel="noopener">Game Rant monster list</a>.</p>
  </div>

  <h2>When he arrives</h2>

  <p>The Dentist is the <strong>Shift 13</strong> encounter &mdash; the last night of Story Mode. He is not a random spawn you might dodge on a good run, and he is not something you can prepare for by buying better gear during the preceding shifts.</p>

  <p>He is also not a surprise. He appears earlier in the story in forms that pose no threat, and the game foreshadows him repeatedly before the final night. That build-up is the point: by the time he is actually chasing you, you are expected to already know who he is, which is why the game never bothers explaining him mid-chase.</p>

  <h2>Everything you normally rely on is dead weight</h2>

  <p>It is worth being specific about which tools fail, because the failure is not partial.</p>

  <table class="facts">
    <tr><th>Firearms and melee</th><td>Confirmed ineffective &mdash; he is described as immune</td></tr>
    <tr><th>Traps</th><td>Confirmed ineffective &mdash; they do not stop him</td></tr>
    <tr><th>Barricades</th><td>No reliable source either way. We are not claiming they work or that they do not.</td></tr>
    <tr><th>Sheriff Clyde</th><td>The only thing that ends the encounter, and it happens in a cutscene</td></tr>
  </table>

  <p>Compare that with the rest of the roster and the difference is stark. The <a href="/monsters/shrieking-doll/">Shrieking Doll</a> dies to a few shots. The <a href="/monsters/marionette/">Marionette</a> is tanky but killable. Even the <a href="/monsters/demented/">Demented</a>, which cannot be shot down, has a defined solution involving traps. The Dentist has no equivalent. Every honest piece of guidance about him is about movement.</p>

  <h2>What to do, step by step</h2>

  <ol>
    <li><strong>Stop treating the shift as a job.</strong> Quota, shelves and the counter are over. Nothing you do at the register affects this.</li>
    <li><strong>Move toward Sheriff Clyde and keep moving.</strong> He is the resolution, so distance from him is the thing that is actually costing you.</li>
    <li><strong>Do not hide.</strong> Hiding is the correct instinct against a hunt; it is the wrong one here, because nothing ends the encounter except reaching the cutscene.</li>
    <li><strong>Do not stop to look back.</strong> Turning to check costs you the only resource you have.</li>
  </ol>

  <p class="src">Steps 2&ndash;4 &mdash; run straight for Clyde, do not hide, do not look back &mdash; are <strong>reported by a single source and not independently confirmed</strong>: <a href="https://www.neonlightsmedia.com/blog/shift-at-midnight-monsters-dentist-guide" target="_blank" rel="noopener">Neon Lights Media</a>. The immunity to weapons and traps is the part corroborated elsewhere.</p>

  <h2>Common mistakes</h2>

  <ul>
    <li><strong>Spending the last shift&rsquo;s money on weapons.</strong> Gear does nothing here, and money is the variable that decides which ending you get &mdash; see below.</li>
    <li><strong>Applying the Demented playbook.</strong> Holding your gaze on a threat freezes a <a href="/monsters/demented/">Demented</a>. There is no source saying it does anything to the Dentist, and standing still to find out is how the chase ends.</li>
    <li><strong>Trying to verify him.</strong> He is not a <a href="/guide/doppelgangers/">doppelganger</a> and he is not a counter problem. There is nothing to scan.</li>
    <li><strong>Laying traps in advance.</strong> Traps are confirmed not to stop him. Preparation time spent on them is time you did not spend banking money.</li>
  </ul>

  <h2>Which achievement this is tied to</h2>

  <p>The Dentist has <strong>no achievement of his own</strong> &mdash; there is no "kill the Dentist", because you cannot. What he is tied to is the <em>True Ending</em>, held by <strong>15.4%</strong> of players.</p>

  <p>The two variables are decided elsewhere. After Shift 12 you choose whether to call Sheriff Clyde, and at the end of Shift 13 the game checks whether your personal savings are <strong>$250 or more</strong>. Not calling Clyde and finishing with at least $250 produces the True Ending, in which the Dentist appears and Clyde helps destroy him, and both Clyde and your pet survive. Calling him instead gives <em>Grave Decision</em> (<strong>31.4%</strong>), where Clyde dies. Not calling him with under $250 gives <em>Empty Home</em> (<strong>9.4%</strong>).</p>

  <p>So the practical takeaway for this page is blunt: <strong>how you handle the chase does not change your ending &mdash; the choice after Shift 12 and your bank balance do.</strong> Full breakdown on the <a href="/endings/">endings page</a>.</p>
  <p class="src">Ending conditions: <a href="https://www.keengamer.com/articles/guides/shift-at-midnight-how-to-get-all-endings/" target="_blank" rel="noopener">KeenGamer</a>. Unlock rates: <a href="https://steamcommunity.com/stats/3722330/achievements/" target="_blank" rel="noopener">Steam global stats</a>, read 5 August 2026.</p>

  <h2>What changed in the patches</h2>

  <p>No patch since launch has touched the Dentist directly. Two changes affect the run that leads to him. The <a href="/updates/">29 July patch</a> removed the patience mechanic, so verifying customers in the shifts beforehand is no longer timed &mdash; which matters because careful verification is how you avoid losing money and shifts on the way to the $250 threshold. The 23 July patch raised the lobby ceiling to six players, though the developer still designs around three.</p>

  <div class="grid two">
    <a class="card" href="/endings/"><b>All three endings</b><span>The Clyde call, the $250 check, and what each one costs.</span></a>
    <a class="card" href="/guide/survival/"><b>Survival guide</b><span>Barricades and hiding &mdash; and the one night they do not apply.</span></a>
  </div>
"""},
{
 "path": "monsters/jack-in-the-box",
 "title": "Shift At Midnight Jack-in-the-Box — Music Box Locations &amp; Rewind",
 "og_short": "Shift At Midnight Jack-in-the-Box",
 "desc": "The Jack-in-the-Box is not a monster — it is the wind-up music box that summons the Marionette after three melodies. Where it spawns, and how to rewind it.",
 "trail": M + [(None, "Jack-in-the-Box")],
 "h1": "Jack-in-the-Box",
 "lede": "Listed as a monster almost everywhere, and it is not one. The Jack-in-the-Box is a <strong>wind-up music box &mdash; a trigger object</strong>. Let its melody play three times and it summons the <a href=\"/monsters/marionette/\">Marionette</a>; rewind it in time and nothing arrives.",
 "body": """
  <div class="tags">
    <span class="tag green">Item, not a monster</span>
    <span class="tag amber">Summons the Marionette</span>
    <span class="tag">From Shift 9</span>
    <span class="tag">Random spawn</span>
  </div>

  <div class="term warn">
    <div class="term-h">The correction</div>
    <p>The Jack-in-the-Box does not attack you, does not chase you, and is not part of the bestiary. <strong>It is an object with a timer.</strong> Guides that list it as a separate enemy alongside the <a href="/monsters/demented/">Demented</a> and the <a href="/monsters/shrieking-doll/">Shrieking Doll</a> have miscounted the roster &mdash; there is one threat here, the Marionette, and this is the switch that turns it on.</p>
  </div>

  <h2>What it actually does</h2>

  <p>From Shift 9 onwards, a wind-up music box can be present somewhere in the store. When it starts playing you are on a count: <strong>three complete melodies summons the Marionette</strong>. Reach the box and <strong>hold E to rewind it</strong> before that third pass, and the encounter never happens.</p>

  <p>That makes it one of the few objects in the game whose entire value is negative &mdash; you gain nothing by interacting with it, you only avoid something. It is closer to a fire alarm than to a weapon, and the correct relationship with it is to know where it is and to silence it quickly.</p>
  <p class="src">Mechanic and locations: <a href="https://gamerant.com/shift-at-midnight-jack-in-the-box-music-box-marionette-location/" target="_blank" rel="noopener">Game Rant music box guide</a>.</p>

  <h2>Where it spawns</h2>

  <p>The position is randomised, so there is no route to memorise. These are the areas that have been documented:</p>

  <table class="facts">
    <tr><th>Break room</th><td>Staff area &mdash; usually the fastest to clear because it is small</td></tr>
    <tr><th>Storage room</th><td>The worst case: cluttered, and far from the counter</td></tr>
    <tr><th>Bathroom</th><td>Easy to overlook entirely if you are sweeping the shop floor first</td></tr>
    <tr><th>Shelving aisles</th><td>On the shop floor, where shelving muffles and bounces the sound</td></tr>
  </table>

  <p>Because it is random per shift, sound beats memory every time. Walk toward the audio rather than running a fixed circuit &mdash; a circuit costs you the same amount of time whether the box is in the first room or the last.</p>

  <h2>The 23 July change that matters most</h2>

  <p>The <a href="https://steamdb.info/patchnotes/24354120/" target="_blank" rel="noopener">23 July 2026 patch</a> <strong>increased the Jack-in-the-Box&rsquo;s volume</strong>. This is the single most useful change the game has had for this mechanic, because locating the box by ear <em>is</em> the counterplay &mdash; and at launch it was quiet enough that players lost the melody count while searching.</p>

  <p>The practical test: if the box is hard to hear on your build, you are not on a current version. The same patch also reduced the Marionette&rsquo;s health, so the failure case is less severe than it used to be as well. See the <a href="/updates/">patch timeline</a>.</p>

  <h2>Rewind it, or let it ring?</h2>

  <p>There is a genuine decision here, and it depends on what you want from the night.</p>

  <ul>
    <li><strong>Rewind it</strong> if you want to finish the shift. This is the safe play, and it costs you nothing except the walk.</li>
    <li><strong>Let it ring three times</strong> if you are chasing <em>Last Performance</em> (Kill a Marionette, <strong>40.0%</strong> of players). You cannot get that achievement while doing the safe thing, which is a large part of why it is the rarest non-hidden achievement in the game.</li>
  </ul>

  <p>If you do go for it, do it deliberately: on a shift that is otherwise calm, with ammunition already purchased, and ideally with teammates. Deciding halfway through the third melody is the worst of both options.</p>

  <h2>Who owns the box in co-op</h2>

  <p>This is the one mechanic in the game that survives being delegated, so delegate it. One player takes the box for the duration and calls the melody count out loud over proximity chat; everyone else keeps serving customers and stays out of the search. Three people half-listening to the same melody is worse than one person listening properly, because nobody ends up certain how many passes have gone by.</p>

  <p>Lobbies have been selectable up to <strong>six players</strong> since 23 July, but the developer was explicit that the game &ldquo;is designed and has always been marketed around a maximum of 3 players&rdquo; and that bigger lobbies &ldquo;may become chaotic&rdquo;. For a mechanic that is decided by hearing one quiet object, extra players are extra footsteps and extra voices. Three is the right number here. More on the <a href="/multiplayer/#co-op">co-op guide</a>.</p>

  <h2>Common mistakes</h2>

  <ul>
    <li><strong>Treating it as an enemy.</strong> Players who think it will spring out and attack them keep their distance. Distance is exactly wrong &mdash; you need to be standing on it.</li>
    <li><strong>Serving the customer first.</strong> Since the 29 July patch there is no patience meter, so the person at your counter will wait indefinitely. The box will not.</li>
    <li><strong>Searching visually.</strong> The box announces itself with audio and nothing else. Sweeping rooms with your eyes while the melody plays wastes the one signal you have.</li>
    <li><strong>Assuming it is present every shift.</strong> It is tied to Shift 9 onwards, and the N.E.T. email is the advance warning. Before that point there is nothing to look for.</li>
  </ul>

  <div class="grid two">
    <a class="card danger" href="/monsters/marionette/"><b>Marionette</b><span>What arrives if the melody finishes, and how to fight it.</span></a>
    <a class="card" href="/achievements/"><b>All achievements</b><span>Last Performance and the rest of the completion curve.</span></a>
  </div>
"""},
{
 "path": "monsters/norbert",
 "title": "Shift At Midnight Norbert — Spare Him or Kill Him?",
 "og_short": "Shift At Midnight Norbert",
 "desc": "Norbert is a gnome doppelganger whose ID scans as fake and who gets flagged by the system — and he is not lethal. Sparing him ends it. Killing him brings him back.",
 "trail": M + [(None, "Norbert")],
 "h1": "Norbert",
 "lede": "A small, magical and extremely annoying gnome. His ID scans as fake and the system flags him as a <a href=\"/guide/doppelgangers/\">doppelganger</a> &mdash; both of which are true without him being dangerous. <strong>Killing him is the trap, not the solution.</strong>",
 "body": """
  <div class="tags">
    <span class="tag amber">Doppelganger &mdash; customer type</span>
    <span class="tag green">Not lethal</span>
    <span class="tag red">Flagged by the system</span>
  </div>

  <div class="term tip">
    <div class="term-h">Short answer</div>
    <p>Let him buy his things and leave. He is <strong>a doppelganger</strong> &mdash; the scanner is not malfunctioning &mdash; but he is a prankster rather than a predator, and shooting him is the expensive option.</p>
  </div>

  <h2>He really is a doppelganger</h2>

  <p>This is where a lot of coverage gets Norbert wrong, in both directions. Some pages call him a monster; others insist he is an ordinary customer and the flag is a bug. Neither is right.</p>

  <p>Norbert is catalogued among the game&rsquo;s doppelgangers &mdash; specifically described as <em>a magical, annoying gnome</em> &mdash; and when you scan him his documents come back fake and the system marks him as a doppelganger. Everything your training says should be true of a threat is true of him on paper. He simply is not violent.</p>
  <p class="src">Classification: <a href="https://www.dualshockers.com/shift-at-midnight-all-doppelgangers/" target="_blank" rel="noopener">DualShockers doppelganger catalogue</a>, which documents 47 named doppelgangers and the tell for each.</p>

  <h2>Which shift does he appear on?</h2>

  <p>We do not know, and we have removed the claim that used to sit on this page. You will find pages pinning Norbert to a specific night &mdash; Night 2 is the number that circulates &mdash; but no source we can verify supports it, and Story Mode&rsquo;s customers and events are <strong>procedurally generated</strong> across its 13 shifts. A fixed night-by-night appearance table is not something the game&rsquo;s own structure supports, so treat any site that publishes one with suspicion.</p>

  <p>What that means in practice: do not plan around meeting him at a particular point. Recognise him when he appears instead.</p>

  <h2>Spare him or kill him</h2>

  <table class="facts">
    <tr><th>Spare him</th><td>He completes his purchase, leaves, and does not appear again for the rest of the shift.</td></tr>
    <tr><th>Kill him</th><td>He comes back &mdash; repeatedly, in different disguises. Reported returns include a poisoned lemonade stand, a motorcycle stunt, and an appearance disguised as a girl. The harassment is described as pranks rather than lethal attacks.</td></tr>
  </table>
  <p class="src">The consequences of killing Norbert are <strong>reported by a single source and not independently confirmed</strong>: <a href="https://allthings.how/shift-at-midnight-what-sparing-norbert-does-to-your-shift/" target="_blank" rel="noopener">allthings.how</a>. We have not published a full behaviour list because there is only one account of it.</p>

  <p>Read as a design decision, the asymmetry is the whole point. Sparing him ends the interaction in about fifteen seconds. Killing him converts one customer into a recurring interruption that runs across the rest of your shift, at exactly the times you need to be paying attention to something else.</p>

  <h2>One thing we cannot reconcile</h2>

  <div class="term warn">
    <div class="term-h">Flagging a genuine conflict in the sources</div>
    <p>The general rule for this game is that <strong>letting any doppelganger complete its checkout and leave</strong> causes it to return that night in monster form to hunt you. The Norbert reporting says the opposite for him specifically &mdash; that he leaves and does not reappear for the rest of the shift. We cannot tell you which behaviour wins, because no source addresses the contradiction directly. Treat &ldquo;Norbert is a safe release&rdquo; as likely but not proven, and do not extrapolate it to any other doppelganger.</p>
  </div>

  <h2>Common mistakes</h2>

  <ul>
    <li><strong>Killing on suspicion.</strong> <em>First Blood</em> &mdash; kill your first customer &mdash; is the most common achievement in the game at <strong>96.6%</strong>. Almost everybody does this, and Norbert is where a lot of players spend it.</li>
    <li><strong>Trusting the flag as a threat readout.</strong> The scanner reports on documents. It does not report on danger. <a href="/monsters/the-dentist/">The Dentist</a> is the same lesson inverted &mdash; genuinely lethal and not a counter problem at all.</li>
    <li><strong>Rushing the check.</strong> Since the <a href="/updates/">29 July patch</a> removed the patience mechanic, customers no longer run down a timer while you verify them. The main reason players used to shoot first is gone.</li>
    <li><strong>Spending ammunition on him.</strong> Ammunition is for the <a href="/monsters/marionette/">Marionette</a> and the <a href="/monsters/shrieking-doll/">Shrieking Doll</a>. Norbert costs you rounds and gives you nothing.</li>
  </ul>

  <h2>How to verify him properly</h2>

  <p>Norbert is a good practice case precisely because the answer is not the one the evidence suggests. Run the full check anyway &mdash; scan the ID card or search the name manually in the N.E.T. database, look for a barcode, and compare what the record says about occupation, appearance and purchase habits against what is standing in front of you. Doing that on a customer who turns out to be harmless is how the routine becomes automatic before it matters. The seven categories of tell are broken down on the <a href="/guide/doppelgangers/">doppelganger identification guide</a>.</p>

  <h2>Does he affect your ending?</h2>

  <p>No. This is worth stating plainly because the speculation is everywhere. The three endings are decided by two things: <strong>whether you call Sheriff Clyde after Shift 12</strong>, and whether your personal savings are <strong>$250 or more</strong> at the end of Shift 13. <em>True Ending</em> sits at <strong>15.4%</strong>, <em>Grave Decision</em> at <strong>31.4%</strong> and <em>Empty Home</em> at <strong>9.4%</strong>, and none of them is gated on who you shot at the counter. See the <a href="/endings/">endings page</a>.</p>

  <div class="grid two">
    <a class="card" href="/guide/doppelgangers/"><b>Doppelganger identification</b><span>The seven tells, the database, and the Anomaly Lens.</span></a>
    <a class="card danger" href="/monsters/the-dentist/"><b>The Dentist</b><span>The threat the scanner will never warn you about.</span></a>
  </div>
"""},
{
 "path": "monsters/shrieking-doll",
 "title": "Shift At Midnight Shrieking Doll — How to Kill It (Silenced)",
 "og_short": "Shift At Midnight Shrieking Doll",
 "desc": "The Shrieking Doll shows up during hunts alongside the Entities. It is fragile — a few shots end it — but every shot you fire tells everything else in the store where you are.",
 "trail": M + [(None, "Shrieking Doll")],
 "h1": "Shrieking Doll",
 "lede": "The most fragile threat in the game, and the easiest monster achievement in it &mdash; <strong>89.2%</strong> of players have <em>Silenced</em>. It is best understood as a <strong>distraction rather than a main threat</strong>. The danger is not the doll; it is what killing the doll costs you.",
 "body": """
  <div class="tags">
    <span class="tag red">Hostile</span>
    <span class="tag green">Fragile &mdash; a few shots</span>
    <span class="tag amber">Achievement: Silenced</span>
    <span class="tag">89.2% of players</span>
  </div>

  <h2>It does not arrive on its own</h2>

  <p>This is the fact that reframes the whole encounter: the Shrieking Doll typically appears <strong>during a hunt, alongside the Entities</strong>. It is not a standalone event you deal with in an otherwise quiet store. By the time you are looking at one, something considerably more dangerous is already in the building with you.</p>

  <p>Hunts themselves start when you let a doppelganger complete its checkout and walk out of the store &mdash; it returns that night in monster form to hunt you. So the doll is downstream of a decision you made at the counter, and the <a href="/guide/doppelgangers/">verification guide</a> is the real prevention for it.</p>
  <p class="src">Behaviour and hunt trigger: <a href="https://gamerant.com/shift-at-midnight-all-monsters/" target="_blank" rel="noopener">Game Rant monster list</a>.</p>

  <h2>How it finds you</h2>

  <p>The doll is small and moves by crawling low along the ground, and it is described as locating you by <strong>line of sight</strong> rather than by sound. Low movement matters in a shop full of shelving, because a crawler has sightlines under and between fixtures that a standing figure does not, and the cover you instinctively read as safe is cover for waist height and above.</p>
  <p class="src">The crawling movement and the sight-based detection are <strong>reported by a single source and not independently confirmed</strong>: <a href="https://www.neonlightsmedia.com/blog/shift-at-midnight-monsters-dentist-guide" target="_blank" rel="noopener">Neon Lights Media</a>. Despite the name, we have not found a verifiable description of a scream that lures you &mdash; so we are not describing one.</p>

  <h2>Killing it is trivial. Killing it quietly is the problem.</h2>

  <p>It goes down in a few shots. That is the entire combat picture, and it is why <em>Silenced</em> is held by nearly nine players in ten.</p>

  <div class="term warn">
    <div class="term-h">The cost you are actually paying</div>
    <p>Staying quiet is what keeps you alive during a hunt &mdash; noise gives away your position. Firing a weapon at the doll is noise, and it can pull other threats to you. So the doll is cheap to kill and potentially very expensive to kill <em>at the wrong moment</em>, while the Entity that came with it is still looking for you.</p>
    <p class="src">The noise-attracts-threats point is <strong>reported by a single source and not independently confirmed</strong> (Neon Lights Media). That it is a minor threat rather than a primary one is corroborated by Game Rant.</p>
  </div>

  <h2>What to do, step by step</h2>

  <ol>
    <li><strong>Register what else is in the building first.</strong> A doll on its own is unusual; assume a hunt is running.</li>
    <li><strong>Decide whether it is worth a shot right now.</strong> If it has not seen you and the Entity is close, moving is better than firing.</li>
    <li><strong>If you engage, engage immediately and finish it.</strong> A few shots is the budget. Trading half a magazine at range is the worst outcome &mdash; full volume, no kill.</li>
    <li><strong>Move after firing.</strong> Whatever the shot told the store, it told it about where you were standing, not where you are now.</li>
  </ol>

  <h2>Common mistakes</h2>

  <ul>
    <li><strong>Treating it as the threat.</strong> It is the least dangerous thing in the room during a hunt. Chasing it while an Entity hunts you is how a survivable night ends.</li>
    <li><strong>Shooting on reflex from a bad position.</strong> Same kill, much worse timing.</li>
    <li><strong>Hiding above floor level.</strong> If the detection really is sight-based from a low crawl, crouching behind low shelving may put you directly in its line rather than out of it. Single-source caveat applies &mdash; treat it as a reason to keep moving rather than a rule.</li>
    <li><strong>Attempting <em>Relentless</em> on the wrong night.</strong> Never on a <a href="/monsters/the-dentist/">Dentist</a> shift &mdash; that one cannot be killed at all.</li>
  </ul>

  <h2>Which achievements this is tied to</h2>

  <p><em>Silenced</em> (Kill a Shrieking Doll) sits at <strong>89.2%</strong>, third behind <em>First Blood</em> at 96.6% and <em>Still Breathing</em> at 93.4%. If you have played more than a couple of shifts you almost certainly have it.</p>

  <p>The more interesting target is <em>Relentless</em> &mdash; finish a hunt within 30 seconds &mdash; at <strong>44.3%</strong>. The doll is the sensible monster to build that attempt around, because it is the one threat you can reliably delete in a couple of shots rather than one you have to find first. Compare with <em>Last Performance</em> at 40.0% for the <a href="/monsters/marionette/">Marionette</a>, where the fight itself is the obstacle. Full list on <a href="/achievements/">achievements</a>.</p>

  <h2>What changed in the patches</h2>

  <p>No patch has altered the Shrieking Doll itself. One change matters indirectly: the <a href="/updates/">29 July patch</a> added a second purchasable firearm, which gives you another option for the quick kill. Ammunition discipline is the same as before &mdash; a bigger arsenal does not make gunfire quieter.</p>

  <p>The 23 July patch is worth a thought too. Lobbies are now selectable up to six players, although the developer still states the game &ldquo;is designed and has always been marketed around a maximum of 3 players&rdquo; and warns that larger lobbies &ldquo;may become chaotic&rdquo;. If noise discipline is what keeps a hunt survivable, six people each free to open fire on a doll is a harder problem to manage than three. That last inference is ours, not the developer&rsquo;s.</p>

  <div class="grid two">
    <a class="card" href="/guide/survival/"><b>Survival guide</b><span>Noise, barricades and traps during a hunt.</span></a>
    <a class="card" href="/monsters/demented/"><b>Demented</b><span>The threat that will not die to gunfire at all.</span></a>
  </div>
"""},
{
 "path": "monsters/demented",
 "title": "Shift At Midnight Demented — Freeze It, Then Trap It (Freed)",
 "og_short": "Shift At Midnight Demented",
 "desc": "The Demented stops moving while you look straight at it, and you cannot simply shoot it down. The confirmed answer is to break your gaze and lead it into a trap.",
 "trail": M + [(None, "Demented")],
 "h1": "Demented",
 "lede": "The one threat that plays by Weeping Angel rules: <strong>as long as you look straight at it, it does not move</strong>. It is also the one you cannot simply shoot down &mdash; the confirmed solution is to break your gaze and lead it into a trap. <strong>78.8%</strong> of players have <em>Freed</em>.",
 "body": """
  <div class="tags">
    <span class="tag red">Hostile</span>
    <span class="tag amber">Freezes while observed</span>
    <span class="tag red">Not killable by gunfire</span>
    <span class="tag">78.8% have Freed</span>
  </div>

  <div class="term warn">
    <div class="term-h">The mechanic in one sentence</div>
    <p><strong>While you are looking directly at the Demented, it cannot move &mdash; and you cannot damage it either.</strong> That combination is what makes it awkward: the state that keeps you safe is also the state in which you can do nothing to it. The confirmed way to remove one is to look away and lure it into a trap.</p>
    <p class="src">Source: <a href="https://gamerant.com/shift-at-midnight-all-monsters/" target="_blank" rel="noopener">Game Rant monster list</a>.</p>
  </div>

  <h2>Why the standard approach fails</h2>

  <p>Everything else in the <a href="/monsters/">bestiary</a> sorts into two buckets. Some things die to gunfire &mdash; the <a href="/monsters/shrieking-doll/">Shrieking Doll</a> in a few shots, the <a href="/monsters/marionette/">Marionette</a> with enough ammunition. Some things cannot be fought at all, like <a href="/monsters/the-dentist/">the Dentist</a>. The Demented is in neither bucket. It can be removed, but not by you directly.</p>

  <p>So the resource that matters here is not ammunition. It is <strong>knowing where your traps are</strong> before the encounter starts, because the trap does the work and your only job is aiming the Demented at it.</p>

  <div class="term tip">
    <div class="term-h">What is confirmed and what is not</div>
    <p>Confirmed: it does not move while observed, and luring it into a trap is a working solution. <strong>Not confirmed:</strong> whether weapons can damage it under any circumstances at all. Sources describe the trap route and nothing else, so that is the only method we will publish. If you see a page quoting a weapon or a damage number for this entity, it is not coming from anywhere we could verify.</p>
  </div>

  <h2>What to do, step by step</h2>

  <ol>
    <li><strong>Look at it and keep looking.</strong> This buys you time at zero cost. Nothing about the encounter gets worse while your eyes are on it.</li>
    <li><strong>Work out where your nearest trap is</strong> while it is frozen. If the answer is &ldquo;I do not have one placed&rdquo;, that is the real problem, and it was created earlier in the shift.</li>
    <li><strong>Reposition so the trap sits between you and it.</strong> You are not running away from it &mdash; you are arranging the room so that its path to you runs through the trap.</li>
    <li><strong>Break the gaze deliberately, not accidentally.</strong> Looking away is what lets it advance, so do it when the geometry is right rather than when you panic.</li>
  </ol>

  <p class="src">Steps 1 and 4 restate the confirmed mechanic. The ordering in steps 2 and 3 is our reasoning from the two confirmed facts &mdash; it freezes while watched, and the trap is the solution &mdash; rather than a sequence lifted from a published guide.</p>

  <p>This is the one encounter where a second player changes the shape of the problem rather than just adding damage. One person holds the gaze &mdash; that is their entire job, and they do not move &mdash; while the other sets or repositions the trap without any time pressure at all. Nothing advances while the watcher watches. Note that this follows from the confirmed freeze mechanic; we have not seen it written up as an official tactic. See the <a href="/multiplayer/#co-op">co-op guide</a>.</p>

  <h2>The sources disagree about its speed</h2>

  <p>One account describes the Demented as the <strong>fastest-moving threat in the game</strong>; another does not characterise it that way at all. Both agree on the part that decides the encounter, which is that it cannot act while you are watching it.</p>

  <p>The practical reading: assume it is fast. If the faster description is right, the cost of assuming so is nothing; if it is wrong, you have simply been careful with your positioning. Do not treat the gap between you as time in the bank.</p>

  <h2>It is not rare</h2>

  <p>You will find this one described as an uncommon encounter. The achievement data does not support that. <em>Freed</em> &mdash; Kill a Demented &mdash; is held by <strong>78.8%</strong> of players, which is more than the share who have killed a <a href="/monsters/marionette/">Marionette</a> (40.0%) and roughly four players in five overall. Something four in five players have done is not rare, and planning your shift on the assumption you probably will not meet one is a bad plan.</p>
  <p class="src">Unlock rates from <a href="https://steamcommunity.com/stats/3722330/achievements/" target="_blank" rel="noopener">Steam global achievement stats</a>, read 5 August 2026.</p>

  <h2>Common mistakes</h2>

  <ul>
    <li><strong>Emptying a magazine into it.</strong> The one thing every source agrees you cannot do. The noise also tells the rest of the hunt where you are.</li>
    <li><strong>Turning to run.</strong> Turning away is precisely the input that unfreezes it. Back off while facing it instead.</li>
    <li><strong>Having no trap placed.</strong> The encounter is lost during the calm part of the shift, not during the encounter.</li>
    <li><strong>Blinking through a door.</strong> Losing line of sight around a corner has the same effect as looking away, so doorways and aisle ends are where a controlled retreat quietly stops being controlled.</li>
  </ul>

  <h2>What changed in the patches</h2>

  <p>Neither the 23 July nor the 29 July patch touched the Demented. The 23 July patch reduced Marionette health and raised music box volume; the 29 July patch added a second firearm, added the Rake to endless and post-story modes only, and removed the patience mechanic. None of that changes how you handle a Demented &mdash; a second gun is still a gun. Timeline on <a href="/updates/">updates</a>.</p>

  <div class="grid two">
    <a class="card" href="/guide/survival/"><b>Survival guide</b><span>Trap placement, barricades and hunt discipline.</span></a>
    <a class="card" href="/achievements/"><b>All achievements</b><span>Where Freed sits on the completion curve.</span></a>
  </div>
"""},
{
 "path": "endings",
 "active": "/endings/",
 "title": "Shift At Midnight Endings — All 3 Endings and How to Get Them",
 "og_short": "Shift At Midnight Endings",
 "desc": "All three Shift At Midnight endings hinge on two things: whether you call Sheriff Clyde after Shift 12, and whether you finish Shift 13 with $250. True Ending sits at 15.4%.",
 "trail": [(None, "Endings")],
 "h1": "Shift At Midnight endings",
 "lede": "Three endings, decided by exactly two variables: <strong>whether you call Sheriff Clyde after Shift 12</strong>, and <strong>whether your savings are $250 or more when Shift 13 ends</strong>. <em>Grave Decision</em> sits at 31.4%, <em>True Ending</em> at 15.4%, <em>Empty Home</em> at 9.4%.",
 "body": """
  <div class="term tip">
    <div class="term-h">If you only read one paragraph</div>
    <p>For the <strong>True Ending</strong>: when the game offers you the choice after Shift 12, <strong>do not call Sheriff Clyde</strong>, and make sure you finish Shift 13 holding <strong>at least $250</strong>. Both conditions, or you get one of the other two outcomes instead.</p>
  </div>

  <h2>The two variables</h2>

  <p>Everything about the ending comes down to a decision and a number.</p>

  <p><strong>The decision</strong> happens after Shift 12: you either call Sheriff Clyde or you do not. Calling him settles the ending on its own &mdash; your money stops mattering entirely at that point.</p>

  <p><strong>The number</strong> is your personal savings at the <em>end</em> of Shift 13, checked against a $250 threshold. This only comes into play if you did not call Clyde, and it is what separates the best ending from the worst one.</p>

  <h2>All three endings</h2>

  <div class="tablewrap">
  <table class="data">
    <thead><tr><th>Ending</th><th>Condition</th><th>What happens</th><th>Steam unlock</th><th>Xbox</th></tr></thead>
    <tbody>
      <tr><td><strong>Grave Decision</strong></td><td>Call Clyde after Shift 12 (money irrelevant)</td><td>Your pet gets the surgery and survives. <strong>Clyde dies.</strong></td><td class="num">31.4%</td><td class="num">100G</td></tr>
      <tr><td><strong>True Ending</strong></td><td>Do <em>not</em> call Clyde <strong>and</strong> finish with $250 or more</td><td>Pet and Clyde both survive. The Dentist appears and Clyde helps destroy him.</td><td class="num">15.4%</td><td class="num">200G</td></tr>
      <tr><td><strong>Empty Home</strong></td><td>Do <em>not</em> call Clyde <strong>and</strong> finish under $250</td><td>Clyde survives, but you cannot pay for the surgery. <strong>Your pet dies.</strong></td><td class="num">9.4%</td><td class="num">100G</td></tr>
    </tbody>
  </table>
  </div>
  <p class="src">Conditions and outcomes: <a href="https://www.keengamer.com/articles/guides/shift-at-midnight-how-to-get-all-endings/" target="_blank" rel="noopener">KeenGamer endings guide</a>. Unlock rates: <a href="https://steamcommunity.com/stats/3722330/achievements/" target="_blank" rel="noopener">Steam global achievement stats</a>, read 5 August 2026. All three achievements are hidden on Steam.</p>

  <p class="updated">Corrected 5 August 2026 &mdash; this page previously listed 26.0% / 13.4% / 7.0%</p>

  <h2>The shape of the choice</h2>

  <p>What makes this good design is that calling Clyde is not obviously wrong. It saves your pet with no financial requirement attached, which means it is the reliable option for a run that went badly. The price is Clyde&rsquo;s life, and you pay it after the choice is locked.</p>

  <p>Not calling him is the greedy line. You keep Clyde alive and you keep the possibility of the best outcome, but you have staked it on a number you may not hit &mdash; and <em>Empty Home</em>, at 9.4%, is what a failed attempt at the True Ending looks like. The two rarest achievements in the game are the two halves of the same gamble.</p>

  <h2>What the unlock rates actually say</h2>

  <p>Add the three together and you get 56.2%, but that is not a completion rate: a player who replays can hold more than one, so the real share of players who have finished the story at all is lower. Set against <em>Still Breathing</em> (survive your first hunt) at <strong>93.4%</strong>, the picture is clear enough &mdash; most people who buy this game never reach Shift 12.</p>

  <p><em>Grave Decision</em> being twice as common as <em>True Ending</em> is the more interesting number. It suggests the safe branch is the default choice for players reaching the end for the first time, which is what you would expect when one option guarantees a survivable outcome and the other depends on how well the last thirteen shifts went financially.</p>

  <h2>Can you see all three in one run?</h2>

  <p>No. The conditions are mutually exclusive within a single playthrough &mdash; you either call Clyde or you do not, and your closing balance is either above the threshold or below it. Collecting all three achievements takes a minimum of three completed runs of Story Mode.</p>

  <p>If you are doing exactly that, the efficient order is to take the True Ending first while you still care about the money, then use the two follow-up runs for the outcomes that require no financial target at all. That sequencing is our suggestion rather than anything the game states.</p>

  <h2>Common mistakes</h2>

  <ul>
    <li><strong>Checking your balance at the decision point.</strong> The threshold is tested at the <em>end of Shift 13</em>, not when you decide about Clyde. Money you spend during the final shift still counts against you.</li>
    <li><strong>Buying weapons for the last night.</strong> Shift 13 is <a href="/monsters/the-dentist/">the Dentist</a>, and he is immune to weapons and unaffected by traps. Gear bought for that night does nothing except move you further from $250.</li>
    <li><strong>Assuming the chase decides the ending.</strong> It does not. How well you run on Shift 13 is not one of the two variables.</li>
    <li><strong>Calling Clyde &ldquo;just to be safe&rdquo; while already above $250.</strong> That converts a True Ending you had already earned into <em>Grave Decision</em>.</li>
    <li><strong>Expecting endings in Endless Mode.</strong> All three are Story Mode outcomes. Endless unlocks after you finish the story and does not have its own ending.</li>
  </ul>

  <h2>How to bank the $250</h2>

  <p>Here we have to stop short. Beyond the $250 threshold itself, we have not found verifiable figures for nightly quotas, item prices or weapon costs, so we are not going to publish a money route with invented numbers in it. What we can say is structural: money you do not spend is money you keep, and the two spending categories that most often eat the buffer are ammunition and weapons.</p>

  <p>One patch genuinely helps here. The <a href="/updates/">29 July update</a> removed the patience mechanic, so customers no longer run down a timer while you verify them. Rushed verification is what lets a doppelganger through, and letting one through is what starts a hunt &mdash; the expensive, ammunition-burning kind of night. Careful checking is now free, which makes the <a href="/guide/doppelgangers/">identification guide</a> the most directly financial page on this site.</p>

  <div class="grid two">
    <a class="card" href="/achievements/"><b>All 10 achievements</b><span>The full list with rarity and the completion curve.</span></a>
    <a class="card" href="/nights-and-levels/#story-mode"><b>Story Mode</b><span>The 13-shift structure the endings sit at the end of.</span></a>
  </div>
"""},
]

if __name__ == "__main__":
    print("生成怪物页 + 结局页:")
    build(PAGES)

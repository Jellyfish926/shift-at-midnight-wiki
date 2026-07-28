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
 "title": "Shift At Midnight Marionette — Music Box &amp; How to Survive",
 "og_short": "Shift At Midnight Marionette Guide",
 "desc": "The Marionette fight is decided before it starts. Wind the music box down and it never begins; let the melody play three times and there is no counter left.",
 "trail": M + [(None, "Marionette")],
 "h1": "Marionette",
 "lede": "The boss encounter, and the one most people lose. Only <strong>35.1%</strong> of players have ever killed a Marionette &mdash; not because it is rare, but because the fight is decided by an object in the room before the fight begins.",
 "body": """
  <div class="tags">
    <span class="tag red">Hostile &mdash; boss</span>
    <span class="tag amber">Achievement: Last Performance</span>
    <span class="tag">35.1% of players</span>
  </div>

  <div class="term warn">
    <div class="term-h">The mechanic in one sentence</div>
    <p>A wind-up <a href="/monsters/jack-in-the-box/">music box</a> governs the encounter: <strong>wind it all the way down and the fight stops before it starts</strong>. Let the box play through its melody three times without winding it, and you face the Marionette with no real counter available.</p>
  </div>

  <h2>Why 65% of players have never killed one</h2>

  <p>The <em>Last Performance</em> achievement sits at 35.1%, well below <em>Freed</em> (75.3%) and <em>Silenced</em> (87.8%). Those two are also just "kill this monster" achievements, so the gap is not about how often the Marionette shows up &mdash; it is about what happens when it does.</p>

  <p>The reason is that the Marionette encounter is not a combat problem you can solve with reflexes or a better weapon. It is a timing problem attached to an object, and if you do not know the object matters, you will spend the melody doing something else entirely. By the time the fight is actually in front of you, the window in which you could have influenced it has closed.</p>

  <h2>The music box</h2>

  <p>The box is a wind-up. Left alone, it plays its melody and runs down. Winding it resets that clock. Two things follow from this:</p>

  <ul>
    <li><strong>Winding it fully down stops the encounter before it begins.</strong> This is the clean answer &mdash; if you can get to the box and keep it wound, the fight does not happen.</li>
    <li><strong>Three full melodies without winding removes your counterplay.</strong> At that point the Marionette arrives and the tool you would have used against it is spent.</li>
  </ul>

  <p>The practical consequence is that the moment you hear the box, it becomes the priority. Not the quota, not the customer at the counter, not restocking. Everything else in the shift can wait; the melody cannot.</p>

  <div class="term tip">
    <div class="term-h">In three-player co-op</div>
    <p>This is the encounter that most rewards role-splitting. One player owns the box for the duration &mdash; that is their whole job &mdash; while the others keep the store running. With <a href="/guide/co-op/">proximity chat</a>, the person on box duty can call the melody count out loud so nobody has to guess how much time is left. Splitting attention across three people who are all half-watching the box is how groups lose this.</p>
  </div>

  <h2>Getting the achievement</h2>

  <p><em>Last Performance</em> requires you to <strong>kill</strong> a Marionette, not to avoid one. That creates a tension with the advice above: winding the box down prevents the fight, which means it also prevents the achievement.</p>

  <p>If you are hunting the achievement deliberately, you want the fight to happen while you still have counterplay in hand &mdash; which means letting the melody run but not letting it reach the third pass. Go in with a weapon already purchased and equipped rather than scrambling mid-encounter, and do it on a shift where the rest of the store is under control rather than during a night that is already going badly.</p>

  <p>If you just want to survive the night, wind it down and move on. There will be another Marionette.</p>

  <h2>What we have not confirmed</h2>

  <p>We are not going to publish damage numbers, exact melody durations in seconds, or a claimed "best weapon" for this fight, because we cannot verify them yet. There is a lot of confident-sounding guidance about this encounter in circulation that traces back to a single unverified source. When we have timings we can stand behind, they will appear here with the date they were confirmed.</p>

  <div class="grid two">
    <a class="card danger" href="/monsters/jack-in-the-box/"><b>Jack-in-the-Box</b><span>The same wind-up box, and what happens if you ignore it.</span></a>
    <a class="card" href="/achievements/"><b>All achievements</b><span>Where Last Performance sits in the completion curve.</span></a>
  </div>
"""},
{
 "path": "monsters/the-dentist",
 "title": "Shift At Midnight The Dentist — Why You Cannot Fight Him",
 "og_short": "Shift At Midnight The Dentist",
 "desc": "The Dentist is eight feet tall, ghostly, and invisible to the ID verification computer. No weapon, trap or barricade works. Every correct answer is about running.",
 "trail": M + [(None, "The Dentist")],
 "h1": "The Dentist",
 "lede": "Eight feet tall, ghostly, and <strong>completely invisible to the gas station's ID verification computer</strong>. He is not a doppelganger and he is not a problem you solve at the counter. There is no weapon, trap or barricade that deals with him.",
 "body": """
  <div class="tags">
    <span class="tag red">Hostile</span>
    <span class="tag red">Cannot be killed</span>
    <span class="tag">Invisible to ID scanner</span>
  </div>

  <div class="term warn">
    <div class="term-h">Do not try to fight this</div>
    <p>Every piece of correct guidance about the Dentist is about <strong>running</strong>. No weapon, trap or barricade is described as effective against him. If your instinct when something comes through the door is to reach for the arsenal, this is the entity that punishes it.</p>
  </div>

  <h2>He does not appear on the computer</h2>

  <p>This is the detail that makes the Dentist genuinely dangerous rather than merely difficult. Your ID verification computer is the tool you have been trained by the whole game to trust &mdash; it tells you whether a document is authentic, and you build your entire threat model around what it reports.</p>

  <p>The Dentist is not in that system at all. He does not scan as a fake ID. He does not scan as anything. A player running the standard mental loop &mdash; check ID, act on result &mdash; gets no signal whatsoever, because the loop has nothing to act on.</p>

  <p>Pair that with <a href="/monsters/norbert/">Norbert</a>, who <em>does</em> scan as a fake ID and is completely harmless, and you have the game's central lesson stated twice from opposite directions: <strong>the scanner reports on documents, not on danger.</strong></p>

  <h2>He is a separate threat, not a customer</h2>

  <p>The Dentist is not a doppelganger. Doppelgangers are the identification puzzle &mdash; entities mimicking humans, which you sort at the counter. The Dentist arrives on top of the job you are already doing. Your quota does not pause, the shelves do not stock themselves, and the customers keep coming.</p>

  <p>In practice that means he is a shift-disruptor. The correct response is not to abandon the store permanently but to break contact, let the encounter pass, and get back to work &mdash; while accepting that the shift's numbers are going to suffer.</p>

  <div class="term tip">
    <div class="term-h">What running actually means</div>
    <p>Break line of sight and keep moving. An eight-foot ghostly figure inside a gas station is dealing with the same aisles and doorways you are, so the store layout is your only real asset. Knowing where the loops are &mdash; which aisles connect, which corners are dead ends &mdash; is the difference between putting distance between you and getting cornered in the stockroom. This is the one entity where map knowledge outranks equipment.</p>
  </div>

  <h2>In co-op</h2>

  <p>Three players give you something a solo player does not have: the ability to know where he is when you cannot see him. With <a href="/guide/co-op/">proximity chat</a>, a teammate's voice getting suddenly urgent from across the store is positional information. Call his location, keep the store between you, and do not converge &mdash; three people running into the same aisle is three people cornered instead of one.</p>

  <h2>Related</h2>

  <div class="grid two">
    <a class="card" href="/guide/doppelgangers/"><b>Doppelganger identification</b><span>What the scanner does and does not tell you.</span></a>
    <a class="card" href="/guide/survival/"><b>Survival guide</b><span>Barricades and hiding &mdash; and when they do not apply.</span></a>
  </div>
"""},
{
 "path": "monsters/jack-in-the-box",
 "title": "Shift At Midnight Jack-in-the-Box &amp; Music Box Explained",
 "og_short": "Shift At Midnight Jack-in-the-Box",
 "desc": "Wind it or it springs out at you. The same wind-up box also decides whether the Marionette encounter is survivable — here is how the two connect.",
 "trail": M + [(None, "Jack-in-the-Box")],
 "h1": "Jack-in-the-Box",
 "lede": "An enemy that waits inside a wind-up box. <strong>If you do not wind it, it springs out and attacks you.</strong> And the same object is the deciding factor in the <a href=\"/monsters/marionette/\">Marionette</a> encounter, which is why this unremarkable-looking prop matters more than anything else in the room.",
 "body": """
  <div class="tags">
    <span class="tag red">Hostile</span>
    <span class="tag amber">Linked to Marionette</span>
    <span class="tag">Counterplay: keep winding</span>
  </div>

  <h2>The basic threat</h2>

  <p>During a hunt you may find a wind-up jack-in-the-box. The rule is simple and unforgiving: <strong>wind it, or it springs out and attacks.</strong> The box is on a timer that you control, and the only input you have is winding.</p>

  <p>What makes this different from most horror-game props is that it is not optional scenery you can walk past. Ignoring it is an active choice with a consequence attached, and the consequence arrives on the box's schedule rather than yours.</p>

  <h2>The connection to the Marionette</h2>

  <div class="term warn">
    <div class="term-h">This is the part people miss</div>
    <p>The music box is connected to the <a href="/monsters/marionette/">Marionette</a> boss encounter. <strong>Wind it all the way down and the Marionette fight stops before it starts.</strong> Let the box play through its melody <strong>three times</strong> without winding it, and you face the Marionette with no real counter.</p>
  </div>

  <p>So the same object serves two functions depending on the situation. In an ordinary hunt it is a threat you manage by winding. In a Marionette encounter it is the entire counterplay &mdash; and the window on it closes after three melodies whether you were paying attention or not.</p>

  <p>This is why <em>Last Performance</em> (kill a Marionette) sits at only 35.1% while the other monster-kill achievements are up at 75&ndash;88%. Players who do not know the box matters spend the melody doing something else, and then meet the boss with nothing.</p>

  <h2>What to do when you hear it</h2>

  <ol>
    <li><strong>Treat the melody as a countdown.</strong> It is the most reliable timer the game gives you.</li>
    <li><strong>Get to the box.</strong> Quota, shelves and customers can all wait; the box cannot.</li>
    <li><strong>Decide what you want.</strong> Winding it fully down is the safe play &mdash; the encounter does not happen. If you are chasing <em>Last Performance</em>, you need the fight to occur while you still have counterplay, which means not letting it reach the third pass.</li>
    <li><strong>In co-op, assign it.</strong> One player owns the box and calls the melody count aloud. See the <a href="/guide/co-op/">co-op guide</a>.</li>
  </ol>

  <div class="term tip">
    <div class="term-h">Why the design works</div>
    <p>A wind-up music box is a genuinely good horror object: it makes noise that tells you it exists, it gives you a task that takes your hands and attention away from everything else, and it runs on a clock you can hear but not read precisely. You always know roughly how much time is left and never exactly. That is the entire encounter.</p>
  </div>

  <div class="grid two">
    <a class="card danger" href="/monsters/marionette/"><b>Marionette</b><span>The boss the box is protecting you from.</span></a>
    <a class="card" href="/monsters/"><b>Full bestiary</b><span>Every named threat and its counterplay.</span></a>
  </div>
"""},
{
 "path": "monsters/norbert",
 "title": "Shift At Midnight Norbert — Who He Is and What to Do",
 "og_short": "Shift At Midnight Norbert",
 "desc": "Norbert is a gnome who arrives on Night 2 with a fake ID. He is not a doppelganger and will not kill you — killing him is the mistake the game wants.",
 "trail": M + [(None, "Norbert")],
 "h1": "Norbert",
 "lede": "A small gnome who shows up on <strong>Night 2</strong>, steps around the counter with his items, and scans as a fake ID. He is <strong>not</strong> a doppelganger, he will not turn into a monster, and he will not try to kill you. He is pure chaos, and he is the game teaching you a lesson.",
 "body": """
  <div class="tags">
    <span class="tag green">Not hostile</span>
    <span class="tag amber">Night 2</span>
    <span class="tag">Scans as fake ID</span>
  </div>

  <div class="term tip">
    <div class="term-h">Short answer: leave him alone</div>
    <p>Norbert's ID scans as fake and the computer tells you he is not what he pretends to be &mdash; and both of those things are true without him being a threat. He does not become a monster. He is chaos, not danger.</p>
  </div>

  <h2>What actually happens</h2>

  <p>On Night 2, Norbert arrives. He is small. He steps around the counter &mdash; which is already a violation of how a customer is supposed to behave, and which is exactly the kind of behavioural tell you have been trained to treat as a red flag. He has items with him. When you scan his ID, the computer reports that the document is fake and that he is not what he claims to be.</p>

  <p>Every signal you have been taught to read says "act". And the correct response is to do nothing.</p>

  <h2>Why he exists</h2>

  <p>Norbert is a designed counterexample. By Night 2 you have built a rule &mdash; fake ID means doppelganger, doppelganger means deal with it &mdash; and Norbert exists to break that rule while the stakes are still low enough to learn from.</p>

  <p>The lesson pairs with <a href="/monsters/the-dentist/">the Dentist</a>, who is the same lesson inverted: an entity that is genuinely lethal and does not register on the scanner at all. Between the two of them the game states its thesis clearly. <strong>The ID verification computer reports on documents. It does not report on danger.</strong> A player who conflates the two will kill a harmless gnome and then get killed by something the machine never saw.</p>

  <div class="term warn">
    <div class="term-h">There is no penalty-free "just in case"</div>
    <p>The most common achievement in the game, at 96.6%, is <em>First Blood</em> &mdash; kill your first customer. Nearly everyone does it. That statistic exists because killing on suspicion is the reflex the game deliberately builds and then punishes. Norbert is where a lot of players spend it.</p>
  </div>

  <h2>Does killing him break anything?</h2>

  <p>We have not confirmed a specific mechanical penalty tied to Norbert individually, and we are not going to invent one. What we can say is that killing customers is tracked by the game as a distinct thing &mdash; it has its own achievement &mdash; and that the ending-related achievements (<em>Grave Decision</em> at 26.0%, <em>True Ending</em> at 13.4%, <em>Empty Home</em> at 7.0%) are all hidden and all rare.</p>

  <p>If any of those gate on how you handled the judgement calls across a run, then who you killed matters. That is inference, clearly labelled, not a claim. See the <a href="/endings/">endings page</a> for what we can and cannot say about it.</p>

  <div class="grid two">
    <a class="card danger" href="/monsters/the-dentist/"><b>The Dentist</b><span>The same lesson, inverted &mdash; lethal and invisible to the scanner.</span></a>
    <a class="card" href="/guide/doppelgangers/"><b>Doppelganger identification</b><span>What the real tells are.</span></a>
  </div>
"""},
{
 "path": "monsters/shrieking-doll",
 "title": "Shift At Midnight Shrieking Doll — How to Kill It (Silenced)",
 "og_short": "Shift At Midnight Shrieking Doll",
 "desc": "The Shrieking Doll is a crawler that screams to pull your attention, then follows you. Killing one unlocks Silenced, held by 87.8% of players. It is killable.",
 "trail": M + [(None, "Shrieking Doll")],
 "h1": "Shrieking Doll",
 "lede": "A creepy-faced crawler that <strong>screams to lure your attention and then follows you</strong>. Unlike most of this bestiary, it is straightforwardly killable &mdash; which is why <strong>87.8%</strong> of players have the achievement for it.",
 "body": """
  <div class="tags">
    <span class="tag red">Hostile</span>
    <span class="tag green">Killable</span>
    <span class="tag amber">Achievement: Silenced</span>
    <span class="tag">87.8% of players</span>
  </div>

  <h2>Behaviour</h2>

  <p>The Shrieking Doll does two things. It <strong>screams</strong>, which pulls your attention toward it, and it <strong>follows</strong> you once it has you. It moves as a crawler rather than upright, which changes its sightlines through a store full of shelving.</p>

  <p>The scream is the interesting part mechanically, because it is a lure rather than an attack. It is designed to make you look, and looking costs you attention you were spending on something else &mdash; a customer at the counter, a quota, or a <a href="/monsters/jack-in-the-box/">music box that is counting down</a>. On a night where something else is already on a timer, the doll's real damage is the distraction.</p>

  <h2>Killing it</h2>

  <p>It comes to you. That is the whole tactical picture, and it is why the achievement rate is so high &mdash; you do not have to hunt this thing, you have to be ready when it arrives. Have a weapon purchased and equipped rather than reacting to the scream by going shopping.</p>

  <p><em>Silenced</em> unlocks on your first kill. At 87.8% it is the third most common achievement in the game, behind only <em>First Blood</em> (96.6%) and <em>Still Breathing</em> (92.8%). If you have played more than a couple of shifts you almost certainly have it already.</p>

  <div class="term tip">
    <div class="term-h">Good target for Relentless</div>
    <p><em>Relentless</em> requires finishing a hunt within 30 seconds, and only 40.1% of players have it. The Shrieking Doll is the sensible monster to attempt it on, precisely because it closes the distance for you instead of hiding. Trying to speed-run a hunt against something you have to find first is a much worse proposition. Never attempt it on a <a href="/monsters/the-dentist/">Dentist</a> night &mdash; that entity cannot be killed at all.</p>
  </div>

  <h2>In co-op</h2>

  <p>The scream is positional information for the whole team. With <a href="/guide/co-op/">proximity chat</a>, whoever hears it loudest is closest, and saying so out loud lets the other two keep doing their jobs instead of all three converging on the noise. The failure mode is the entire crew abandoning the counter to look at a doll while the actual problem develops somewhere else.</p>

  <div class="grid two">
    <a class="card" href="/achievements/"><b>All achievements</b><span>Where Silenced and Relentless sit.</span></a>
    <a class="card" href="/guide/weapons/"><b>Weapons arsenal</b><span>What to have equipped before the scream.</span></a>
  </div>
"""},
{
 "path": "monsters/demented",
 "title": "Shift At Midnight Demented — How to Kill One (Freed)",
 "og_short": "Shift At Midnight Demented",
 "desc": "The Demented is a hostile entity you can put down. Killing one unlocks Freed, held by 75.3% of players — one of the threats nearly everyone meets early.",
 "trail": M + [(None, "Demented")],
 "h1": "Demented",
 "lede": "A hostile entity that you <strong>can</strong> put down &mdash; killing one unlocks <em>Freed</em>, held by <strong>75.3%</strong> of players. It sits in the group of threats nearly everyone encounters within their first few shifts.",
 "body": """
  <div class="tags">
    <span class="tag red">Hostile</span>
    <span class="tag green">Killable</span>
    <span class="tag amber">Achievement: Freed</span>
    <span class="tag">75.3% of players</span>
  </div>

  <h2>Where it sits in the difficulty curve</h2>

  <p>The achievement data tells a clear story about this one. <em>Freed</em> is at 75.3%, which puts the Demented in the same tier as the <a href="/monsters/shrieking-doll/">Shrieking Doll</a> (87.8%) rather than the <a href="/monsters/marionette/">Marionette</a> (35.1%). Three quarters of everyone who has played this game has killed a Demented.</p>

  <p>That means two things. It appears often enough that ordinary play produces the encounter, and it is winnable with ordinary equipment &mdash; there is no gimmick object gating the fight the way the music box gates the Marionette. If you have a weapon and you commit, you win.</p>

  <p>The ~25% who do not have it are mostly people who stopped playing early rather than people who kept failing the fight. The drop-off between <em>Freed</em> at 75.3% and <em>Relentless</em> at 40.1% is where the game stops handing achievements out for simply continuing.</p>

  <h2>The name</h2>

  <p>The achievement for killing one is called <em>Freed</em>, not "Slain" or "Cleared". That word choice is doing something. In a game whose entire premise is that the things coming through your door are wearing stolen humanity, an achievement that frames killing as <em>release</em> is a deliberate piece of framing.</p>

  <p>We are flagging this as tone, not mechanics &mdash; we cannot tell you it unlocks anything or feeds into an ending. But it is consistent with a game where the rare hidden achievements are called <em>Grave Decision</em> and <em>Empty Home</em>, and it is worth noticing while you play.</p>

  <div class="term tip">
    <div class="term-h">Practical approach</div>
    <p>Have a weapon bought and equipped before the encounter, not after it starts. That single habit accounts for most of the difference between players who clear early threats comfortably and players who spend every hunt scrambling. The <a href="/guide/weapons/">weapons arsenal</a> is also an achievement in its own right &mdash; <em>Locked And Loaded</em>, at 20.6% &mdash; so the money is not wasted.</p>
  </div>

  <h2>What we have not confirmed</h2>

  <p>Specific health values, attack patterns, and whether particular weapons perform better against a Demented than others are not things we can verify yet, so we are not publishing numbers. When we can confirm them they will appear here with the date.</p>

  <div class="grid two">
    <a class="card" href="/monsters/"><b>Full bestiary</b><span>Every named threat, and the two that are not what they look like.</span></a>
    <a class="card" href="/achievements/"><b>All achievements</b><span>The full completion curve with rarity.</span></a>
  </div>
"""},
{
 "path": "endings",
 "active": "/endings/",
 "title": "Shift At Midnight Endings — True Ending &amp; Empty Home Explained",
 "og_short": "Shift At Midnight Endings",
 "desc": "Shift At Midnight has multiple endings. True Ending sits at 13.4% and Empty Home at 7.0% — here is what the achievement data actually tells us, and what it does not.",
 "trail": [(None, "Endings")],
 "h1": "Shift At Midnight endings",
 "lede": "Three of the game's ten achievements are hidden, and all three look ending-related: <strong>Grave Decision</strong> (26.0%), <strong>True Ending</strong> (13.4%) and <strong>Empty Home</strong> (7.0%). Here is what the rarity data supports, and where the honest answer is still &ldquo;we do not know yet&rdquo;.",
 "body": """
  <div class="term warn">
    <div class="term-h">Read this before the rest of the page</div>
    <p>Steam hides the descriptions for all three of these achievements. That means nobody has an official requirement text to quote &mdash; including the sites that are writing as though they do. Everything below is split into <strong>fact</strong> (achievement names and global unlock rates, which are publicly readable) and <strong>inference</strong> (clearly labelled). We are not going to guess and present it as knowledge.</p>
  </div>

  <h2>The data</h2>

  <div class="tablewrap">
  <table class="data">
    <thead><tr><th>Achievement</th><th>Description</th><th>Global unlock</th></tr></thead>
    <tbody>
      <tr><td><strong>Grave Decision</strong></td><td>Hidden</td><td class="num">26.0%</td></tr>
      <tr><td><strong>True Ending</strong></td><td>Hidden</td><td class="num">13.4%</td></tr>
      <tr><td><strong>Empty Home</strong></td><td>Hidden</td><td class="num">7.0%</td></tr>
    </tbody>
  </table>
  </div>

  <p class="updated">Rarity read from public Steam global stats on 28 July 2026</p>

  <h2>What the ordering tells us</h2>

  <p>The three rates are meaningfully separated: 26.0%, then 13.4%, then 7.0%. If <em>Empty Home</em> were simply a step on the road to <em>True Ending</em>, you would expect it to be at least as common. It is half as common. <strong>That strongly suggests these are separate outcomes rather than a sequence</strong> &mdash; different endings, or an ending plus a distinct end-state, rather than milestones on one path.</p>

  <p><em>Grave Decision</em> at 26.0% is the most reachable of the three and reads like a branch point rather than a conclusion. A quarter of players hitting it is consistent with "most players who finish a run encounter this choice, and some fraction take the branch that fires the achievement".</p>

  <h2>Why a run's judgement calls probably matter</h2>

  <p><strong>Inference, clearly labelled.</strong> Shift At Midnight is built entirely around one repeated decision: the person at your counter is either human or is wearing a human, and you decide what happens to them. The game tracks that you make this call badly &mdash; <em>First Blood</em>, for killing your first customer, is held by 96.6% of players and is the most common achievement in the game.</p>

  <p>A game that instruments its central moral decision that carefully, and then hides three rare achievements behind names like <em>Grave Decision</em> and <em>Empty Home</em>, is very likely gating those outcomes on how you handled the decisions rather than on raw survival. Note that <em>Still Breathing</em> &mdash; survive your first hunt &mdash; is at 92.8%, so mere survival is clearly not the scarce thing.</p>

  <p>We cannot confirm the trigger. What we can say is that if you are chasing these, playing carefully at the counter is a more plausible lever than playing aggressively, and that <a href="/monsters/norbert/">Norbert</a> &mdash; the harmless gnome with a fake ID on Night 2 &mdash; is the clearest test the game gives you of whether you kill on suspicion.</p>

  <div class="term tip">
    <div class="term-h">If you want to hunt these yourself</div>
    <p>Keep a written log across runs: who you served, who you killed, what the scanner said, and which achievement fired at the end. Because the descriptions are hidden, the community's path to confirming these is people correlating their own run notes. A single run tells you nothing; ten logged runs from a few players will crack it.</p>
  </div>

  <h2>What we will not tell you</h2>

  <p>We are not publishing a step-by-step for <em>True Ending</em>, because we would be making it up. There is confidently-worded guidance circulating that traces back to guesswork, and following it costs you runs. When a trigger is confirmed &mdash; by reproducible player reports or by the developer &mdash; it goes on this page with the date and the source.</p>

  <p>If you have reproducible notes on any of the three, that is genuinely the missing piece.</p>

  <div class="grid two">
    <a class="card" href="/achievements/"><b>All 10 achievements</b><span>The full list with rarity and the completion curve.</span></a>
    <a class="card" href="/guide/story-mode/"><b>Story Mode</b><span>The shift structure the endings sit at the end of.</span></a>
  </div>
"""},
]

if __name__ == "__main__":
    print("生成怪物页 + 结局页:")
    build(PAGES)

#!/usr/bin/env python3
"""按 RelatedKeywords 表补的高量词页 + 站点法务页(教程检查清单要求 + AdSense 硬门槛)。

各页对应的 28 天搜索量与难度写在注释里,便于日后按 GSC 数据复盘。
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _build import build

PAGES = [

# release date 5120@难度13 + when is it coming out 600@12 + when does it come out 540@16
# + when will it be released 490 + launch date + release delayed 460@14  → 全表性价比最高的一块
{
 "path": "release-date", "active": "/guides/",
 "title": "Shift At Midnight Release Date — Out Now (22 July 2026)",
 "og_short": "Shift At Midnight Release Date",
 "desc": "Shift At Midnight released 22 July 2026 after two delays from the original 28 May date. Platforms, price, Game Pass, and what the two post-launch patches changed.",
 "trail": [(None, "Release date")],
 "h1": "Shift At Midnight release date",
 "lede": "<strong>Shift At Midnight is out now &mdash; it released on 22 July 2026.</strong> If you are finding older pages that say May, those are out of date: the game was delayed twice before it shipped.",
 "body": """
  <div class="term tip">
    <div class="term-h">The short answer</div>
    <p><strong>Released:</strong> 22 July 2026, on Steam, Xbox Series X|S and the Microsoft Store &mdash; day one on Xbox Game Pass. <strong>Price:</strong> $9.99 USD. It is available right now; there is nothing left to wait for.</p>
  </div>

  <table class="facts">
    <tr><th>Release date</th><td>22 July 2026</td></tr>
    <tr><th>Original date</th><td>28 May 2026 &mdash; delayed</td></tr>
    <tr><th>Platforms</th><td>Steam (Windows), Xbox Series X|S, Microsoft Store</td></tr>
    <tr><th>Xbox Game Pass</th><td>Day one &mdash; console and PC</td></tr>
    <tr><th>Price</th><td>$9.99 USD (10% launch discount, ended 29 July 2026)</td></tr>
    <tr><th>Developer</th><td>Bun Muen (solo)</td></tr>
    <tr><th>Publisher</th><td>Kwalee</td></tr>
    <tr><th>Engine</th><td>Unity</td></tr>
    <tr><th>Steam languages</th><td>English, French, German, Spanish (Spain), Japanese, Russian, Simplified Chinese, Traditional Chinese, Portuguese (Brazil) &mdash; nine, interface and subtitles</td></tr>
    <tr><th>Content notes</th><td>Steam lists &ldquo;plenty of gore and blood&rdquo;</td></tr>
    <tr><th>Achievements</th><td>10, three of them hidden &mdash; <a href="/achievements/">full list with unlock rates</a></td></tr>
    <tr><th>Endless Mode</th><td>BETA playable since launch &mdash; full version free, Q4 2026</td></tr>
  </table>

  <h2>Why so many pages still say May</h2>

  <p>Shift At Midnight was originally announced for <strong>28 May 2026</strong>. That date was pushed back, and then pushed back again, landing on 22 July 2026. A lot of coverage was written against the earlier dates and never updated, which is why searching for the release date still turns up contradictory answers months later.</p>

  <p>If you are reading a page that says the game is "coming soon" or gives a May date, it predates the final schedule. The game shipped on 22 July 2026 and has been out since.</p>

  <h2>Was the delay a bad sign?</h2>

  <p>Not obviously. This is a solo developer's commercial release published by Kwalee, launching simultaneously on Steam, Xbox Series X|S and Game Pass. Day-one Game Pass placement involves certification on Microsoft's side, and Xbox Play Anywhere adds another layer. Hitting three storefronts at once with one developer is a genuine scheduling problem, and slipping twice to get it right is a reasonable outcome rather than a red flag.</p>

  <p>The launch build shipped with ten achievements, a full Story Mode, three-player online co-op and a playable Endless Mode beta, with the finished version of Endless Mode promised as a free Q4 2026 update. That is a complete release, not a rushed one.</p>

  <h2>How the launch actually went</h2>

  <p>Well, then badly, in that order. Steam concurrents reached <strong>12,556 players on 23 July</strong>, the day after release, and the game charted as high as <strong>#8 on Steam&rsquo;s top sellers</strong> (<a href="https://steamdb.info/app/3722330/charts/" target="_blank" rel="noopener">SteamDB</a>). That was not the ceiling &mdash; SteamDB&rsquo;s all-time peak for the game is <strong>37,590</strong>, set on 26 July 2026 and read on 12 August 2026; see <a href="/player-count/">player count</a>. It also could not reliably put those players into a lobby: enough people were unable to create or join games that the developer pushed a temporary opt-in beta branch the same evening as a stopgap, which only worked if everyone in a party switched to it together.</p>

  <p>No announcement has ever been published retiring that branch, so we cannot date it as fixed. If you and a friend opted in at launch and never switched back, it is the first thing to check when you are both online but cannot see each other &mdash; the steps are on <a href="/troubleshooting/">troubleshooting</a>.</p>

  <h2>What has changed since release</h2>

  <p>Two patches so far, and the second changed the game rather than the plumbing.</p>

  <ul>
    <li><strong>23 July &mdash; lobbies and balance.</strong> Lobby size became selectable up to six, though the developer was clear that the game &ldquo;is designed and has always been marketed around a maximum of 3 players&rdquo; and does not recommend six for a first run. The Marionette lost HP and the music box got louder.</li>
    <li><strong>29 July &mdash; new content.</strong> A second purchasable firearm, a new <strong>Rake</strong> enemy that appears in endless and post-story modes only, and the removal of the customer patience meter &mdash; which is why careful ID checking is far less punishing now than it was at launch.</li>
    <li><strong>The 10% launch discount ended on 29 July.</strong> The price is back to $9.99 with no active discount as of 5 August 2026.</li>
  </ul>

  <p>Nothing has been announced since 29 July. Full notes with sources are on the <a href="/updates/">patch notes page</a>.</p>

  <h2>Where to get it</h2>

  <ul>
    <li><strong>Xbox Game Pass</strong> &mdash; included at no extra cost, console and PC. If you subscribe, this is the answer.</li>
    <li><strong>Microsoft Store</strong> &mdash; $9.99, and it is an Xbox Play Anywhere title, so one purchase covers Xbox and Windows.</li>
    <li><strong>Steam</strong> &mdash; $9.99, with Steam Achievements and Family Sharing.</li>
  </ul>

  <div class="term warn">
    <div class="term-h">Check this before you buy</div>
    <p>Steam players <strong>cannot</strong> play with Xbox or PC Game Pass players. The two ecosystems have separate multiplayer pools. If you are buying so you can play with friends, everyone needs to be on the same side &mdash; see <a href="/crossplay/">crossplay</a>.</p>
  </div>

  <h2>What is still coming</h2>

  <ul>
    <li><strong>Endless Mode</strong> &mdash; the beta shipped on day one and unlocks once you finish story mode. The finished version, with more customers, traps, weapons and monsters, is a free update planned for <strong>Q4 2026</strong>. See <a href="/nights-and-levels/#endless-mode">Endless Mode</a>.</li>
    <li><strong>Full crossplay including Steam</strong> &mdash; confirmed as a post-release update, with no date attached to it.</li>
    <li><strong>A public server browser</strong> &mdash; announced before launch, still not live as of 5 August 2026.</li>
  </ul>

  <h2>What is not coming</h2>

  <p>No PlayStation 5, Nintendo Switch, mobile or VR version has been announced. The game is PC and Xbox only. Full detail on <a href="/platforms/">the platforms page</a>, including the app store and PS5 questions specifically.</p>

  <div class="grid two">
    <a class="card" href="/platforms/"><b>All platforms</b><span>PS5, mobile, Switch &mdash; the honest answers.</span></a>
    <a class="card" href="/review/#price"><b>Price</b><span>$9.99, and whether Game Pass makes that moot.</span></a>
  </div>
"""},

# is it available on app store 820 + on mobile 660 + ps5 610 + can you play on ps5 + install on phone
{
 "path": "platforms", "active": "/guides/",
 "title": "Shift At Midnight Platforms — PS5, Mobile &amp; Switch Answered",
 "og_short": "Shift At Midnight Platforms",
 "desc": "Is Shift At Midnight on PS5, mobile or the App Store? No. It is PC (Steam, Microsoft Store) and Xbox Series X|S only. Here is the full platform breakdown.",
 "trail": [(None, "Platforms")],
 "h1": "What platforms is Shift At Midnight on?",
 "lede": "Short version: <strong>PC and Xbox only</strong>. There is no PlayStation version, no mobile version, and nothing on the App Store or Google Play. If someone told you otherwise, they were wrong or describing a different game.",
 "body": """
  <div class="tablewrap">
  <table class="data">
    <thead><tr><th>Platform</th><th>Available?</th><th>Notes</th></tr></thead>
    <tbody>
      <tr><td><strong>PC &mdash; Steam</strong></td><td class="num">✅ Yes</td><td>Windows 10/11 64-bit. $9.99</td></tr>
      <tr><td><strong>PC &mdash; Microsoft Store</strong></td><td class="num">✅ Yes</td><td>Xbox Play Anywhere</td></tr>
      <tr><td><strong>PC Game Pass</strong></td><td class="num">✅ Yes</td><td>Day one, included</td></tr>
      <tr><td><strong>Xbox Series X|S</strong></td><td class="num">✅ Yes</td><td>Day one on Game Pass</td></tr>
      <tr><td><strong>PlayStation 5</strong></td><td class="num">❌ No</td><td>Not announced</td></tr>
      <tr><td><strong>PlayStation 4</strong></td><td class="num">❌ No</td><td>Not announced</td></tr>
      <tr><td><strong>Nintendo Switch</strong></td><td class="num">❌ No</td><td>Not announced</td></tr>
      <tr><td><strong>iOS / App Store</strong></td><td class="num">❌ No</td><td>Not announced</td></tr>
      <tr><td><strong>Android / Play Store</strong></td><td class="num">❌ No</td><td>Not announced</td></tr>
      <tr><td><strong>VR</strong></td><td class="num">❌ No</td><td>Not announced</td></tr>
    </tbody>
  </table>
  </div>

  <h2>Can you play Shift At Midnight on PS5?</h2>

  <p><strong>No.</strong> There is no PlayStation 5 version, and neither Bun Muen nor Kwalee has indicated that a PS5 port is coming. The same applies to PS4.</p>

  <p>This is worth stating plainly because the question gets asked a lot and the answer keeps getting hedged. There is no announced port, no release window, and no statement of intent. If a PS5 version is ever announced, it will come from the developer or publisher &mdash; not from a wiki guessing.</p>

  <h2>Is Shift At Midnight on mobile or the App Store?</h2>

  <p><strong>No.</strong> There is no iOS or Android version, and nothing on the App Store or Google Play. The game is a PC and Xbox title.</p>

  <p>If you have found something in a mobile app store using this name, it is not this game. Popular PC horror titles attract copycat mobile listings, and installing one is a bad idea. The only legitimate places to get Shift At Midnight are Steam, the Microsoft Store and Xbox Game Pass.</p>

  <div class="term warn">
    <div class="term-h">"How do I install it on my phone using Steam?"</div>
    <p>You cannot install it on a phone. Steam Link and similar remote-play tools <em>stream</em> a game running on your PC to another screen &mdash; the game still runs on the PC, and you still need the PC. That is not the same as a mobile version, and it will not work if you do not own a machine that can run it.</p>
  </div>

  <h2>Is it on Nintendo Switch?</h2>

  <p>No, and nothing has been announced. The game is a 2026 release built for PC and current-generation Xbox hardware.</p>

  <h2>Why only PC and Xbox?</h2>

  <p>Shift At Midnight is an <strong>Xbox Play Anywhere</strong> title with day-one Game Pass placement. That is a deliberate platform strategy: Microsoft's programme covers Xbox console and Windows as a single release with shared purchases and shared multiplayer, which is a lot of reach for a solo developer to get from one certification process.</p>

  <p>Adding PlayStation or Switch would mean separate certification, separate builds and separate ongoing support &mdash; a substantial commitment for one person. It is a reasonable place to stop for a first commercial release.</p>

  <h2>Xbox specifics worth knowing</h2>

  <ul>
    <li><strong>Optimized for Xbox Series X|S</strong> &mdash; the Microsoft listing carries the badge.</li>
    <li><strong>Xbox cloud saves</strong> &mdash; progress follows you between the console and the Windows build, which is the practical half of Play Anywhere.</li>
    <li><strong>Xbox Cloud Gaming</strong> &mdash; supported, but streaming requires <strong>Game Pass Ultimate</strong>; console-only or PC Game Pass will not stream it. It streams the Xbox build from Microsoft&rsquo;s servers, so it is still not a native version for any other device.</li>
  </ul>

  <h2>Which platforms can play together</h2>

  <p>Xbox consoles and PC Game Pass have shared one multiplayer pool since day one. <strong>Steam is a separate pool</strong> &mdash; a Steam copy cannot join a Game Pass friend, and no setting changes that. Bun Muen has confirmed full crossplay as a post-release update but has attached <strong>no date</strong> to it, so treat it as unscheduled rather than imminent. Details on <a href="/crossplay/">crossplay</a>.</p>

  <div class="grid two">
    <a class="card" href="/crossplay/"><b>Crossplay</b><span>Steam and Xbox players cannot play together.</span></a>
    <a class="card" href="/release-date/"><b>Release date</b><span>Out now &mdash; 22 July 2026.</span></a>
  </div>
"""},

# employee package 990 + employee packag 490 + giveaway
{
 "path": "employee-package", "active": "/guides/",
 "title": "Shift At Midnight Employee Package — What Is It?",
 "og_short": "Shift At Midnight Employee Package",
 "desc": "The Shift At Midnight Employee Package is a physical merch bundle Kwalee gave away — poster, duffel bag, rat plushie, Joe's Diner cap, badge and retro peripherals.",
 "trail": [(None, "Employee Package")],
 "h1": "Shift At Midnight Employee Package",
 "lede": "It is not DLC, an in-game item or a paid edition. The <strong>Employee Package</strong> is a physical merchandise bundle that publisher Kwalee ran as a <strong>giveaway</strong> &mdash; which is why you cannot find a buy button for it.",
 "body": """
  <div class="term tip">
    <div class="term-h">Short answer</div>
    <p>A promotional prize bundle from Kwalee, distributed through a giveaway rather than sold. There is no in-game content attached to it and nothing in the game is locked behind it.</p>
  </div>

  <h2>What was in it</h2>

  <ul>
    <li>Shift At Midnight <strong>poster</strong></li>
    <li>Red <strong>duffel bag</strong></li>
    <li>Soft <strong>rat plushie</strong></li>
    <li><strong>Joe's Diner baseball cap</strong></li>
    <li><strong>Employee badge</strong></li>
    <li>Physical <strong>OG ticket</strong></li>
    <li>Retro <strong>mechanical keyboard</strong></li>
    <li>Retro <strong>mouse</strong></li>
  </ul>

  <p>The theming is consistent with the game: you play a night-shift employee at a roadside gas station, so the prize is dressed as employee kit &mdash; a badge, a cap from <a href="/employee-package/#newsletter">Joe's Diner</a>, and 1990s-era peripherals matching the game's retro presentation.</p>

  <h2>Can you still get one?</h2>

  <p>The Employee Package was distributed through a Gleam giveaway run by Kwalee. Giveaways of this kind run for a fixed window and then close. <strong>We are not going to tell you it is still open, because we cannot verify that it is</strong> &mdash; and pages that keep stale giveaway links live are how people end up entering competitions that ended months ago.</p>

  <p>If you want to know whether anything similar is running now, the reliable sources are Kwalee's own channels and the game's Steam news feed. Not a wiki.</p>

  <div class="term warn">
    <div class="term-h">Careful with "Employee Package" links</div>
    <p>Merch giveaways for horror games attract fake entry pages that harvest logins. If a page asks you to sign in with your Steam or Microsoft account to "claim" a physical prize, close it. A legitimate giveaway does not need your game account credentials. Verify any campaign from the publisher's own channels first.</p>
  </div>

  <h2>Is there any paid merch or special edition?</h2>

  <p>No paid special edition, deluxe edition or season pass has been announced. Shift At Midnight is a single $9.99 release. The only official way to spend more on Steam is one of the three co-op <strong>bundles</strong> pairing it with Phasmophobia, Escape the Backrooms or YAPYAP &mdash; each takes 10% off, and that saving stacks with other Steam discounts (<a href="https://store.steampowered.com/app/3722330/Shift_At_Midnight/" target="_blank" rel="noopener">Steam store page</a>). Those buy you other games, not extras for this one &mdash; see <a href="/similar-games/">similar games</a>.</p>

  <p>Going the other way, the Steam version supports <strong>Family Sharing</strong>, so a household can play the single copy without buying a second.</p>

  <p>Announced future content is free. The <a href="/nights-and-levels/#endless-mode">Endless Mode</a> beta is already playable once you finish the story, and its finished version &mdash; along with more customers, traps, weapons and monsters &mdash; is a free update planned for Q4 2026. None of it is behind a paywall, and none of it is behind a giveaway.</p>

  <div class="grid two">
    <a class="card" href="/review/#price"><b>Price &amp; editions</b><span>One edition, $9.99, no paid DLC.</span></a>
    <a class="card" href="/employee-package/#newsletter"><b>Joe's Diner</b><span>The in-game diner the cap references.</span></a>
  </div>
"""},

# like games 840 + are there any games similiar
{
 "path": "similar-games", "active": "/guides/",
 "title": "Games Like Shift At Midnight — 8 Co-op Horror Picks",
 "og_short": "Games Like Shift At Midnight",
 "desc": "Eight co-op horror games to play after Shift At Midnight, what half of it each one shares, and which three come in an official Steam bundle at 10% off.",
 "trail": [(None, "Similar games")],
 "h1": "Games like Shift At Midnight",
 "lede": "Shift At Midnight sits at the crossing point of two things: <strong>three-player co-op horror</strong> and <strong>deciding whether the person in front of you is lying</strong>. Most recommendations only give you one of those. Here is what shares which half.",
 "body": """
  <div class="term tip">
    <div class="term-h">If you want one answer instead of eight</div>
    <p>Same <strong>group panic</strong>: R.E.P.O. Same <strong>look-carefully-then-panic rhythm</strong>: Phasmophobia. Same <strong>clock in for a cursed job</strong> framing: Content Warning. The rest of this page is the reasoning, and what each one gives up.</p>
  </div>

  <h2>At a glance</h2>

  <div class="tablewrap">
  <table class="data">
    <thead><tr><th>Game</th><th>Players</th><th>Closest to Shift At Midnight in&hellip;</th><th>Bundled with it</th></tr></thead>
    <tbody>
      <tr><td><strong>Phasmophobia</strong></td><td class="num">Up to 4</td><td>Evidence work, proximity voice</td><td class="num">Yes</td></tr>
      <tr><td><strong>Escape the Backrooms</strong></td><td class="num">Up to 4</td><td>Being somewhere wrong, together</td><td class="num">Yes</td></tr>
      <tr><td><strong>YAPYAP</strong></td><td class="num">Co-op</td><td>Tone &mdash; comic co-op horror</td><td class="num">Yes</td></tr>
      <tr><td><strong>R.E.P.O.</strong></td><td class="num">Up to 6</td><td>Cheap, loud, group-failure comedy</td><td class="num">&mdash;</td></tr>
      <tr><td><strong>Content Warning</strong></td><td class="num">Up to 4</td><td>The &ldquo;horror is your job&rdquo; framing</td><td class="num">&mdash;</td></tr>
      <tr><td><strong>Demonologist</strong></td><td class="num">Up to 4</td><td>Methodical paranormal investigation</td><td class="num">&mdash;</td></tr>
      <tr><td><strong>Dark Hours</strong></td><td class="num">Co-op</td><td>Atmosphere, staying unseen</td><td class="num">&mdash;</td></tr>
      <tr><td><strong>PEAK</strong></td><td class="num">Co-op</td><td>Co-op tension, very little horror</td><td class="num">&mdash;</td></tr>
    </tbody>
  </table>
  </div>

  <p>Player counts come from each game&rsquo;s own Steam listing and can move with updates. For comparison, Shift At Midnight is built around three players and now allows lobbies of up to six &mdash; see <a href="/multiplayer/">multiplayer</a>.</p>

  <h2>The three you can buy alongside it at a discount</h2>

  <p>Three of these ship in an <strong>official Steam bundle</strong> with Shift At Midnight. Each bundle takes <strong>10% off</strong>, and that saving stacks with other Steam discounts &mdash; so a sale is the cheapest moment to pick one up. Shift At Midnight itself is back to its normal <strong>$9.99</strong> now the launch discount has ended; the bundles are listed on the <a href="https://store.steampowered.com/app/3722330/Shift_At_Midnight/" target="_blank" rel="noopener">Steam store page</a>. More on the pricing at <a href="/review/#price">is it worth it</a>.</p>

  <h3>Phasmophobia</h3>
  <p>The closest thing this game has to a sibling. Both are proximity-voice co-op horror where the frightening act is <em>examining something carefully</em> and the failure state is being caught doing it. What differs is the subject: Phasmophobia hands you instruments and asks which <strong>type of ghost</strong> is in the house, while Shift At Midnight hands you an ID scanner and a database and asks whether the <strong>person at the counter</strong> is a person at all. If building a case from evidence was your favourite part, take this one.</p>

  <h3>Escape the Backrooms</h3>
  <p>Up to four players, and the bundle makes it a cheap experiment. It keeps the co-op dread and drops the job completely: level-by-level escape and exploration, with no counter to run, no quota, and nobody to question. Good if what you wanted was the feeling of being somewhere wrong with friends and you are happy to lose the management layer that came with it.</p>

  <h3>YAPYAP</h3>
  <p>The third bundle partner and the odd one out &mdash; magic-themed co-op horror rather than a workplace one. It is on this list for tone, not mechanics. Pick it for a group that wants to keep the shouting and never wants to see a form again.</p>

  <h2>If the chaos mattered more than the counter</h2>

  <h3>R.E.P.O.</h3>
  <p>Up to six players, similarly cheap, and the surest recommendation for a group that came to Shift At Midnight to laugh. The loop is physically hauling fragile valuables out of a building without smashing them, so the horror grows out of somebody else&rsquo;s clumsiness rather than a judgement call you got wrong. If your group&rsquo;s best stories are about panic and not deduction, start here.</p>

  <h3>Content Warning</h3>
  <p>Shares the framing that makes Shift At Midnight work: you are at work, the work is horror, and there are numbers to hit. What management wants is different &mdash; views. You film the monsters instead of processing customers, and the whole thing leans harder into comedy. Up to four players.</p>

  <h3>PEAK</h3>
  <p>Co-op, tense, and barely a horror game &mdash; the pressure comes from terrain and stamina rather than from something hunting you. Worth knowing about if your group is tired of being scared but still wants something to fail at together. Skip it if the fear was the point.</p>

  <h2>If the investigating mattered more</h2>

  <h3>Demonologist</h3>
  <p>Up to four players, and the most direct paranormal-investigation pick after Phasmophobia: traditional exorcism and haunted-house work. There is no business to run &mdash; no stock, no till, no shift target &mdash; so it satisfies the investigation half without the store-management layer some players bounce off.</p>

  <h3>Dark Hours</h3>
  <p>Co-op and atmosphere-led, built around sneaking and avoidance rather than confrontation. Shift At Midnight puts the threat across a counter and makes you question it; this one is about never sharing a room with it. A real change of pace, and a different skill.</p>

  <h2>Why the coverage kept reaching for Five Nights at Freddy&rsquo;s</h2>

  <p>Most launch write-ups compared it to FNAF, and the shorthand is fair enough: an underpaid employee, a workplace that turns hostile after dark, and a shift that has to be survived before you are allowed to leave. Reviewers also gave it credit for doing something of its own with that setup and for the nostalgic low-poly presentation. What the comparison misses is the part below.</p>

  <h2>What none of the eight replaces</h2>

  <p>Very few games make the <em>moral</em> decision the mechanical one. Here the frightening action is administrative: you decide whether to serve someone or kill them, on incomplete information, while a queue builds behind them. <strong>96.9% of players have killed a customer</strong> (<a href="https://steamcommunity.com/stats/3722330/achievements/" target="_blank" rel="noopener">Steam achievement stats</a>, checked 13 August 2026) &mdash; that is the design working as intended, not a community of monsters. Nothing on this list reproduces it, which is why every honest recommendation here shares one half of the game rather than replacing it.</p>

  <div class="grid two">
    <a class="card" href="/review/"><b>Is it worth it?</b><span>Price, the free demo, and what the review data says.</span></a>
    <a class="card" href="/guide/doppelgangers/"><b>The identification loop</b><span>The half none of these eight copy.</span></a>
  </div>
"""},

# are there levels 10 + is night three the last level 10@难度10 + 13 shifts
{
 "path": "nights-and-levels", "active": "/guides/",
 "title": "Shift At Midnight Nights &amp; Levels — How Many Are There?",
 "og_short": "Shift At Midnight Nights &amp; Levels",
 "desc": "Does Shift At Midnight have levels? It has shifts, and they are procedurally generated. What that means for night three and for guides promising a fixed route.",
 "trail": [(None, "Nights &amp; levels")],
 "h1": "Nights, shifts and levels",
 "lede": "Shift At Midnight does not have <em>levels</em> in the usual sense. It has <strong>shifts</strong>, and they are <strong>procedurally generated</strong> &mdash; which changes what any guide can honestly promise you about &ldquo;night three&rdquo;.",
 "body": """
  <h2>Why you will not find a night-by-night table here</h2>
  <p>Search for &ldquo;Shift At Midnight night 4&rdquo; and you will find pages that confidently list what
    turns up on each shift. Be careful with those. The customers and the events inside a shift are
    <strong>procedurally generated</strong> &mdash; the developer describes the run that way, and it matches
    what players report: two people on Shift 5 do not get the same shift. A fixed per-night monster
    schedule almost certainly does not exist to be documented.</p>
  <p>What is fixed is the spine: Shift 9 turns on the music box, the decision after Shift 12 sets your
    ending, and Shift 13 is the chase. Everything between those points escalates rather than switches.
    If you want to know what a given threat does when it shows up, the <a href="/monsters/">bestiary</a>
    is organised by threat rather than by night for exactly this reason.</p>

  <h2>Is night three the last level?</h2>

  <p><strong>No.</strong> If your run ended at night three, the run ended &mdash; the game did not. Story Mode continues well past that point.</p>

  <p>This question comes up because the demo covered a limited slice, so a lot of people's mental model of the game's length was set by a build that deliberately stopped early. The full release is considerably longer.</p>

  <h2>&ldquo;Levels&rdquo; is the wrong frame</h2>

  <p>A level is a fixed piece of authored content: same layout, same encounters, same order every time. Shift At Midnight's shifts are not that. They are generated, which means the specific sequence of customers and threats you get on any given night is not the sequence someone else got.</p>

  <p>The practical consequence, and the reason this matters: <strong>any guide handing you a night-by-night walkthrough is describing one person's run, not yours.</strong> That is why this wiki organises around <a href="/monsters/">threats</a> and systems rather than a numbered route &mdash; recognising a <a href="/monsters/shrieking-doll/">Shrieking Doll</a> by its scream is true on every seed; "on night four you will meet X" is not.</p>

  <div class="term tip">
    <div class="term-h">The one fixed beat</div>
    <p><a href="/monsters/norbert/">Norbert</a> is consistently reported on <strong>Night 2</strong> &mdash; a scripted teaching moment placed inside a procedural structure, early enough that learning the lesson still helps. If something is going to be fixed, it makes sense that it is the tutorial for the game's central rule.</p>
  </div>

  <h2>How long is a run?</h2>

  <p>Story Mode runs a sequence of shifts to a conclusion, with multiple possible outcomes &mdash; the three hidden achievements (<em>Grave Decision</em> 33.1%, <em>True Ending</em> 16.0%, <em>Empty Home</em> 10.1%) sit at the end of it. See <a href="/endings/">endings</a> for what those do and do not tell us.</p>

  <p>Endless Mode is the mode for people who want shifts without an ending, and it is worth being precise about its status because it is easy to read wrong: <strong>the Endless beta has been in the game since launch day</strong>, unlocked once the 13-shift story is finished. The free <strong>Q4 2026</strong> update is the <em>finished</em> version of that mode, not its arrival. See <a href="/nights-and-levels/#endless-mode">Endless Mode</a> below.</p>

  <h2>The Rake, and why it is not on the shift list</h2>

  <p>The <a href="/updates/">29 July 2026 patch</a> added a new enemy called the <strong>Rake</strong>. It
    belongs on this page for one reason: <strong>Story Mode never spawns one.</strong> The official
    announcement places Rakes in endless mode, emerging from the forests around the station.</p>

  <p>So if you are working through the 13 shifts waiting to meet one, you are waiting for something that
    will not arrive. And if you finished the story before 29 July, you have never seen a Rake &mdash;
    finishing again will not introduce you either, because Endless is where they live and Endless opens
    only after Shift 13.</p>

  <div class="term warn">
    <div class="term-h">Almost everything else about the Rake is undocumented</div>
    <p>One sentence in one patch announcement is the entire official record: Rakes emerge from forests in
      endless mode. A single-source community description of their behaviour is quoted, and clearly flagged
      as unconfirmed, on the <a href="/monsters/">bestiary</a>. Past that we have <strong>no verified
      counterplay and no health, damage or speed figures</strong>, and no confirmation of how many appear or
      what brings them out. The pages that do carry those details had no source we could check &mdash; two of
      the sites people cite for them were unreachable when we tried on 12 August 2026, and a third is an
      automated content farm we will not source from.</p>
  </div>

  <p>That is why there is no Rake page on this wiki. The six threats that do have their own pages have
    something worth writing down &mdash; a music box with a three-melody clock, a warning email before
    Shift 9, an achievement tied to the kill, a documented reason the obvious response gets you killed.
    The Rake currently has a mode and a treeline. When there is more, it gets a page, with a date on it.</p>

  <div class="grid two">
    <a class="card" href="/nights-and-levels/#story-mode"><b>Story Mode</b><span>The structure in full.</span></a>
    <a class="card" href="/endings/"><b>Endings</b><span>What the run is building toward.</span></a>
  </div>
"""},

# --- 2026-08-12 补页(取证底稿 facts.md A 表判 OK 的四条)---------------------
# 每页末尾都有「什么没写、为什么」一节 —— 与 /guide/doppelgangers/、/mods/ 同一做法。
# 所有数字带采集日期;单一来源的说法在正文里标 not independently verified。

# system requirements / can i run it / steam deck —— 竞品 shiftatmidnightwiki.wiki 与
# theclick.gg 都已建页,本站此前完全空白
{
 "path": "system-requirements", "active": "/guides/",
 "title": "Shift At Midnight System Requirements — PC, Steam Deck &amp; Xbox",
 "og_short": "System Requirements",
 "desc": "Shift At Midnight needs a GTX 1050 Ti, an i5-10400F and 8 GB of RAM at minimum, with a 3 GB install. Full Steam specs, the Steam Deck rating and what the Xbox listing adds.",
 "trail": [(None, "System requirements")],
 "h1": "Shift At Midnight system requirements",
 "lede": "<strong>Minimum is a GTX 1050 Ti, an Intel Core i5-10400F and 8 GB of RAM, and the install is 3 GB.</strong> Both tiers below are copied field for field from the Steam store listing, alongside what the Xbox listing adds and where the Steam Deck rating actually comes from.",
 "body": """
  <div class="term tip">
    <div class="term-h">The short answer</div>
    <p>This is a small game and the requirements say so. <strong>Minimum: Windows 10/11 64-bit, an i5-10400F, 8 GB RAM, a GTX 1050 Ti, DirectX 11 and 3 GB of free space.</strong> A broadband connection is listed on both tiers, because the co-op is online only. Every figure on this page was read from the official store listings on <strong>12 August 2026</strong>.</p>
  </div>

  <h2>Minimum specification, as Steam lists it</h2>

  <table class="facts">
    <tr><th>OS</th><td>Windows 10/11 (64-bit)</td></tr>
    <tr><th>Processor</th><td>Intel Core i5-10400F or Equivalent</td></tr>
    <tr><th>Memory</th><td>8 GB RAM</td></tr>
    <tr><th>Graphics</th><td>NVIDIA GeForce GTX 1050 Ti or Equivalent</td></tr>
    <tr><th>DirectX</th><td>Version 11</td></tr>
    <tr><th>Network</th><td>Broadband Internet connection</td></tr>
    <tr><th>Storage</th><td>3 GB available space</td></tr>
  </table>

  <h2>Recommended specification, as Steam lists it</h2>

  <table class="facts">
    <tr><th>OS</th><td>Windows 11 (64-bit)</td></tr>
    <tr><th>Processor</th><td>Intel Core i5-10400 / AMD Ryzen 7 5800X or Equivalent</td></tr>
    <tr><th>Memory</th><td>16 GB RAM</td></tr>
    <tr><th>Graphics</th><td>NVIDIA GeForce GTX 1660 Ti (6GB) or Equivalent</td></tr>
    <tr><th>DirectX</th><td>Version 12</td></tr>
    <tr><th>Network</th><td>Broadband Internet connection</td></tr>
    <tr><th>Storage</th><td>3 GB available space</td></tr>
  </table>

  <p class="src">Source: the <a href="https://store.steampowered.com/app/3722330/Shift_At_Midnight/" target="_blank" rel="noopener">Steam store listing</a>, read 12 August 2026. Both tiers list the same 3 GB install size.</p>

  <h2>The processor row that looks like a mistake</h2>

  <p>Read the two processor lines next to each other and the recommended tier looks like a downgrade: minimum asks for an <strong>i5-10400F</strong>, recommended asks for an <strong>i5-10400</strong>. We have reproduced both rows exactly as the store page prints them rather than tidying one to match the other. <strong>We do not know whether that is a typo on the listing or deliberate</strong>, and there is no second source for either row &mdash; the store page is the only place these specs are published.</p>

  <p>The usable reading is that a tenth-generation i5 clears both tiers, and the real distance between minimum and recommended sits elsewhere: the graphics card, the RAM, and DirectX 11 against 12.</p>

  <h2>Steam Deck: rated Playable, and by whom</h2>

  <p>SteamDB records Shift At Midnight as <strong>Playable</strong> on Steam Deck, in both its app info panel and its main app page, with Valve&rsquo;s standard wording for that tier: &ldquo;Some functionality is not accessible when using the default controller configuration, requiring use of the touchscreen or virtual keyboard, or a community configuration.&rdquo;</p>

  <div class="term warn">
    <div class="term-h">Single source &mdash; not independently verified</div>
    <p>Both places that rating appears are SteamDB. When we read the Steam store page itself on 12 August 2026 we <strong>did not see a Deck compatibility panel at all</strong> &mdash; that may be a limitation of how we fetched the page, or the rating may simply not be shown there. If you are buying specifically to play on a Deck, <strong>look for the badge on the store page yourself first</strong>. ProtonDB, the other place people check, needs JavaScript to render its reports and we could not read it.</p>
  </div>

  <p>Playable is not Verified, and the gap matters for this game in particular: it is built around comparing documents at a terminal, which is exactly the kind of interaction Valve&rsquo;s Playable wording warns may need the touchscreen or a community layout. There is also an open Steam discussion thread titled &ldquo;Steam deck - i press play and nothing happens&rdquo;. We have no verified fix for that &mdash; what we can and cannot say about it is on <a href="/troubleshooting/">troubleshooting</a>.</p>

  <h2>What the Xbox listing promises that the Steam one does not</h2>

  <table class="facts">
    <tr><th>Price</th><td>$9.99 &mdash; included with PC Game Pass and Xbox Game Pass Ultimate</td></tr>
    <tr><th>Co-op</th><td>Online co-op 2&ndash;3 players; Xbox cross-platform co-op</td></tr>
    <tr><th>Display</th><td>4K Ultra HD; Optimized for Xbox Series X|S</td></tr>
    <tr><th>Saves</th><td>Xbox cloud saves</td></tr>
    <tr><th>Ownership</th><td>Xbox Play Anywhere</td></tr>
    <tr><th>Handheld</th><td>Handheld compatible</td></tr>
    <tr><th>Streaming</th><td>Cloud playable, with Game Pass Ultimate</td></tr>
  </table>

  <p>Two of those rows change the answer to &ldquo;can I run it&rdquo;. <strong>Cloud playable</strong> means a Game Pass Ultimate subscriber can start it on hardware that meets none of the specs above, because the game is not running on their machine. <strong>Xbox cloud saves</strong> is a capability the Steam version does not list at all &mdash; see the next section.</p>

  <p>One row is worth flagging rather than smoothing over: the Xbox listing still records online co-op as <strong>2&ndash;3 players</strong>, while the 23 July 2026 patch made the lobby cap selectable up to six on Steam. We have found no official statement about whether that six-player option exists on Xbox, so we are not going to assume it does. See <a href="/multiplayer/">multiplayer</a> for what the developer actually said about lobby size.</p>

  <h2>Saves: Steam does not list Steam Cloud</h2>

  <p>The Steam feature list for this game reads: Single-player, Multi-player, Co-op, Online Co-op, Steam Achievements, Adjustable Text Size, Custom Volume Controls, Stereo Sound, Family Sharing. <strong>Steam Cloud is not on it.</strong> We checked the store page a second time specifically for that entry and it is absent, while the Xbox listing does carry Xbox cloud saves.</p>

  <p>The practical consequence for Steam players: treat your progress as living on one machine. We are not going to tell you which folder to back up, because we could not verify a save path &mdash; that is in the last section, with the reason.</p>

  <h2>Controller, accessibility and two different age ratings</h2>

  <ul>
    <li><strong>Controller:</strong> SteamDB&rsquo;s app info panel records <em>Gamepad supported</em>. That is a listing flag rather than a statement about how well the game plays on a pad, and we have found no official note on which inputs are or are not mapped.</li>
    <li><strong>Accessibility:</strong> Steam records <em>Adjustable Text Size</em> and <em>Custom Volume Controls</em> as features, and lists audio as <em>Stereo Sound</em>. There is no surround or spatial-audio flag on the listing, which is worth knowing in a game where sound direction is a survival tool &mdash; see <a href="/guide/survival/">survival</a>.</li>
    <li><strong>Languages:</strong> nine on Steam, listed in full on <a href="/release-date/">release date</a>.</li>
    <li><strong>Family Sharing:</strong> listed as supported on Steam.</li>
    <li><strong>Age rating:</strong> the two storefronts present this very differently. Steam&rsquo;s listing carries a required age of 0 with content descriptors for <em>Violence</em> and <em>Gore/Blood</em>; the Xbox store lists it as <strong>MATURE 17+</strong> for Violence, Blood and Gore, and Language. Same game, two labels that look nothing alike.</li>
  </ul>

  <h2>What this page cannot tell you, and why</h2>

  <p>Four things people ask that are deliberately missing above:</p>

  <ul>
    <li><strong>Frame rates on specific hardware.</strong> No benchmark we could check has been published. A spec sheet is not a benchmark and we are not going to convert one into the other.</li>
    <li><strong>Save file locations, config file paths, and the in-game graphics options list.</strong> The usual reference for this is PC Gaming Wiki. Both URL variants we tried returned HTTP 403 on 12 August 2026, so there is nothing here we could verify and nothing to copy.</li>
    <li><strong>Xbox install size.</strong> The Xbox listing did not show one when we read it. The 3 GB above is the Steam number and we are not assuming it transfers.</li>
    <li><strong>Linux and Proton behaviour.</strong> ProtonDB requires JavaScript to render and we could not read it. The SteamDB Deck rating above is the only compatibility signal we have, and it carries the caveat in that section.</li>
  </ul>

  <p>If any of those become verifiable, they get added here with a date and a source, the way everything else on this page is.</p>

  <div class="grid two">
    <a class="card" href="/troubleshooting/"><b>It installed and will not run</b><span>Lobby errors, crashes, black screens &mdash; and which of them have official fixes.</span></a>
    <a class="card" href="/platforms/"><b>Platforms &amp; Game Pass</b><span>Where the game exists at all, and what Play Anywhere covers.</span></a>
  </div>
"""},

# demo steam 560 + how much content in demo 520 + how long is the demo
# 原 /demo/ 页曾并入 /review/#demo;2026-08-12 拆回独立页,同时撤掉 vercel.json 的三条 308。
{
 "path": "demo", "active": "/guides/",
 "title": "Shift At Midnight Demo — What Is In It vs the Full Game",
 "og_short": "Shift At Midnight Demo",
 "desc": "The free Shift At Midnight demo is limited to three pre-scripted shifts against 13 randomly generated ones in the full game. What it contains, and the free itch.io build it grew out of.",
 "trail": [(None, "Demo")],
 "h1": "The Shift At Midnight demo",
 "lede": "<strong>There is a free demo, and it was still listed on 12 August 2026.</strong> The developer describes it as three pre-scripted shifts with a limited set of tools; the full game runs 13 randomly generated ones. This page covers that difference, and the free itch.io build the whole thing started as.",
 "body": """
  <div class="term tip">
    <div class="term-h">The short answer</div>
    <p>The demo is a <strong>separate free app on Steam</strong> called <em>Shift At Midnight Multiplayer Demo</em>, released 29 September 2025 by the same developer and publisher as the full game. It limits you to <strong>three pre-scripted shifts</strong>. The full game is $9.99, or included with Game Pass, and runs <strong>13 randomly generated</strong> shifts.</p>
  </div>

  <table class="facts">
    <tr><th>Demo</th><td>Shift At Midnight Multiplayer Demo &mdash; free, separate Steam app (ID 4050060)</td></tr>
    <tr><th>Demo released</th><td>29 September 2025</td></tr>
    <tr><th>Made by</th><td>Bun Muen, published by Kwalee &mdash; same as the full game</td></tr>
    <tr><th>Demo content</th><td>Three pre-scripted shifts; a limited set of tools and weapons</td></tr>
    <tr><th>Full game content</th><td>13 randomly generated shifts &mdash; see <a href="/nights-and-levels/">nights &amp; shifts</a></td></tr>
    <tr><th>Still available?</th><td>Yes &mdash; the store page still showed a Download Demo button on 12 August 2026</td></tr>
    <tr><th>Does progress carry over?</th><td>No official statement either way &mdash; see below</td></tr>
  </table>

  <h2>What the demo limits, in the developer&rsquo;s own words</h2>

  <p>The demo&rsquo;s own store page says it plainly enough that paraphrasing would only blur it:</p>

  <div class="term tip">
    <div class="term-h">Quoted from the demo store page</div>
    <p><em>&ldquo;This demo contains some introductory content from the full version of Shift at Midnight. This demo limits the gameplay to three pre-scripted shifts, while the full game will contain 13 randomly generated shifts. The demo also provides a limited set of tools and weapons to experiment with.&rdquo;</em></p>
  </div>

  <p>There are three separate claims in there, and each one changes what the demo can honestly tell you about the full game.</p>

  <h2>Pre-scripted against randomly generated</h2>

  <p>This is the difference that matters most, and the one most demo write-ups skip. The demo&rsquo;s three shifts are <strong>scripted</strong> &mdash; the same events in the same order for everyone who plays it. Story mode&rsquo;s 13 shifts are <strong>generated</strong>, which is why this wiki refuses to publish a night-by-night table, and why two players comparing notes about &ldquo;shift five&rdquo; are often describing different nights.</p>

  <p>So the demo is an accurate preview of the <em>loop</em> &mdash; a customer at the counter, a document that may not be real, a decision with consequences &mdash; and a misleading preview of the <em>experience</em>, because what keeps the full game tense is not knowing what is queued behind the door. If you played the demo twice and found the second run flat, that is the scripting, not the game.</p>

  <h2>A limited set of tools and weapons</h2>

  <p>The store text says the demo hands you a reduced kit, without listing what is held back. <strong>We are not going to fill that list in.</strong> No official inventory of the demo build has been published, demo builds were revised over the run-up to launch, and any list we wrote would be one person&rsquo;s recollection of one version presented as a specification.</p>

  <p>What the full release definitively adds is documented elsewhere on this wiki with sources: the complete <a href="/monsters/">bestiary</a>, all ten <a href="/achievements/">achievements</a>, the ending structure the three hidden ones sit behind, and everything the two post-launch patches introduced &mdash; a second purchasable firearm and the Rake, neither of which existed when the demo shipped. See <a href="/updates/">patch notes</a>.</p>

  <h2>Where this game actually started: the free itch.io build</h2>

  <p>Before the Steam demo there was a free itch.io release, still up at <a href="https://bunmuen.itch.io/shiftatmidnight" target="_blank" rel="noopener">bunmuen.itch.io/shiftatmidnight</a>. It is a different thing from the Steam demo, and worth knowing about if you want to see where the design came from:</p>

  <ul>
    <li><strong>Single-player</strong>, free, PC download, and around 40 minutes long by the page&rsquo;s own description.</li>
    <li>Rated <strong>4.7 out of 5 from 360 ratings</strong> on that page.</li>
    <li>Carries the label <strong>&ldquo;No generative AI used&rdquo;</strong>.</li>
    <li>Tagged 3D, Atmospheric, Creepy, Psychological Horror and First-Person, under Simulation and Horror.</li>
    <li>The page describes its own next step as a multiplayer co-op Steam demo, expanding the original from one night to three.</li>
  </ul>

  <p>That last line is the useful piece of history: <strong>the co-op was added on the way to the Steam demo, not present at the start.</strong> The game people now describe as &ldquo;the one where three friends argue about a customer&rdquo; began as a 40-minute solo horror piece.</p>

  <h2>Does demo progress carry into the full game?</h2>

  <p><strong>We could not find an answer, and we are not going to guess at one.</strong> No statement from the developer or the publisher addresses whether demo saves, progress or unlocks transfer, and the demo is a separate Steam app rather than a mode inside the full one. Plan on starting over, and treat any page that answers this confidently without a source as unreliable.</p>

  <h2>Is it still worth downloading now the full game is out?</h2>

  <p>Two situations where it genuinely still is:</p>

  <ul>
    <li><strong>You are not sure your machine runs it.</strong> A free download is a better test than a refund request. The published specs are on <a href="/system-requirements/">system requirements</a>, but a spec sheet is a prediction and the demo is a measurement.</li>
    <li><strong>You want to hear proximity chat before buying for a group.</strong> It is the mechanic the game is built on, and the one people either love or immediately want to switch off.</li>
  </ul>

  <p>Against that: if you have Game Pass the full game already costs you nothing, and at $9.99 the demo&rsquo;s selling job is mostly done. See <a href="/review/">is it worth it?</a></p>

  <h2>What this page does not claim about the demo</h2>

  <ul>
    <li><strong>A shift-by-shift walkthrough of the demo.</strong> Three scripted shifts could be documented in principle, but not from any source we can verify, and a walkthrough written from memory is exactly the sort of content this wiki exists to avoid.</li>
    <li><strong>How many people played it.</strong> One outlet, GameRant, reported on 23 July 2026 that the demo had been reviewed by more than 8,000 players. That is a single report and <strong>not independently verified</strong> &mdash; we could not confirm it against Steam directly, so treat it as one outlet&rsquo;s figure rather than a fact.</li>
    <li><strong>Whether today&rsquo;s demo build matches the launch-week one.</strong> There is no changelog for the demo app, so we cannot tell you whether it has been updated since.</li>
    <li><strong>An exact playtime for the Steam demo.</strong> The itch.io page gives roughly 40 minutes for the original single-player build. Nobody has published a figure for the three-shift Steam demo, and we are not converting one into the other.</li>
  </ul>

  <div class="grid two">
    <a class="card" href="/review/"><b>Is it worth it?</b><span>Price, the Steam review data, and the honest case against buying.</span></a>
    <a class="card" href="/guide/beginners/"><b>Beginner&rsquo;s guide</b><span>What the demo teaches, and the parts it never gets to.</span></a>
  </div>
"""},

# troubleshooting / cant join lobby / crash / black screen —— 竞品 theshiftatmidnight.com、
# lagofast、shiftatmidnightguide.wiki 都靠这组词排名,官方讨论区也高频
{
 "path": "troubleshooting", "active": "/guides/",
 "title": "Shift At Midnight Not Working — Lobby, Crash &amp; Audio Problems",
 "og_short": "Troubleshooting",
 "desc": "Cannot join a lobby in Shift At Midnight, or hitting crashes, a black screen or no sound? The developer's official steps, what each patch fixed, and which problems have no verified fix.",
 "trail": [(None, "Troubleshooting")],
 "h1": "Shift At Midnight troubleshooting",
 "lede": "Two of the problems people hit have <strong>official, published fixes</strong>. The rest do not, and this page is careful about which is which. Nothing below is a registry edit, a driver cleaner or a &ldquo;booster&rdquo; download.",
 "body": """
  <div class="term tip">
    <div class="term-h">Read this first</div>
    <p>Almost every report falls into one of three shapes: a <strong>lobby you cannot create or join</strong>, a <strong>party split across two storefronts</strong>, or a <strong>party split across two Steam branches</strong>. The first has official steps, the second cannot be fixed at all, and the third is a two-minute check. Everything further down is honest about being unresolved.</p>
  </div>

  <h2>Cannot create or join a lobby</h2>

  <p>On launch day, 22 July 2026, the developer published a post titled &ldquo;CAN&rsquo;T JOIN A LOBBY?&rdquo; offering an opt-in Steam branch as a temporary measure while the connection problems were being worked on. These are the steps as published:</p>

  <ol>
    <li>Open your Steam library and <strong>right-click Shift At Midnight</strong>.</li>
    <li>Go to <strong>Properties</strong>.</li>
    <li>Open <strong>Game Versions &amp; Betas</strong>.</li>
    <li>Enter the code exactly as written: <code>networkissues</code></li>
    <li>Opt into the branch that becomes available &mdash; <code>network-issues-patch</code>.</li>
  </ol>

  <p>The announcement adds one line that people skip, and it is the line that decides whether any of this works: <strong>&ldquo;Everyone you play with must also follow these instructions.&rdquo;</strong> One person on the branch and two on the default build is not a partial fix &mdash; it is a party that cannot see each other. GameGrin restated the same steps in a 23 July 2026 write-up, which is the only second source we found for them.</p>

  <div class="term warn">
    <div class="term-h">Status of that branch: unclear, and we will not pretend otherwise</div>
    <p>It was published as a <strong>launch-week stopgap</strong>. The 23 July patch that followed did fix Russian-region players being unable to create joinable lobbies, but <strong>no announcement has ever been published retiring the branch</strong>, so we cannot give you a date on which it stopped being necessary. Two practical consequences: if you opted in during launch week and never switched back, check which branch you are on; and if you opt in now, everyone in the party has to do it together.</p>
  </div>

  <h2>You are all online and still cannot see each other</h2>

  <p>This is the most common &ldquo;the multiplayer is broken&rdquo; report, and most of the time nothing is broken. Work down this list in order:</p>

  <ul>
    <li><strong>Are you on the same storefront?</strong> Steam players connect only to Steam players. Xbox console and PC Game Pass players share one pool through Play Anywhere. A Steam player and a Game Pass player <strong>cannot</strong> play together and no setting changes that &mdash; see <a href="/crossplay/">crossplay</a>, or run your group through the <a href="/tools/#crossplay-checker">crossplay checker</a>.</li>
    <li><strong>Are you on the same branch?</strong> See the section above. Mismatched Steam branches produce exactly this symptom.</li>
    <li><strong>Are you on the same build?</strong> If one of you still sees a patience meter on customers, or cannot set a lobby above three, that install has not updated. <a href="/updates/">Patch notes</a> lists the tells.</li>
    <li><strong>Is lobby size the problem?</strong> The cap has been selectable up to six since 23 July 2026, but the developer has been explicit that the game is designed around three. See <a href="/multiplayer/">multiplayer</a>.</li>
  </ul>

  <p>There is no server browser to fall back on. One was announced before launch as a post-release addition and it is still not live, so joining is invite and party based &mdash; which is why a mismatch anywhere in that list looks like an outage.</p>

  <h2>Crashes, and the cursor problem that follows them</h2>

  <p>Two patches have touched this, and one known issue is on the record:</p>

  <ul>
    <li><strong>23 July 2026.</strong> The announcement closed by previewing that the next patch would address <strong>&ldquo;cursor interaction issues after crashes&rdquo;</strong> &mdash; the developer&rsquo;s own words for a state where the game has crashed and the mouse afterwards does not behave.</li>
    <li><strong>29 July 2026.</strong> Those patch notes list &ldquo;various bug fixes and crash fixes&rdquo; without itemising them, and <strong>do not say whether the cursor issue was among them</strong>. We looked for a follow-up announcement clarifying it; there is not one.</li>
  </ul>

  <p>So the honest position on crashes is this: the developer acknowledged a specific cursor-after-crash problem, shipped an unspecified set of crash fixes six days later, and never closed the loop publicly. If you are hitting it, you are not imagining it, and it is not fixed on the record.</p>

  <p>Two steps we can stand behind: <strong>let Steam verify the game files</strong> rather than reinstalling &mdash; the install is only 3 GB, so a verify is quick &mdash; and confirm you are actually on the newest build, because a stalled update is the cheapest explanation for a problem the patch notes claim was fixed.</p>

  <h2>Black screens, missing audio and a PC that switches itself off</h2>

  <p>These are real threads on the official Steam discussion board: a black screen report, a no-audio report, and one titled &ldquo;PC Shuts itself down?&rdquo; with several replies. We list them because knowing other people have the same symptom is worth something. What we are <strong>not</strong> doing is inventing steps.</p>

  <div class="term warn">
    <div class="term-h">No verified fix exists for any of these</div>
    <p>None has an official acknowledgement, a patch note, or a developer reply that we could find. Anything you read that confidently &ldquo;fixes&rdquo; a black screen in this specific game &mdash; particularly a page that ends in a download &mdash; is written from a template rather than from evidence. Report the symptom on the Steam board or the game&rsquo;s Discord, where the developer takes bug reports, and include your build and your hardware.</p>
  </div>

  <h2>Steam Deck: pressing Play does nothing</h2>

  <p>There is a Steam discussion thread titled &ldquo;Steam deck - i press play and nothing happens&rdquo;. We have no verified fix and no official comment on it. What we can give you is the context: the only Deck compatibility rating we could find is SteamDB&rsquo;s <strong>Playable</strong>, it comes from a single source, and the Steam store page itself did not show a compatibility panel when we read it on 12 August 2026. The detail, and why that matters before you buy, is on <a href="/system-requirements/">system requirements</a>.</p>

  <h2>Things that look like bugs and are not</h2>

  <ul>
    <li><strong>Endless Mode is locked.</strong> It is not missing. Endless shipped as a beta on launch day but unlocks only once you have finished the 13-shift story &mdash; see <a href="/nights-and-levels/#endless-mode">Endless Mode</a>.</li>
    <li><strong>Norbert scans as a fake ID.</strong> Working as designed. He is flagged and he is harmless; the scanner reports on documents, not on intent. See <a href="/monsters/norbert/">Norbert</a>.</li>
    <li><strong>Customers no longer run out of patience.</strong> The patience mechanic was removed on 29 July 2026. If a guide told you to hurry, the guide is older than the patch.</li>
    <li><strong>The music box got louder.</strong> Also deliberate &mdash; the 23 July patch raised Jack-in-the-Box volume, and locating it by ear is the entire counterplay to the <a href="/monsters/marionette/">Marionette</a>.</li>
    <li><strong>Swearing is no longer filtered.</strong> The profanity filter was removed on 23 July 2026.</li>
  </ul>

  <h2>Reports we could not corroborate, and fixes we will not invent</h2>

  <ul>
    <li><strong>Microphone not detected.</strong> There is one discussion thread on this, posted 29 September 2025 &mdash; during the demo period, ten months before release &mdash; from a player whose main microphone was not picked up while a webcam mic worked. It has <strong>no replies and no developer response</strong>. One unanswered post about a different build is not enough to write a fix around, so we have not.</li>
    <li><strong>Whether the launch beta branch is still needed.</strong> Never officially retired, as above.</li>
    <li><strong>Anything that would require a save file or config path.</strong> We could not verify where this game stores either &mdash; the reference we would normally use returned HTTP 403 &mdash; so there is no &ldquo;delete this folder&rdquo; step anywhere on this page.</li>
    <li><strong>Network tuning, VPNs and &ldquo;lag fix&rdquo; tools.</strong> Several sites rank for this game&rsquo;s connection problems by recommending a product. We have no evidence that any of them addresses a lobby problem whose official fix was a Steam branch, so we do not recommend them.</li>
  </ul>

  <p>When any of these gets an official answer, it lands here with the date and the source.</p>

  <div class="grid two">
    <a class="card" href="/updates/"><b>Patch notes</b><span>Every published change since launch, and what each one actually fixed.</span></a>
    <a class="card danger" href="/crossplay/"><b>Crossplay</b><span>The one problem on this page that has no fix at all.</span></a>
  </div>
"""},

# player count / is anyone still playing / steam charts —— SteamDB、Raijin、games-popularity
# 都有该词条页;三源数字互不一致,所以页面写成「截至 X 日 + 逐源标注」而不是给一个数
{
 "path": "player-count", "active": "/guides/",
 "title": "Shift At Midnight Player Count — Is Anyone Still Playing?",
 "og_short": "Player Count",
 "desc": "Shift At Midnight peaked at 37,590 concurrent Steam players in July 2026 by SteamDB's count, and the trackers do not agree with each other. Every figure here carries its source and date.",
 "trail": [(None, "Player count")],
 "h1": "Shift At Midnight player count",
 "lede": "<strong>Yes, people are still playing.</strong> But the trackers do not agree with one another, so every number below carries the source it came from and the moment it was read &mdash; and one widely-quoted figure is one we will not repeat, for a reason we show you.",
 "body": """
  <div class="term tip">
    <div class="term-h">The short answer, as of 12 August 2026</div>
    <p>SteamDB&rsquo;s all-time concurrent peak for Shift At Midnight is <strong>37,590</strong>, set on 26 July 2026. Its chart page &mdash; carrying its own timestamp of 10 August 2026, 19:42:18 UTC &mdash; showed <strong>6,664 players in game</strong> and a 24-hour peak of <strong>14,691</strong>. Those are Steam concurrents only: Xbox and Game Pass numbers are not published anywhere.</p>
  </div>

  <h2>The numbers, and when each one was read</h2>

  <table class="facts">
    <tr><th>SteamDB &mdash; all-time peak</th><td>37,590, on 26 July 2026</td></tr>
    <tr><th>SteamDB &mdash; 24-hour peak</th><td>14,691</td></tr>
    <tr><th>SteamDB &mdash; in game</th><td>6,664, page timestamped 10 August 2026 19:42:18 UTC</td></tr>
    <tr><th>Raijin &mdash; all-time peak</th><td>37,447, recorded as July 2026</td></tr>
    <tr><th>Raijin &mdash; in game</th><td>7,491, read 11 August 2026 UTC</td></tr>
    <tr><th>Softonic, 27 July 2026</th><td>&ldquo;37,000 players by July 27&rdquo;</td></tr>
    <tr><th>Xbox / Game Pass players</th><td>Not published &mdash; no public source exists</td></tr>
  </table>

  <p class="src">All three sources were read on 11&ndash;12 August 2026. Where a page carried its own timestamp we have used that rather than ours.</p>

  <h2>The three trackers disagree, and that is the point</h2>

  <p>Look down the all-time peak rows: <strong>37,590</strong>, <strong>37,447</strong>, and &ldquo;37,000&rdquo;. Then the live rows: <strong>6,664</strong> against <strong>7,491</strong>, read roughly a day apart. Both spreads are small, but they are spreads &mdash; and every site quoting one of those numbers as <em>the</em> player count is presenting one sampler&rsquo;s reading as a census.</p>

  <p>Two things cause it. <strong>Sampling:</strong> none of these services receives a live feed of every session, so each polls on its own schedule, and an all-time peak is whatever the highest sample happened to catch. <strong>Timing:</strong> a live figure read at 19:42 UTC and one read the next day describe different points in a daily cycle that rises and falls with evenings in each region.</p>

  <p><strong>Our position:</strong> use SteamDB, cite the date, and do not average across trackers. Averaging numbers produced by different methods invents a figure that no source supports.</p>

  <h2>The figure we are not going to repeat</h2>

  <p>One tracker reports that in August 2026 so far the game is averaging 10,311 players a day with a peak of 26,230, and describes that as an increase of <strong>36.3%</strong> over July.</p>

  <p>That does not hold together. The same site&rsquo;s own all-time peak, 37,447, sits in July. A month peaking at 26,230 is not up 36.3% on a month that peaked at 37,447, whatever is being averaged underneath. We cannot see the method, so we cannot say which half is wrong &mdash; only that both cannot be right, which is enough reason to leave the number off this page. <strong>When an aggregate contradicts the same page&rsquo;s own history, the aggregate is the part to distrust.</strong></p>

  <h2>Concurrents are not the player base</h2>

  <p>&ldquo;6,664 players&rdquo; means 6,664 sessions running at one instant on one storefront. It is not how many people own the game, not how many played that day, and not how many played that week. For this game the gap is unusually wide, for three specific reasons:</p>

  <ul>
    <li><strong>Game Pass is invisible here.</strong> The game launched day one on Xbox and PC Game Pass, and none of those sessions appear in a Steam chart. For a title where a large share of players may never have paid for it, a Steam-only count is watching one of two front doors.</li>
    <li><strong>It is co-op, so sessions cluster.</strong> Groups of three playing on a Friday evening produce a very different chart shape from the same number of people playing alone across a week.</li>
    <li><strong>It is short and it is finishable.</strong> A 13-shift story is meant to be completed and put down. A falling concurrent count for this kind of release is the expected curve, not a verdict.</li>
  </ul>

  <h2>The review count is the other half of the picture</h2>

  <p>Reviews accumulate rather than fluctuate, which makes them a steadier signal of how many people have actually played than any concurrent reading. Read from the Steam store page on <strong>12 August 2026</strong>:</p>

  <ul>
    <li>Overall: <strong>Very Positive</strong>, from <strong>7,114</strong> reviews.</li>
    <li>English: <strong>94% of 3,363</strong> reviews positive.</li>
    <li>Simplified Chinese: Mostly Positive, 2,014 reviews. Russian: Very Positive, 672.</li>
  </ul>

  <p>For contrast, GameRant reported on <strong>23 July 2026</strong>, the day after launch, that more than 800 players had reviewed the game at 90% positive. Whatever the trackers disagree about, a review count that has grown roughly ninefold in three weeks is a consistent picture of a game people kept buying.</p>

  <div class="term warn">
    <div class="term-h">One conflict we cannot resolve</div>
    <p>The Steam store page gave <strong>7,114</strong> reviews on 12 August 2026. One tracker reported <strong>8.2K</strong> reviews at 88% positive on 11 August 2026 &mdash; a day earlier, and higher. We have not found a way to reconcile the two and it may be a difference in what each counts. <strong>We quote the store page because it is the primary source</strong>, and we are flagging the other figure rather than quietly dropping it.</p>
  </div>

  <h2>What no public number can tell you</h2>

  <ul>
    <li><strong>Xbox and Game Pass players.</strong> Microsoft does not publish per-title figures, and neither the developer nor the publisher has released any. Every &ldquo;total players&rdquo; number you see for this game is a Steam number wearing a bigger hat.</li>
    <li><strong>Unique players, or how many finished it.</strong> The closest public proxy is achievement rarity &mdash; 93.8% survive a first hunt, 16.0% reach the True Ending &mdash; and those are percentages of Steam owners, not counts. See <a href="/achievements/">achievements</a>.</li>
    <li><strong>Whether the game is growing or shrinking this month.</strong> We have one all-time peak with a date and two live readings a day apart. That is not a trend, and the one source that offered a month-over-month figure contradicted itself, as above.</li>
    <li><strong>How many are in the demo.</strong> The <a href="/demo/">free demo</a> is a separate app with its own, unpublished numbers.</li>
  </ul>

  <p>If a source with a visible methodology publishes any of that, it lands here with the date attached.</p>

  <div class="grid two">
    <a class="card" href="/review/"><b>Is it worth it?</b><span>What the review data and the achievement curve actually support.</span></a>
    <a class="card" href="/multiplayer/"><b>Finding people to play with</b><span>Player count is not why your group cannot connect &mdash; this usually is.</span></a>
  </div>
"""},

# --- 站点法务/信任页:教程检查清单要求 + AdSense 硬门槛 ---
# 结构沿用 beastofreincarnation.online 已验证的版本(联系表 / 不做什么 / 编辑标准)
{
 "path": "about", "active": "",
 "title": "About Shift At Midnight Wiki — Who We Are &amp; How We Source",
 "og_short": "About This Wiki",
 "desc": "Who runs this Shift At Midnight wiki, our editorial standards, and the rule we follow: label inference as inference and never invent a requirement.",
 "trail": [(None, "About")],
 "h1": "About this site",
 "lede": "shiftatmidnightwiki.site is an independent, fan-made guide hub for <strong>Shift At Midnight</strong> &mdash; the co-op survival horror game by solo developer Bun Muen, published by Kwalee, released 22 July 2026 on Steam, Xbox Series X|S and Xbox Game Pass.",
 "body": """
  <h2>Who runs this site</h2>
  <p>This site is curated and edited by <strong>Jellyfish</strong>, an independent games-content creator, with the goal of building the most useful English-language resource for Shift At Midnight players. We are a small independent project &mdash; not a content farm, and not affiliated with any publisher.</p>

  <h2>Our editorial standards</h2>
  <ol>
    <li><strong>Facts come from primary sources.</strong> Release dates, pricing, platforms and feature lists come from the official Steam store listing and the publisher's own material. Achievement names and global unlock percentages are read from public Steam global stats.</li>
    <li><strong>Inference is labelled as inference.</strong> Where we reason from evidence rather than quote a source &mdash; for example, what the rarity ordering of the hidden achievements suggests &mdash; we say so in the text. You should always be able to tell which is which.</li>
    <li><strong>No fabrication.</strong> Where a mechanic has no reliable source, we say so instead of inventing one. There is no credible night-by-night monster schedule for this game &mdash; shifts are procedurally generated &mdash; so we do not publish one, and we say why. The same goes for the Rake&rsquo;s health and spawn rate, per-weapon damage numbers, and regional pricing: absent from every source we trust, therefore absent here.</li>
    <li><strong>We correct in public.</strong> When we get something wrong, the fix is dated on the page rather than quietly swapped in. Our <a href="/endings/">endings page</a> carries a visible note about the unlock percentages it used to show.</li>
    <li><strong>Everything is dated.</strong> Each page carries a verification date. Achievement percentages drift as the player base grows; a number without a date is not useful.</li>
    <li><strong>Corrections are applied fast.</strong> If you spot an error, <a href="/contact/">contact us</a> &mdash; verified corrections are applied within 48 hours and the page is re-dated.</li>
  </ol>

  <div class="term tip">
    <div class="term-h">Why this matters for this game specifically</div>
    <p>Shift At Midnight launched with three hidden achievements that nobody has publicly solved. That creates a vacuum, and vacuums get filled with confident guesses that spread as fact. Following unverified guidance costs you runs. We would rather tell you we do not know.</p>
  </div>

  <h2>What this site is not</h2>
  <ul>
    <li>We are <strong>not affiliated with, endorsed by, or connected to</strong> Kwalee or Bun Muen.</li>
    <li>We do not host game files, distribute cracks or link to pirated copies.</li>
    <li>We do not accept payment for coverage, scores or placement in our guides.</li>
    <li>We do not publish Discord invite links &mdash; invites expire and get replaced. Verify community links from the publisher's own channels.</li>
  </ul>

  <h2>How this site is funded</h2>
  <p>Running costs are covered by advertising. Ads never affect what we write, which pages we build, or what verdict we reach &mdash; see <a href="/privacy/">how advertising and analytics operate here</a>.</p>

  <div class="grid two">
    <a class="card" href="/contact/"><b>Contact us</b><span>Corrections, findings and business enquiries.</span></a>
    <a class="card" href="/privacy/"><b>Privacy policy</b><span>What data is collected and by whom.</span></a>
  </div>
"""},
{
 "path": "contact", "active": "",
 "title": "Contact Us — Shift At Midnight Wiki",
 "og_short": "Contact Us",
 "desc": "Found an error, have a tip or a business enquiry about Shift At Midnight Wiki? Here is how to reach us, what helps, and what we cannot help with.",
 "trail": [(None, "Contact")],
 "h1": "Contact us",
 "lede": "Found an error? Have a tip, a question, or a business enquiry? We read everything &mdash; here is how to reach us and what to expect.",
 "body": """
  <h2>Email</h2>
  <p>Write to us at: <strong>zsn2740784715@gmail.com</strong></p>
  <p>We usually reply within <strong>48 hours</strong>.</p>

  <h2>What to contact us about</h2>
  <div class="tablewrap">
  <table class="data">
    <thead><tr><th>Topic</th><th>What helps us help you</th></tr></thead>
    <tbody>
      <tr><td><strong>Corrections</strong></td><td>Link the exact page and quote the passage you believe is wrong, ideally with an official source. Verified corrections are applied within 48 hours and the page is re-dated.</td></tr>
      <tr><td><strong>Hidden achievements</strong></td><td>The trigger conditions for <em>Grave Decision</em>, <em>True Ending</em> and <em>Empty Home</em> are now documented on our <a href="/endings/">endings page</a> &mdash; the Sheriff Clyde decision after Shift 12, plus whether you finish Shift 13 with at least $250 saved. What we still want are edge cases: runs where you met the stated condition and got a different ending. Tell us what you did and which achievement fired.</td></tr>
      <tr><td><strong>Guide requests</strong></td><td>Tell us what you searched for and could not find. Reader requests directly shape what we build next.</td></tr>
      <tr><td><strong>Tips &amp; discoveries</strong></td><td>Found a strategy, secret or interaction our guides miss? We would love to test and credit it.</td></tr>
      <tr><td><strong>Still-open questions</strong></td><td>Four things we would take good evidence on today: whether a <a href="/monsters/demented/">Demented</a> can ever be damaged by a weapon rather than a trap; the <a href="/monsters/">Rake</a>&rsquo;s health, damage and spawn rate; the full melee weapon list and prices behind <em>Locked And Loaded</em>; and the author of the <a href="/employee-package/#newsletter">Joe's Diner newsletter</a>.</td></tr>
      <tr><td><strong>Business &amp; press</strong></td><td>Partnership or advertising questions &mdash; please include your organisation and a link.</td></tr>
    </tbody>
  </table>
  </div>

  <h2>What we do not do</h2>
  <ul>
    <li>We cannot provide <strong>technical support for the game itself</strong>. For crashes, refunds or account issues, contact Kwalee or your storefront (Steam, Microsoft Store, Xbox). The developer's public contact is <strong>bun.muen.work@gmail.com</strong>.</li>
    <li>We do not accept payment for coverage, scores or placement in our guides.</li>
    <li>We cannot recover accounts, issue keys, or run giveaways. If a page claims to give away an <a href="/employee-package/">Employee Package</a> in exchange for your game login, it is not legitimate.</li>
  </ul>

  <h2>Rights holders</h2>
  <p>This is an unofficial fan resource. If you represent Kwalee or Bun Muen and want something changed or removed, email the address above and we will respond promptly.</p>

  <div class="grid two">
    <a class="card" href="/about/"><b>About this site</b><span>Who we are and how we source.</span></a>
    <a class="card" href="/privacy/"><b>Privacy policy</b><span>What data is collected and by whom.</span></a>
  </div>
"""},
{
 "path": "privacy", "active": "",
 "title": "Privacy Policy — Shift At Midnight Wiki",
 "og_short": "Privacy Policy",
 "desc": "Plain-language privacy policy for Shift At Midnight Wiki: what data is collected, how Google AdSense advertising cookies are used, how to opt out, and who to contact.",
 "trail": [(None, "Privacy Policy")],
 "h1": "Privacy policy",
 "lede": "This page explains, in plain language, what data is collected when you visit shiftatmidnightwiki.site, which third-party services we use for analytics and advertising &mdash; Google AdSense included &mdash; what your choices are, and how to contact us.",
 "updated": "Effective 28 July 2026 &middot; Site operator contact: zsn2740784715@gmail.com",
 "body": """
  <h2>1. Who we are</h2>
  <p>shiftatmidnightwiki.site ("this site", "we") is an independent, fan-operated guide website about the video game Shift At Midnight. It is curated by an independent games-content creator &mdash; see <a href="/about/">About</a>. We do not require accounts, do not offer purchases, and do not knowingly collect personal information beyond what is described below.</p>

  <h2>2. Data we collect directly</h2>
  <ul>
    <li><strong>Nothing you must provide.</strong> The site has no registration, login, comment or newsletter forms.</li>
    <li><strong>Email.</strong> If you choose to email us, we receive your address and message content, used solely to reply. We do not add you to any list or share your address.</li>
    <li><strong>Server logs.</strong> Our hosting and CDN provider may process standard technical logs (IP address, user agent, requested URL, timestamp) to deliver the site securely.</li>
  </ul>

  <h2>3. Analytics</h2>
  <p>This site uses <strong>Google Analytics</strong> and <strong>Microsoft Clarity</strong> to understand which guides help players, in aggregate. These services set cookies or use similar technologies and record page URL, referring site, approximate region, device type and browser. We use it to decide what to write next &mdash; not to build a profile of you, and not to identify you personally. You can opt out of Google Analytics entirely with the <a href="https://tools.google.com/dlpage/gaoptout" rel="noopener" target="_blank">Google Analytics opt-out browser add-on</a>.</p>

  <h2>4. Advertising &mdash; Google AdSense</h2>
  <p>Advertising on this site is served by two third-party networks. <strong>Google AdSense</strong> (Google is a third-party vendor) and <strong>Adsterra</strong>, which serves the display banner near the foot of each guide page. Both they and their demand partners may set cookies or use similar identifiers to select, deliver and measure ads. Adsterra&rsquo;s handling of that data is covered by <a href="https://adsterra.com/privacy-policy/" rel="nofollow noopener" target="_blank">its own privacy policy</a>. Ad slots may sit empty while approval or ad fill is pending; everything below applies from the moment an ad is served. If we add any further advertising network, it will be named here before it goes live.</p>
  <ul>
    <li><strong>Google and its partners use advertising cookies.</strong> They are used to serve and measure ads based on your prior visits to this site and to other sites on the internet. Where personalised advertising requires your consent, these cookies are used for personalisation only after you have given that consent.</li>
    <li><strong>You can switch personalised advertising off</strong> in <a href="https://adssettings.google.com" rel="noopener" target="_blank">Google Ads Settings</a>. That stops the personalisation, not the ads.</li>
    <li><strong>What Google does with the data</strong> it collects when you use this site is set out in <a href="https://policies.google.com/technologies/partner-sites" rel="noopener" target="_blank">How Google uses information from sites or apps that use our services</a>.</li>
    <li><strong>Third-party advertising vendors other than Google may also serve ads here</strong> and set their own cookies or device identifiers. Many of them can be opted out of in one place at <a href="https://www.aboutads.info/choices" rel="noopener" target="_blank">aboutads.info/choices</a>.</li>
  </ul>
  <p>What those vendors collect is governed by <strong>their own privacy policies</strong>, not by this one. If we ever add an advertising network besides AdSense, it will be named on this page before it starts serving.</p>
  <p>Advertising never affects what we write, which pages we build, or what verdict we reach. Nothing on this site is gated behind allowing ads.</p>

  <h2>5. Cookies</h2>
  <p>We set no cookies of our own &mdash; there is no login, no saved preference and no first-party tracker. Every cookie you receive on this site is set by the third parties described in sections 3 and 4, which in practice means the <strong>Google advertising cookies</strong> covered above plus any analytics cookie. You can block or delete them in your browser at any time; no content here is withheld if you do.</p>

  <h2>6. External links</h2>
  <p>We link to Steam, the Microsoft Store and other sites. Once you follow a link you are on that site and subject to its privacy policy. We do not control what those sites collect.</p>

  <h2>7. Children</h2>
  <p>This site covers a horror game that Steam labels as containing "plenty of gore and blood". It is not directed at children, and we do not knowingly collect information from them.</p>

  <h2>8. Your choices</h2>
  <ul>
    <li>Block or clear third-party cookies in your browser settings.</li>
    <li>Enable tracking protection, or use an ad blocker.</li>
    <li>Use your device's advertising-identifier reset or opt-out controls.</li>
    <li>Email us with any privacy question &mdash; see <a href="/contact/">contact</a>.</li>
  </ul>

  <h2>9. Changes</h2>
  <p>If this policy changes, the effective date at the top of this page changes with it.</p>
"""},
]

if __name__ == "__main__":
    print("生成关键词补充页 + 法务页:")
    build(PAGES)

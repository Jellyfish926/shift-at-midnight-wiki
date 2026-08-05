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

  <p>Well, then badly, in that order. Steam concurrents peaked at <strong>12,556 players on 23 July</strong>, the day after release, and the game charted as high as <strong>#8 on Steam&rsquo;s top sellers</strong> (<a href="https://steamdb.info/app/3722330/charts/" target="_blank" rel="noopener">SteamDB</a>). It also could not reliably put those players into a lobby: enough people were unable to create or join games that the developer pushed a temporary opt-in beta branch the same evening as a stopgap, which only worked if everyone in a party switched to it together.</p>

  <p>The real fix went into the main build on 23 July, so that branch is obsolete. If you and a friend opted in at launch and never switched back, it is the first thing to check when you are both online but cannot see each other &mdash; the steps are on <a href="/updates/">updates</a>.</p>

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

  <p>Very few games make the <em>moral</em> decision the mechanical one. Here the frightening action is administrative: you decide whether to serve someone or kill them, on incomplete information, while a queue builds behind them. <strong>96.6% of players have killed a customer</strong> (<a href="https://steamcommunity.com/stats/3722330/achievements/" target="_blank" rel="noopener">Steam achievement stats</a>, checked 5 August 2026) &mdash; that is the design working as intended, not a community of monsters. Nothing on this list reproduces it, which is why every honest recommendation here shares one half of the game rather than replacing it.</p>

  <div class="grid two">
    <a class="card" href="/review/"><b>Is it worth it?</b><span>Price, the free demo, and what the review data says.</span></a>
    <a class="card" href="/guide/doppelgangers/"><b>The identification loop</b><span>The half none of these eight copy.</span></a>
  </div>
"""},

# demo steam 560 + how much content in demo 520 + why is it demo but you can play with others 10@难度6
{
 "path": "demo", "active": "/guides/",
 "title": "Shift At Midnight Demo — Is There One, and Is It Free?",
 "og_short": "Shift At Midnight Demo",
 "desc": "What the Shift At Midnight demo included, how much content it had, why it supported co-op, and whether you still need it now the full game is out.",
 "trail": [(None, "Demo")],
 "h1": "The Shift At Midnight demo",
 "lede": "The demo did its job &mdash; it is how most people first heard about this game. Now that the <a href=\"/release-date/\">full version is out</a>, the useful question is what the demo actually contained and whether it still matters.",
 "body": """
  <div class="term tip">
    <div class="term-h">If you are asking "is the game free"</div>
    <p>The full game is <strong>not</strong> free &mdash; it is $9.99. But it is <strong>included with Xbox Game Pass</strong> at no extra cost, console and PC. For a lot of people that is the practical answer to "can I play this without paying". See <a href="/review/#price">price</a>.</p>
  </div>

  <h2>Why the demo let you play with other people</h2>

  <p>This confused a lot of players: a demo that included online co-op. It makes sense once you see what the demo was for. Shift At Midnight's entire appeal is three people shouting at each other about whether the customer at the counter is human. A single-player demo would have shown you the mechanics and none of the reason people actually buy it.</p>

  <p>Including co-op meant the demo produced exactly the thing that sells a game like this &mdash; streamable, clippable moments of a group falling apart. That is a deliberate marketing decision, and it worked.</p>

  <h2>How much content was in it</h2>

  <p>The demo was a slice, not a chapter &mdash; enough shifts to teach the loop of serving customers, checking IDs and dealing with the first threats, without the full progression, the complete <a href="/monsters/">bestiary</a> or the ending structure.</p>

  <p><strong>We are not going to give you a precise shift count</strong>, because demo builds were revised over the run-up to launch and we cannot verify which version any given claim refers to. What is certain is that the full release contains substantially more: the complete Story Mode, all ten <a href="/achievements/">achievements</a>, the full monster roster including the <a href="/monsters/marionette/">Marionette</a> boss, and the ending structure the rarest achievements sit behind.</p>

  <h2>Is the demo still worth downloading?</h2>

  <p>Probably not, for two reasons. First, if you have Game Pass, the full game costs you nothing &mdash; there is no reason to play a reduced version. Second, at $9.99 the full game is priced close enough to an impulse purchase that the demo's job is mostly done.</p>

  <p>The exception is hardware: if you are unsure whether your machine runs it, a demo is a better test than a refund request.</p>

  <div class="grid two">
    <a class="card" href="/review/#price"><b>Price</b><span>$9.99, or free on Game Pass.</span></a>
    <a class="card" href="/guide/beginners/"><b>Beginner's guide</b><span>Everything the demo taught, plus what it did not.</span></a>
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

  <p>Story Mode runs a sequence of shifts to a conclusion, with multiple possible outcomes &mdash; the three hidden achievements (<em>Grave Decision</em> 31.4%, <em>True Ending</em> 15.4%, <em>Empty Home</em> 9.4%) sit at the end of it. See <a href="/endings/">endings</a> for what those do and do not tell us.</p>

  <p>Endless Mode, announced as a free Q4 2026 update, is the mode for people who want shifts without an ending.</p>

  <div class="grid two">
    <a class="card" href="/nights-and-levels/#story-mode"><b>Story Mode</b><span>The structure in full.</span></a>
    <a class="card" href="/endings/"><b>Endings</b><span>What the run is building toward.</span></a>
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
  <p>Advertising on this site is served by <strong>Google AdSense</strong>. Google is a third-party vendor, and AdSense is currently the only advertising network used on this site. Ad slots may sit empty while approval or ad fill is pending; everything below applies from the moment an ad is served.</p>
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

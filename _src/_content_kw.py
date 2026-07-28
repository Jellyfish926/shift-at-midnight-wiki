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
 "desc": "Shift At Midnight released 22 July 2026 after two delays from the original 28 May date. Platforms, price, Game Pass and what the delay actually changed.",
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
    <tr><th>Price</th><td>$9.99 USD (10% introductory discount at launch)</td></tr>
    <tr><th>Developer</th><td>Bun Muen (solo)</td></tr>
    <tr><th>Publisher</th><td>Kwalee</td></tr>
    <tr><th>Next update</th><td>Endless Mode &mdash; free, Q4 2026</td></tr>
  </table>

  <h2>Why so many pages still say May</h2>

  <p>Shift At Midnight was originally announced for <strong>28 May 2026</strong>. That date was pushed back, and then pushed back again, landing on 22 July 2026. A lot of coverage was written against the earlier dates and never updated, which is why searching for the release date still turns up contradictory answers months later.</p>

  <p>If you are reading a page that says the game is "coming soon" or gives a May date, it predates the final schedule. The game shipped on 22 July 2026 and has been out since.</p>

  <h2>Was the delay a bad sign?</h2>

  <p>Not obviously. This is a solo developer's commercial release published by Kwalee, launching simultaneously on Steam, Xbox Series X|S and Game Pass. Day-one Game Pass placement involves certification on Microsoft's side, and Xbox Play Anywhere adds another layer. Hitting three storefronts at once with one developer is a genuine scheduling problem, and slipping twice to get it right is a reasonable outcome rather than a red flag.</p>

  <p>The launch build shipped with ten achievements, a full Story Mode and three-player online co-op, with Endless Mode already announced as a free Q4 2026 update. That is a complete release, not a rushed one.</p>

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

  <h2>What is not coming</h2>

  <p>No PlayStation 5, Nintendo Switch, mobile or VR version has been announced. The game is PC and Xbox only. Full detail on <a href="/platforms/">the platforms page</a>, including the app store and PS5 questions specifically.</p>

  <div class="grid two">
    <a class="card" href="/platforms/"><b>All platforms</b><span>PS5, mobile, Switch &mdash; the honest answers.</span></a>
    <a class="card" href="/price/"><b>Price</b><span>$9.99, and whether Game Pass makes that moot.</span></a>
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

  <p>The theming is consistent with the game: you play a night-shift employee at a roadside gas station, so the prize is dressed as employee kit &mdash; a badge, a cap from <a href="/joes-diner-newsletter/">Joe's Diner</a>, and 1990s-era peripherals matching the game's retro presentation.</p>

  <h2>Can you still get one?</h2>

  <p>The Employee Package was distributed through a Gleam giveaway run by Kwalee. Giveaways of this kind run for a fixed window and then close. <strong>We are not going to tell you it is still open, because we cannot verify that it is</strong> &mdash; and pages that keep stale giveaway links live are how people end up entering competitions that ended months ago.</p>

  <p>If you want to know whether anything similar is running now, the reliable sources are Kwalee's own channels and the game's Steam news feed. Not a wiki.</p>

  <div class="term warn">
    <div class="term-h">Careful with "Employee Package" links</div>
    <p>Merch giveaways for horror games attract fake entry pages that harvest logins. If a page asks you to sign in with your Steam or Microsoft account to "claim" a physical prize, close it. A legitimate giveaway does not need your game account credentials. Verify any campaign from the publisher's own channels first.</p>
  </div>

  <h2>Is there any paid merch or special edition?</h2>

  <p>No paid special edition, deluxe edition or season pass has been announced. Shift At Midnight is a single $9.99 release, and the only announced future content is <a href="/guide/endless-mode/">Endless Mode</a>, which is free and due in Q4 2026.</p>

  <div class="grid two">
    <a class="card" href="/price/"><b>Price &amp; editions</b><span>One edition, $9.99, no paid DLC.</span></a>
    <a class="card" href="/joes-diner-newsletter/"><b>Joe's Diner</b><span>The in-game diner the cap references.</span></a>
  </div>
"""},

# like games 840 + are there any games similiar
{
 "path": "similar-games", "active": "/guides/",
 "title": "Games Like Shift At Midnight — 7 Co-op Horror Picks",
 "og_short": "Games Like Shift At Midnight",
 "desc": "If you liked Shift At Midnight: co-op horror and suspicious-customer games worth playing next, and what each one actually shares with it.",
 "trail": [(None, "Similar games")],
 "h1": "Games like Shift At Midnight",
 "lede": "Shift At Midnight sits at the crossing point of two things: <strong>three-player co-op horror</strong> and <strong>deciding whether the person in front of you is lying</strong>. Most recommendations only give you one of those. Here is what shares which half.",
 "body": """
  <h2>If you came for the co-op panic</h2>

  <h3>Lethal Company</h3>
  <p>The obvious comparison and a fair one. Small team, proximity voice, a job to do while something hunts you, and the comedy that comes from people shouting over each other. Shift At Midnight is more structured &mdash; you have a counter, a quota and an ID scanner rather than an open scavenging loop &mdash; but the social texture is the same.</p>

  <h3>Phasmophobia</h3>
  <p>Shares the "investigate carefully, then panic" rhythm and the use of tools to identify something you cannot simply fight. If the part of Shift At Midnight you enjoyed was building a case from evidence, this is the closer match.</p>

  <h3>Content Warning</h3>
  <p>Same three-friends-in-a-dark-place energy, much sillier. Good if you liked the chaos and not the paperwork.</p>

  <h2>If you came for the "is this person lying" part</h2>

  <h3>Papers, Please</h3>
  <p>The clearest ancestor of Shift At Midnight's actual core loop. A booth, a document, a queue building behind the person in front of you, and a decision with consequences. No monsters &mdash; the horror is bureaucratic. If the counter work was your favourite part, play this.</p>

  <h3>Not For Broadcast / The Bureau-style document games</h3>
  <p>Same family: scrutinise material under time pressure, make a call, live with it.</p>

  <h2>If you came for the retro night-shift horror</h2>

  <h3>Five Nights at Freddy's</h3>
  <p>The night-shift-at-a-cursed-workplace template that Shift At Midnight is clearly aware of. Much more static, but the DNA is visible &mdash; you are an underpaid employee, the building is against you, and the shift has to end before you can leave.</p>

  <h3>Buckshot Roulette</h3>
  <p>Different genre entirely, but similar in one specific way: a tight, cheap, well-made horror premise from a small developer that does one idea properly.</p>

  <div class="term tip">
    <div class="term-h">What actually makes Shift At Midnight distinct</div>
    <p>Very few games make the <em>moral</em> decision the mechanical one. Here, the scary action is administrative: you decide whether to serve someone or kill them, with incomplete information, while a queue builds. The fact that 96.6% of players have <a href="/achievements/">killed a customer</a> is the design working as intended. That specific tension is hard to find elsewhere.</p>
  </div>

  <div class="grid two">
    <a class="card" href="/review/"><b>Is it worth it?</b><span>What the completion data suggests.</span></a>
    <a class="card" href="/guide/doppelgangers/"><b>The identification loop</b><span>The part Papers, Please fans will recognise.</span></a>
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
    <p>The full game is <strong>not</strong> free &mdash; it is $9.99. But it is <strong>included with Xbox Game Pass</strong> at no extra cost, console and PC. For a lot of people that is the practical answer to "can I play this without paying". See <a href="/price/">price</a>.</p>
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
    <a class="card" href="/price/"><b>Price</b><span>$9.99, or free on Game Pass.</span></a>
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

  <p>Story Mode runs a sequence of shifts to a conclusion, with multiple possible outcomes &mdash; the three hidden achievements (<em>Grave Decision</em> 26.0%, <em>True Ending</em> 13.4%, <em>Empty Home</em> 7.0%) sit at the end of it. See <a href="/endings/">endings</a> for what those do and do not tell us.</p>

  <p>Endless Mode, announced as a free Q4 2026 update, is the mode for people who want shifts without an ending.</p>

  <div class="grid two">
    <a class="card" href="/guide/story-mode/"><b>Story Mode</b><span>The structure in full.</span></a>
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
    <li><strong>No fabrication.</strong> Three of this game's achievements have hidden descriptions and no published trigger. Rather than write a confident-sounding guess, our <a href="/endings/">endings page</a> says plainly that it is unconfirmed.</li>
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
      <tr><td><strong>Hidden achievements</strong></td><td>The big one. For <em>Grave Decision</em>, <em>True Ending</em> or <em>Empty Home</em>: tell us what you did across the run and which achievement fired. One run proves nothing; several logged runs from different players is how these get solved.</td></tr>
      <tr><td><strong>Guide requests</strong></td><td>Tell us what you searched for and could not find. Reader requests directly shape what we build next.</td></tr>
      <tr><td><strong>Tips &amp; discoveries</strong></td><td>Found a strategy, secret or interaction our guides miss? We would love to test and credit it.</td></tr>
      <tr><td><strong>Still-open questions</strong></td><td>The <a href="/joes-diner-newsletter/">Joe's Diner newsletter</a> author, exact demo content, and per-weapon performance data are all unresolved on this site.</td></tr>
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
 "desc": "Plain-language privacy policy for Shift At Midnight Wiki: what data is collected, which third parties are involved in analytics and advertising, and your choices.",
 "trail": [(None, "Privacy Policy")],
 "h1": "Privacy policy",
 "lede": "This page explains, in plain language, what data is collected when you visit shiftatmidnightwiki.site, which third-party services we use for analytics and advertising, what your choices are, and how to contact us.",
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
  <p>We may use analytics to understand which guides help players, in aggregate. These services set cookies or use similar technologies and record page URL, referring site, approximate region, device type and browser. It is used to decide what to write next &mdash; not to build a profile of you, and not to identify you personally.</p>

  <h2>4. Advertising</h2>
  <p>This site may display advertising supplied by third-party advertising partners. Those partners may use cookies, device identifiers or similar technologies to serve and measure ads. Their collection is governed by <strong>their own privacy policies</strong>, not by this one.</p>
  <p>Advertising never affects what we write, which pages we build, or what verdict we reach. Nothing on this site is gated behind allowing ads.</p>

  <h2>5. Cookies</h2>
  <p>We do not set cookies for our own purposes. Any cookies you receive here come from the third parties described in sections 3 and 4.</p>

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

#!/usr/bin/env python3
"""2026-09-10 新增页正文 —— 五个缺口页。

/controls/   控制方式与手柄支持(Steam 商店 JSON 全部 controller 标志为 false)
/languages/  九种语言,Steam 与 Xbox 两处独立佐证
/credits/    开发者 / 作曲 / 发行,itch.io 原型溯源
/cheats/     无官方控制台;第三方修改器只陈述存在,不背书
/monsters/rake/  Endless 专属威胁 —— 补上 /monsters/ 自己点名「还没有独立页」的那一个

事实无可靠出处的一律不写数字(生命值/伤害/刷新率),与本仓既有红线一致。
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))

M = [("/monsters/", "Monsters")]

PAGES = [
{
 "path": "controls",
 "active": "/guides/",
 "title": "Shift At Midnight Controls: No Controller Support on PC",
 "og_short": "Controls &amp; controller support",
 "desc": "Shift At Midnight has zero controller support on Steam — keyboard and mouse only, confirmed by Valve's own store data. What is and isn't verified.",
 "trail": [(None, "Controls")],
 "h1": "Shift At Midnight controls",
 "lede": "On PC &mdash; Steam or the Microsoft Store &mdash; <strong>Shift At Midnight has no controller support at all.</strong> Not partial, not community-only: the developer's own Steam listing declares every controller category false. If you bought it on PC, you are playing with a keyboard and mouse whether or not you own a gamepad. The Xbox Series X|S version is the opposite case &mdash; that build is controller-only by definition.",
 "updated": "Last verified 10 September 2026 &middot; game version: 29 July 2026 patch",
 "body": """
  <div class="tags">
    <span class="tag red">PC: no controller support</span>
    <span class="tag amber">Xbox: controller native</span>
    <span class="tag">Keyboard &amp; mouse required on Steam</span>
    <span class="tag red">Steam Input: not declared</span>
  </div>

  <div class="term warn">
    <div class="term-h">The direct answer</div>
    <p>Shift At Midnight's Steam store listing carries a controller-support data block, and every field in it reads <strong>false</strong>: full Xbox controller support, partial Xbox controller support, PS4, PS4 Bluetooth, PS5, PS5 Bluetooth, and Steam Input API support. The developer has completed Valve's controller-support declaration &mdash; this is not a blank field waiting to be filled in, it is an explicit "no" across the board. On PC, that means keyboard and mouse only.</p>
  </div>

  <h2>Why this feels wrong for an Xbox game</h2>
  <p>Shift At Midnight launched day one on Xbox Game Pass and is an <a href="/platforms/">Xbox Play Anywhere title</a>, which makes the lack of PC controller support genuinely counterintuitive. Xbox Play Anywhere links one purchase across Xbox Series X|S and Windows, and the natural assumption is that a game built for a console controller carries that support into its PC build. It does not. The Xbox Series X|S version is a native controller experience; the Windows build shares the save data and the Play Anywhere entitlement, but not the input method.</p>
  <p>This is also why the question keeps coming up in the game's own <a href="https://steamcommunity.com/app/3722330/discussions/0/591784051117068817/" target="_blank" rel="noopener">Steam discussions</a>, where a thread titled "Is controller support planned?" sits alongside a separate "Please add gamepad support!" post. Neither has a developer reply confirming a change, so treat controller support as absent until Kwalee or Bun Muen says otherwise &mdash; not as something quietly being worked on.</p>

  <h2>What actually works: keyboard and mouse</h2>
  <p>The verified interaction model is mouse-driven. Serving a customer means reading an ID at a terminal, cross-checking details in the N.E.T. database, and making a judgement call &mdash; all screen-and-cursor tasks that do not map cleanly onto a gamepad's face buttons and sticks, which is the most plausible reason a solo developer skipped controller support rather than shipping a broken one.</p>
  <p>One binding is confirmed from in-game material this wiki has already verified: interacting with the wind-up music box that triggers the <a href="/monsters/marionette/">Marionette</a> encounter is done by holding <strong>E</strong> to rewind it &mdash; see the <a href="/monsters/jack-in-the-box/">Jack-in-the-Box page</a>. Beyond that specific, confirmed key, we have not found an official, complete keybind list published by the developer, and we are not going to invent one. Standard first-person conventions (WASD movement, mouse-look, mouse-click to interact) are a safe general assumption for a game in this genre, but treat anything more specific than the E-to-rewind binding as unconfirmed until we can source it.</p>

  <div class="term tip">
    <div class="term-h">If you were hoping to remap keys</div>
    <p>We found no evidence of an in-game key-rebinding menu in any source we checked, official or otherwise. If remapping matters to you, the safer route on PC is a system-level or Steam-level remap (Steam's own controller/keyboard configurator, or Windows key-remapping software) rather than assuming the game exposes one itself. We have not tested this ourselves, so we're not calling it confirmed either way &mdash; just the more realistic option.</p>
  </div>

  <div class="term warn">
    <div class="term-h">A conflicting note elsewhere on this wiki</div>
    <p>This wiki's own <a href="/system-requirements/">system requirements page</a> separately notes that SteamDB's app-info panel records a generic &ldquo;Gamepad supported&rdquo; flag for this game, distinct from the field-by-field controller-support breakdown described above, and says outright that no official note on which inputs are mapped could be found. We have not been able to reconcile that flag with the all-false declaration this page is built on, so treat the SteamDB tag as an open question rather than something this page resolves.</p>
  </div>

  <h2>Steam Deck and controller-only handhelds</h2>
  <p>Because the PC build has no declared controller support, a Steam Deck run inherits that gap directly. The <a href="/system-requirements/">system requirements page</a> covers the Deck compatibility rating in detail, but the short version connects straight back to this page: Valve's own Deck compatibility notes for this game flag that the default controller configuration is not fully functional and that some interactions need the touchscreen or a community control layout &mdash; which lines up exactly with a game that was never built for a gamepad in the first place.</p>

  <h2>Can you force a controller to work anyway?</h2>
  <p>People do get gamepads working on PC shooters with no native support through Steam's generic gamepad-to-keyboard/mouse translation (via a Steam Input desktop configuration) or third-party tools like a community controller layout. We have not verified a working configuration for Shift At Midnight specifically, and the game's own <code>bSteamInputAPISupport: false</code> flag means the developer has not built in any awareness of Steam Input &mdash; a workaround, if one exists, is entirely a community effort layered on top, not something the game recognises. If you find one that works reliably, the most useful place to report it is the game's own Steam discussions, not a third-party trainer site.</p>

  <h2>What the most recent patch changed</h2>
  <p><strong>Unconfirmed:</strong> we have not been able to source patch content newer than the <a href="/updates/">29 July 2026 update</a> against this wiki's own patch-notes page, which was still listing that as the newest public announcement as of its last check. If a later update has shipped, we have not verified its contents well enough to describe new key bindings here, so we are not guessing at one. If this is the first page of the wiki you've landed on, the <a href="/start-here/">reading order guide</a> sequences everything else from here.</p>

  <h2>Quick answers</h2>
  <div class="faq">
    <details>
      <summary>Does Shift At Midnight have full controller support?</summary>
      <div class="a"><p>No, not on PC. The Steam listing declares no Xbox, PlayStation, or generic Steam Input controller support. The Xbox Series X|S version is controller-only by definition, but that is a separate build from the PC version.</p></div>
    </details>
    <details>
      <summary>Can I use a controller on the Steam version?</summary>
      <div class="a"><p>Not officially. Nothing in the game recognises a gamepad on its own. Community workarounds using Steam's generic input translation may exist, but we have not verified one, and the developer has not declared any Steam Input support.</p></div>
    </details>
    <details>
      <summary>Is it playable on Steam Deck without a controller working properly?</summary>
      <div class="a"><p>Valve rates it Playable, not Verified, and the flagged issue is exactly this &mdash; the default controller configuration is not fully functional, so some screens need the touchscreen or a community layout. Full detail on <a href="/system-requirements/">system requirements</a>.</p></div>
    </details>
  </div>

  <div class="grid two">
    <a class="card" href="/system-requirements/"><b>System requirements &amp; Steam Deck</b><span>The Playable rating, and exactly which checks it failed.</span></a>
    <a class="card" href="/platforms/"><b>Platforms</b><span>Where the Xbox controller build actually lives.</span></a>
    <a class="card" href="/monsters/jack-in-the-box/"><b>Jack-in-the-Box</b><span>The one confirmed keybind in the game &mdash; hold E to rewind.</span></a>
    <a class="card" href="/multiplayer/"><b>Multiplayer &amp; co-op</b><span>Proximity chat and lobby size, for when input method stops being the only variable.</span></a>
  </div>
""",
},
{
 "path": "languages",
 "active": "/guides/",
 "title": "Shift At Midnight Languages: All 9 Supported",
 "og_short": "Language support",
 "desc": "Shift At Midnight supports 9 languages on both Steam and Xbox. Whether audio is fully localized or interface/subtitles only is disputed between this wiki's own pages, and unresolved.",
 "trail": [(None, "Languages")],
 "h1": "Shift At Midnight language support",
 "lede": "Shift At Midnight ships in <strong>9 languages</strong>, confirmed identically on both the Steam store page and the Xbox listing, which both list \"9 supported languages\" independently. Whether that support extends to full voice audio in every language, or is interface-and-subtitles only, is <strong>unconfirmed</strong> &mdash; see below.",
 "updated": "Last verified 10 September 2026 &middot; game version: 29 July 2026 patch",
 "body": """
  <div class="tags">
    <span class="tag green">9 languages, confirmed on Steam and Xbox</span>
    <span class="tag amber">Full audio vs. subtitles-only: disputed</span>
    <span class="tag amber">Mature 17+ rating (Xbox)</span>
  </div>

  <h2>The full list</h2>
  <p>All nine languages below are confirmed as supported. What level of support each one gets &mdash; interface only, interface plus subtitles, or full voice audio &mdash; is the disputed part; see the note beneath the table before assuming every row has audio.</p>

  <table class="facts">
    <tr><th>English</th><td>Interface, subtitles &mdash; audio: unconfirmed</td></tr>
    <tr><th>French</th><td>Interface, subtitles &mdash; audio: unconfirmed</td></tr>
    <tr><th>German</th><td>Interface, subtitles &mdash; audio: unconfirmed</td></tr>
    <tr><th>Spanish (Spain)</th><td>Interface, subtitles &mdash; audio: unconfirmed</td></tr>
    <tr><th>Japanese</th><td>Interface, subtitles &mdash; audio: unconfirmed</td></tr>
    <tr><th>Russian</th><td>Interface, subtitles &mdash; audio: unconfirmed</td></tr>
    <tr><th>Simplified Chinese</th><td>Interface, subtitles &mdash; audio: unconfirmed</td></tr>
    <tr><th>Traditional Chinese</th><td>Interface, subtitles &mdash; audio: unconfirmed</td></tr>
    <tr><th>Portuguese (Brazil)</th><td>Interface, subtitles &mdash; audio: unconfirmed</td></tr>
  </table>

  <p class="src">Source for the count and rows: the <a href="https://store.steampowered.com/app/3722330/Shift_At_Midnight/" target="_blank" rel="noopener">official Steam store listing</a>. The count is independently corroborated by the <a href="https://www.xbox.com/en-US/games/store/shift-at-midnight/9n0wdpmxnhwn" target="_blank" rel="noopener">Xbox store listing</a>, which also states "9 Supported languages" without listing them individually on the visible page.</p>

  <div class="term warn">
    <div class="term-h">An unresolved conflict on this wiki</div>
    <p>This page cannot tell you with confidence whether every language has full voice audio. This wiki's own <a href="/release-date/">release date page</a> lists these same nine languages as &ldquo;interface and subtitles&rdquo; &mdash; no audio claim at all &mdash; while a separate reading of the Steam API used elsewhere on this site suggested full audio for all nine. The two have not been reconciled, and this page is not going to pick one over the other. <strong>Treat any specific claim about voice audio in a given language as unconfirmed</strong> until this is sorted out.</p>
  </div>

  <h2>What this means if you're playing in a language other than English</h2>
  <p>Because the core loop is <a href="/guide/doppelgangers/">reading a customer's ID, cross-checking the N.E.T. database, and judging their behaviour</a>, audio and text localization would matter more here than in a lot of genres if the audio claim holds &mdash; a doppelganger's tell can be something said, not just something shown. Since patience-meter pressure was removed in the <a href="/updates/">29 July 2026 patch</a>, there is less time cost either way regardless of which localization level you actually have.</p>

  <h2>Content rating, and why it comes up in the same searches</h2>
  <p>The Xbox store listing carries a <strong>Mature 17+</strong> rating with the descriptors "Violence, Blood and Gore" and "Language" &mdash; separate from the language-localization question above, but people frequently search for language support and content rating together when deciding whether a game is appropriate for a household. Steam's own content description is looser but consistent: the developers describe the game as containing "plenty of gore and blood," which lines up with the Xbox descriptor rather than contradicting it.</p>

  <div class="term tip">
    <div class="term-h">Language support and crossplay are unrelated</div>
    <p>Playing in a different language does not affect who you can play with. The barrier for multiplayer is the storefront, not the localization &mdash; Steam and Xbox/PC Game Pass players are split for reasons covered on the <a href="/crossplay/">crossplay page</a>, and that split exists regardless of which of the nine languages either player has selected.</p>
  </div>

  <h2>How to change the language</h2>
  <p>We have not found an official step-by-step from Kwalee for switching the in-game language, so treat the following as the standard approach for this kind of Steam release rather than a confirmed, game-specific procedure. On Steam, language usually follows your Steam client's interface language by default, with an in-game settings menu to override it if the game exposes one; on Xbox, it typically follows your console or Microsoft account's display language. If the game does not expose its own language selector in the options menu, the Steam client language is the first thing to check &mdash; right-click the game in your library, open Properties, and look for a Language dropdown before assuming the game is missing support it actually has.</p>
  <p><strong>Unconfirmed:</strong> whether Shift At Midnight has its own in-game language override independent of the platform setting. If you have verified this either way, <a href="/contact/">let us know</a> and we will update this section with the confirmed steps.</p>

  <h2>Languages not on the list</h2>
  <p>Nine covers a lot of the largest PC and Xbox markets, but it leaves out several common requests: Italian, Korean, Polish, and Thai are not on either store listing as of this check. There is no announced plan to add more languages that we have found &mdash; if one is announced, it will show up as a new row on the official store listings before it shows up anywhere else, this page included.</p>

  <h2>Quick answers</h2>
  <div class="faq">
    <details>
      <summary>Is Shift At Midnight available in my language?</summary>
      <div class="a"><p>Check the table above. If your language is not one of the nine listed, it is not currently supported on either Steam or Xbox, and the interface will default to whichever supported language is closest to your system settings (typically English).</p></div>
    </details>
    <details>
      <summary>Does it have voice acting in every language, or just subtitles?</summary>
      <div class="a"><p><strong>Unconfirmed.</strong> Sources checked across this wiki disagree &mdash; one reading of the Steam listing suggests full audio for all nine, another page on this site lists interface and subtitles only. We have not resolved which is correct.</p></div>
    </details>
    <details>
      <summary>Is Simplified and Traditional Chinese both supported?</summary>
      <div class="a"><p>Yes, both are listed separately on the Steam store page, each with interface and subtitle support. See the note above on the unresolved audio question.</p></div>
    </details>
  </div>

  <div class="grid two">
    <a class="card" href="/platforms/"><b>Platforms</b><span>Where the game is available, separate from what language it's in.</span></a>
    <a class="card" href="/crossplay/"><b>Crossplay</b><span>The actual barrier between players &mdash; storefront, not language.</span></a>
  </div>
""",
},
{
 "path": "credits",
 "active": "/guides/",
 "title": "Who Made Shift At Midnight — Developer, Composer &amp; Credits",
 "og_short": "Who made Shift At Midnight",
 "desc": "Shift At Midnight was built by solo developer Bun Muen, scored by Ryan Q, and published by Kwalee. How a free itch.io prototype became a Steam and Xbox release.",
 "trail": [(None, "Credits")],
 "h1": "Who made Shift At Midnight",
 "lede": "Shift At Midnight is built by a single developer, <strong>Bun Muen</strong>, with music by <strong>Ryan Q</strong>, and published by <strong>Kwalee</strong>. The Steam and Xbox release did not start there &mdash; it started as a free single-player demo on itch.io, and the credits trail across both versions is worth untangling because a lot of the game's design choices only make sense once you know that history.",
 "updated": "Last verified 10 September 2026 &middot; game version: 29 July 2026 patch",
 "body": """
  <div class="tags">
    <span class="tag">Developer: Bun Muen (solo)</span>
    <span class="tag">Publisher: Kwalee</span>
    <span class="tag">Composer: Ryan Q</span>
    <span class="tag">Origin: free itch.io demo</span>
  </div>

  <h2>The short answer</h2>
  <table class="facts">
    <tr><th>Developer</th><td>Bun Muen &mdash; solo developer</td></tr>
    <tr><th>Publisher</th><td>Kwalee</td></tr>
    <tr><th>Music</th><td>Ryan Q</td></tr>
    <tr><th>Original prototype</th><td>Free demo on itch.io, singleplayer, before the Steam co-op version existed</td></tr>
    <tr><th>Steam / Xbox release</th><td>22 July 2026</td></tr>
    <tr><th>AI content</th><td>The itch.io listing states "No generative AI was used"</td></tr>
  </table>

  <h2>One developer, not a studio</h2>
  <p>Bun Muen made Shift At Midnight alone, which this wiki's own <a href="/about/">about page</a> already notes in passing &mdash; it is a solo project that Kwalee picked up to publish, not a Kwalee-built game with Kwalee's name attached from the start. That distinction matters for expectations: the pace of content updates, the size of the credits list, and the studio's public communication style (a single dev account posting patch notes directly) all trace back to it being one person's project rather than a team's.</p>
  <p>Kwalee's role is publishing &mdash; distribution, storefront presence, and presumably marketing support &mdash; rather than development. The <a href="https://store.steampowered.com/eula/3722330_eula_0" target="_blank" rel="noopener">game's EULA</a> is issued under Kwalee's name as publisher, which is standard for this kind of publisher/developer split.</p>

  <h2>The composer: Ryan Q</h2>
  <p>The game's music is credited to <strong>Ryan Q</strong>, listed on the original itch.io project page with a direct contact (an Instagram handle, <a href="https://www.instagram.com/ryanqkfcman/" target="_blank" rel="noopener">@ryanqkfcman</a>) for anyone looking to reach the composer directly. This is not information repeated anywhere else on this wiki, and it does not appear on the Steam store page itself &mdash; the credit only surfaces on the original itch.io listing, which is one more reason this page exists separately from the <a href="/about/">about page</a>.</p>
  <p>We have not found a released soundtrack, a dedicated composer statement about the score, or interviews discussing the music specifically. If one surfaces, this page is where it will get added, dated.</p>

  <h2>It started as a free single-player demo</h2>
  <p>Before Shift At Midnight was a $9.99 Steam and Xbox release, it existed as a free, downloadable prototype on itch.io &mdash; singleplayer only, and by the developer's own description on that page, without the randomly-generated shifts the full release has. The itch.io page still exists and carries the game's original development log, including the point where it was <a href="https://bunmuen.itch.io/shiftatmidnight" target="_blank" rel="noopener">upgraded into a multiplayer co-op Steam demo</a>, ahead of the eventual full release.</p>
  <p>That page also states that the step from the original singleplayer prototype to the multiplayer Steam demo expanded the game from one night to three. <strong>Unconfirmed:</strong> we have not found a source describing which specific content carried over unchanged versus what was rebuilt for the multiplayer version, so we are not going to guess at a night-by-night breakdown. Neither demo used the shift-to-shift procedural generation that the full release relies on &mdash; that came later, in the Steam release proper. See <a href="/demo/">the demo page</a> for what is playable today versus what these earlier builds were.</p>

  <div class="term tip">
    <div class="term-h">Why the itch.io rating (4.7 stars, 360 ratings) isn't the Steam review score</div>
    <p>The itch.io page carries its own rating, separate from Steam's review percentages covered on <a href="/review/">the review page</a>. They measure different audiences at different points in the game's life &mdash; the itch.io number reflects reactions to the free prototype, not the paid release. Don't conflate the two when someone quotes a rating at you without saying which storefront it's from.</p>
  </div>

  <h2>The "no generative AI" statement</h2>
  <p>The itch.io listing carries a content disclosure reading "No generative AI was used." Steam's own listing does not repeat this specific wording, but nothing on the Steam page contradicts it either. We are noting it here because it is a real, sourced statement from the developer's own storefront page, and questions about AI use in indie horror games come up often enough that a direct, dated answer is more useful than silence.</p>

  <h2>Official channels, if you want to follow development directly</h2>
  <p>The developer's own itch.io page lists Discord as the place to find other players and follow updates, alongside the official <a href="https://x.com/BunMuenGames" target="_blank" rel="noopener">@BunMuenGames</a> account this wiki already links from every page footer. For business or press contact, the itch.io listing lists a direct developer email rather than routing through Kwalee &mdash; consistent with Bun Muen retaining an independent public presence even after signing with a publisher.</p>

  <h2>The gap between the itch.io page and the Steam page</h2>
  <p>It's worth being explicit about why these two credits sources don't fully overlap. Steam's store page lists Bun Muen as developer and Kwalee as publisher, and stops there &mdash; it is not a full credits roll. The itch.io page, being the developer's own original project page rather than a storefront listing, carries the composer credit, the demo history, and the AI-use statement that Steam's listing simply doesn't have a field for. Neither page is wrong; they're built for different purposes, and a full picture needs both.</p>

  <h2>Where this fits with the rest of the wiki</h2>
  <p>This page exists to answer "who made this" on its own, rather than making readers dig it out of the <a href="/about/">about page</a> (which covers this site's own editorial policy, not the game's credits) or the <a href="/similar-games/">similar games page</a> (which is about what to play next, not who built this one). If you came here chasing the composer credit or the itch.io history specifically, this is the page; everything else about the game itself &mdash; release date, platforms, price &mdash; is covered on <a href="/release-date/">the release date page</a>.</p>

  <div class="grid two">
    <a class="card" href="/demo/"><b>Demo</b><span>What's playable for free today, and how it differs from the original itch.io prototype.</span></a>
    <a class="card" href="/about/"><b>About this wiki</b><span>Our own editorial standards &mdash; a different thing from the game's own credits.</span></a>
  </div>
""",
},
{
 "path": "cheats",
 "active": "/guides/",
 "title": "Shift At Midnight Cheats &amp; Console Commands: The Real Answer",
 "og_short": "Cheats &amp; console commands",
 "desc": "Shift At Midnight has no official console commands or cheat menu. What trainers actually offer, what the EULA says, and the risk in a co-op game.",
 "trail": [(None, "Cheats &amp; console commands")],
 "h1": "Shift At Midnight cheats and console commands",
 "lede": "<strong>There are no official console commands or developer cheat menu in Shift At Midnight.</strong> Nothing in the game's Steam feature list, its store page, or its patch notes mentions one. What exists instead is a small ecosystem of third-party trainers that inject values into a running process from outside the game &mdash; a different thing, with different risks, and this page is about telling the two apart.",
 "updated": "Last verified 10 September 2026 &middot; game version: 29 July 2026 patch",
 "body": """
  <div class="tags">
    <span class="tag red">No official commands</span>
    <span class="tag amber">Third-party trainers exist</span>
    <span class="tag">Online co-op game</span>
    <span class="tag red">EULA prohibits reverse engineering</span>
  </div>

  <div class="term warn">
    <div class="term-h">If you searched for a specific cheat code</div>
    <p>Pages listing "item IDs" or "spawn codes" for this game are describing a feature Shift At Midnight does not have. There is no publicly documented developer console, and nothing in the official Steam feature list (Single-player, Multi-player, Co-op, Online Co-op, Steam Achievements, Family Sharing &mdash; this wiki's own <a href="/system-requirements/">system requirements page</a> notes Steam Cloud is specifically absent from it) points to one existing. Treat any specific code you find on a random blog as unverified until you can trace it to the developer.</p>
  </div>

  <h2>What "no official commands" actually means</h2>
  <p>Some PC games ship a developer console left over from testing &mdash; a tilde-key menu that spawns items or toggles god mode. Shift At Midnight's public-facing feature set gives no indication of one, and neither Kwalee's store listing nor its update posts have ever referenced a debug or command console for players. That absence is itself the answer to "how do I open the console" &mdash; there almost certainly isn't one to open.</p>
  <p>This matters because a search for this game's name plus "cheats" turns up several sites presenting confident-looking lists of console commands and item codes. We are not going to link to those as sources, because we cannot verify a single entry against anything Kwalee has published, and a list that specific, for a feature the game does not advertise, is a strong signal of content generated to rank rather than tested against the real build.</p>

  <h2>What third-party trainers actually are</h2>
  <p>A trainer is separate software that attaches to the game's process while it runs and edits values in memory &mdash; money, for example &mdash; from outside the game itself. It is not a feature the developer built; it is a workaround built by someone else, and it works (when it works) regardless of whether the game has console commands.</p>
  <p>Searching for this game turns up trainer listings on sites like <a href="https://www.wemod.com/cheats/shift-at-midnight-trainers" target="_blank" rel="noopener">WeMod</a> and <a href="https://www.plitch.com/en/games/shift-at-midnight-502009159622070272" target="_blank" rel="noopener">PLITCH</a>, plus a memory cheat table on the Cheat Engine community site Fearless Revolution. Their existence confirms that people have built memory-editing tools for this game; it does not mean any specific one is safe, current, or does what its listing claims. We have not run any of them ourselves, and we are not recommending one.</p>

  <table class="facts">
    <tr><th>Official console commands</th><td>None found. Not part of the advertised feature set.</td></tr>
    <tr><th>Official cheat menu / debug mode</th><td>None found.</td></tr>
    <tr><th>Third-party trainers</th><td>Exist, from multiple providers &mdash; unverified by this site</td></tr>
    <tr><th>Item ID / spawn code lists</th><td>Circulating online, but not traceable to an official source</td></tr>
  </table>

  <h2>What Kwalee's own terms say</h2>
  <p>The <a href="https://store.steampowered.com/eula/3722330_eula_0" target="_blank" rel="noopener">Shift At Midnight EULA</a>, published by Kwalee, includes a standard clause (section 3.4) prohibiting you from decompiling, disassembling, reverse-engineering, or modifying the game. A memory-editing trainer works by reading and writing the game's runtime memory, which sits squarely in the territory that clause is written to cover &mdash; using one is against the terms you agree to when you install the game, even where it is not against any law.</p>
  <p>That is a different question from whether it will get you banned. Shift At Midnight has Steam Achievements but no announced anti-cheat system, and we have not found reports of account action taken specifically over trainer use. The absence of anti-cheat is not the same as permission &mdash; it just means enforcement, if any, is not automated.</p>

  <h2>Why this matters more in a co-op game</h2>
  <p>Shift At Midnight is built around <a href="/multiplayer/">online co-op for up to three players</a> (six since the 23 July 2026 patch), and the loop &mdash; serving customers, hitting a quota, surviving a hunt &mdash; is shared. A money or health edit that only benefits one player in a lobby changes the experience for everyone in it, not just the person running the trainer, in a way that single-player cheating does not. If you are set on trying one, doing it in single-player rather than a shared lobby is the version that only affects your own run.</p>

  <h2>The safety angle that matters most</h2>
  <p>This is the same caution this wiki gives on the <a href="/employee-package/">Employee Package giveaway page</a>: horror games with an active player base attract fake tools alongside real ones. A trainer that asks you to disable your antivirus, sign in with a game or platform account, or download through a shortened link is a bigger risk than anything in the EULA. Get a trainer, if you use one at all, from a source you already trust for other games &mdash; not from a page that exists only to rank for this specific search.</p>

  <h2>Quick answers</h2>
  <div class="faq">
    <details>
      <summary>Does Shift At Midnight have cheat codes?</summary>
      <div class="a"><p>No official ones. Nothing in the game's advertised feature set or patch history mentions a cheat menu or code entry system.</p></div>
    </details>
    <details>
      <summary>Is there a console command list?</summary>
      <div class="a"><p>Not an official one. Lists circulating online claiming to be item IDs or spawn codes are not traceable to Kwalee or Bun Muen, and we do not reproduce them.</p></div>
    </details>
    <details>
      <summary>Will using a trainer get me banned?</summary>
      <div class="a"><p>Unclear &mdash; the game has no announced anti-cheat system, but using one violates the EULA's anti-modification clause regardless of enforcement. See <a href="/faq/">the FAQ</a> for more on official policy questions we could not get a direct answer to.</p></div>
    </details>
  </div>

  <div class="grid two">
    <a class="card" href="/employee-package/"><b>Employee Package &amp; giveaway safety</b><span>The same phishing caution, applied to merch giveaways instead of trainers.</span></a>
    <a class="card" href="/multiplayer/"><b>Multiplayer &amp; co-op</b><span>Why a memory edit in a shared lobby is not the same as one in single-player.</span></a>
  </div>
""",
},
{
 "path": "monsters/rake",
 "title": "Shift At Midnight Rake — The Endless Mode Forest Threat",
 "og_short": "Shift At Midnight Rake Guide",
 "desc": "The Rake is Shift At Midnight's Endless Mode-only monster — fast, red-glowing, and after your customers, not you. What's confirmed, and what isn't.",
 "trail": M + [(None, "Rake")],
 "h1": "The Rake",
 "lede": "The Rake is a fast, four-legged threat added on <strong>29 July 2026</strong>, and it only exists in <strong>Post-Story Endless Mode</strong> &mdash; if you have not finished Story Mode, or you have never touched Endless, you have not met one and will not. It comes from the forest around the station and goes after your customers rather than you directly.",
 "updated": "Last verified 10 September 2026 &middot; game version: 29 July 2026 patch",
 "body": """
  <div class="tags">
    <span class="tag amber">Endless / Post-Story only</span>
    <span class="tag">Killable</span>
    <span class="tag">No dedicated achievement</span>
    <span class="tag red">Behavioural detail: single source</span>
  </div>

  <div class="term tip">
    <div class="term-h">Why this monster does not have a page yet on most guides</div>
    <p>The Rake is new enough that it is not on the original launch bestiary, and this wiki's own <a href="/monsters/">monsters hub</a> flagged it by name as "the one without its own page" while we gathered enough to write about it properly. This page is that follow-up.</p>
  </div>

  <h2>What we know for certain, and from whom</h2>
  <p>The primary source is the developer's own account, <a href="https://x.com/ShiftAtMidnight" target="_blank" rel="noopener">@ShiftAtMidnight on X</a>, which posted on 3 August 2026: <em>"We added a new monster to shift at midnights Endless/Post-Story Mode, monsters called 'Rakes' will slowly emerge from the forest. You must shoot them before they reach the playable area, or bad stuff will happen."</em> That single sentence is the only developer-confirmed description of the Rake that exists, and everything in it is treated as fact on this page: the name, the Endless/Post-Story restriction, the forest spawn point, and the instruction to shoot it before it reaches the shop. We found that post embedded in the secondary write-up cited below rather than by reading the timeline directly, which is disclosed here rather than smoothed over.</p>
  <p>Everything more specific than that &mdash; exact speed, whether it can be trapped instead of shot, its health, its damage &mdash; comes from secondary reporting rather than the developer, and we are labelling it that way rather than presenting it as confirmed. The most detailed secondary write-up we found is <a href="https://allthings.how/shift-at-midnight-how-to-deal-with-rakes-in-endless-mode/" target="_blank" rel="noopener">AllThings.How's Rake guide</a>, and the behavioural claims below trace back to that single piece unless stated otherwise.</p>

  <table class="facts">
    <tr><th>Added</th><td>29 July 2026 patch</td></tr>
    <tr><th>Where it appears</th><td>Post-Story Endless Mode only &mdash; not Story Mode</td></tr>
    <tr><th>Spawn point</th><td>Emerges from the forest surrounding the gas station</td></tr>
    <tr><th>Stated counter</th><td>Shoot it before it reaches the playable area (developer's own wording)</td></tr>
    <tr><th>Health / damage figures</th><td>No reliable source. We are not publishing invented numbers.</td></tr>
  </table>

  <h2>What it looks and sounds like</h2>
  <p>Secondary reporting &mdash; not the developer post itself &mdash; describes the Rake as running on all fours, glowing red, and closing distance quickly once it appears. The same reporting says a customer's scream is the audio cue that one has spawned nearby, which would make it play like a mid-shift alarm rather than something you have to actively watch for. <strong>Treat this paragraph as secondary and unconfirmed by Kwalee directly</strong> &mdash; it is consistent across the reporting we found, but it traces to one detailed write-up rather than an official source.</p>

  <h2>How it changes an Endless shift</h2>
  <p>The rest of the bestiary mostly shows up during a <em>hunt</em> &mdash; the sequence that starts after you let a <a href="/guide/doppelgangers/">doppelganger</a> slip past you. The Rake is reported to work differently: it can appear on an otherwise calm shift, with no doppelganger mistake required to trigger it. If that reporting holds up, it removes the safety of a quiet Endless shift entirely, since the threat is not gated behind a decision you made at the counter.</p>
  <p>It is also reported to go after your <strong>customers</strong> specifically rather than you, which is a different failure mode than most of the roster. A <a href="/monsters/marionette/">Marionette</a> or an <a href="/monsters/entity/">Entity</a> coming for you is a survival problem; a Rake going for your customers is a quota problem, since a customer scared off or killed before they pay is lost revenue on top of whatever danger you were in.</p>

  <div class="term warn">
    <div class="term-h">What we are not going to tell you</div>
    <p>We have not found a confirmed health value, a confirmed damage number, or a confirmed spawn rate for Rakes, and we are not inventing any of the three. If you see a specific number attached to a Rake anywhere, ask where it came from before you plan a run around it.</p>
  </div>

  <h2>The practical approach, as reported</h2>
  <ol>
    <li><strong>Treat a customer scream as an alert.</strong> If this holds, it is your earliest warning that a Rake is on the map, separate from the Entity/hunt audio cues you already know.</li>
    <li><strong>Look toward the treeline.</strong> The forest edge around the station is the reported spawn zone, and the red glow is described as easy to pick out against it at night.</li>
    <li><strong>Engage before it closes the distance.</strong> The developer's own instruction &mdash; shoot it before it reaches the playable area &mdash; is the one piece of guidance we would call confirmed rather than reported.</li>
    <li><strong>In co-op, split the job.</strong> One player tracking and calling its position while another lines up the shot is the same delegation pattern that works for the <a href="/monsters/jack-in-the-box/">Jack-in-the-Box</a> &mdash; a person who is only watching finds a moving threat faster than a person doing three things at once.</li>
  </ol>

  <h2>Why there is no achievement for it</h2>
  <p>None of the game's <a href="/achievements/">ten achievements</a> mention the Rake by name, and all ten were part of the original launch achievement list, which predates the Rake's 29 July addition. That is expected, not a gap in this page &mdash; new content added after launch does not automatically get its own Steam achievement, and Kwalee has not announced one for it.</p>

  <h2>Does this affect Story Mode?</h2>
  <p>No. The Rake is locked to <strong>Post-Story Endless Mode</strong>, so a player working through the 13 story shifts will never encounter one, regardless of how those shifts go. See <a href="/nights-and-levels/">nights, shifts and Endless Mode</a> for what does and does not carry over between the two modes, and note that Endless itself is still in beta, with its full version planned as a free Q4 2026 update. If you are still working through Story Mode and want the full page order, the <a href="/start-here/">reading order guide</a> covers what to read before Endless content like this becomes relevant.</p>

  <div class="grid two">
    <a class="card" href="/nights-and-levels/"><b>Nights &amp; Endless Mode</b><span>What Endless actually is, and why night-by-night guides for Story Mode don't apply to it.</span></a>
    <a class="card danger" href="/monsters/"><b>Full bestiary</b><span>Every other named threat, and why the counterplay is different for each one.</span></a>
  </div>
""",
},
]

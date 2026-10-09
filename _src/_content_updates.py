#!/usr/bin/env python3
"""/updates/ —— 发售后补丁时间线。

新增这一页的理由:发售后的改动是竞品站最难跟的内容(要持续盯官方公告),
也是本站唯一能做到「比对手新」的地方。全部事实取自 Steam 官方公告 RSS、
SteamDB 补丁记录与开发者官网,每条都在页面上标了出处。
"""
from _build import build

U = [(None, "Updates")]

PAGES = [
{
 "path": "updates", "active": "/updates/",
 "title": "Shift At Midnight Patch Notes — Every Update Since Launch",
 "og_short": "Patch notes &amp; updates",
 "desc": "Every Shift At Midnight patch since the 22 July 2026 launch: 6-player lobbies, the Rake enemy, the second firearm, and what the developer has confirmed is still coming.",
 "trail": U,
 "h1": "Shift At Midnight updates and patch notes",
 "lede": "Four patches and one emergency beta branch since launch, the newest on 1 September 2026. <strong>The 29 July patch added a new enemy</strong> &mdash; if you finished the story before then, you have not met it.",
 "updated": "Last verified 10 October 2026 against the official Steam announcement feed &middot; game version: 1 September 2026 patch",
 "published": "2026-09-10",
 "body": """
  <div class="term tip">
    <div class="term-h">Where these come from</div>
    <p>Bun Muen does not use version numbers. Patches are announced by title on the Steam news feed,
      and the build IDs below come from SteamDB. Every entry links to its source &mdash; if a change is
      not in an official announcement, it is not on this page.</p>
  </div>

  <h2>1 September 2026 &mdash; &ldquo;30 new customers + more&rdquo;</h2>
  <p>The newest patch as of 10 October 2026. The changelog lists:</p>
  <ul>
    <li><strong>30 new customers</strong> added to Story Mode and Endless Mode.</li>
    <li><strong>Chainsaw</strong> added as a purchasable melee weapon &mdash; in the changelog&rsquo;s words,
      &ldquo;now required for the LOCKED AND LOADED achievement&rdquo;. See <a href="/achievements/">achievements</a>.</li>
    <li><strong>Security cameras</strong> added in Endless Mode. They &ldquo;can be viewed on the computer and
      let you keep an eye on anything that might emerge from the forest&rdquo;.</li>
    <li>You can now purchase your <strong>pet</strong> for the store in Endless Mode.</li>
    <li><strong>Patience re-enabled</strong> for Endless Mode.</li>
    <li>Two bear traps and two planks added in the storage room for the first shift of Endless Mode, and
      you can now purchase three additional bear traps instead of two.</li>
    <li>Quota, personal funds and pet info removed from the End Of Day Report in Endless Mode, and emails
      disabled in Endless Mode.</li>
    <li>&ldquo;Lots of various bug fixes and crash fixes&rdquo;.</li>
    <li><strong>Previewed for the next update:</strong> &ldquo;Next update will have some more spooky stuff
      for endless mode&rdquo;.</li>
  </ul>
  <p class="src">Source: <a href="https://steamcommunity.com/ogg/3722330/announcements/detail/710033254358451283"
    target="_blank" rel="noopener">Steam announcement, 1 September 2026</a>.</p>

  <h2>20 August 2026 &mdash; &ldquo;15 customers + bug fixes&rdquo;</h2>
  <p>The third post-launch patch. The changelog lists:</p>
  <ul>
    <li><strong>15 new customers</strong> added to Story Mode and Endless Mode.</li>
    <li><strong>Individual volume sliders</strong> added for each player.</li>
    <li><strong>Cloud saves</strong> added for Steam.</li>
    <li>Product prices equalized &ldquo;so getting true ending is less RNG&rdquo; &mdash; see
      <a href="/endings/">endings</a>.</li>
    <li>Fixed an issue with some start-of-shift notes not being randomized, and certain UI and world
      issues in other languages.</li>
    <li>&ldquo;Lots of various bug fixes and crash fixes&rdquo;.</li>
    <li><strong>Previewed for the next update:</strong> &ldquo;The next content update will be bigger and
      (probably) sooner than this one&rdquo;.</li>
  </ul>
  <p class="src">Source: <a href="https://steamcommunity.com/ogg/3722330/announcements/detail/672877388439226838"
    target="_blank" rel="noopener">Steam announcement, 20 August 2026</a>.</p>

  <h2>29 July 2026 &mdash; &ldquo;Balancing + bug fixes&rdquo;</h2>
  <p>The second post-launch patch, and the first to add an enemy and a weapon.</p>
  <ul>
    <li><strong>New enemy: the Rake.</strong> Rakes appear in <em>endless and post-story modes only</em>
      and emerge from the forests around the station. If you played story mode start to finish
      before this patch, you never saw one &mdash; and you still will not, because story mode does not
      spawn them.</li>
    <li><strong>A second purchasable firearm.</strong> Until this patch there was exactly one gun to buy.
      This matters most for the <a href="/achievements/">Locked And Loaded</a> achievement, which is
      about filling out the arsenal. Since the 1 September 2026 patch the Chainsaw is also
      &ldquo;now required for the LOCKED AND LOADED achievement&rdquo;, per that changelog.</li>
    <li><strong>Patience was removed in Endless Mode / post-story mode.</strong> The changelog line is
      &ldquo;Removed patience in ENDLESS MODE / POST-STORY MODE&rdquo;; it does not mention Story Mode.
      The 1 September 2026 patch re-enabled patience for Endless Mode (see above).</li>
    <li>Assorted bug and crash fixes.</li>
  </ul>
  <p class="src">Source: <a href="https://store.steampowered.com/news/app/3722330/view/695394018676179340"
    target="_blank" rel="noopener">Steam announcement, 29 July 2026</a>.</p>

  <h2>23 July 2026 &mdash; &ldquo;6 player lobbies + fixes&rdquo; (build 24354120)</h2>
  <p>The day-one patch, and the one that changed the answer to the most-asked question about this game.</p>
  <ul>
    <li><strong>Lobby size is now selectable up to six players.</strong> The developer was blunt about
      what this is: the game &ldquo;is designed and has always been marketed around a maximum of
      3 players&rdquo;, and above that it &ldquo;will likely become too chaotic, and is not recommended
      for your first playthrough&rdquo;. Treat it as a party mode, not the intended experience.
      See <a href="/multiplayer/">multiplayer</a> for how this plays out.</li>
    <li><strong>Marionette HP reduced.</strong> The Shift 9 music-box encounter got noticeably more
      survivable. See <a href="/monsters/marionette/">Marionette</a>.</li>
    <li><strong>Jack-in-the-Box volume increased.</strong> The music box is now much easier to locate
      by ear &mdash; which is the entire counterplay to the Marionette.</li>
    <li>Fixed Russian-region players being unable to create joinable lobbies.</li>
    <li>The profanity filter was removed.</li>
    <li><strong>Previewed for the next patch:</strong> the announcement closed by saying the following
      patch &ldquo;will aim to address the issue of people who crash, and are then unable to interact
      with the cursor or any buttons in the game&rdquo;. The 29 July notes list
      &ldquo;various bug fixes and crash fixes&rdquo; without saying whether that was among them, and no
      later announcement clarifies it &mdash; see <a href="/troubleshooting/">troubleshooting</a>.</li>
  </ul>
  <p class="src">Source: <a href="https://steamdb.info/patchnotes/24354120/" target="_blank"
    rel="noopener">SteamDB patch notes, build 24354120</a>.</p>

  <h2>22 July 2026 &mdash; the lobby connection beta branch</h2>
  <p>Launch day did not go smoothly. Enough players could not create or join lobbies that the developer
    shipped a temporary opt-in branch the same evening, before the proper fix landed the next day.</p>
  <p>No announcement has ever been published retiring that branch, so we cannot date it as fixed. If you
    or a friend opted in at launch and never switched back, that is worth checking. In your Steam library, right-click
    the game &rarr; Properties &rarr; <em>Game Versions &amp; Betas</em>, and make sure you are on
    the default branch rather than <code>network-issues-patch</code>.
    <strong>Everyone in a party has to be on the same branch to play together</strong>, which is the
    usual cause of &ldquo;we are all online but cannot see each other&rdquo;.</p>

  <h2>Announced, not confirmed as shipped</h2>
  <table>
    <tr><th>What</th><th>Status</th></tr>
    <tr><td>Public server browser</td>
        <td>The 10 July 2026 announcement says: &ldquo;There will be a Steam-only public server browser
          either on-launch, or shortly after launch.&rdquo; No later changelog mentions it going live
          (the 23 July, 29 July, 20 August and 1 September notes, checked on 10 October 2026). We have
          not tested it in game.</td></tr>
    <tr><td>Endless Mode updates</td>
        <td>The same announcement says: &ldquo;Throughout the rest of the year I plan to update endless
          mode with exclusive customers, traps, ways of detecting doppelgangers, etc.&rdquo; The 20 August
          and 1 September patches each added Endless Mode content (above). A free &ldquo;Q4 2026&rdquo;
          full release, which this page previously listed, is <strong>not confirmed by any official
          Steam announcement</strong> (all 31 checked on 10 October 2026). See
          <a href="/nights-and-levels/#endless-mode">Endless Mode</a>.</td></tr>
  </table>
  <p class="src">Source: <a href="https://steamcommunity.com/ogg/3722330/announcements/detail/715657047106918977" target="_blank" rel="noopener">Steam announcement, 10 July 2026</a>,
    and the later Steam announcements listed above.</p>

  <h2>Not announced</h2>
  <table>
    <tr><th>What</th><th>Status</th></tr>
    <tr><td>Crossplay between Steam and Xbox</td>
        <td><strong>Not announced.</strong> No official Steam announcement promises it (all 31 checked
          on 10 October 2026). The developer&rsquo;s 10 July 2026 post says Xbox and PC Game Pass players
          will have crossplay and Steam players will only play with other Steam players &mdash; see
          <a href="/crossplay/">crossplay</a>.</td></tr>
  </table>

  <h2>How to tell which build you are on</h2>
  <p>There is no in-game version number. The quickest tells:</p>
  <ul>
    <li><strong>Can you buy a Chainsaw?</strong> Only on the 1 September 2026 patch or later.</li>
    <li><strong>Are there individual volume sliders for each player?</strong> Only on 20 August or later.</li>
    <li><strong>Can you set a lobby above three players?</strong> If not, you are on the launch build.</li>
    <li><strong>Is there a second gun in the shop?</strong> Only on 29 July or later.</li>
  </ul>
  <p>If any of those are wrong, let Steam re-verify the files rather than reinstalling &mdash; the game
    is small and a verify usually resolves it. Problems a verify does not resolve are on
    <a href="/troubleshooting/">troubleshooting</a>.</p>

  <h2>What the patch pattern tells you</h2>
  <p>Four patches is a small sample, but the shape so far is worth knowing if you are deciding when to
    play. The first two landed within eight days of release, on 23 and 29 July; the next two followed on
    20 August and 1 September. All four announcements were posted on a weekday afternoon UTC. The last
    three end by asking players to report bugs through Discord &mdash; the 1 September notes say
    &ldquo;I'm only 1 guy, I can't find everything myself!&rdquo; &mdash; and each changelog is a short
    bulleted list with no version number.</p>
  <p>The practical consequence: <strong>a guide written before 1 September 2026 is describing an older build</strong>.
    It will not know about the Chainsaw, the security cameras, the 45 customers added across the last two
    patches, or that patience is back in Endless Mode.
    If a page you are reading does not carry a date, that is the first thing to check.</p>

  <h2>Nothing since 1 September</h2>
  <p>As of <strong>10 October 2026</strong> the 1 September patch is the newest patch announcement on the
    official Steam feed. The only official post after it is a 1 October 2026 Steam Autumn Sale notice,
    which lists no game changes. We check the official feed rather than aggregators, and this page is
    dated whenever it changes.</p>
"""},
]

if __name__ == "__main__":
    print("生成 /updates/:")
    build(PAGES)

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
 "lede": "Two real patches and one emergency beta branch since launch. <strong>The 29 July patch added a new enemy</strong> &mdash; if you finished the story before then, you have not met it.",
 "body": """
  <div class="term tip">
    <div class="term-h">Where these come from</div>
    <p>Bun Muen does not use version numbers. Patches are announced by title on the Steam news feed,
      and the build IDs below come from SteamDB. Every entry links to its source &mdash; if a change is
      not in an official announcement, it is not on this page.</p>
  </div>

  <h2>29 July 2026 &mdash; &ldquo;Balancing + bug fixes&rdquo;</h2>
  <p>The most consequential patch so far, because it added content rather than fixing plumbing.</p>
  <ul>
    <li><strong>New enemy: the Rake.</strong> Rakes appear in <em>endless and post-story modes only</em>
      and emerge from the forests around the station. If you played story mode start to finish
      before this patch, you never saw one &mdash; and you still will not, because story mode does not
      spawn them.</li>
    <li><strong>A second purchasable firearm.</strong> Until this patch there was exactly one gun to buy.
      This matters most for the <a href="/achievements/">Locked And Loaded</a> achievement, which is
      about filling out the arsenal.</li>
    <li><strong>The patience mechanic was removed.</strong> Customers no longer run down a patience
      meter while you verify them. In practice this makes careful ID checking much less punishing &mdash;
      the main reason players used to rush a scan and let a doppelganger through.</li>
    <li>Assorted bug and crash fixes.</li>
  </ul>
  <p class="src">Source: <a href="https://store.steampowered.com/news/app/3722330/view/695394018676179340"
    target="_blank" rel="noopener">Steam announcement, 29 July 2026</a>.</p>

  <h2>23 July 2026 &mdash; &ldquo;6 player lobbies + fixes&rdquo; (build 24354120)</h2>
  <p>The day-one patch, and the one that changed the answer to the most-asked question about this game.</p>
  <ul>
    <li><strong>Lobby size is now selectable up to six players.</strong> The developer was blunt about
      what this is: the game &ldquo;is designed and has always been marketed around a maximum of
      3 players&rdquo;, larger lobbies &ldquo;may become chaotic&rdquo;, and they do not recommend six
      for a first playthrough. Treat it as a party mode, not the intended experience.
      See <a href="/multiplayer/">multiplayer</a> for how this plays out.</li>
    <li><strong>Marionette HP reduced.</strong> The Shift 9 music-box encounter got noticeably more
      survivable. See <a href="/monsters/marionette/">Marionette</a>.</li>
    <li><strong>Jack-in-the-Box volume increased.</strong> The music box is now much easier to locate
      by ear &mdash; which is the entire counterplay to the Marionette.</li>
    <li>Fixed Russian-region players being unable to create joinable lobbies.</li>
    <li>The profanity filter was removed.</li>
    <li>Known issue left open: a crash related to mouse cursor interaction.</li>
  </ul>
  <p class="src">Source: <a href="https://steamdb.info/patchnotes/24354120/" target="_blank"
    rel="noopener">SteamDB patch notes, build 24354120</a>.</p>

  <h2>22 July 2026 &mdash; the lobby connection beta branch</h2>
  <p>Launch day did not go smoothly. Enough players could not create or join lobbies that the developer
    shipped a temporary opt-in branch the same evening, before the proper fix landed the next day.</p>
  <p>The branch is no longer needed &mdash; the fix is in the main build &mdash; but if you or a friend
    opted in at launch and never switched back, that is worth checking. In your Steam library, right-click
    the game &rarr; Properties &rarr; <em>Game Versions &amp; Betas</em>, and make sure you are on
    the default branch rather than <code>network-issues-patch</code>.
    <strong>Everyone in a party has to be on the same branch to play together</strong>, which is the
    usual cause of &ldquo;we are all online but cannot see each other&rdquo;.</p>

  <h2>Confirmed, but not out yet</h2>
  <table>
    <tr><th>What</th><th>Status</th></tr>
    <tr><td>Full crossplay including Steam</td>
        <td>Confirmed as a post-release update, <strong>no date</strong>. Today crossplay works only
          between Xbox and PC Game Pass &mdash; see <a href="/crossplay/">crossplay</a>.</td></tr>
    <tr><td>Public server browser</td>
        <td>Announced before launch as a post-release addition. Not shipped as of 5 August 2026.</td></tr>
    <tr><td>Endless Mode full release</td>
        <td>Free update planned for <strong>Q4 2026</strong>, alongside more customers, traps, weapons
          and monsters. The beta is already playable &mdash; see
          <a href="/nights-and-levels/#endless-mode">Endless Mode</a>.</td></tr>
  </table>
  <p class="src">Sources: <a href="https://bunmuen.com/" target="_blank" rel="noopener">bunmuen.com</a>
    and the Steam announcement archive.</p>

  <h2>How to tell which build you are on</h2>
  <p>There is no in-game version number. The quickest tells:</p>
  <ul>
    <li><strong>Does a customer have a patience meter?</strong> If yes, you are on a pre-29-July build
      and Steam has not updated.</li>
    <li><strong>Can you set a lobby above three players?</strong> If not, you are on the launch build.</li>
    <li><strong>Is there a second gun in the shop?</strong> Only on 29 July or later.</li>
  </ul>
  <p>If any of those are wrong, let Steam re-verify the files rather than reinstalling &mdash; the game
    is small and a verify usually resolves it.</p>

  <h2>What the patch pattern tells you</h2>
  <p>Three data points is not a trend, but the shape so far is worth knowing if you are deciding when to
    play. Both real patches landed within eight days of release, both were pushed on a weekday afternoon
    UTC, and both mixed balance changes with content rather than being pure bug fixes. The developer is a
    solo studio working with a publisher, and takes bug reports through Discord rather than a tracker,
    which is why patch notes read as short prose instead of an itemised changelog.</p>
  <p>The practical consequence: <strong>a guide written before 29 July is describing a different game</strong>
    in at least three respects &mdash; no Rakes, a patience meter on customers, and one purchasable gun.
    If a page you are reading does not carry a date, that is the first thing to check.</p>

  <h2>Nothing since 29 July</h2>
  <p>As of <strong>5 August 2026</strong> the 29 July patch is still the newest public announcement.
    SteamDB shows background depot activity after that date with no accompanying patch notes, which
    normally means store-page or build housekeeping rather than a player-facing change. We check the
    official feed rather than aggregators, and this page is dated whenever it changes.</p>
"""},
]

if __name__ == "__main__":
    print("生成 /updates/:")
    build(PAGES)

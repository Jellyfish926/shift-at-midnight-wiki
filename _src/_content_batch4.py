#!/usr/bin/env python3
"""2026-09-11 第四批新增页 —— 实体页,素材全部来自本仓已发布内容,不引入新事实。

盘点结论(可引用素材词数 ≥500 才做):
  /endings/true-ending/     True Ending 相关唯一句 995 词  → 做
  /endings/grave-decision/  Grave Decision 相关唯一句 694 词 → 做
  /endings/empty-home/      Empty Home 相关唯一句 755 词   → 做
  /achievements/monster-kills/   四个击杀成就 + 三个怪物页的反制素材 → 做
  /achievements/hunt-and-arsenal/ 三个 hunt/装备成就 + Entity/survival 素材 → 做
不做:单个成就页(每个独有素材 30-60 词)、单个具名 doppelganger 页(11-31 词)、
单个破绽类别页(31-126 词)、单个里程碑页(Shift 9 / Night 2 素材几乎全是怪物页原文,
会变成怪物页的翻版)。

成就解锁率两个读数并列:achievements.json(2026-09-07 抓取)与老页 2026-08-13 读数
不一致,不挑边,两个日期都写出来。
"""
import json as _json
import pathlib as _pathlib

_ACH_FILE = _pathlib.Path(__file__).resolve().parent.parent / "achievements.json"
_ACH = {a["name"]: a["pct"] for a in _json.loads(_ACH_FILE.read_text())["achievements"]}

E = [("/endings/", "Endings")]
A = [("/achievements/", "Achievements")]

UPD = "Last verified 11 September 2026 &middot; game version: 29 July 2026 patch"

RATE_NOTE = ("""  <div class="term warn">
    <div class="term-h">Two readings of the same number</div>
    <p>Global unlock rates move as more people buy the game, and this wiki now holds two readings taken a
      month apart. Where they differ, both are given &mdash; the <strong>7 September 2026</strong> figure first,
      the <strong>13 August 2026</strong> figure in brackets. Neither is wrong; a percentage of a growing
      player base is a moving number, and nothing on this page depends on which of the two you use.</p>
  </div>""")

PAGES = [

# ─────────────────────────────────────────────── /endings/true-ending/
{
 "path": "endings/true-ending",
 "active": "/endings/",
 "title": "Shift At Midnight True Ending: Both Conditions Explained",
 "og_short": "True Ending conditions",
 "desc": ("The True Ending needs two things at once: refuse the Sheriff Clyde call after Shift 12, and end "
          "Shift 13 holding $250 or more."),
 "trail": E + [(None, "True Ending")],
 "h1": "True Ending",
 "lede": ("The only outcome where <strong>nobody you care about dies</strong> &mdash; and the only one that asks "
          "you to satisfy two unrelated requirements in the same run. One is a refusal, the other is a bank "
          "balance, and missing either drops you into a different ending without warning."),
 "updated": UPD,
 "body": f"""
  <div class="tags">
    <span class="tag green">Best outcome</span>
    <span class="tag amber">Two conditions, both required</span>
    <span class="tag">Hidden on Steam</span>
    <span class="tag">{_ACH['True Ending']}% unlocked</span>
  </div>

  <table class="facts">
    <tr><th>Condition one</th><td><strong>Do not</strong> call Sheriff Clyde when the choice appears after Shift 12</td></tr>
    <tr><th>Condition two</th><td>Personal savings of <strong>$250 or more</strong> when Shift 13 ends</td></tr>
    <tr><th>When condition two is checked</th><td>At the <strong>end</strong> of Shift 13 &mdash; not at the decision point</td></tr>
    <tr><th>Outcome</th><td>Your pet and Clyde both live; the Dentist appears and Clyde helps destroy him</td></tr>
    <tr><th>Steam unlock</th><td>{_ACH['True Ending']}% (13 August reading: 16.0%) &mdash; description hidden</td></tr>
    <tr><th>Xbox</th><td>200G &mdash; twice what either other ending awards</td></tr>
    <tr><th>Available in Endless Mode?</th><td>No. All three endings belong to Story Mode</td></tr>
  </table>

{RATE_NOTE}

  <h2>Why this one is harder than it reads</h2>

  <p>Written out, neither requirement sounds demanding. Declining a phone call costs nothing, and $250 is not a
    large sum across thirteen working nights. What makes the ending rare is that the two halves pull against each
    other in time: the refusal happens at a moment you can plan for, and the money is graded a full shift later,
    after a night in which the temptation to spend is at its highest.</p>

  <p>That gap is where runs are lost. A player can make the correct call after Shift 12, walk into the final night
    holding a comfortable buffer, spend it on preparation, and finish under the line. Nothing flags the mistake
    while it is being made, because the check happens once, at the end, silently.</p>

  <h2>Condition one: leave the phone alone</h2>

  <p>After Shift 12 the game offers the Clyde call. Taking it resolves your ending immediately and permanently &mdash;
    from that point your balance is irrelevant, and you are locked into
    <a href="/endings/grave-decision/">Grave Decision</a> no matter how the last night goes. Declining keeps both
    remaining outcomes live, which is exactly why declining is the greedy option rather than the safe one.</p>

  <p>Worth being blunt about the trade, since the choice is genuinely well built: calling Clyde guarantees your pet
    survives and asks nothing of your finances. Refusing gambles that guarantee against a number you may not hit.
    The <a href="/endings/">endings overview</a> sets the two branches side by side if you want the comparison in
    one table.</p>

  <h2>Condition two: the balance at the end of the last night</h2>

  <p>The threshold is tested against your personal savings when Shift 13 finishes. Money you were holding when you
    refused the call does not count for anything if you spend it afterwards, and there is no partial credit &mdash;
    $249 and $0 land in the same place.</p>

  <p>The single most expensive habit on the final night is buying gear for it. Shift 13 is
    <a href="/monsters/the-dentist/">the Dentist</a>, who is described as immune to your weapons, with traps not
    stopping him either. Every dollar spent arming yourself against him buys nothing and moves you away from the
    threshold. There is no combat loadout that changes that encounter; the published route through it is movement
    toward Clyde, and movement is free.</p>

  <div class="term tip">
    <div class="term-h">The one patch that helps the money</div>
    <p>The <a href="/updates/">29 July 2026 patch</a> removed the patience mechanic, so customers no longer run down a
      timer while you verify them. Rushed verification is what lets a doppelganger through, and a doppelganger that
      gets through becomes a Hunt, and a Hunt is the expensive kind of night &mdash; ammunition, replacements, a
      shift spent not selling. Careful checking now costs nothing, which quietly makes
      <a href="/guide/doppelgangers/">the identification guide</a> the most financial page on this wiki.</p>
  </div>

  <h2>What this wiki will not tell you about the money</h2>

  <p>Beyond the $250 figure itself, we have found no verifiable numbers for nightly quotas, item prices or weapon
    costs, so there is no earnings route published here and there will not be an invented one. What can be said is
    structural, and it is enough to act on: money not spent is money kept, and the two categories that most reliably
    eat a buffer are ammunition and the <a href="/guide/survival/#weapons">weapons arsenal</a>. The arsenal has its
    own achievement attached, which makes it an easy thing to chase on precisely the run where you should not be
    chasing it.</p>

  <h2>Common mistakes</h2>
  <ul>
    <li><strong>Checking the balance at the decision point.</strong> The threshold applies at the end of Shift 13. What
      you were holding after Shift 12 is not what gets measured.</li>
    <li><strong>Arming up for the final night.</strong> Gear does nothing against the Dentist and costs you the only
      variable still in play.</li>
    <li><strong>Chasing the arsenal on the same run.</strong> Filling out every melee weapon is a separate achievement
      with a separate budget; stacking it onto a True Ending attempt puts both at risk. See
      <a href="/achievements/hunt-and-arsenal/">the arsenal achievement</a>.</li>
    <li><strong>Assuming the chase itself matters.</strong> How well the final shift goes is not one of the two
      variables. Surviving badly and surviving cleanly produce the same ending.</li>
    <li><strong>Waiting for Endless Mode.</strong> Endless unlocks after the story and has no ending of its own &mdash;
      see <a href="/nights-and-levels/">nights and Endless Mode</a>.</li>
  </ul>

  <h2>Where it sits against the rest of the curve</h2>

  <p>At {_ACH['True Ending']}%, this is the second-rarest of the ten achievements, above only
    <a href="/endings/empty-home/">Empty Home</a>. Set that against <em>Still Breathing</em> &mdash; surviving one Hunt,
    held by {_ACH['Still Breathing']}% &mdash; and the shape of the player base is clear: almost everyone survives their
    first bad night, and most never see Shift 12 at all. The
    <a href="/achievements/">full achievement list</a> has the whole curve.</p>

  <p>Because the conditions are mutually exclusive within a run, collecting all three endings takes at least three
    completed stories. If that is the plan, this is the one to take first, while the money still matters to you &mdash;
    the other two ask nothing financial. The <a href="/tools/completion-tracker/">completion tracker</a> keeps count.</p>

  <h2>Sources on this site</h2>
  <ul>
    <li><a href="/endings/">Endings overview</a> &mdash; the two variables, all three outcomes, and the unlock rates read on 13 August 2026.</li>
    <li><a href="/monsters/the-dentist/">The Dentist</a> &mdash; Shift 13, weapon and trap immunity, and the Clyde resolution.</li>
    <li><a href="/achievements/">All 10 achievements</a> &mdash; the completion curve and the hidden descriptions.</li>
    <li><a href="/guide/doppelgangers/">Identifying doppelgangers</a> and <a href="/updates/">patch notes</a> &mdash; the removed patience meter.</li>
  </ul>

  <div class="grid two">
    <a class="card" href="/endings/grave-decision/"><b>Grave Decision</b><span>What taking the call guarantees, and what it costs.</span></a>
    <a class="card" href="/endings/empty-home/"><b>Empty Home</b><span>What a failed attempt at this page looks like.</span></a>
  </div>
""",
},

# ─────────────────────────────────────────── /endings/grave-decision/
{
 "path": "endings/grave-decision",
 "active": "/endings/",
 "title": "Grave Decision Ending: The Call, and What It Costs",
 "og_short": "Grave Decision ending",
 "desc": ("Calling Sheriff Clyde after Shift 12 locks the Grave Decision ending on the spot, with no money "
          "requirement at all. Your pet lives, Clyde does not."),
 "trail": E + [(None, "Grave Decision")],
 "h1": "Grave Decision",
 "lede": ("The branch that asks nothing of your bank balance, and the most commonly held of the three ending "
          "achievements. One phone call settles it &mdash; and it settles it the moment you make it, which is "
          "both the appeal and the trap."),
 "updated": UPD,
 "body": f"""
  <div class="tags">
    <span class="tag amber">Locked by one choice</span>
    <span class="tag green">No money requirement</span>
    <span class="tag">Hidden on Steam</span>
    <span class="tag">{_ACH['Grave Decision']}% unlocked</span>
  </div>

  <table class="facts">
    <tr><th>Condition</th><td>Call Sheriff Clyde when the choice appears after Shift 12</td></tr>
    <tr><th>Does money matter?</th><td>No &mdash; your savings stop counting the moment you take the call</td></tr>
    <tr><th>Outcome</th><td>Your pet gets the surgery and survives. <strong>Clyde dies.</strong></td></tr>
    <tr><th>Steam unlock</th><td>{_ACH['Grave Decision']}% (13 August reading: 33.1%) &mdash; description hidden</td></tr>
    <tr><th>Xbox</th><td>100G</td></tr>
    <tr><th>Rank among the three</th><td>Most common, by roughly two to one over <a href="/endings/true-ending/">True Ending</a></td></tr>
  </table>

{RATE_NOTE}

  <h2>The choice is not a trick</h2>

  <p>It would be easy to file this as the wrong answer, and that reading misses what makes the decision work. Calling
    Clyde does the thing the whole run has been about: your pet gets the surgery, and no financial target stands
    between you and that outcome. For a run that went badly &mdash; a Hunt that ate the takings, a shift lost to a
    doppelganger you waved through &mdash; it is the option that still produces something worth having.</p>

  <p>The cost is a life, and it is charged after the decision is locked. That ordering is the whole design: you are
    not asked to weigh Clyde against your savings while you can still see both, you are asked to commit and then shown
    the bill. Nothing in the moment tells you this is the branch where he does not come home.</p>

  <h2>What the call closes off</h2>

  <p>Taking it resolves the ending immediately. Whatever happens across the final night, and whatever you are holding
    when it ends, the outcome is already written. That has one practical consequence worth stating plainly: if you were
    already above the $250 threshold when the choice appeared, calling Clyde converts an outcome you had effectively
    earned into this one. Players do it for reassurance, which is exactly when it is most expensive.</p>

  <p>If the balance is genuinely short, the arithmetic runs the other way. Refusing with no realistic path to $250 does
    not produce the best ending &mdash; it produces <a href="/endings/empty-home/">Empty Home</a>, where Clyde survives
    and your pet does not. Refusing is only the better line when the number is reachable. The
    <a href="/endings/">endings overview</a> lays the branches out in one table.</p>

  <h2>What the unlock rate suggests</h2>

  <p>At {_ACH['Grave Decision']}% this is comfortably the most held of the three, and roughly double
    <a href="/endings/true-ending/">True Ending</a> at {_ACH['True Ending']}%. That gap is the sort of thing you would
    expect when one branch guarantees a survivable result and the other is staked on how thirteen nights of trading
    went. First-time finishers default to the certain outcome, which is a reasonable thing for first-time finishers
    to do.</p>

  <p>Add all three ending achievements together and you do not get a completion rate, because a player who replays can
    hold more than one. What the numbers do support is the broader picture on the
    <a href="/achievements/">achievements page</a>: the drop-off is not at the ending, it is long before it.</p>

  <h2>What happens on the final night</h2>

  <p>This wiki documents Shift 13 as <a href="/monsters/the-dentist/">the Dentist</a>'s night &mdash; the final shift's
    pursuer, immune to weapons, unaffected by traps, ended only when Sheriff Clyde takes over in a cutscene. The
    endings overview names the Dentist specifically in the True Ending line, where Clyde helps destroy him. Whether the
    encounter plays out identically on this branch is <strong>not confirmed</strong> by anything published here, and we
    are not going to describe a scene we cannot source. What is safe to carry into the night either way: gear does not
    help, and preparation spent on weapons is preparation wasted.</p>

  <h2>If you are collecting all three</h2>

  <p>The conditions are mutually exclusive inside a single run, so three completed stories is the floor. This one is the
    natural second or third pass rather than the first, precisely because it has no financial requirement &mdash; take
    <a href="/endings/true-ending/">True Ending</a> while you still care about the balance, then spend the follow-up runs
    on the two outcomes that ask nothing of it. That sequencing is our suggestion, not something the game states. The
    <a href="/tools/completion-tracker/">completion tracker</a> has all three as tick boxes.</p>

  <h2>Common mistakes</h2>
  <ul>
    <li><strong>Calling for safety while already above the line.</strong> The one genuinely avoidable way to lose a
      True Ending you had earned.</li>
    <li><strong>Refusing on principle with an empty balance.</strong> Refusal is not a better ending, it is a different
      gamble, and the losing side of it kills your pet.</li>
    <li><strong>Expecting money to rescue the run afterwards.</strong> Once the call is made, savings are irrelevant.
      Banking through Shift 13 does nothing here.</li>
    <li><strong>Looking for this ending in Endless Mode.</strong> Endless unlocks after the story and has no endings of
      its own &mdash; see <a href="/nights-and-levels/">nights and Endless Mode</a>.</li>
  </ul>

  <h2>Sources on this site</h2>
  <ul>
    <li><a href="/endings/">Endings overview</a> &mdash; conditions, outcomes, Xbox gamerscore and the 13 August unlock rates.</li>
    <li><a href="/achievements/">All 10 achievements</a> &mdash; the hidden descriptions and the shape of the curve.</li>
    <li><a href="/monsters/the-dentist/">The Dentist</a> &mdash; what Shift 13 is, and why gear does not help.</li>
    <li><a href="/nights-and-levels/">Nights and Endless Mode</a> &mdash; where the 13-shift story ends and Endless begins.</li>
  </ul>

  <div class="grid two">
    <a class="card" href="/endings/true-ending/"><b>True Ending</b><span>The branch this one closes off, and both of its conditions.</span></a>
    <a class="card" href="/endings/empty-home/"><b>Empty Home</b><span>What refusing the call looks like when the money is not there.</span></a>
  </div>
""",
},

# ─────────────────────────────────────────────── /endings/empty-home/
{
 "path": "endings/empty-home",
 "active": "/endings/",
 "title": "Empty Home Ending: The Failed True Ending Attempt",
 "og_short": "Empty Home ending",
 "desc": ("Empty Home is what happens when you refuse the Sheriff Clyde call and finish Shift 13 under "
          "$250: the rarest achievement in the game, and nobody plans for it."),
 "trail": E + [(None, "Empty Home")],
 "h1": "Empty Home",
 "lede": ("The rarest achievement in the game, and the only one people unlock by accident on a run they thought "
          "was going well. It is not a separate route to anything &mdash; it is the losing half of the same gamble "
          "that produces the <a href=\"/endings/true-ending/\">True Ending</a>."),
 "updated": UPD,
 "body": f"""
  <div class="tags">
    <span class="tag red">Worst outcome</span>
    <span class="tag amber">Usually unintended</span>
    <span class="tag">Hidden on Steam</span>
    <span class="tag">{_ACH['Empty Home']}% unlocked &mdash; rarest</span>
  </div>

  <table class="facts">
    <tr><th>Condition</th><td><strong>Do not</strong> call Sheriff Clyde after Shift 12, <strong>and</strong> finish Shift 13 under $250</td></tr>
    <tr><th>Outcome</th><td>Clyde survives, but the surgery cannot be paid for. <strong>Your pet dies.</strong></td></tr>
    <tr><th>Steam unlock</th><td>{_ACH['Empty Home']}% (13 August reading: 10.1%) &mdash; rarest of the ten</td></tr>
    <tr><th>Xbox</th><td>100G</td></tr>
    <tr><th>Relationship to True Ending</th><td>Same branch, opposite side of one number</td></tr>
  </table>

{RATE_NOTE}

  <h2>Rarer does not mean harder</h2>

  <p>It is the lowest percentage on the <a href="/achievements/">achievement list</a>, which invites the wrong
    conclusion. Nothing about this outcome is difficult; it is uncommon because it sits at the end of a long run that
    most players never finish, and because the people who do finish tend to either take the guaranteed branch or clear
    the threshold. Being rarer than <a href="/endings/true-ending/">True Ending</a> also rules out the natural
    assumption that it is a step on the way there. It is not a stage. It is the other result.</p>

  <h2>How players actually get here</h2>

  <p>Almost nobody sets out for this. The run that produces it looks like a True Ending attempt right up to the last
    few minutes:</p>

  <ul>
    <li><strong>Spending during the final shift.</strong> The balance is graded when Shift 13 <em>ends</em>, not when you
      refuse the call. A buffer that was comfortable at the decision point can be gone by the time it is measured.</li>
    <li><strong>Buying weapons for the last night.</strong> Shift 13 is <a href="/monsters/the-dentist/">the Dentist</a>,
      who is immune to weapons and unaffected by traps. That purchase does nothing except move the number down.</li>
    <li><strong>An expensive Hunt late in the run.</strong> Letting a doppelganger through turns a trading night into an
      ammunition night &mdash; see <a href="/monsters/entity/">the Entity</a> for what a Hunt is and
      <a href="/guide/doppelgangers/">the identification guide</a> for how it starts.</li>
    <li><strong>Refusing the call out of habit.</strong> Declining is only the stronger line when $250 is realistically
      reachable. With no path to it, refusal converts a guaranteed <a href="/endings/grave-decision/">Grave Decision</a>
      into this.</li>
  </ul>

  <h2>Avoiding it</h2>

  <p>There is exactly one rule, and it is boring: if you have refused the call, treat every dollar during Shift 13 as
    spent against the ending rather than against the night. The final shift has no purchase that improves the encounter,
    because the encounter is not a combat problem. Running toward Sheriff Clyde is free.</p>

  <p>If the balance is already hopeless when the choice arrives, the honest play is to take the call. You lose Clyde and
    keep the pet, which is a worse result than the True Ending and a much better one than this page.</p>

  <div class="term tip">
    <div class="term-h">The patch that changed the economics</div>
    <p>The <a href="/updates/">29 July 2026 update</a> removed the patience meter, so nothing rushes you at the counter
      any more. Since the expensive nights are the ones that start with a bad verification, slow checking is now the
      cheapest money-saving habit available &mdash; and the one that keeps the $250 within reach without any grinding at
      all.</p>
  </div>

  <h2>If you want it deliberately</h2>

  <p>Collecting all three endings takes at least three completed stories, because the conditions cannot overlap inside a
    single run. On a dedicated pass this is the least demanding of the three: refuse the call, then simply do not clear
    the threshold. Our suggested order is to take the <a href="/endings/true-ending/">True Ending</a> first, while the
    balance still matters, and leave the two outcomes with no financial requirement for the follow-up runs. The
    <a href="/tools/completion-tracker/">completion tracker</a> holds all three, along with every other achievement this
    wiki can source.</p>

  <h2>What it says about the player base</h2>

  <p>Put this next to <em>Still Breathing</em> &mdash; survive one Hunt, held by {_ACH['Still Breathing']}% &mdash; and the
    distance is the story. Surviving a bad night is ordinary. Reaching the decision after Shift 12 at all is not, which is
    why all three ending achievements sit near the bottom of the curve and why the two halves of this particular gamble are
    the two rarest entries in the game. The <a href="/endings/">endings overview</a> works through what those numbers do and
    do not prove.</p>

  <h2>Sources on this site</h2>
  <ul>
    <li><a href="/endings/">Endings overview</a> &mdash; the two variables, the outcome text and the 13 August unlock rates.</li>
    <li><a href="/achievements/">All 10 achievements</a> &mdash; where this sits on the completion curve.</li>
    <li><a href="/monsters/the-dentist/">The Dentist</a> &mdash; why nothing bought for Shift 13 is worth its price.</li>
    <li><a href="/monsters/entity/">The Entity</a> and <a href="/guide/survival/">the survival guide</a> &mdash; how a Hunt drains a run's savings.</li>
  </ul>

  <div class="grid two">
    <a class="card" href="/endings/true-ending/"><b>True Ending</b><span>The same branch, played well enough.</span></a>
    <a class="card" href="/endings/grave-decision/"><b>Grave Decision</b><span>The guaranteed outcome this run gave up.</span></a>
  </div>
""",
},

# ────────────────────────────────────── /achievements/monster-kills/
{
 "path": "achievements/monster-kills",
 "active": "/achievements/",
 "title": "Shift At Midnight Kill Achievements: All Four, In Order",
 "og_short": "Kill achievements guide",
 "desc": ("First Blood, Silenced, Freed and Last Performance: four kill achievements, four different "
          "threats, four completely different methods."),
 "trail": A + [(None, "Kill achievements")],
 "h1": "The four kill achievements",
 "lede": ("Four of the ten achievements are variations on &ldquo;kill one of these&rdquo;, and they are nothing "
          "alike in practice: one you will get by accident, one is a few shots, one cannot be shot at all, and "
          "one is a race against a music box."),
 "updated": UPD,
 "body": f"""
  <div class="tags">
    <span class="tag">4 of 10 achievements</span>
    <span class="tag green">None are hidden</span>
    <span class="tag amber">{_ACH['First Blood']}% down to {_ACH['Last Performance']}%</span>
  </div>

  <table class="facts">
    <tr><th>First Blood</th><td>Kill your first customer &mdash; {_ACH['First Blood']}% (13 August reading: 96.9%)</td></tr>
    <tr><th>Silenced</th><td>Kill a <a href="/monsters/shrieking-doll/">Shrieking Doll</a> &mdash; {_ACH['Silenced']}% (89.8%)</td></tr>
    <tr><th>Freed</th><td>Kill a <a href="/monsters/demented/">Demented</a> &mdash; {_ACH['Freed']}%</td></tr>
    <tr><th>Last Performance</th><td>Kill a <a href="/monsters/marionette/">Marionette</a> &mdash; {_ACH['Last Performance']}% (41.6%)</td></tr>
  </table>

{RATE_NOTE}

  <p>One of those pairs moved the other way between readings: the Marionette kill sits higher in the September
    snapshot than in the August one, where every other rate drifted down. We have not established why, and we are
    not going to guess &mdash; both figures are printed above so you can see the discrepancy rather than inherit
    a tidied version of it.</p>

  <h2>First Blood &mdash; the one you do not aim for</h2>

  <p>Killing a customer unlocks it, and at {_ACH['First Blood']}% it is the most widely held achievement in the game.
    That number is worth reading as a difficulty statement about the job rather than a milestone: nearly everyone who
    plays kills a real person, because the whole loop is a judgement call made under uncertainty at a counter.</p>

  <p>It is also the cheaper of the two errors available to you. Shooting a genuine customer costs you a sale; waving a
    doppelganger through costs you the night, because it comes back that same shift as
    <a href="/monsters/entity/">an Entity</a> to hunt you. If you are going to be wrong, the game charges far less for
    this direction of wrong. <a href="/guide/doppelgangers/">The identification guide</a> covers the checks that keep
    you from being wrong in either.</p>

  <h2>Silenced &mdash; easy kill, expensive timing</h2>

  <p>The <a href="/monsters/shrieking-doll/">Shrieking Doll</a> is the most fragile threat in the game and goes down in
    a few shots, which is why {_ACH['Silenced']}% of players already have this. The part worth planning is not the kill,
    it is when you take it.</p>

  <p>The doll typically arrives <strong>during a Hunt, alongside the Entities</strong>, so by the time one is in front
    of you something considerably worse is already in the building. Firing is noise, and the Entity that came with it
    navigates by sound. A doll killed at the wrong moment is a flare fired at the thing hunting you. If you need this
    achievement, take the shot when the Entity is not close, then move &mdash; the shot described where you were
    standing, not where you are now.</p>

  <h2>Freed &mdash; the one that cannot be shot</h2>

  <p>The <a href="/monsters/demented/">Demented</a> freezes for exactly as long as you look straight at it, and while you
    are looking you cannot damage it either. The confirmed removal method is not a weapon at all: break your gaze
    deliberately, with a trap positioned between you and it, and let the trap do the work.</p>

  <p>That makes this a preparation achievement dressed up as a combat one. The resource that decides it is knowing where
    your traps already are, which is a decision made earlier in the shift &mdash; see
    <a href="/guide/survival/">traps, barricades and hiding</a>. At {_ACH['Freed']}% it is still the fourth most widely held
    achievement in the game, so whatever you have read about the Demented being rare, it is not.</p>

  <h2>Last Performance &mdash; a clock, not a fight</h2>

  <p>The <a href="/monsters/marionette/">Marionette</a> arrives from <strong>Shift 9</strong> onward, flagged in advance
    by an N.E.T. email, and announced live by a music box starting somewhere in the store. The counter-play is to reach
    the box and hold <strong>E</strong> to rewind it before the melody finishes three times &mdash; which prevents the
    Marionette from arriving at all.</p>

  <p>For this achievement you want the opposite. Letting the clock run is how you get something to kill, and the fight is
    an ammunition problem: it is tougher than a standard entity, though the 23 July 2026 patch cut its health, so advice
    written before that date describes a harder fight than the one you will have. A second player helps more here than
    anywhere else on this list.</p>

  <div class="term warn">
    <div class="term-h">Four kills, not seven</div>
    <p>The bestiary is larger than this list. There is no kill achievement for the
      <a href="/monsters/entity/">Entity</a>, for <a href="/monsters/jack-in-the-box/">the Jack-in-the-Box</a>, for
      <a href="/monsters/norbert/">Norbert</a> or for the Post-Story <a href="/monsters/rake/">Rake</a>, and
      <a href="/monsters/the-dentist/">the Dentist</a> has no achievement of his own and cannot be killed at all.
      <a href="/monsters/compare/">The comparison page</a> sorts every threat by what actually works against it.</p>
  </div>

  <h2>A sensible order</h2>
  <ol>
    <li><strong>First Blood</strong> will happen on its own. Do not spend a run on it.</li>
    <li><strong>Silenced</strong> next, since dolls turn up inside ordinary Hunts and the kill is cheap.</li>
    <li><strong>Freed</strong> once you are laying traps before you need them rather than during a chase.</li>
    <li><strong>Last Performance</strong> last, on a Shift 9 or later night where the email gave you warning and you went
      in stocked.</li>
  </ol>
  <p>Every one of these is tickable in the <a href="/tools/completion-tracker/">completion tracker</a>, alongside the
    endings and the story milestones.</p>

  <h2>Sources on this site</h2>
  <ul>
    <li><a href="/achievements/">All 10 achievements</a> &mdash; the full list, the curve, and the 13 August rate readings.</li>
    <li><a href="/monsters/shrieking-doll/">Shrieking Doll</a>, <a href="/monsters/demented/">Demented</a> and <a href="/monsters/marionette/">Marionette</a> &mdash; the mechanics each kill depends on.</li>
    <li><a href="/monsters/entity/">The Entity</a> and <a href="/guide/survival/">the survival guide</a> &mdash; what else is in the room while you are collecting these.</li>
    <li><a href="/guide/doppelgangers/">Identifying doppelgangers</a> &mdash; the counter work that decides how often you are in a Hunt at all.</li>
  </ul>

  <div class="grid two">
    <a class="card" href="/achievements/hunt-and-arsenal/"><b>The other three</b><span>Still Breathing, Relentless and the arsenal achievement.</span></a>
    <a class="card danger" href="/monsters/compare/"><b>Compare all threats</b><span>Which ones can be killed, and which ones cannot.</span></a>
  </div>
""",
},

# ─────────────────────────────────── /achievements/hunt-and-arsenal/
{
 "path": "achievements/hunt-and-arsenal",
 "active": "/achievements/",
 "title": "Hunt and Arsenal Achievements in Shift At Midnight",
 "og_short": "Hunt &amp; arsenal achievements",
 "desc": ("Still Breathing, Relentless and Locked And Loaded are decided by the Hunt: one arrives on its "
          "own, one is a 30-second clock, one is a budget."),
 "trail": A + [(None, "Hunt &amp; arsenal")],
 "h1": "The Hunt and arsenal achievements",
 "lede": ("Three achievements sit on the wrong side of a night you caused: surviving a Hunt, ending one inside "
          "half a minute, and owning every melee weapon when it starts. The first is near-universal, the other "
          "two are where the completion curve falls off a cliff."),
 "updated": UPD,
 "body": f"""
  <div class="tags">
    <span class="tag">3 of 10 achievements</span>
    <span class="tag green">None are hidden</span>
    <span class="tag amber">{_ACH['Still Breathing']}% down to {_ACH['Locked And Loaded']}%</span>
  </div>

  <table class="facts">
    <tr><th>Still Breathing</th><td>Survive your first Hunt &mdash; {_ACH['Still Breathing']}% (13 August reading: 93.8%)</td></tr>
    <tr><th>Relentless</th><td>Finish a Hunt within 30 seconds &mdash; {_ACH['Relentless']}% (45.4%)</td></tr>
    <tr><th>Locked And Loaded</th><td>Purchase all melee weapons and fill out the weapons arsenal &mdash; {_ACH['Locked And Loaded']}% (23.5%)</td></tr>
  </table>

{RATE_NOTE}

  <h2>A Hunt is something you caused</h2>

  <p>All three of these depend on a mechanic that is not random. Let a doppelganger complete its purchase and walk out
    and it returns <strong>that same shift</strong> in its real form to hunt you &mdash; that is
    <a href="/monsters/entity/">the Entity</a>, and it is the bill for a decision made minutes earlier at the counter.
    The exception is a Blood Moon shift, where blood rain falls and the Hunt happens regardless of how clean your
    verification was.</p>

  <p>Which means the fastest route to all three achievements runs through
    <a href="/guide/doppelgangers/">the identification guide</a> in both directions: it tells you how to stop causing
    Hunts, and it tells you exactly which mistake to make on purpose when you want one.</p>

  <h2>Still Breathing &mdash; {_ACH['Still Breathing']}%, and you already have it</h2>

  <p>Surviving a single Hunt is held by nearly everyone who plays, and the reason is in the timing: the Hunt comes at the
    end of the shift rather than the instant the doppelganger leaves, so you usually know it is coming and have a window
    to spend money before it does. Ammunition, a second weapon, wooden boards on doors and windows &mdash; barricades slow
    the Entity down, and putting them up beforehand is not the same job as hammering them while something is already
    listening for you.</p>

  <p>The one instinct to correct is noise. The Entity is <strong>blind</strong> and tracks sound, including proximity voice
    chat, so a teammate narrating its position over voice is mechanically bait. See <a href="/multiplayer/">multiplayer and
    co-op</a> for how that reshapes a three-player night.</p>

  <h2>Relentless &mdash; the only pure skill check in the game</h2>

  <p>Ending a Hunt inside 30 seconds is the one achievement on the list that no amount of patience substitutes for, and the
    drop from {_ACH['Freed']}% on <em>Freed</em> to {_ACH['Relentless']}% here is where casual play stops. Everything above
    that line happens if you keep playing; everything below it you have to go looking for.</p>

  <p>What the clock actually demands is that the preparation is already done. A weapon bought and equipped before the night
    turns, a known route through the store, and a decision made in advance about where you intend to meet the thing. Half a
    minute is not enough time to shop. Our <a href="/achievements/">achievements page</a> suggests going for it on an early
    shift against a threat you know you can kill quickly &mdash; a <a href="/monsters/shrieking-doll/">Shrieking Doll</a>
    is a reasonable target since it comes to you.</p>

  <div class="term warn">
    <div class="term-h">Nights not to attempt it on</div>
    <p>Not a <a href="/monsters/marionette/">Marionette</a> night, where the encounter is decided by a music box in another
      room rather than by damage. Never Shift 13 &mdash; <a href="/monsters/the-dentist/">the Dentist</a> is immune to your
      weapons, traps do not stop him, and there is no version of that night that ends in 30 seconds.</p>
  </div>

  <h2>Locked And Loaded &mdash; a budget, not a boss</h2>

  <p>The requirement is specific: purchase every melee weapon and fill out the weapons arsenal. At
    {_ACH['Locked And Loaded']}% it is the rarest achievement in the game that is not an ending, and it is rare for a
    reason that has nothing to do with skill. Restocking pays tonight and keeps the quota healthy; the arsenal pays on a
    night that may never come. Under pressure, people buy the immediate thing, every shift, forever.</p>

  <p>The fix is a decision rather than a technique: make a fixed slice of each shift's takings untouchable, from early on,
    instead of planning to chase the arsenal later. Two details narrow the target usefully &mdash; firearms sit
    <em>outside</em> this achievement, and the 29 July 2026 patch added a second purchasable gun alongside the launch one,
    so neither of them counts toward it. The full breakdown is on
    <a href="/guide/survival/#weapons">the weapons arsenal section</a>.</p>

  <p>What we will not give you is a weapon list, prices or a tier ranking. There is no published list of the melee weapons
    or what they cost, and the confident numbers circulating for this game are unsourced, so there is nothing here to
    budget against precisely. Bank a slice and buy what appears.</p>

  <h2>Do not stack this on an ending run</h2>

  <p>The arsenal and the <a href="/endings/true-ending/">True Ending</a> compete for exactly the same money, and the True
    Ending's $250 check happens at the end of Shift 13. Chasing both on one run is the classic way to finish with neither.
    Take the arsenal on a run where the ending does not matter &mdash; a <a href="/endings/grave-decision/">Grave Decision</a>
    pass asks nothing financial of you, which makes it the natural place to spend freely.</p>

  <h2>Order of attack</h2>
  <ol>
    <li><strong>Still Breathing</strong> arrives on its own. Nothing to plan.</li>
    <li><strong>Locked And Loaded</strong> next, banked across many shifts in the background while you learn the store.</li>
    <li><strong>Relentless</strong> last, once the arsenal is stocked and you know the layout well enough to close distance
      instead of circling.</li>
  </ol>
  <p>All three are tick boxes in the <a href="/tools/completion-tracker/">completion tracker</a>, along with the four
    <a href="/achievements/monster-kills/">kill achievements</a> and the three endings.</p>

  <h2>Sources on this site</h2>
  <ul>
    <li><a href="/achievements/">All 10 achievements</a> &mdash; the full list, the curve and the 13 August rate readings.</li>
    <li><a href="/monsters/entity/">The Entity</a> &mdash; how a Hunt starts, Blood Moon shifts, and why sound is the mechanic.</li>
    <li><a href="/guide/survival/">Traps, barricades and hiding</a> &mdash; sound discipline and the weapons arsenal.</li>
    <li><a href="/updates/">Patch notes</a> &mdash; the second firearm and the removed patience meter, both from 29 July 2026.</li>
  </ul>

  <div class="grid two">
    <a class="card" href="/achievements/monster-kills/"><b>The four kill achievements</b><span>First Blood, Silenced, Freed and Last Performance.</span></a>
    <a class="card" href="/monsters/entity/"><b>The Entity</b><span>The threat all three of these achievements are measured against.</span></a>
  </div>
""",
},
]

if __name__ == "__main__":
    from _build import build
    build(PAGES)

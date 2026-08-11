/* Adsterra 装载器 —— shiftatmidnightwiki.site
 * ============================================================
 * 本文件【只有 Native Banner】。Banner / Social Bar / Popunder 的
 * key 和代码分支已在 2026-08-10 全部删除 —— 不是关掉,是删掉。
 * 理由见下面的实测记录:留着开关就有被误翻开的一天,而后台没有任何
 * 单元级停用功能(publisher 面板无控件,Publisher API 只支持 GET),
 * 所以代码是唯一能保证「只跑 Native Banner」的地方。
 *
 * 要恢复其他格式,必须回 Adsterra 后台重新 GET CODE 拿 key ——
 * 这道摩擦是故意的。
 *
 * ── 实测记录(真机 + 移动网络,不挂代理)──────────────────
 *
 * 2026-07-31
 *   仅 Native Banner(Popunder / Social Bar 连单元都没建;
 *   站点级与单元级 Adult ads 均关闭;全站仅 1 个广告单元)
 *   → 手机打开本站【被强制跳转】,页面无法浏览。
 *   停用 Native Banner,改 Social Bar + Banner 300x250
 *   → 【仍然打开即跳转】。
 *   当时结论:跳转与格式无关,是零流量新站 + 分类 Other 的库存质量问题。
 *
 * 2026-08-10  ← 这次做了对照组,结论被推翻
 *   全部关闭            → 【不跳转】   ← 对照组,证明跳转确实来自 Adsterra
 *   Banner 300x250 单开 → 【强制跳转】
 *   Native Banner 单开  → 【不跳转】
 *   → 十天里 Adsterra 的需求侧填充变了。格式之间确实有差别。
 *
 * ⚠️ 所以:**任何结论都有保质期。** 2026-07-31 那条「Native Banner 永久
 *    置 false,不要再打开」差点让我们错过唯一能用的格式。每次改动之后
 *    都要重新真机实测,不要拿旧记录当依据。
 *
 * ⚠️ 机房 IP 会被广告网络拒投(403),在服务器上 curl 或挂代理浏览器
 *    **测不出真实行为**。必须用真实手机 + 移动网络。
 *
 * ⛔ 永远不接 Popunder:Google 2017 年起的明文红线,接了 AdSense 就别想过。
 * ============================================================ */

/* ══ 总闸 ══
 * 出现强制跳转、或者要提交 AdSense 审核之前,把它改成 true 就够了。
 * 一行 Adsterra 代码都不会执行,也不会发出任何请求。 */
var KILL_ALL = false;

/* Native Banner —— 单元 30483620(NativeBanner_1)。
 * 整段取自后台 GET CODE,逐字节核对。 */
var NATIVE_SRC = "https://pl30584119.effectivecpmnetwork.com/f7bf84b6fd5f9bcf83b18332a482d287/invoke.js";
var NATIVE_ID  = "container-f7bf84b6fd5f9bcf83b18332a482d287";

(function () {
  "use strict";

  if (KILL_ALL) { return; }
  if (!NATIVE_SRC || !NATIVE_ID) { return; }

  // 页面模板里只有 .ad-banner 这个占位(历史遗留,构建脚本还在发它),
  // 没有 .ad-native。找不到就地建一个宿主 —— 否则 querySelector 拿到 null
  // 会静默跳过,实测时会得出「不跳转」的【假阴性】。这个坑踩过一次。
  var host = document.querySelector(".ad-native");
  if (!host) {
    var anchor = document.querySelector(".ad-banner");
    if (!anchor) { return; }
    host = document.createElement("aside");
    host.className = "ad-native";
    host.setAttribute("aria-label", "Advertisement");
    anchor.parentNode.insertBefore(host, anchor);
  }

  var box = document.createElement("div");
  box.id = NATIVE_ID;
  host.appendChild(box);
  host.hidden = false;

  var s = document.createElement("script");
  s.src = NATIVE_SRC;
  s.async = true;
  s.setAttribute("data-cfasync", "false");
  document.body.appendChild(s);
})();

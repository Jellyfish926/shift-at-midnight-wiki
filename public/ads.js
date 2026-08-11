/* Adsterra 广告装载器 —— 按格式分开的开关
 * ============================================================
 * 每种格式一个独立开关。出问题时能精确定位是哪一种,
 * 而不是"全部关掉"再靠猜。
 *
 * 【2026-07-31 事故记录 —— 不要重蹈】
 * 曾只启用 Native Banner(内容区最温和的格式;Popunder 和 Social Bar 连单元都没建;
 * 站点级与单元级 Adult ads 均已关闭;全站仅 1 个广告单元),
 * 结果用户用手机打开本站**被强制跳转到其他网站,页面无法浏览**。
 * 排查:页面本身干净(外部脚本只有 adsbygoogle 验证码 + gtag,
 * location.href/replace/window.open/document.write/eval/atob 全站 0 命中),
 * 跳转来自 Adsterra invoke.js 投放出来的广告内容;
 * 后台站点级、单元级、账户级 Settings **都没有任何控制广告质量的选项**。
 * 结论:不是配置错误,是「零流量新站 + Other 分类」的库存质量问题——
 * 需求侧只有跳转/popunder 类广告主愿意填,且出价最高。
 * → USE_NATIVE_BANNER 永久置 false,不要再打开。
 *
 * ⚠️ 上线任何格式后,必须用**真实手机 + 移动网络(不挂代理)**实测一遍再收工。
 *    机房 IP 会被广告网络拒绝投放(返回 403),在服务器上 curl 或用代理浏览器
 *    **测不出真实行为**——上次就是栽在这一步。
 * ============================================================ */

/* ══ 总闸 ══════════════════════════════════════════════════
 * 2026-08-10:用户实测重开 Banner 后【仍然出现强制跳转】。
 * 全部关闭后实测【不再跳转】—— 对照组成立,跳转确认来自 Adsterra。
 * 当前阶段:逐格式复测,只开 Native Banner。
 *
 * KILL_ALL = true 时,下面三个格式开关全部失效,一行 Adsterra 代码都不会执行,
 * 也不会向 highperformanceformat / effectivecpmnetwork 发出任何请求。
 *
 * 恢复投放:把 KILL_ALL 改回 false,再单独打开想要的格式开关。
 * 但在查清跳转来源之前不要恢复。
 * ═════════════════════════════════════════════════════════ */
var KILL_ALL = false;

/* ── 开关:只改这一段(KILL_ALL=true 时以下全部无效)───────────
 * 2026-08-10:按用户决定重新开启变现。只开 Banner;
 * Native Banner 与 Social Bar 维持关闭(见上方事故记录),Popunder 从未建过单元。
 * ───────────────────────────────────────────────────────── */
var USE_SOCIAL_BAR    = false;   // 浮层气泡/通知条,可关闭,不抢走页面控制权
var USE_NATIVE_BANNER = true;  // ⛔ 曾导致强制跳转,不要打开
var USE_BANNER        = false;   // 300x250 静态 iframe 横幅,结构上无法劫持导航
/* ────────────────────────────────────────────────────────── */

var ADSTERRA = {
  // Social Bar —— 单元 30557489(SocialBar_1),2026-07-31 新建,状态 Active。
  // 浮层形态,可关闭,不接管页面导航。src 取自后台 GET CODE,已逐字节核对。
  socialBarSrc: "https://pl30657988.effectivecpmnetwork.com/e8/d2/20/e8d220430d38a9f7a87d671e7a9b44ac.js",

  // Native Banner —— 单元 30483620。保留仅为存档,USE_NATIVE_BANNER 已永久关闭。
  nativeBannerSrc: "https://pl30584119.effectivecpmnetwork.com/f7bf84b6fd5f9bcf83b18332a482d287/invoke.js",
  nativeBannerId:  "container-f7bf84b6fd5f9bcf83b18332a482d287",

  // Banner —— 单元 30557643(300x250_1),2026-07-31 新建,状态 Active。
  // 选 300x250:标准尺寸里收益最好,且 300px 在 375 手机上不溢出(内容区窄屏 339px)。
  // 728x90 会撑破手机,未选。
  bannerKey:    "a4139a1920b5914fb2de99a2efe30a76",
  bannerWidth:  300,
  bannerHeight: 250
};

(function () {
  "use strict";

  if (KILL_ALL) { return; }   // 总闸:什么都不做

  function inject(src) {
    var s = document.createElement("script");
    s.src = src;
    s.async = true;
    s.setAttribute("data-cfasync", "false");
    document.body.appendChild(s);
  }

  if (USE_SOCIAL_BAR && ADSTERRA.socialBarSrc) {
    inject(ADSTERRA.socialBarSrc);
  }

  if (USE_NATIVE_BANNER && ADSTERRA.nativeBannerSrc && ADSTERRA.nativeBannerId) {
    // 页面模板里只有 .ad-banner,没有 .ad-native。
    // 原来这里 querySelector 拿到 null 就静默跳过 —— 开关打开也不会加载任何东西,
    // 实测时会得出「不跳转」的【假阴性】。所以找不到就地建一个宿主。
    var host = document.querySelector(".ad-native");
    if (!host) {
      var anchor = document.querySelector(".ad-banner");
      if (anchor) {
        host = document.createElement("aside");
        host.className = "ad-native";
        host.setAttribute("aria-label", "Advertisement");
        anchor.parentNode.insertBefore(host, anchor);
      }
    }
    if (host) {
      var box = document.createElement("div");
      box.id = ADSTERRA.nativeBannerId;
      host.appendChild(box);
      host.hidden = false;
      inject(ADSTERRA.nativeBannerSrc);
    }
  }

  if (USE_BANNER && ADSTERRA.bannerKey) {
    var slot = document.querySelector(".ad-banner");
    if (slot) {
      window.atOptions = {
        key: ADSTERRA.bannerKey,
        format: "iframe",
        height: ADSTERRA.bannerHeight,
        width: ADSTERRA.bannerWidth,
        params: {}
      };
      slot.hidden = false;
      inject("https://www.highperformanceformat.com/" + ADSTERRA.bannerKey + "/invoke.js");
    }
  }
})();

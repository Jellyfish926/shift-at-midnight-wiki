/* Adsterra 广告装载器
 * ============================================================
 * ✅ 已投放(2026-07-31 按用户指令开启)
 *
 * 背景:AdSense 站点审核 2026-07-29 提交,截至开启时仍是「正在准备」。
 * 明知审核期挂第三方广告有风险仍然开,是因为 ROI 核算改变了性质——
 * 本站可及点击池仅 17,518/月,6 个月中性预期 1,139 次访问,
 * 而 AdSense 起付线 $100 需要约 71,400 次访问,差 63 倍,
 * 也就是说走 AdSense 这条路这个站一分钱也拿不到。
 * Adsterra 起付线低得多,是唯一可能真正到账的路径。
 *
 * 只投 Native Banner:Popunder 几乎必然导致 AdSense 拒审,
 * Social Bar 是常驻浮层同样有风险。要加格式去后台建单元再填下面的字段。
 *
 * 要关掉:把 ENABLED 改回 false,提交部署即可。
 * ============================================================ */

var ENABLED = false;   // ← 只改这一行

var ADSTERRA = {
  // Native Banner —— 单元 30483620,站点 5943265,状态 Active
  // 呈现为「相关阅读」,是攻略站最自然、对 AdSense 审核最友好的格式
  nativeBannerSrc: "https://pl30584119.effectivecpmnetwork.com/f7bf84b6fd5f9bcf83b18332a482d287/invoke.js",
  nativeBannerId:  "container-f7bf84b6fd5f9bcf83b18332a482d287",

  // 以下两种未创建。Popunder 几乎必然导致 AdSense 拒审;
  // Social Bar 是常驻浮层,同样有风险。需要时去 Adsterra 后台建单元再填。
  socialBarSrc: null,
  bannerKey:    null,
  bannerWidth:  728,
  bannerHeight: 90
};

(function () {
  "use strict";
  if (!ENABLED) return;

  function inject(src) {
    var s = document.createElement("script");
    s.src = src; s.async = true;
    s.setAttribute("data-cfasync", "false");
    document.body.appendChild(s);
  }

  if (ADSTERRA.socialBarSrc) inject(ADSTERRA.socialBarSrc);

  if (ADSTERRA.nativeBannerSrc && ADSTERRA.nativeBannerId) {
    var host = document.querySelector(".ad-native");
    if (host) {
      var box = document.createElement("div");
      box.id = ADSTERRA.nativeBannerId;
      host.appendChild(box);
      host.hidden = false;
      inject(ADSTERRA.nativeBannerSrc);
    }
  }

  if (ADSTERRA.bannerKey) {
    var slot = document.querySelector(".ad-banner");
    if (slot) {
      window.atOptions = {
        key: ADSTERRA.bannerKey, format: "iframe",
        height: ADSTERRA.bannerHeight, width: ADSTERRA.bannerWidth, params: {}
      };
      slot.hidden = false;
      inject("//www.highperformanceformat.com/" + ADSTERRA.bannerKey + "/invoke.js");
    }
  }
})();

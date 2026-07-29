/* Adsterra 广告装载器
 * ============================================================
 * 真实代码已填好。是否投放由下面一个开关控制。
 *
 * ⚠️ 当前 ENABLED = false,原因:
 *    AdSense 站点审核于 2026-07-29 提交,审核员会访问线上页面。
 *    站点当前日流量为 0,此刻投放 Adsterra 收益为 $0,
 *    却可能让 AdSense 审核出问题——而 AdSense 的 RPM 高一个量级,
 *    且 playbook 记着「首站过审 = 全站群加速器」。
 *
 * ✅ 何时打开:AdSense 审核出结果之后。
 *    - 通过 → 用 AdSense,Adsterra 保持关闭(或仅在 AdSense 未填充的位置补)
 *    - 拒审 → 把下面 ENABLED 改成 true,提交部署,Adsterra 立即接管
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

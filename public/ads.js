/* Adsterra 广告装载器 — 全站唯一改动点
 * ============================================================
 * 拿到 Adsterra 后台的代码后,只改这个文件,30 个页面全部生效。
 * 每页已经通过 <script src="/ads.js" defer> 引入,并预置了容器 div。
 *
 * 前置:先在 Adsterra 后台 Websites → Add Website 添加
 *       shiftatmidnightwiki.site 并等待审核通过,才能创建版位。
 *
 * 用法:把下面 SLOTS 里的 null 换成后台给你的对应值,保存,重新部署。
 * 没填的版位会自动跳过,不会报错、不会留空白框。
 * ============================================================ */

var ADSTERRA = {
  // ① Social Bar —— 全站浮层,不占版面,移动端 CTR 最高。
  //    后台 Native/Social Bar 版位会给你一行 <script src="//xxxxx.com/xx/yy/zz/....js">
  //    把那个 src 的值(引号里的整串)填到这里。
  socialBarSrc: null,     // 例:"//pl12345678.example.com/aa/bb/cc/invoke.js"

  // ② Native Banner —— 跟在正文后面,伪装成"相关阅读",对攻略站最自然。
  //    后台会给 <script async data-cfasync="false" src="//xxx/invoke.js"></script>
  //    加一个 <div id="container-XXXXXXXX"></div>。把 src 和那个 container id 填进来。
  nativeBannerSrc: null,  // 例:"//pl87654321.example.com/dd/ee/ff/invoke.js"
  nativeBannerId:  null,  // 例:"container-a1b2c3d4e5f6"

  // ③ 横幅 —— 侵入性最强,建议**排名稳定后**再开。先留空。
  //    后台给的是带 atOptions 的内联脚本,把其中 key 的值填这里。
  bannerKey:    null,     // 例:"a1b2c3d4e5f67890abcdef1234567890"
  bannerWidth:  728,
  bannerHeight: 90
};

(function () {
  "use strict";

  function inject(src, attrs) {
    var s = document.createElement("script");
    s.src = src;
    s.async = true;
    s.setAttribute("data-cfasync", "false");
    if (attrs) { Object.keys(attrs).forEach(function (k) { s.setAttribute(k, attrs[k]); }); }
    document.body.appendChild(s);
  }

  // ① Social Bar
  if (ADSTERRA.socialBarSrc) {
    inject(ADSTERRA.socialBarSrc);
  }

  // ② Native Banner —— 注入到页面预置的 .ad-native 容器里
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

  // ③ 横幅
  if (ADSTERRA.bannerKey) {
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
      inject("//www.highperformanceformat.com/" + ADSTERRA.bannerKey + "/invoke.js");
    }
  }
})();

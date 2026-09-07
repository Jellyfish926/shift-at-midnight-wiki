#!/usr/bin/env python3
"""抓 Steam 公开成就页(名称 / 描述 / 全球解锁率 / 图标)→ JSON,给站内成就追踪器用。
用法: fetch_achievements.py APPID OUT.json
免 key:数据来自 https://steamcommunity.com/stats/APPID/achievements/ (公开页)。
描述为空 = Steam 本身就没给(隐藏成就),原样留空,不编。
退出码:0 写入成功;2 抓不到或条数为 0(不覆盖旧文件)。"""
import sys, re, json, html, datetime, urllib.request, pathlib

appid, out = sys.argv[1], pathlib.Path(sys.argv[2])
req = urllib.request.Request(f"https://steamcommunity.com/stats/{appid}/achievements/",
                             headers={"User-Agent": "Mozilla/5.0", "Accept-Language": "en-US,en;q=0.9"})
try:
    page = urllib.request.urlopen(req, timeout=40).read().decode("utf-8", "ignore")
except Exception as e:
    print("fetch failed:", e, file=sys.stderr); sys.exit(2)

rows = re.findall(r'<div class="achieveRow\s*">(.*?)<div style="clear: both;">', page, re.S)
items = []
for r in rows:
    name = re.search(r"<h3>(.*?)</h3>", r, re.S)
    desc = re.search(r"<h5>(.*?)</h5>", r, re.S)
    pct = re.search(r'achievePercent">([\d.]+)%', r)
    icon = re.search(r'<img src="([^"]+)"', r)
    if not name or not pct:
        continue
    items.append({
        "name": html.unescape(name.group(1)).strip(),
        "desc": html.unescape(desc.group(1)).strip() if desc else "",
        "pct": float(pct.group(1)),
        "icon": icon.group(1) if icon else None,
    })
total = re.search(r'Total achievements:\s*<span class="wt">(\d+)</span>', page)
if not items:
    print("no achievements parsed — page layout changed?", file=sys.stderr); sys.exit(2)

data = {
    "appid": appid,
    "source": f"https://steamcommunity.com/stats/{appid}/achievements/",
    "captured": datetime.date.today().isoformat(),
    "total": int(total.group(1)) if total else len(items),
    "achievements": sorted(items, key=lambda x: -x["pct"]),
}
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n")
print(f"{appid}: {len(items)}/{data['total']} achievements → {out} ({data['captured']})")

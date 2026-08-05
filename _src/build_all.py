#!/usr/bin/env python3
"""全站唯一构建入口。

以前四个 _content_*.py 各自 build 各自的页 —— 合并需要跨文件(比如 /demo/ 在 kw
里、/review/ 在 guides 里),所以必须先汇总再产出。

顺序不能改:
  汇总 → 合并 → 产出 → 拉齐手写页 → 删被合并页的残留 → 全量改链接 → 重建 sitemap
「删残留」必须在「产出」之后(否则会被重新写出来),
「改链接」必须在「拉齐手写页」之后(否则手写页的旧链接改不到)。
"""
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import _build as B
import _merge as M
import _content_guides, _content_kw, _content_monsters, _content_tools, _content_updates

# 不由 build() 生成、正文手写的页(由 _patch_handwritten.py 拉齐样板)
HANDWRITTEN = ["achievements", "crossplay", "monsters"]


def main() -> int:
    pages = (_content_kw.PAGES + _content_monsters.PAGES + _content_guides.PAGES
             + _content_tools.PAGES + _content_updates.PAGES)
    before = len(pages)

    kept = M.apply_merges(pages)
    print(f"合并: {before} 页 → {len(kept)} 页(另有 {len(HANDWRITTEN) + 1} 个手写页)")

    print("产出:")
    B.build(kept)

    print("拉齐手写页:")
    subprocess.run([sys.executable, "_patch_handwritten.py"],
                   cwd=str(Path(__file__).resolve().parent), check=True)

    gone = M.prune_dropped()
    print(f"删除被合并页残留: {len(gone)} 个 —— {', '.join(gone) if gone else '无'}")

    n = M.rewrite_public_tree()
    print(f"改写站内链接: {n} 个文件命中")

    total = M.write_sitemap([p["path"] for p in kept] + HANDWRITTEN)
    print(f"重建 sitemap: {total} 条 URL")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

# 备份 2026-10-10（A7 回炉加厚三页之前，HEAD 982158a）

- `crossplay.public.index.html`：/crossplay/ 是手写页，源就是 public/crossplay/index.html 本身（由 _patch_handwritten.py 拉齐样板），此文件即源也是产物。
- `platforms.source-snippet.py.txt`：/platforms/ 的源片段（_content_kw.py 的 platforms + 并入的 _content_guides.py game-pass + _merge.py 的 meta）。
- `multiplayer.source-snippet.py.txt`：/multiplayer/ 的源片段（_content_guides.py 的 multiplayer + 并入的 guide/co-op、discord + _merge.py 的 meta）。
- `platforms.public.index.html`、`multiplayer.public.index.html`：改前产物。
- `_content_guides.py.full-copy.txt`、`_content_kw.py.full-copy.txt`：两个源文件改前整份副本（.txt 后缀，避免被当成模块）。

回滚：把对应片段贴回源文件（或 `git checkout 982158a -- <路径>`），再 `cd _src && python3 build_all.py`。

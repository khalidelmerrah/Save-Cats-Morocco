"""Inline vendor/three.min.js into src/feed-or-dont.src.html -> feed-or-dont.html (one offline file)."""
from pathlib import Path

ROOT = Path(__file__).parent
PLACEHOLDER = "/*@@THREE@@*/"

src = (ROOT / "src" / "feed-or-dont.src.html").read_text(encoding="utf-8")
lib = (ROOT / "vendor" / "three.min.js").read_text(encoding="utf-8")

if src.count(PLACEHOLDER) != 1:
    raise SystemExit("build: expected exactly one Three.js placeholder in the source")
if "</script" in lib.lower():
    raise SystemExit("build: library contains '</script' and cannot be inlined safely")

out = ROOT / "feed-or-dont.html"
out.write_text(src.replace(PLACEHOLDER, lib), encoding="utf-8")
print(f"build: wrote {out.name} ({out.stat().st_size // 1024} KB)")

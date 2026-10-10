"""Render assets/top-languages.svg from the source in my repositories.

GitHub's language bar counts an HTML file as HTML even when most of it is an
inline <script>, and it counts vendored data copies too. This script counts
bytes per language itself so the card reflects code I actually wrote:

* inline <script> and <style> blocks inside HTML count as JavaScript and CSS
* base64 data: URIs (embedded fonts and images) are dropped
* vendored, imported and fixture directories are skipped

Usage:
    python scripts/top_languages.py PATH [PATH ...]      # local checkouts
    GH_TOKEN=... python scripts/top_languages.py --clone  # all repos I own
"""

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
import urllib.request
from pathlib import Path

OWNER = "amorphose"
SKIP_REPOS = {"amorphose"}  # this profile repo
SKIP_DIRS = {".git", ".github", "node_modules", "vendor", "third_party",
             "imports", "fixtures", "dist", "build", "__pycache__"}
TOP_N = 6
OUT = Path(__file__).resolve().parent.parent / "assets" / "top-languages.svg"

EXTENSIONS = {
    ".html": "HTML", ".htm": "HTML",
    ".js": "JavaScript", ".mjs": "JavaScript", ".cjs": "JavaScript",
    ".ts": "TypeScript", ".tsx": "TypeScript",
    ".css": "CSS", ".scss": "SCSS",
    ".py": "Python",
    ".bat": "Batchfile", ".cmd": "Batchfile",
    ".sh": "Shell",
    ".rs": "Rust", ".go": "Go", ".java": "Java", ".kt": "Kotlin",
    ".c": "C", ".h": "C", ".cpp": "C++", ".cs": "C#",
    ".swift": "Swift", ".rb": "Ruby", ".php": "PHP", ".lua": "Lua",
    ".sql": "SQL", ".r": "R", ".jl": "Julia", ".ipynb": "Jupyter Notebook",
}

# Linguist's colours, so the card matches the bars on GitHub repo pages.
COLORS = {
    "HTML": "#e34c26", "JavaScript": "#f1e05a", "TypeScript": "#3178c6",
    "CSS": "#663399", "SCSS": "#c6538c", "Python": "#3572A5",
    "Batchfile": "#C1F12E", "Shell": "#89e051", "Rust": "#dea584",
    "Go": "#00ADD8", "Java": "#b07219", "Kotlin": "#A97BFF", "C": "#555555",
    "C++": "#f34b7d", "C#": "#178600", "Swift": "#F05138", "Ruby": "#701516",
    "PHP": "#4F5D95", "Lua": "#000080", "SQL": "#e38c00", "R": "#198CE7",
    "Julia": "#a270ba", "Jupyter Notebook": "#DA5B0B",
}

DATA_URI = re.compile(r"data:[\w/+.-]+;base64,[A-Za-z0-9+/=]+")
SCRIPT = re.compile(r"<script\b[^>]*>(.*?)</script>", re.S | re.I)
STYLE = re.compile(r"<style\b[^>]*>(.*?)</style>", re.S | re.I)


def count_repo(root: Path, totals: dict) -> None:
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for name in filenames:
            path = Path(dirpath, name)
            lang = EXTENSIONS.get(path.suffix.lower())
            if not lang or name.endswith((".min.js", ".min.css")):
                continue
            text = DATA_URI.sub("", path.read_text(encoding="utf-8", errors="ignore"))
            size = len(text.encode())
            if lang == "HTML":
                js = sum(len(m.encode()) for m in SCRIPT.findall(text))
                css = sum(len(m.encode()) for m in STYLE.findall(text))
                totals["JavaScript"] = totals.get("JavaScript", 0) + js
                totals["CSS"] = totals.get("CSS", 0) + css
                size -= js + css
            totals[lang] = totals.get(lang, 0) + size


def owned_repos(token: str) -> list:
    repos, page = [], 1
    while True:
        req = urllib.request.Request(
            f"https://api.github.com/user/repos?affiliation=owner&per_page=100&page={page}",
            headers={"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json"},
        )
        batch = json.load(urllib.request.urlopen(req))
        repos += [r["name"] for r in batch
                  if not r["fork"] and not r["archived"] and r["name"] not in SKIP_REPOS
                  and r["owner"]["login"].lower() == OWNER]
        if len(batch) < 100:
            return repos
        page += 1


def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;")


def render(totals: dict) -> str:
    total = sum(totals.values())
    top = sorted(totals.items(), key=lambda kv: -kv[1])[:TOP_N]
    w, pad, bar_w = 440, 24, 392
    rows = (len(top) + 1) // 2
    h = 94 + rows * 26 + 4

    segs, x = [], pad
    for i, (lang, n) in enumerate(top):
        seg = bar_w * n / total
        segs.append(f'<rect x="{x:.1f}" y="56" width="{seg:.1f}" height="8" '
                    f'fill="{COLORS.get(lang, "#8b8b8b")}" class="seg" '
                    f'style="animation-delay:{0.15 + i * 0.12:.2f}s"/>')
        x += seg

    items = []
    for i, (lang, n) in enumerate(top):
        cx, cy = pad + (i % 2) * 200, 94 + (i // 2) * 26
        items.append(
            f'<g class="item" style="animation-delay:{0.5 + i * 0.1:.1f}s">'
            f'<circle cx="{cx + 5}" cy="{cy - 4}" r="5" fill="{COLORS.get(lang, "#8b8b8b")}"/>'
            f'<text x="{cx + 18}" y="{cy}" class="lang">{esc(lang)}</text>'
            f'<text x="{cx + 176}" y="{cy}" class="pct" text-anchor="end">{100 * n / total:.1f}%</text></g>')

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="Most used languages">
<style>
.title{{font:600 13px 'Segoe UI',Ubuntu,'Helvetica Neue',sans-serif;fill:#c9a84c;letter-spacing:.18em}}
.lang{{font:400 13px 'Segoe UI',Ubuntu,'Helvetica Neue',sans-serif;fill:#d8d4c8}}
.pct{{font:400 12px ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;fill:#8a8574}}
.seg{{transform-box:fill-box;transform-origin:left;transform:scaleX(0);animation:grow .7s ease-out forwards}}
.item{{opacity:0;animation:fade .6s ease-out forwards}}
@keyframes grow{{to{{transform:scaleX(1)}}}}
@keyframes fade{{to{{opacity:1}}}}
@media (prefers-reduced-motion:reduce){{.seg{{animation:none;transform:none}}.item{{animation:none;opacity:1}}}}
</style>
<rect x=".5" y=".5" width="{w - 1}" height="{h - 1}" rx="10" fill="#0d0d10" stroke="#3a3324"/>
<text x="{pad}" y="36" class="title">MOST USED LANGUAGES</text>
<clipPath id="bar"><rect x="{pad}" y="56" width="{bar_w}" height="8" rx="4"/></clipPath>
<rect x="{pad}" y="56" width="{bar_w}" height="8" rx="4" fill="#1d1c19"/>
<g clip-path="url(#bar)">{"".join(segs)}</g>
{"".join(items)}
</svg>
'''


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="*", type=Path)
    ap.add_argument("--clone", action="store_true", help="clone every repo I own using GH_TOKEN")
    args = ap.parse_args()

    totals: dict = {}
    if args.clone:
        token = os.environ.get("GH_TOKEN")
        if not token:
            sys.exit("GH_TOKEN is not set")
        with tempfile.TemporaryDirectory() as tmp:
            for name in owned_repos(token):
                dest = Path(tmp, name)
                subprocess.run(["git", "clone", "-q", "--depth", "1",
                                f"https://x-access-token:{token}@github.com/{OWNER}/{name}", str(dest)],
                               check=True)
                count_repo(dest, totals)
                print(f"counted {name}")
    else:
        for p in args.paths:
            count_repo(p, totals)

    total = sum(totals.values())
    totals = {k: v for k, v in totals.items() if v / total >= 0.005}  # hide slivers under 0.5%
    total = sum(totals.values())
    for lang, n in sorted(totals.items(), key=lambda kv: -kv[1]):
        print(f"{lang:18} {n:>10,}  {100 * n / total:5.1f}%")
    OUT.write_text(render(totals))
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()

"""Rewrite the dwarf-planet watchlist table in README.md from candidates.csv.

The table lives between <!-- watchlist:start --> and <!-- watchlist:end -->.
candidates.csv comes from amorphose/Vera-Rubin-Analytics-Bot, which updates it
daily. "Last change" is the date the tables themselves last changed: the date
already in README.md is kept while the rows stay the same, and replaced with
today's (UTC) date when they differ.

Usage:
    python scripts/watchlist.py PATH/TO/candidates.csv
    GH_TOKEN=... python scripts/watchlist.py --fetch
"""

import argparse
import csv
import io
import os
import re
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

README = Path(__file__).resolve().parent.parent / "README.md"
SOURCE = "https://api.github.com/repos/amorphose/Vera-Rubin-Analytics-Bot/contents/candidates.csv"
STATE_ORDER = {"candidate": 0, "watched": 1}
TIER_ORDER = {"likely": 0, "watched": 1}
LAST_CHANGE = re.compile(r"Last change (\d{1,2} \w{3} \d{4})\.")


def fetch(token: str) -> str:
    req = urllib.request.Request(SOURCE, headers={
        "Authorization": f"Bearer {token}", "Accept": "application/vnd.github.raw+json"})
    return urllib.request.urlopen(req).read().decode()


def num(s: str):
    try:
        return float(s)
    except ValueError:
        return None


def radius(row: dict) -> str:
    for col in ("jpl_diameter_km", "johnston_diameter_km"):
        d = num(row[col])
        if d:
            return f"{d / 2:,.0f}"
    r = num(row["est_radius_km"])
    return f"~{r:,.0f}" if r else "?"


def site(row: dict) -> str:
    who = row["discoverers"]
    if "Rubin" in who:
        return "Rubin Observatory"
    return who.replace("Cerro Tololo-DECam", "DECam, Cerro Tololo")


def status(row: dict) -> str:
    if row["state"] == "candidate":
        return "🟢 candidate"
    return "🟡 likely" if row["tier"] == "likely" else "⚪ watched"


def render(text: str, previous: str = "") -> str:
    rows = [r for r in csv.DictReader(io.StringIO(text)) if r["state"] in STATE_ORDER]
    rows.sort(key=lambda r: (STATE_ORDER[r["state"]], TIER_ORDER.get(r["tier"], 9),
                             num(r["h_mpc"]) or 99))
    head = ("| Object | Status | Radius (km) | H | a (AU) | Found | By |\n"
            "|---|---|--:|--:|--:|---|---|\n")
    line = lambda r: (f"| **{r['designation']}** | {status(r)} | {radius(r)} | {r['h_mpc']} | "
                      f"{num(r['a_au']):.1f} | {r['discovery_date']} | {site(r)} |\n")
    rubin = sum("Rubin" in r["discoverers"] for r in rows)
    shown = [r for r in rows if r["state"] == "candidate" or r["tier"] == "likely"]
    folded = [r for r in rows if r not in shown]
    out = '<div align="center">\n\n' + head + "".join(line(r) for r in shown) + "\n</div>\n"
    if folded:
        out += (f"\n<details><summary>{len(folded)} more on the watchlist</summary>\n\n"
                + '<div align="center">\n\n' + head + "".join(line(r) for r in folded) + "\n</div>\n</details>\n")
    old_tables, _, old_footer = previous.partition("\n<sub>")
    kept = LAST_CHANGE.search(old_footer)
    if kept and out == old_tables:
        updated = datetime.strptime(kept.group(1), "%d %b %Y").date()
    else:
        updated = datetime.now(timezone.utc).date()
    out += (f"\n<sub>{len(rows)} objects tracked, {rubin} of them discovered by Rubin Observatory. "
            f"~ marks a size estimated from brightness (H) at albedo 0.09. "
            f"Last change {updated:%d %b %Y}.</sub>\n")
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("csv", nargs="?", type=Path)
    ap.add_argument("--fetch", action="store_true", help="read candidates.csv from GitHub using GH_TOKEN")
    args = ap.parse_args()
    if args.fetch:
        token = os.environ.get("GH_TOKEN") or sys.exit("GH_TOKEN is not set")
        text = fetch(token)
    elif args.csv:
        text = args.csv.read_text()
    else:
        sys.exit("pass a CSV path or --fetch")

    readme = README.read_text()
    new = re.sub(r"(<!-- watchlist:start -->\n)(.*?)(<!-- watchlist:end -->)",
                 lambda m: m.group(1) + render(text, m.group(2)) + m.group(3), readme, flags=re.S)
    if new == readme and "<!-- watchlist:start -->" not in readme:
        sys.exit("watchlist markers not found in README.md")
    README.write_text(new)
    print("watchlist updated")


if __name__ == "__main__":
    main()

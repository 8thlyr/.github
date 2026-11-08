#!/usr/bin/env python3
"""Regenerate the project list in profile/README.md from the org's public repos.

Lists public, non-archived, non-fork repos (except .github itself), sorted by
stars then last push. Rewrites only the block between the PROJECTS markers.
Needs `gh` on PATH (GH_TOKEN in CI). Exit 0 always; prints whether it changed.
"""

import json
import pathlib
import re
import subprocess
import sys

ORG = "8thlyr"
README = pathlib.Path(__file__).resolve().parent.parent / "profile" / "README.md"
START, END = "<!-- PROJECTS:START -->", "<!-- PROJECTS:END -->"
SKIP = {".github"}


def fetch() -> list[dict]:
    out = subprocess.run(
        [
            "gh",
            "api",
            "--paginate",
            f"orgs/{ORG}/repos?type=public&per_page=100",
            "--jq",
            ".[] | tojson",
        ],
        check=True,
        capture_output=True,
        text=True,
    ).stdout
    repos = [json.loads(line) for line in out.splitlines() if line.strip()]
    return [
        r
        for r in repos
        if not r["private"] and not r["archived"] and not r["fork"] and r["name"] not in SKIP
    ]


def render(repos: list[dict]) -> str:
    if not repos:
        return "_First projects land soon._"
    repos.sort(key=lambda r: r["pushed_at"], reverse=True)
    repos.sort(key=lambda r: r["stargazers_count"], reverse=True)
    rows = ["| Project | What it does | Lang |", "|---|---|---|"]
    for r in repos:
        desc = (r.get("description") or "").replace("|", "\\|").strip() or "—"
        if r.get("is_template"):
            desc += " _(template)_"
        lang = r.get("language") or ""
        rows.append(f"| [**{r['name']}**]({r['html_url']}) | {desc} | {lang} |")
    return "\n".join(rows)


def main() -> int:
    text = README.read_text()
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)
    if not pattern.search(text):
        print("markers missing", file=sys.stderr)
        return 1
    new = pattern.sub(lambda _: f"{START}\n{render(fetch())}\n{END}", text)
    if new == text:
        print("unchanged")
    else:
        README.write_text(new)
        print("updated")
    return 0


if __name__ == "__main__":
    sys.exit(main())

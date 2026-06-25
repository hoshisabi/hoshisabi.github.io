# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "requests",
#   "html2text",
#   "beautifulsoup4",
# ]
# ///
"""
Export dec2rpg.wikidot.com to rpg/dec2rpg/ as markdown files.

Usage:
    uv run scripts/export-dec2rpg.py

Pages are saved to rpg/dec2rpg/<prefix>/<slug>.md for namespaced pages
(e.g. rtg:session-logs -> rpg/dec2rpg/rtg/session-logs.md),
and rpg/dec2rpg/<slug>.md for top-level pages.
"""

import time
import re
from pathlib import Path

import requests
from bs4 import BeautifulSoup
import html2text

BASE_URL = "http://dec2rpg.wikidot.com"
OUT_DIR = Path(__file__).parent.parent / "rpg" / "dec2rpg"
DELAY = 0.75  # seconds between requests, be polite


def get_all_page_slugs() -> list[str]:
    """Crawl system:list-all-pages (paginated) and return all page slugs."""
    slugs = []
    page = 1
    while True:
        url = f"{BASE_URL}/system:list-all-pages/p/{page}"
        print(f"  Fetching page list page {page}: {url}")
        r = requests.get(url, timeout=15)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")

        items = soup.select(".list-pages-item a")
        if not items:
            break

        for a in items:
            href = a.get("href", "").lstrip("/")
            if href:
                slugs.append(href)

        # Check for next page
        next_link = soup.select_one(".pager .target a[href*='/p/']")
        pager_text = soup.select_one(".pager-no")
        if pager_text:
            m = re.search(r"page (\d+) of (\d+)", pager_text.text)
            if m and int(m.group(1)) >= int(m.group(2)):
                break
        else:
            break

        page += 1
        time.sleep(DELAY)

    return slugs


def slug_to_path(slug: str) -> Path:
    """Convert a wiki slug to a local file path."""
    if ":" in slug:
        prefix, name = slug.split(":", 1)
        return OUT_DIR / prefix / f"{name}.md"
    else:
        return OUT_DIR / f"{slug}.md"


def fetch_page_markdown(slug: str) -> str | None:
    """Fetch a wiki page and return its content as markdown, or None on failure."""
    url = f"{BASE_URL}/{slug}"
    try:
        r = requests.get(url, timeout=15)
        r.raise_for_status()
    except requests.RequestException as e:
        print(f"    ERROR fetching {url}: {e}")
        return None

    soup = BeautifulSoup(r.text, "html.parser")

    # Extract the title
    title_el = soup.select_one("#page-title")
    title = title_el.get_text(strip=True) if title_el else slug

    # Extract the main content div
    content_el = soup.select_one("#page-content")
    if not content_el:
        print(f"    WARNING: no #page-content found for {slug}")
        return None

    # Remove any edit/discuss buttons that bleed into content
    for el in content_el.select(".page-rate-widget-box, .rate-box-with-credit-button"):
        el.decompose()

    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = False
    h.body_width = 0  # don't wrap lines
    h.protect_links = True

    body_md = h.handle(str(content_el)).strip()

    # Build front matter + content
    source_url = f"{BASE_URL}/{slug}"
    md = f"""---
title: "{title.replace('"', "'")}"
source: "{source_url}"
---

# {title}

{body_md}
"""
    return md


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    print("Collecting page list...")
    slugs = get_all_page_slugs()
    print(f"Found {len(slugs)} pages.\n")

    # Skip system: pages — they're Wikidot infrastructure, not content
    content_slugs = [s for s in slugs if not s.startswith("system:")]
    skipped = len(slugs) - len(content_slugs)
    if skipped:
        print(f"Skipping {skipped} system: pages.\n")

    errors = []
    for i, slug in enumerate(content_slugs, 1):
        out_path = slug_to_path(slug)
        if out_path.exists():
            print(f"[{i}/{len(content_slugs)}] SKIP (exists): {slug}")
            continue

        print(f"[{i}/{len(content_slugs)}] Fetching: {slug}")
        md = fetch_page_markdown(slug)
        if md is None:
            errors.append(slug)
            continue

        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(md, encoding="utf-8")
        time.sleep(DELAY)

    print("\nDone.")
    if errors:
        print(f"\nFailed ({len(errors)}):")
        for s in errors:
            print(f"  {s}")


if __name__ == "__main__":
    main()

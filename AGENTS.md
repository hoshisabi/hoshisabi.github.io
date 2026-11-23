# hoshisabi.github.io

Jekyll site (GitHub Pages) — player-facing content for Dan's DM campaigns.

## Key files

- `_data/campaigns.yml` — campaign list and stats on the landing page
- `_data/recent_session.yml` — "latest session" teaser on the landing page
- `_data/pando_schedule.yml` — PandoDnD session schedule
- `_adventures/` — published session write-ups (markdown, one file per adventure)

## Active campaigns

- **Icewind Dale** — AL Dungeoncraft, in-person at Pandemonium Games
- **PandoDnD** — AL drop-in table, online (Discord). Community one-shots and DungeonCraft modules; settings change by night.

## DM source notes

Raw prep notes, transcripts, and brainstorming live at `../hoshisabi-dm`.
That's where material comes from before it's shaped for players.

## Before calling a change done

- Build the site with `bundle exec jekyll build` and check the rendered
  page, not only the source. Generated output (nav lists, data-driven
  titles) can differ from what the template suggests.
- Run `git status`. New files (images, pages, data) must be added, or
  the live site gets broken links.
- When a file replaces another (for example a `.png` converted to
  `.webp`), search for remaining references and delete the old file if
  none are left.
- Keep unrelated changes in separate commits: one concern per commit.
- Don't invent facts for public pages (totals, dates, attendance). Use
  what's in the repo or ask.
- Match the surrounding code style; don't rewrite working code that the
  task doesn't touch.
- In the final report, list what was built, run, or checked, and what wasn't.

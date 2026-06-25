# dec2rpg migration tasks

Source: http://dec2rpg.wikidot.com/

## Campaigns to surface

Three campaigns worth building out as proper entries alongside the existing site campaigns:

- **Return to Guntsville** (`rtg/`) — D&D 5e (early)
- **Greyhawk Retread** (`gr/`) — D&D 5e
- **Isidec** — merge `isidec.md` + `isidec-reborn.md` + `ir/` session logs into one campaign
  - Multi-system lineage: D&D 3.0 → 3.5 → GURPS → D&D 4e
  - Note the lineage in the index rather than tagging individual sessions

## Archive only (keep in rpg/dec2rpg/, do not surface)

- Dungeon Fantasy — GURPS, retired
- Not D&D / Not Shadowrun — GURPS, never really launched
- Tavaline — no real content
- Greyhawk — no real content
- Tonsasnak — run by Dave, retired, not ours to publish

## House rules

`feats.md`, `spells.md`, `house-rules.md`, `d20/` — cross-campaign D&D 3.x/3.5 material.
Potentially adapt into a general shared house rules reference page.

## Content review

All content needs review before removing the Jekyll exclusion in `_config.yml`.
Players had creative license on the wiki — some pages may need editing before publishing.

## Migration steps (per campaign)

1. Create `rpg/<slug>/campaign.yaml` with name, system, dm, status: retired
2. Create `rpg/<slug>/public/index.md` — pull campaign description prose from wikidot page
3. Move/copy session logs from `rpg/dec2rpg/<prefix>/` into `rpg/<slug>/public/sessions/`
4. Add minimal front matter to each session (title, date from slug)
5. Rewrite internal links (`/rtg:slug` → local relative paths)
6. Remove surfaced content from `rpg/dec2rpg/` or leave as-is (archive copy stays)

## When ready to publish

Remove `rpg/dec2rpg/` from the `exclude:` list in `_config.yml` (or leave it excluded
and only publish the migrated campaign directories).

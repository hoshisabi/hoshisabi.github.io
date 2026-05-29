# hoshisabi.github.io

Source for [hoshisabi.com](https://hoshisabi.com) — Dan Chapman's RPG & Adventure Portal.

## Local development

```powershell
bundle exec jekyll serve --livereload
```

Open `http://localhost:4000`. If gems are missing: `bundle install` first.

## New machine setup

```powershell
git clone https://github.com/hoshisabi/hoshisabi.github.io.git
```

## Repo structure

```
rpg/icewind-dale/
  public/          # public-facing campaign pages (on the site)
  campaign.yaml    # campaign config and image prompt settings
rpg/pandodnd/
  public/
  campaign.yaml
_layouts/          # Jekyll layouts
assets/css/        # site stylesheet
scripts/           # helper scripts
```

## Related repos

- **[hoshisabi-dm](https://github.com/hoshisabi/hoshisabi-dm)** — private DM notes, session prep, and brainstorming. Kept separate from this repo.
- **[scrollcase](https://github.com/hoshisabi/scrollcase)** — toolchain for session processing and artwork generation.

# hoshisabi.github.io

Source for [hoshisabi.com](https://hoshisabi.com) — Dan Chapman's RPG & Adventure Portal.

## Daily operations

Three scripts in `scripts/` cover everything. Run them from anywhere in the repo.

| Script | When |
|---|---|
| `scripts/dm-pull.ps1` | **Start of any session** — pulls site + DM notes |
| `scripts/dm-push.ps1` | After editing DM notes — prompts for message, handles everything |
| `scripts/site-push.ps1` | After editing public site files |

If you changed both: run `dm-push.ps1` first, then `site-push.ps1`.

## Local development

```powershell
bundle exec jekyll serve --livereload
```

Open `http://localhost:4000`. If gems are missing: `bundle install` first.

## New machine setup

```powershell
git clone https://github.com/hoshisabi/hoshisabi.github.io.git
cd hoshisabi.github.io
git submodule update --init        # pulls private DM notes from hoshisabi-dm
```

Run this once so pulls automatically include the DM submodule:

```powershell
git config --global submodule.recurse true
```

## Repo structure

```
rpg/icewind-dale/
  public/          # public-facing campaign pages (on the site)
  dm/              # private DM notes — git submodule → hoshisabi-dm (private repo)
scripts/           # helper scripts for daily push/pull operations
_layouts/          # Jekyll layouts
assets/css/        # site stylesheet
```

## The DM notes submodule

`rpg/icewind-dale/dm/` is a separate private repo. The public repo only stores a pointer
(a commit hash) — no DM content is visible publicly.

If `git status` shows `dm` as modified after pulling, that's the pointer being stale.
Run `scripts/dm-push.ps1` to commit and sync it.

If you see the dm/ directory as empty after cloning, you forgot `git submodule update --init`.

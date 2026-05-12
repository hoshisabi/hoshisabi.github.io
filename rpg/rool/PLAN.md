# Rool Campaign Log — Transcription Plan

## Goal
Transcribe all session note PDFs (Rocketbook handwritten scans) into readable markdown,
linked from `index.md`. The campaign has a clear ending. Get it documented before details fade.

## Workflow (per session)

1. Claude reads the PDF directly (handles Rocketbook handwriting well)
2. Optionally paste the Rocketbook OCR text if available — helps reconcile ambiguous words
3. Claude produces a clean transcription; confirm proper nouns / WBtW names
4. Save as `session_notes/session_NN_YYYY-MM-DD.md`
5. Update the `[transcription]` link in `index.md`
6. Commit

**Tip:** Export Rocketbook transcriptions from Google Docs in bulk (File → Download → Plain text)
before starting a session — paste the raw OCR alongside the PDF read for best results.

## Session Inventory

| # | Date | PDF in repo | Transcription |
|---|------|-------------|---------------|
| 00 | 2022-08-25 | ✓ | todo |
| 01 | 2022-09-01 | ✓ | todo |
| 02 | 2022-09-08 | ✓ | todo |
| 03 | 2022-09-15 | ✓ | todo |
| 04 | 2022-09-22 | ✓ | todo |
| 05 | 2022-09-29 | ✓ | todo |
| 06 | 2022-10-06 | ✓ | todo |
| 07 | 2022-10-20 | ✓ | todo |
| 08 | 2022-11-03 | ✓ | todo |
| 09 | 2022-11-10 | ✓ | todo |
| 10 | 2022-11-17 | ✓ | todo |
| 11 | 2022-12-01 | ✓ | todo |
| 12 | 2022-12-15 | MISSING | — |
| 13 | 2022-12-22 | MISSING | — |
| 14 | 2022-12-29 | MISSING | — |
| 15 | 2023-01-05 | ✓ | todo |
| 16 | 2023-02-09 | ✓ | todo |
| 17 | 2023-02-16 | MISSING (index.md has wrong link — points to session 16) | — |
| 18 | 2023-02-23 | ✓ | todo |
| 19 | 2023-03-02 | ✓ | todo |
| 20 | 2023-03-09 | ✓ | todo |
| 21 | 2023-03-16 | ✓ | todo |
| 22 | 2023-03-23 | ✓ | todo |
| 23 | 2023-03-30 | ✓ | todo |
| 24 | 2023-04-13 | ✓ | todo |
| 25 | 2023-04-20 | ✓ | todo |
| 26 | 2023-04-27 | MISSING | — |
| 27 | 2023-05-04 | ✓ | todo |
| 28 | 2023-05-11 | ✓ | todo |
| 29 | 2023-05-18 | ✓ | todo |
| 30 | 2023-05-25 | ✓ (copied from Drive) | todo |
| 31 | 2023-06-08 | ✓ (copied from Drive) | todo — note: two versions existed in Drive (`__ 6-8-23` and `2023-06-08`); larger used |
| 32 | 2023-06-15 | ✓ (copied from Drive) | todo — note: two versions existed in Drive; larger used |
| 33 | 2023-06-30 | ✓ (copied from Drive) | todo |
| 34 | 2023-07-13 | ✓ (copied from Drive) | todo — source filename had typo: `7-183-23` |
| 35 | 2023-07-27 | ✓ (copied from Drive) | todo |
| 36 | 2023-08-03 | ✓ (copied from Drive) | todo |
| 37 | 2023-08-10 | ✓ (copied from Drive) | todo |
| 38 | 2023-08-14 | ✓ (JPG, 2pp, copied from FridayGame) | todo |
| 39 | 2023-08-17 | ✓ (JPG, 2pp, copied from FridayGame) | todo — possibly the campaign finale; verify |

Session numbers 30–37 are estimated sequentially. Verify against memory if any sessions
between May 18 and the end were unrecorded.

## Known issues in index.md
- Session 17 link is broken (points to Session 16 PDF) — likely no notes exist for it
- "placeholder information" blurb at top of index.md — flesh out after log is complete

## Notes
- The 6-8-23 PDF had two pages: WBtW session + an unrelated Icewind Dale Session 0 (6/1/23)
  on the reverse. That second page can be ignored for this log.
- WBtW-specific proper nouns to watch for: Korreds, Gleam (Gloom's sister), Hurly,
  Motherhorn, Endelyn Moongrave, Prismeer, Hither/Thither/Yon, Witchlight Carnival
- Kate (DM: Kate Hoff) added DMs Guild content and original story — names won't always
  match the published module. Use context + player memory to resolve.
- Rocketbook has likely been erased — the PDFs in this repo are the canonical source.
- **Don't trust filenames for dates or session numbers** — read the page content to
  determine what session it actually is. Session numbers in filenames are best guesses.
- **Source file cleanup**: once a transcription is confident and reviewed, delete both
  the source file from Google Drive (`H:\My Drive\D&D Notes\`) and the PDF/JPG from the
  repo. The transcription markdown is the permanent record.
- **Format preference**: JPGs are ~40% smaller and read identically. Existing PDFs aren't
  worth converting (small total size, all destined for deletion anyway). Prefer JPG for any
  future scans added to the repo.

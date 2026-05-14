---
campaign_url: /rpg/pandodnd/public/
campaign_name: PandoDnD Pub Crawl
layout: default
title: Pandemonium Pub Crawl
dm: Daniel E. Chapman II
location: online (Discord)
status: Active
---

# Pandemonium Pub Crawl

*Adventurers League DungeonCraft — Planescape Season. Online, run on Discord.*

---

A rotating cast of adventurers wanders the planes, stumbling into trouble one pub at a time. Each session is a self-contained adventure — drop in, play a Tier 2 character, and find out what Pandemonium, Sigil, and the rest of the multiverse have in store. Memory loss, ancient conspiracies, and extremely questionable tavern choices are recurring themes.

Adventures are drawn from the DC (DungeonCraft) catalog.

---

## Sessions

{% assign sessions = site.pages | where_exp: "p", "p.path contains 'pandemonium/public/sessions'" | sort: "title" %}
{% for session in sessions %}
- [{{ session.title }} — {{ session.session_title }}]({{ session.url }}): {{ session.description }}
{% endfor %}

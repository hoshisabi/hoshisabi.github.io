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

Adventures are drawn from the DC (DungeonCraft) catalog unless otherwise noted.

---

## Sessions

{% assign sessions = site.pages | where_exp: "p", "p.path contains 'pandodnd/public/sessions'" | sort: "title" %}
{% for session in sessions %}
- [{{ session.title }} — {{ session.session_title }}]({{ session.url }}): {{ session.description }}
{% endfor %}

## Characters we've catalogued

Party composition changes weekly; pages here capture **appearances observed** during published sessions—not a canonical roster.

{% assign appearances = site.pages | where_exp: "p", "p.path contains 'pandodnd/public/characters'" | sort: "title" %}
<div class="npc-grid">
{% for char in appearances %}
<a href="{{ char.url }}" class="npc-card">
  {% if char.image %}<img src="{{ char.image }}" alt="{{ char.title }}">{% else %}<div class="npc-no-image"></div>{% endif %}
  <span>{{ char.title }}</span>
  {% if char.player %}<span class="card-player">{{ char.player }}</span>{% endif %}
</a>
{% endfor %}
</div>

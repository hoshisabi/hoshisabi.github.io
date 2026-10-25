---
campaign_url: /rpg/pandodnd/public/
campaign_name: PandoDnD
layout: default
title: PandoDnD
dm: Daniel E. Chapman II
location: online (Discord)
status: Active
---

# PandoDnD

*Adventurers League drop-in table. Online, run on Discord.*

---

Wednesday nights at PandoDnD. Bring a legal AL character, drop in, play. Each session is its own adventure — no shared plot to catch up on, no homework from last week. Settings, tiers, and authors change from night to night. We run a wide variety of adventures, often with a focus on community written content.

We've been running this table online since 2020 — nearly every week, fifty-plus sessions a year. Recaps on this page start with the **Planescape Pub Crawl** (PS-DC-PUB), a planar tavern crawl through Sigil and the Great Wheel. That series is done; from here, we're widening what we run.

Sign up on [Warhorn](https://warhorn.net/events/pandodnd/schedule).

---

## Sessions

{% assign sessions = site.pages | where_exp: "p", "p.path contains 'pandodnd/public/sessions'" | sort: "path" %}
{% assign sessions_count = sessions | size %}
{% assign sessions_reversed = sessions | reverse %}

{% for session in sessions_reversed limit:3 %}
- [{{ session.title }} — {{ session.session_title }}]({{ session.url }}){% if session.adventure %} ({{ session.adventure }}){% endif %}: {{ session.description }}
{% endfor %}

{% if sessions_count > 3 %}
<details class="session-list-toggle">
<summary>{{ sessions_count | minus: 3 }} older sessions</summary>
<ul>
{% for session in sessions_reversed offset:3 %}
<li><a href="{{ session.url }}">{{ session.title }} — {{ session.session_title }}</a>{% if session.adventure %} ({{ session.adventure }}){% endif %}: {{ session.description }}</li>
{% endfor %}
</ul>
</details>
{% endif %}

{% assign characters = site.pages | where: "layout", "character" | where: "campaign_url", page.campaign_url %}
{% assign players = site.pages | where: "layout", "player" | where: "campaign_url", page.campaign_url | sort_natural: "title" %}

## Players

<div class="npc-grid">
{% for player in players %}
{% assign player_chars = characters | where: "player_slug", player.player_slug %}
{% assign latest = player_chars | sort: "last_seen" | last %}
{% assign others = player_chars.size | minus: 1 %}
<a href="{{ player.url }}" class="npc-card">
  {% if latest.image %}<img src="{{ latest.image }}" alt="{{ latest.title }}">{% else %}<div class="npc-no-image"></div>{% endif %}
  <span>{{ player.title }}</span>
  {% if latest %}<span class="card-player">{{ latest.title }}{% if others > 0 %}<br>(+{{ others }} other{% if others != 1 %}s{% endif %}){% endif %}</span>{% endif %}
</a>
{% endfor %}
</div>

[View all {{ characters.size }} characters →](all-characters)

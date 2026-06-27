---
campaign_url: /rpg/icewind-dale/public/
campaign_name: Icewind Dale
layout: default
title: Icewind Dale Campaign
dm: Daniel E. Chapman II
location: in-person
status: Active
---

# Icewind Dale

*A D&D 5e Adventurers League campaign, run at Pandemonium Games.*

---

Icewind Dale does not care whether you survive. The cold is not malicious — it is simply indifferent, and indifferent things are harder to reason with than hostile ones. The blizzards come without warning and last without mercy. The snow hides rivers, the ice hides drops, and the things that live out here have adapted to conditions that kill travelers in hours. The party has survived three sessions of this. Barely, and not without cost.

What they have found, besides frostbite and exhaustion, is the Coldpeak — an orc tribe who have carved out a life in these mountains by being harder than what the mountains throw at them. The tribe has its own problems: a shaman gone missing, hunters disappearing, and something large and deliberate leaving messages in goat entrails at the camp entrance. The party arrived as outsiders. They are still outsiders. But they have fought beside Kaarsk and earned something that might, eventually, become trust.

The blizzard outside the camp reads: *Soon.*

---

## Sessions

{% assign sessions = site.pages | where_exp: "p", "p.path contains 'icewind-dale/public/sessions'" | sort: "path" %}
{% assign sessions_count = sessions | size %}
{% assign sessions_reversed = sessions | reverse %}

{% for session in sessions_reversed limit:3 %}
- [{{ session.title }} — {{ session.session_title }}]({{ session.url }}): {{ session.description }}
{% endfor %}

{% if sessions_count > 3 %}
<details class="session-list-toggle">
<summary>All sessions ({{ sessions_count }} total)</summary>
<ul>
{% for session in sessions %}
<li><a href="{{ session.url }}">{{ session.title }} — {{ session.session_title }}</a>: {{ session.description }}</li>
{% endfor %}
</ul>
</details>
{% endif %}

## Player Characters

{% assign characters = site.pages | where_exp: "p", "p.path contains 'icewind-dale/public/characters'" | sort: "title" %}
<div class="npc-grid">
{% for char in characters %}
<a href="{{ char.url }}" class="npc-card">
  {% if char.image %}<img src="{{ char.image }}" alt="{{ char.title }}">{% else %}<div class="npc-no-image"></div>{% endif %}
  <span>{{ char.title }}</span>
  {% if char.player %}<span class="card-player">{{ char.player }}</span>{% endif %}
</a>
{% endfor %}
</div>

## Notable NPCs

{% assign npcs = site.pages | where_exp: "p", "p.path contains 'icewind-dale/public/npcs'" | sort: "title" %}
<div class="npc-grid">
{% for npc in npcs %}
<a href="{{ npc.url }}" class="npc-card">
  {% if npc.image %}<img src="{{ npc.image }}" alt="{{ npc.title }}">{% else %}<div class="npc-no-image"></div>{% endif %}
  <span>{{ npc.title }}</span>
</a>
{% endfor %}
</div>

## Locations

{% assign locations = site.pages | where_exp: "p", "p.path contains 'icewind-dale/public/locations'" | sort: "title" %}
<div class="npc-grid">
{% for loc in locations %}
<a href="{{ loc.url }}" class="npc-card">
  {% if loc.image %}<img src="{{ loc.image }}" alt="{{ loc.title }}">{% else %}<div class="npc-no-image"></div>{% endif %}
  <span>{{ loc.title }}</span>
</a>
{% endfor %}
</div>

## Items of Note

{% assign items = site.pages | where_exp: "p", "p.path contains 'icewind-dale/public/items'" | sort: "title" %}
<div class="npc-grid">
{% for item in items %}
<a href="{{ item.url }}" class="npc-card">
  {% if item.image %}<img src="{{ item.image }}" alt="{{ item.title }}">{% else %}<div class="npc-no-image"></div>{% endif %}
  <span>{{ item.title }}</span>
</a>
{% endfor %}
</div>

## Lore

{% assign lore = site.pages | where_exp: "p", "p.path contains 'icewind-dale/public/lore'" | sort: "title" %}
<div class="npc-grid">
{% for entry in lore %}
<a href="{{ entry.url }}" class="npc-card">
  {% if entry.image %}<img src="{{ entry.image }}" alt="{{ entry.title }}">{% else %}<div class="npc-no-image"></div>{% endif %}
  <span>{{ entry.title }}</span>
  {% if entry.category %}<span class="card-player">{{ entry.category }}</span>{% endif %}
</a>
{% endfor %}
</div>

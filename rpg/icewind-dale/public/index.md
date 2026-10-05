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

*A D&D 5e home campaign run at Pandemonium Games. It started in Adventurers League and has been a home game since Session 20.*

**[House Rules](house-rules)**: magic items, leveling, gold, and the camp.

---

Icewind Dale does not care whether you survive. The cold is not malicious — it is simply indifferent, and indifferent things are harder to reason with than hostile ones. The blizzards come without warning and last without mercy. The snow hides rivers, the ice hides drops, and the things that live out here have adapted to conditions that kill travelers in hours.

The party came to the Dale as outsiders and found the Coldpeak, an orc tribe who carved out a life in these mountains by being harder than what the mountains throw at them. Twenty sessions later, the party is responsible for them. Durok's oasis feeds the camp. Something from the northwest keeps sending elementals against it, and the compass rose on their cores is the Arcane Brotherhood's. A giant bird called Rime Talon takes people and doesn't bring them back.

There is also the mountain over there, which has a name now, Arveth, and a guardian, Father Joseph. Twice the world has been rewoven around a deal with her. Joseph remembers what changed and nobody else does. River sometimes meets the versions of himself that were left behind.

Now the party is bringing the Elk home to Coldpeak under a new name, the Tribe of the Weaver, and the mountain is closer than it used to be.

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
<summary>{{ sessions_count | minus: 3 }} older sessions</summary>
<ul>
{% for session in sessions_reversed offset:3 %}
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

## The Camp

{% assign camp = site.pages | where_exp: "p", "p.path contains 'icewind-dale/public/camp/'" | sort: "title" %}
<div class="npc-grid">
{% for entry in camp %}
<a href="{{ entry.url }}" class="npc-card">
  {% if entry.image %}<img src="{{ entry.image }}" alt="{{ entry.title }}">{% else %}<div class="npc-no-image"></div>{% endif %}
  <span>{{ entry.title }}</span>
  {% if entry.status %}<span class="card-player">{{ entry.status }}</span>{% endif %}
</a>
{% endfor %}
</div>

Rules for building and running the camp are on [House Rules](house-rules).

## Notable NPCs

{% assign npcs = site.pages | where_exp: "p", "p.path contains 'icewind-dale/public/npcs'" | sort: "title" %}
<div class="npc-grid">
{% for npc in npcs %}
<a href="{{ npc.url }}" class="npc-card">
  {% if npc.image %}<img src="{{ npc.image }}" alt="{{ npc.title }}">{% else %}<div class="npc-no-image"></div>{% endif %}
  <span>{{ npc.title }}</span>
  {% if npc.association %}<span class="card-player">{{ npc.association }}</span>{% endif %}
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
  {% if loc.association %}<span class="card-player">{{ loc.association }}</span>{% endif %}
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
  {% if item.association %}<span class="card-player">{{ item.association }}</span>{% endif %}
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

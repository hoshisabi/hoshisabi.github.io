---
layout: default
title: Icewind Dale Campaign
---

# Icewind Dale

*A D&D 5e Adventurers League campaign, run at Pandemonium Games.*

---

Icewind Dale does not care whether you survive. The cold is not malicious — it is simply indifferent, and indifferent things are harder to reason with than hostile ones. The blizzards come without warning and last without mercy. The snow hides rivers, the ice hides drops, and the things that live out here have adapted to conditions that kill travelers in hours. The party has survived three sessions of this. Barely, and not without cost.

What they have found, besides frostbite and exhaustion, is the Coldpeak — an orc tribe who have carved out a life in these mountains by being harder than what the mountains throw at them. The tribe has its own problems: a shaman gone missing, hunters disappearing, and something large and deliberate leaving messages in goat entrails at the camp entrance. The party arrived as outsiders. They are still outsiders. But they have fought beside Kaarsk and earned something that might, eventually, become trust.

The blizzard outside the camp reads: *Soon.*

---

## Sessions

{% assign sessions = site.pages | where_exp: "p", "p.path contains 'icewind-dale/public/sessions'" | sort: "title" %}
{% for session in sessions %}
- [{{ session.title }} — {{ session.session_title }}]({{ session.url }}): {{ session.description }}
{% endfor %}

## Player Characters

{% assign characters = site.pages | where_exp: "p", "p.path contains 'icewind-dale/public/characters'" | sort: "title" %}
{% for char in characters %}
- [{{ char.title }}]({{ char.url }})
{% endfor %}

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
{% for loc in locations %}
- [{{ loc.title }}]({{ loc.url }})
{% endfor %}

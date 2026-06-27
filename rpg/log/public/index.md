---
campaign_url: /rpg/log/public/
campaign_name: Legends of Greyhawk
layout: default
title: Legends of Greyhawk Campaign
dm: Bryan
location: in-person
status: Active
---

# Legends of Greyhawk

*A D&D 5e Adventurers League campaign.*

---

The Free City of Greyhawk sits at the center of a world with a long memory. Old temples get repurposed by worse things than their original tenants. River towns operate under law that doesn't answer to any king. Spies go dark in the swamp and no one asks too many questions about why. The work tends to involve finding people who don't want to be found, in places that don't want to be visited, alongside guards who don't want to be bribed — and usually some combination of all three.

The party started in Hommlet, where the trouble was organized enough to have a hierarchy. Now they're in Nolb, where the Pirate Queen keeps the peace by being the most dangerous thing in it. The spy they're looking for hasn't come back from wherever the Queen sent her. The south road is iced over in summer. Something is waiting in the dark at the end of it.

---

## Sessions

{% assign sessions = site.pages | where_exp: "p", "p.path contains 'log/public/sessions'" | sort: "path" %}
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

{% assign characters = site.pages | where_exp: "p", "p.path contains 'log/public/characters'" | sort: "title" %}
<div class="npc-grid">
{% for char in characters %}
<a href="{{ char.url }}" class="npc-card">
  {% if char.image %}<img src="{{ char.image }}" alt="{{ char.title }}">{% else %}<div class="npc-no-image"></div>{% endif %}
  <span>{{ char.title }}</span>
  {% if char.player %}<span class="card-player">{{ char.player }}</span>{% endif %}
</a>
{% endfor %}
</div>

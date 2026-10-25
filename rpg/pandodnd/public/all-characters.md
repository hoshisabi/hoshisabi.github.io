---
campaign_url: /rpg/pandodnd/public/
campaign_name: PandoDnD
layout: default
title: PandoDnD Characters
---

{% include campaign-nav.html %}

# Characters we've catalogued

Party composition changes weekly; pages here capture **appearances observed** during published sessions—not a canonical roster.

{% assign characters = site.pages | where: "layout", "character" | where: "campaign_url", page.campaign_url | sort: "title" %}
<p class="card-player">{{ characters.size }} characters</p>
<div class="npc-grid">
{% for char in characters %}
{% include character-card.html char=char %}
{% endfor %}
</div>

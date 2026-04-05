---
title: My Adventures
---

All of my published adventures are for D&D Adventurers League, available on the DMs Guild.

<!--
  LEARNING NOTE: loops and filters
  ──────────────────────────────────
  site.data.series   → the array from _data/series.yml
  site.adventures    → all documents in _adventures/

  The pattern here is:
    1. Loop through the series list (so we control display order)
    2. For each series, filter the collection to matching adventures
    3. Sort those adventures by their "order" front-matter field
    4. Loop through and render each one

  "where" and "sort" are Liquid array filters.
  "assign" creates a local variable.
-->

{% for series in site.data.series %}
<div class="adventure-series">

## {{ series.title }}

{% assign series_adventures = site.adventures | where: "series", series.id | sort: "order" %}
{% for adventure in series_adventures %}
<div class="adventure-card">
  <div class="adventure-card-inner">
    {% if adventure.image %}
    <a href="{{ adventure.link }}" class="adventure-card-image">
      <img src="{{ adventure.image }}" alt="{{ adventure.title }} cover" loading="lazy">
    </a>
    {% endif %}
    <div class="adventure-card-body">
      <h3><a href="{{ adventure.link }}">{{ adventure.title }}</a></h3>
      <div class="adventure-code">{{ adventure.code }}</div>
      {{ adventure.content }}
      {% unless adventure.bundle %}
      <div class="adventure-meta">
        <span>Tier {{ adventure.tier }}</span>
        <span>Levels {{ adventure.levels }}, APL {{ adventure.apl }}</span>
        <span>{{ adventure.runtime }}</span>
        {% if adventure.dungeoncraft_seed %}<span>DungeonCraft: {{ adventure.dungeoncraft_seed }}</span>{% endif %}
      </div>
      {% endunless %}
    </div>
  </div>
</div>
{% endfor %}

</div>
{% endfor %}

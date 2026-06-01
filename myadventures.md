---
title: My Adventures
layout: default
wide: true
---

<p class="adventures-intro">
  All of my published adventures are written for D&amp;D Adventurers League and available on the DMs Guild. Most run in two to four hours, ship with their own DungeonCraft seed, and are designed to drop straight into your home table.
</p>

{%- comment -%}
  LEARNING NOTE: loops and filters
  ──────────────────────────────────
  site.data.series   → the array from _data/series.yml
  site.adventures    → all documents in _adventures/

  Outer loop walks series in declared order; inner loop renders
  adventures filtered to that series and sorted by `order`.
  We skip empty series so the count stays meaningful.
{%- endcomment -%}

{%- assign visible_series = "" | split: "" -%}
{%- for s in site.data.series -%}
  {%- assign matches = site.adventures | where: "series", s.id -%}
  {%- if matches.size > 0 -%}
    {%- assign visible_series = visible_series | push: s -%}
  {%- endif -%}
{%- endfor -%}
{%- assign series_total = visible_series.size -%}

{% for series in visible_series %}
{% assign series_idx = forloop.index %}
{% assign series_adventures = site.adventures | where: "series", series.id | sort: "order" %}
<section class="adventure-series" id="series-{{ series.id }}">
  <div class="series-head">
    <div>
      <div class="series-num">★ Series {{ series_idx | prepend: "0" | slice: -2, 2 }} / {{ series_total | prepend: "0" | slice: -2, 2 }}{% if series.tagline %} · {{ series.tagline }}{% endif %}</div>
      <h2>{{ series.title }}</h2>
    </div>
    <div class="series-count">{{ series_adventures.size }} adventure{% if series_adventures.size != 1 %}s{% endif %}</div>
  </div>
  {% if series.description %}
  <p class="series-desc">{{ series.description | strip_newlines }}</p>
  {% endif %}
  <div class="adventure-grid">
    {% for adventure in series_adventures %}
    <article class="adventure-card{% if adventure.bundle %} is-bundle{% endif %}">
      <a class="adventure-card-inner" href="{{ adventure.link }}" target="_blank" rel="noopener">
        {% if adventure.image %}
        <div class="adventure-card-image">
          <img src="{{ adventure.image }}" alt="{{ adventure.title }} cover" loading="lazy">
        </div>
        {% endif %}
        <div class="adventure-card-body">
          <div class="adventure-code">{{ adventure.code }}</div>
          <h3>{{ adventure.title }}</h3>
          {% if adventure.coauthors %}
          <div class="adventure-coauthors">With <strong>{{ adventure.coauthors }}</strong></div>
          {% endif %}
          {{ adventure.content }}
          {% if adventure.dungeoncraft_seed %}
          <div class="adventure-seed">
            <span class="seed-lbl">★ Seed</span>
            <span class="seed-val">{{ adventure.dungeoncraft_seed }}</span>
          </div>
          {% endif %}
          {% unless adventure.bundle %}
          {%- if adventure.runtime == "2 hours" -%}{%- assign runtime_class = "hours-2" -%}
          {%- elsif adventure.runtime == "4 hours" -%}{%- assign runtime_class = "hours-4" -%}
          {%- else -%}{%- assign runtime_class = "" -%}{%- endif -%}
          <div class="adventure-meta">
            <span class="meta-pill tier-{{ adventure.tier }}">Tier {{ adventure.tier }}</span>
            <span class="meta-pill">Lvl {{ adventure.levels }} · APL {{ adventure.apl }}</span>
            <span class="meta-pill {{ runtime_class }}">{{ adventure.runtime }}</span>
          </div>
          {% endunless %}
        </div>
        {% if adventure.bundle %}
        <div class="bundle-flag">★ Bundle</div>
        {% endif %}
        <span class="ext-arr" aria-hidden="true">
          <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M7 17l10-10"/><polyline points="8 7 17 7 17 16"/></svg>
        </span>
      </a>
    </article>
    {% endfor %}
  </div>
</section>
{% endfor %}

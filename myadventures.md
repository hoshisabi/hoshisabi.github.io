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

{%- assign tier_list = site.adventures | where_exp: "a", "a.bundle != true" | map: "tier" | compact | uniq | sort -%}

<div class="filter-toolbar" aria-label="Filter adventures">
  <div class="filter-bar" role="group" aria-label="Filter by tier">
    <span class="filter-label">Tier</span>
    <button class="filter-pill" type="button" data-adv-tier="all" aria-pressed="true">All</button>
    {%- for t in tier_list -%}
    <button class="filter-pill" type="button" data-adv-tier="{{ t }}" aria-pressed="false">Tier {{ t }}</button>
    {%- endfor -%}
  </div>
  <div class="filter-bar" role="group" aria-label="Filter by runtime">
    <span class="filter-label">Length</span>
    <button class="filter-pill" type="button" data-adv-runtime="all" aria-pressed="true">All</button>
    <button class="filter-pill" type="button" data-adv-runtime="2" aria-pressed="false">2 hours</button>
    <button class="filter-pill" type="button" data-adv-runtime="4" aria-pressed="false">4 hours</button>
    <button class="filter-pill" type="button" data-adv-runtime="flex" aria-pressed="false">Flexible</button>
  </div>
  <div class="filter-status">
    <span id="adv-filter-count" aria-live="polite"></span>
    <button class="filter-reset" type="button" id="adv-filter-reset" hidden>Reset</button>
  </div>
</div>

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
    {%- assign rt_bucket = "flex" -%}
    {%- if adventure.runtime == "2 hours" -%}{%- assign rt_bucket = "2" -%}
    {%- elsif adventure.runtime == "4 hours" -%}{%- assign rt_bucket = "4" -%}
    {%- endif -%}
    <article class="adventure-card{% if adventure.bundle %} is-bundle{% endif %}" data-tier="{{ adventure.tier }}" data-runtime="{{ rt_bucket }}" data-bundle="{% if adventure.bundle %}true{% else %}false{% endif %}">
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

<p class="filter-empty" id="adv-filter-empty" hidden>No adventures match those filters.</p>

<script>
(function () {
  var tier = 'all';
  var runtime = 'all';
  var tierBtns = document.querySelectorAll('[data-adv-tier]');
  var rtBtns = document.querySelectorAll('[data-adv-runtime]');
  var sections = document.querySelectorAll('.adventure-series');
  var countEl = document.getElementById('adv-filter-count');
  var resetBtn = document.getElementById('adv-filter-reset');
  var emptyEl = document.getElementById('adv-filter-empty');

  function apply() {
    var active = tier !== 'all' || runtime !== 'all';
    var totalShown = 0;
    var totalNonBundle = 0;

    sections.forEach(function (sec) {
      var cards = sec.querySelectorAll('.adventure-card');
      var secShown = 0;
      cards.forEach(function (card) {
        var isBundle = card.dataset.bundle === 'true';
        if (!isBundle) totalNonBundle++;
        var match = !active || (!isBundle
          && (tier === 'all' || card.dataset.tier === tier)
          && (runtime === 'all' || card.dataset.runtime === runtime));
        card.hidden = !match;
        if (match) {
          secShown++;
          if (!isBundle) totalShown++;
        }
      });
      sec.hidden = secShown === 0;
    });

    if (countEl) {
      countEl.textContent = active ? ('Showing ' + totalShown + ' of ' + totalNonBundle + ' adventures') : '';
    }
    if (resetBtn) resetBtn.hidden = !active;
    if (emptyEl) emptyEl.hidden = !active || totalShown > 0;
  }

  tierBtns.forEach(function (btn) {
    btn.addEventListener('click', function () {
      tier = btn.dataset.advTier;
      tierBtns.forEach(function (b) { b.setAttribute('aria-pressed', b === btn ? 'true' : 'false'); });
      apply();
    });
  });

  rtBtns.forEach(function (btn) {
    btn.addEventListener('click', function () {
      runtime = btn.dataset.advRuntime;
      rtBtns.forEach(function (b) { b.setAttribute('aria-pressed', b === btn ? 'true' : 'false'); });
      apply();
    });
  });

  if (resetBtn) {
    resetBtn.addEventListener('click', function () {
      tier = 'all';
      runtime = 'all';
      tierBtns.forEach(function (b) { b.setAttribute('aria-pressed', b.dataset.advTier === 'all' ? 'true' : 'false'); });
      rtBtns.forEach(function (b) { b.setAttribute('aria-pressed', b.dataset.advRuntime === 'all' ? 'true' : 'false'); });
      apply();
    });
  }
})();
</script>

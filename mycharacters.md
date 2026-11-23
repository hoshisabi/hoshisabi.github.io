---
title: Characters
layout: default
wide: true
---

<nav class="campaign-breadcrumb"><a href="{{ '/' | relative_url }}">← Home</a></nav>

{%- assign sorted = site.data.campaigns.playing | sort: "last_updated" | reverse -%}
{%- assign active_count = sorted | where: "status", "active" | size -%}
{%- assign finished_count = sorted | where: "status", "finished" | size -%}
{%- assign retired_count = sorted | where: "status", "retired" | size -%}
<section class="lp-sec">
  <div class="sec-head">
    <div>
      <h2>Characters I <em>play</em></h2>
    </div>
    <span class="sec-aside" id="char-count">{{ sorted.size }} characters · Player</span>
  </div>

  <div class="filter-bar" role="group" aria-label="Filter characters by status">
    <button class="filter-pill" type="button" data-char-filter="all" aria-pressed="true">All <span class="filter-count">{{ sorted.size }}</span></button>
    {%- if active_count > 0 -%}
    <button class="filter-pill" type="button" data-char-filter="active" aria-pressed="false">Active <span class="filter-count">{{ active_count }}</span></button>
    {%- endif -%}
    {%- if finished_count > 0 -%}
    <button class="filter-pill" type="button" data-char-filter="finished" aria-pressed="false">Finished <span class="filter-count">{{ finished_count }}</span></button>
    {%- endif -%}
    {%- if retired_count > 0 -%}
    <button class="filter-pill" type="button" data-char-filter="retired" aria-pressed="false">Retired <span class="filter-count">{{ retired_count }}</span></button>
    {%- endif -%}
  </div>

  <div class="star-grid" id="char-grid">
    {%- for c in sorted -%}
    {%- if c.href -%}
    <a class="star-card is-{{ c.status }}" href="{{ c.href | relative_url }}" data-status="{{ c.status }}">
    {%- elsif c.dnd_beyond -%}
    <a class="star-card is-{{ c.status }}" href="{{ c.dnd_beyond }}" target="_blank" rel="noopener noreferrer" data-status="{{ c.status }}">
    {%- else -%}
    <div class="star-card is-{{ c.status }}" data-status="{{ c.status }}">
    {%- endif -%}
      <div class="star-head">
        {%- if c.portrait -%}
        <div class="star-identity">
          <img class="star-avatar" src="{{ c.portrait }}" alt="{{ c.title | escape }}" loading="lazy">
          <div class="star-identity-text">
            <div class="star-title">{{ c.title }}</div>
            <div class="star-sub">{{ c.sub }}</div>
          </div>
        </div>
        {%- else -%}
        <div>
          <div class="star-title">{{ c.title }}</div>
          <div class="star-sub">{{ c.sub }}</div>
        </div>
        {%- endif -%}
        <span class="star-pill {{ c.status }}">{{ c.status | capitalize }}</span>
      </div>
      <div class="star-desc">{{ c.desc }}</div>
      <div class="star-foot">
        <span>{{ c.campaign }}</span>
        {%- if c.dm -%}<span class="dim">·</span><span>DM: {{ c.dm }}</span>{%- endif -%}
        {%- if c.organized_play -%}<span class="dim">·</span><span>{{ c.organized_play }}</span>{%- endif -%}
      </div>
    {%- if c.href or c.dnd_beyond -%}
    </a>
    {%- else -%}
    </div>
    {%- endif -%}
    {%- endfor -%}
  </div>
</section>

<script>
(function () {
  var buttons = document.querySelectorAll('[data-char-filter]');
  var cards = document.querySelectorAll('#char-grid [data-status]');
  var countEl = document.getElementById('char-count');
  var total = cards.length;

  buttons.forEach(function (btn) {
    btn.addEventListener('click', function () {
      var filter = btn.dataset.charFilter;
      buttons.forEach(function (b) {
        b.setAttribute('aria-pressed', b === btn ? 'true' : 'false');
      });
      var shown = 0;
      cards.forEach(function (card) {
        var match = filter === 'all' || card.dataset.status === filter;
        card.hidden = !match;
        if (match) shown++;
      });
      if (countEl) {
        countEl.textContent = filter === 'all'
          ? total + ' characters · Player'
          : 'Showing ' + shown + ' of ' + total + ' characters';
      }
    });
  });
})();
</script>

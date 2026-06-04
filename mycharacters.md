---
title: Characters
layout: default
wide: true
---

<nav class="campaign-breadcrumb"><a href="{{ '/' | relative_url }}">← Home</a></nav>

{%- assign sorted = site.data.campaigns.playing | sort: "last_updated" | reverse -%}
<section class="lp-sec">
  <div class="sec-head">
    <div>
      <h2>Characters I <em>play</em></h2>
    </div>
    <span class="sec-aside">{{ sorted.size }} characters · Player</span>
  </div>
  <div class="star-grid">
    {%- for c in sorted -%}
    {%- if c.href -%}
    <a class="star-card is-{{ c.status }}" href="{{ c.href | relative_url }}">
    {%- elsif c.dnd_beyond -%}
    <a class="star-card is-{{ c.status }}" href="{{ c.dnd_beyond }}" target="_blank" rel="noopener noreferrer">
    {%- else -%}
    <div class="star-card is-{{ c.status }}">
    {%- endif -%}
      <div class="star-head">
        {%- if c.portrait -%}
        <div style="display:flex;gap:0.5rem;align-items:flex-start;min-width:0;">
          <img src="{{ c.portrait }}" alt="{{ c.title }}" style="width:40px;height:40px;object-fit:cover;border-radius:4px;flex-shrink:0;">
          <div style="min-width:0;">
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
        {%- if c.organized_play -%}<span class="dim">·</span><span>{{ c.organized_play | capitalize }}</span>{%- endif -%}
      </div>
    {%- if c.href or c.dnd_beyond -%}
    </a>
    {%- else -%}
    </div>
    {%- endif -%}
    {%- endfor -%}
  </div>
</section>

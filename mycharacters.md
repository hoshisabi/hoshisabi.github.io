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
    <a class="star-card is-{{ c.status }}" href="{{ c.href | relative_url }}">
      <div class="star-head">
        <div>
          <div class="star-title">{{ c.title }}</div>
          <div class="star-sub">{{ c.sub }}</div>
        </div>
        <span class="star-pill {{ c.status }}">{{ c.status | capitalize }}</span>
      </div>
      <div class="star-desc">{{ c.desc }}</div>
      <div class="star-foot">
        <span>{{ c.campaign }}</span>
        <span class="dim">·</span>
        <span>DM: {{ c.dm }}</span>
      </div>
    </a>
    {%- endfor -%}
  </div>
</section>

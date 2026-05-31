---
title: Campaigns
layout: default
wide: true
---

{%- assign sorted = site.data.campaigns.running | sort: "last_updated" | reverse -%}
<section class="lp-sec">
  <div class="sec-head">
    <div>
      <h2>Campaigns I <em>run</em></h2>
    </div>
    <span class="sec-aside">{{ sorted.size }} campaigns · DM</span>
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
        <span>Portal</span>
        <span class="dim">·</span>
        <span>{{ c.sessions }} sessions</span>
      </div>
    </a>
    {%- endfor -%}
  </div>
</section>

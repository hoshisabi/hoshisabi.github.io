---
title: Home
layout: default
home: true
---

{%- assign next = site.data.pando_schedule.entries | first -%}
{%- assign session = site.data.recent_session -%}
{%- assign _wd = site.time | date: "%-j" | plus: 0 -%}
{%- assign _wi = _wd | modulo: 7 -%}
{%- if _wi == 0 -%}
  {%- assign _wlbl = "Splines reticulated" -%}
  {%- assign _wnum = _wd | times: 137 | modulo: 9000 | plus: 1000 -%}
{%- elsif _wi == 1 -%}
  {%- assign _wlbl = "Cursed dice rolled" -%}
  {%- assign _wnum = _wd | times: 23 | modulo: 900 | plus: 100 -%}
{%- elsif _wi == 2 -%}
  {%- assign _wlbl = "Flumphs that can dance on a pin" -%}
  {%- assign _wnum = _wd | times: 7 | modulo: 9 | plus: 1 -%}
{%- elsif _wi == 3 -%}
  {%- assign _wlbl = "Number P4ND0 is thinking of" -%}
  {%- assign _wnum = _wd | times: 59 | modulo: 98 | plus: 1 -%}
{%- elsif _wi == 4 -%}
  {%- assign _wlbl = "Whatever you do — don't pick" -%}
  {%- assign _wnum = _wd | times: 11 | modulo: 19 | plus: 1 -%}
{%- elsif _wi == 5 -%}
  {%- assign _wlbl = "Plot hooks the party ignored" -%}
  {%- assign _wnum = _wd | times: 13 | modulo: 16 | plus: 7 -%}
{%- else -%}
  {%- assign _wlbl = "Times the DM smiled without explaining" -%}
  {%- assign _wnum = _wd | times: 17 | modulo: 11 | plus: 3 -%}
{%- endif -%}

<section class="lp-hero">
  <div class="hero-eyebrow">Dan Chapman · @hoshisabi</div>
  <h1 class="hero-title">hoshi<strong>sabi</strong></h1>
  <p class="hero-tag">
    An experienced DM with <em>two active campaigns</em> and weekly session logs — plus a small set of code and the occasional note. A working space for things I'm bothering to finish.
  </p>
  <div class="hero-ctas">
    <a class="lp-btn ghost" href="{{ '/myadventures' | relative_url }}">
      My Adventures {% include icons.html name="arrow" %}
    </a>
    <a class="lp-btn ghost" href="{{ '/rpg/pandodnd/public/' | relative_url }}">
      PandoDnD schedule
    </a>
    <a class="lp-btn ghost" href="https://hoshisabi.com/al_adventure_catalog/" target="_blank" rel="noopener">
      AL Adventure Catalog
    </a>
  </div>
</section>

<section class="lp-telemetry">
  <div class="tel-stats">
    <div class="tel-stat">
      <div class="tel-num">{{ site.data.campaigns.stats.active_campaigns }}</div>
      <div class="tel-lbl">Active campaigns</div>
    </div>
    <div class="tel-stat">
      <div class="tel-num">{{ site.data.campaigns.stats.sessions_logged }}<span>+</span></div>
      <div class="tel-lbl">Sessions logged</div>
    </div>
    <div class="tel-stat">
      <div class="tel-num">{{ site.adventures.size }}</div>
      <div class="tel-lbl">Adventures written</div>
    </div>
    <div class="tel-stat">
      <div class="tel-num">∞</div>
      <div class="tel-lbl">Unfinished tasks</div>
    </div>
    <div class="tel-stat">
      <div class="tel-num">{{ _wnum }}</div>
      <div class="tel-lbl">{{ _wlbl }}</div>
    </div>
  </div>
  <div class="tel-divider"></div>
  {%- if next -%}
  <a class="tel-upnext" href="{{ next.link }}" target="_blank" rel="noopener">
    <div class="upn-date">
      <div class="upn-day">{{ next.date | date: "%a" }}</div>
      <div class="upn-num">{{ next.date | date: "%-d" }}</div>
      <div class="upn-month">{{ next.date | date: "%b" }}</div>
    </div>
    <div class="upn-info">
      <div class="upn-lbl"><span class="feed-dot live"></span> Up next at the table · PandoDnD</div>
      <div class="upn-title">{{ next.title }}</div>
      <div class="upn-meta">{{ next.code }} · {{ next.tier }} · {{ next.date | date: "%-I:%M %p" }}</div>
    </div>
    <div class="upn-arr">{% include icons.html name="arrow" %}</div>
  </a>
  {%- else -%}
  <div class="tel-upnext">
    <div class="upn-info">
      <div class="upn-lbl">Up next at the table</div>
      <div class="upn-empty">No sessions on the books — check back soon.</div>
    </div>
  </div>
  {%- endif -%}
</section>

{%- assign sorted_running = site.data.campaigns.running | sort: "last_updated" | reverse -%}
<section class="lp-sec">
  <div class="sec-head">
    <div>
      <div class="sec-num">★ Section 01</div>
      <h2>Campaigns I <em>run</em></h2>
    </div>
    <a class="sec-aside sec-aside-link" href="{{ '/mycampaigns' | relative_url }}">
      View all {% include icons.html name="arrow" %}
    </a>
  </div>
  <div class="star-grid">
    {%- for c in sorted_running limit: 3 -%}
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

{%- assign sorted_playing = site.data.campaigns.playing | sort: "last_updated" | reverse -%}
<section class="lp-sec">
  <div class="sec-head">
    <div>
      <div class="sec-num">★ Section 02</div>
      <h2>Characters I <em>play</em></h2>
    </div>
    <a class="sec-aside sec-aside-link" href="{{ '/mycharacters' | relative_url }}">
      View all {% include icons.html name="arrow" %}
    </a>
  </div>
  <div class="star-grid">
    {%- for c in sorted_playing limit: 3 -%}
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

<section class="lp-sec">
  <div class="sec-head">
    <div>
      <div class="sec-num">★ Section 03</div>
      <h2>Latest <em>session</em></h2>
    </div>
    <span class="sec-aside">Updated {{ session.date }}</span>
  </div>
  <a class="lp-session" href="{{ session.href | relative_url }}">
    <div class="session-eyebrow">{{ session.campaign }} · {{ session.session_label }}</div>
    <div class="session-title">&ldquo;{{ session.title }}&rdquo;</div>
    <div class="session-sub">{{ session.adventure_code }} · {{ session.date }}</div>
    <div class="session-body">{{ session.excerpt }}</div>
    <div class="session-foot">Read the recap {% include icons.html name="arrow" %}</div>
  </a>
</section>

<section class="lp-sec">
  <div class="sec-head">
    <div>
      <div class="sec-num">★ Section 04</div>
      <h2>Coming up <em>at PandoDnD</em></h2>
    </div>
    <span class="sec-aside">
      <span class="feed-dot live"></span>
      Live · Warhorn
    </span>
  </div>
  {%- if site.data.pando_schedule.entries.size > 0 -%}
  <div class="pando-grid">
    {%- for e in site.data.pando_schedule.entries limit: 4 -%}
    <a class="pando-card {% if forloop.first %}is-next{% endif %}" href="{{ e.link }}" target="_blank" rel="noopener">
      {%- if forloop.first -%}<div class="pando-flag">★ Next session</div>{%- endif -%}
      <div class="pando-code">{{ e.code }}</div>
      <div class="pando-title">{{ e.title }}</div>
      <div class="pando-when">{{ e.date | date: "%a, %b %-d" }} · {{ e.date | date: "%-I:%M %p" }}</div>
      <div class="pando-summary">{{ e.summary }}</div>
      <div class="pando-foot">
        <span>Warhorn</span>
        {% include icons.html name="external" size=11 %}
      </div>
    </a>
    {%- endfor -%}
  </div>
  {%- else -%}
  <div class="pando-empty">Schedule is currently empty.</div>
  {%- endif -%}
</section>

<section class="lp-sec">
  <div class="sec-head">
    <div>
      <div class="sec-num">★ Section 05</div>
      <h2>Code I'm <em>tinkering with</em></h2>
    </div>
    <a class="sec-aside sec-aside-link" href="https://github.com/hoshisabi">
      github.com/hoshisabi {% include icons.html name="external" size=11 %}
    </a>
  </div>
  <div class="proj-grid">
    {%- for p in site.data.projects -%}
    {%- assign status_class = p.status | replace: " ", "-" -%}
    <a class="proj-card" href="{{ p.href }}" target="_blank" rel="noopener">
      <div class="proj-head">
        {% include icons.html name="github" size=14 %}
        <span class="proj-repo">{{ p.repo }}</span>
        <span class="proj-status {{ status_class }}">{{ p.status }}</span>
      </div>
      <div class="proj-title">{{ p.name }}</div>
      <div class="proj-desc">{{ p.desc }}</div>
      <div class="proj-foot">
        <span class="proj-lang">
          <span class="proj-dot lang-{{ p.lang | downcase }}"></span>
          {{ p.lang }}
        </span>
        <span class="proj-arr">{% include icons.html name="arrow" %}</span>
      </div>
    </a>
    {%- endfor -%}
  </div>
</section>

<section class="lp-sec">
  <div class="sec-head">
    <div>
      <div class="sec-num">★ Section 06</div>
      <h2>U-Con <em>Adventurers League</em></h2>
    </div>
    <span class="sec-aside">Returning November 2026</span>
  </div>
  <div class="ucon-block">
    <div>
      <div class="ucon-eyebrow">U-Con · Ann Arbor</div>
      <h3>We ran AL at U-Con — and we're coming back.</h3>
      <p>If you're an organizer, a DM, or a player who'd like to sit at our tables next year, get in touch. The convention site has the lay of the land at <a href="https://www.ucon-gaming.org/">ucon-gaming.org</a>.</p>
      <p style="margin-bottom: 0;">This year we also fundraised for Doctors Without Borders.</p>
    </div>
    <div class="ucon-cause">
      <div class="ucon-cause-lbl">★ Fundraiser</div>
      <div class="ucon-cause-name">Doctors Without Borders</div>
      <div class="ucon-cause-desc">A personal campaign raising funds alongside our U-Con games. Donations remain open.</div>
      <a class="ucon-cause-btn" href="https://events.doctorswithoutborders.org/index.cfm?fuseaction=donordrive.personalCampaign&participantID=8648">
        Donate {% include icons.html name="arrow" %}
      </a>
    </div>
  </div>
</section>

<section class="lp-sec">
  <div class="sec-head">
    <div>
      <div class="sec-num">★ Section 07</div>
      <h2>Reference <em>shelf</em></h2>
    </div>
    <span class="sec-aside">Curated</span>
  </div>
  <div class="resources">
    {%- for r in site.data.resources -%}
    <a class="resource" href="{{ r.href | relative_url }}"{% if r.external %} target="_blank" rel="noopener"{% endif %}>
      <span class="resource-arr">{% include icons.html name="external" size=11 %}</span>
      <div class="resource-num">{{ forloop.index | prepend: '00' | slice: -2, 2 }} / ref</div>
      <div class="resource-t">{{ r.title }}</div>
      <div class="resource-d">{{ r.desc }}</div>
    </a>
    {%- endfor -%}
  </div>
</section>

---
layout: default
title: Icewind Dale Campaign
---

# Icewind Dale

*A D&D 5e campaign.*

## Sessions

{% for session in site.pages %}
{% if session.path contains 'icewind-dale/public/sessions' %}
- [{{ session.title }}]({{ session.url }})
{% endif %}
{% endfor %}

## Characters

{% for char in site.pages %}
{% if char.path contains 'icewind-dale/public/characters' %}
- [{{ char.title }}]({{ char.url }})
{% endif %}
{% endfor %}

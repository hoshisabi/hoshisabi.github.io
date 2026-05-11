---
layout: default
title: Icewind Dale Campaign
---

# Icewind Dale

*A D&D 5e campaign.*

## Sessions

{% assign sessions = site.pages | where_exp: "p", "p.path contains 'icewind-dale/public/sessions'" | sort: "title" %}
{% for session in sessions %}
- [{{ session.title }}]({{ session.url }})
{% endfor %}

## Characters

{% assign characters = site.pages | where_exp: "p", "p.path contains 'icewind-dale/public/characters'" | sort: "title" %}
{% for char in characters %}
- [{{ char.title }}]({{ char.url }})
{% endfor %}

---
title: Table test
---

<table class="sortable">
{% for adventure in site.data.adventures %}
{% if forloop.first %}
<thead><tr>
  {% for pair in adventure %}
    <th>{{ pair[0] }}</th>
  {% endfor %}
</tr></thead>
{% endif %}


  {% if adventure.runtime == "2" or adventure.runtime == "2-4" %}
    {% tablerow pair in adventure %}
        {{ pair[1] }}
    {% endtablerow %}
  {% endif %}
{% endfor %}

</table>
    
<link href="https://cdn.jsdelivr.net/gh/tofsjonas/sortable@latest/sortable.min.css" rel="stylesheet" />
<script src="https://cdn.jsdelivr.net/gh/tofsjonas/sortable@latest/sortable.min.js"></script>
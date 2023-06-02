---
title: Table test
---

<table class="sortable" id="csv-table">
  {% for row in site.data.adventures %}
    {% if forloop.first %}
    <thead><tr>
      {% for pair in row %}
        <th>{{ pair[0] }}</th>
      {% endfor %}
    </tr></thead>
    {% endif %}

    {% tablerow pair in row %}
      {{ pair[1] }}
    {% endtablerow %}
{% endfor %}
</table>


<script>
    const filterInput = document.getElementById('filter-input');
    const csvTable = document.getElementById('csv-table');
    const rows = csvTable.getElementsByTagName('tr');
    const headers = Array.from(csvTable.getElementsByTagName('th'));

    filterInput.addEventListener('keyup', function () {
        const filterValue = this.value.toLowerCase();

        for (let i = 0; i < rows.length; i++) {
            const row = rows[i];
            const cells = row.getElementsByTagName('td');
            let display = false;

            for (let j = 0; j < cells.length; j++) {
                const cell = cells[j];
                const header = headers[j].innerText.toLowerCase();

                if (cell.innerText.toLowerCase().includes(filterValue) && header !== 'dmguild') {
                    display = true;
                    break;
                }
            }

            row.style.display = display ? '' : 'none';
        }
    });
</script>
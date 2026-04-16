---
layout: default
title: Case Reports
description: "Concrete case studies illustrating violations of physiological rights within healthcare systems."
---

# Case Reports

{% for item in site.reports %}
<div class="card">
  <h3><a href="{{ item.url | relative_url }}">{{ item.title }}</a></h3>
  {% if item.description %}<p>{{ item.description }}</p>{% endif %}
</div>
{% endfor %}

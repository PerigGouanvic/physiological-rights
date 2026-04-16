---
layout: default
title: Editorials
description: "Editorial positions and critical reflections on physiological rights and their recognition."
---

# Editorials

{% for item in site.editorials %}
<div class="card">
  <h3><a href="{{ item.url | relative_url }}">{{ item.title }}</a></h3>
  {% if item.description %}<p>{{ item.description }}</p>{% endif %}
</div>
{% endfor %}

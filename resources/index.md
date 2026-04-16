---
layout: default
title: Resources
description: "References, legal texts, and supporting documentation for the physiological rights framework."
---

# Resources

{% for item in site.resources %}
<div class="card">
  <h3><a href="{{ item.url | relative_url }}">{{ item.title }}</a></h3>
  {% if item.description %}<p>{{ item.description }}</p>{% endif %}
</div>
{% endfor %}

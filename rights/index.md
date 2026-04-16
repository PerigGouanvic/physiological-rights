---
layout: default
title: Specific Physiological Rights
description: "An index of specific physiological rights — each documenting a recognised biological need, the systematic violations observed, and the applicable legal framework."
---

# Specific Physiological Rights

Each page documents a specific physiological right: the scientific context, the systematic violations observed, and the applicable legal framework.

<div class="rights-grid">
{% for right in site.rights %}
<div class="card">
  <h3><a href="{{ right.url | relative_url }}">{{ right.title }}</a></h3>
  {% if right.description %}<p>{{ right.description }}</p>{% endif %}
</div>
{% endfor %}
</div>

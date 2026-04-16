---
layout: default
title: Core Definitions
description: "The foundational concepts underlying physiological rights: what they are, how they differ from the right to health, and why they constitute a justiciable category of human rights."
---

# Core Definitions

{% for item in site.definitions %}
<div class="card">
  <h3><a href="{{ item.url | relative_url }}">{{ item.title }}</a></h3>
  {% if item.description %}<p>{{ item.description }}</p>{% endif %}
</div>
{% endfor %}

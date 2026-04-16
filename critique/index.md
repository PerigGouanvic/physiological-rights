---
layout: default
title: Nutritional Critique
description: "A critical analysis of mainstream nutritional concepts — why notions such as 'balanced diet' and 'healthy food' are insufficient to guarantee physiological integrity at the individual level."
---

# Nutritional Critique

{% for item in site.critique %}
<div class="card">
  <h3><a href="{{ item.url | relative_url }}">{{ item.title }}</a></h3>
  {% if item.description %}<p>{{ item.description }}</p>{% endif %}
</div>
{% endfor %}

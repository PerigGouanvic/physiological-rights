---
layout: default
title: Currents
description: "A living map of the currents adjacent to the Physiological Rights framing: the researchers, jurists, and institutions actually engaged today with what an adequate physiology requires and what a right to it entails."
---

# Currents

A map of the currents adjacent to the framing this resource develops. Not the historical figures documented in the rights pages, but the researchers, jurists, and institutions active today whose work engages the question of what an adequate physiology requires and what a right to it entails.

The map is organised along three axes.

- **Nutritional and physiological science.** Living researchers who document the insufficiency of the current thresholds and describe the physiological needs the ordinary framework misses.
- **Right to health, academic and legal.** Living jurists and institutions working on the operationalization of the right to health and the right to food.
- **Structurally adjacent, not aligned.** Entities whose vocabulary overlaps with the concerns of this resource but whose structural position obscures rather than serves the underlying question. Documenting them is part of the map, because the specificity of the framing appears by contrast.

Each entry has its own page, however brief. The map is deliberately built stub by stub: presence first, depth later.

<div class="currents-index">
{% assign axes = "nutritional-science,right-to-health,structural-adjacent" | split: "," %}
{% for axis in axes %}
<div class="axis-block">
  <h2>{% case axis %}{% when 'nutritional-science' %}Nutritional and physiological science{% when 'right-to-health' %}Right to health{% when 'structural-adjacent' %}Structurally adjacent{% endcase %}</h2>
  <ul>
  {% for entry in site.currents %}
    {% if entry.axis == axis %}
    <li><a href="{{ entry.url | relative_url }}"><strong>{{ entry.title }}</strong></a>{% if entry.role %} · {{ entry.role }}{% endif %}{% if entry.affiliation %} · {{ entry.affiliation }}{% endif %}</li>
    {% endif %}
  {% endfor %}
  </ul>
</div>
{% endfor %}
</div>

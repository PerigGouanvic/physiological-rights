---
layout: default
title: Did you know…
description: "Compact facts from physiology and clinical nutrition. Each one is a standalone finding that could sit on its own on a fridge magnet, and each one points back to the fuller argument it comes from."
---

# Did you know…

A running collection of compact physiological facts. Each one is short enough to stand alone and specific enough to be verified. Together they form the substrate from which the longer arguments on this resource are built.

The list grows as new pieces are written. Every article on this resource contributes at least one entry.

---

<ul class="dyk-list">
{% assign dyk = site.did-you-know | sort: "date" | reverse %}
{% for item in dyk %}
  <li class="dyk-item">
    <a href="{{ item.url | relative_url }}">
      <strong>{{ item.title }}</strong>
    </a>
    {% if item.short_form %}
    <p class="dyk-short">{{ item.short_form }}</p>
    {% endif %}
  </li>
{% endfor %}
</ul>

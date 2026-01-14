---
layout: default
title: Catador de alfajores
---

# Catador de alfajores

Bienvenido al blog sobre alfajores argentinos.

## Posts recientes

{% for post in site.posts limit:10 %}
  {% if post.title and post.title != "" and post.title != nil %}
- [{{ post.title }}]({{ site.baseurl }}{{ post.url }}) - {{ post.date | date: "%d/%m/%Y" }}
  {% endif %}
{% endfor %}

{% assign valid_count = 0 %}
{% for post in site.posts %}
  {% if post.title and post.title != "" and post.title != nil %}
    {% assign valid_count = valid_count | plus: 1 %}
  {% endif %}
{% endfor %}
{% if valid_count > 10 %}
<p><a href="{{ site.baseurl }}/posts">Ver todos los posts ({{ valid_count }} total)</a></p>
{% endif %}


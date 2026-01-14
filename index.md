---
layout: default
title: Catador de alfajores
---

# Catador de alfajores

Bienvenido al blog sobre alfajores argentinos.

## Posts recientes

{% assign valid_posts = site.posts | where_exp: "post", "post.title and post.title != '' and post.title != nil" %}
{% for post in valid_posts limit:10 %}
- [{{ post.title }}]({{ site.baseurl }}{{ post.url }}) - {{ post.date | date: "%d/%m/%Y" }}
{% endfor %}

{% assign valid_posts_count = site.posts | where_exp: "post", "post.title and post.title != '' and post.title != nil" | size %}
{% if valid_posts_count > 10 %}
<p><a href="{{ site.baseurl }}/posts">Ver todos los posts ({{ valid_posts_count }} total)</a></p>
{% endif %}


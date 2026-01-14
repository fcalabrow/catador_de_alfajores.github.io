---
layout: default
title: Todos los posts
permalink: /posts/
---

# Todos los posts

{% for post in site.posts %}
  {% if post.title and post.title != "" and post.title != nil %}
- [{{ post.title }}]({{ site.baseurl }}{{ post.url }}) - {{ post.date | date: "%d/%m/%Y" }}
  {% endif %}
{% endfor %}


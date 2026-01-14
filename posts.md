---
layout: default
title: Todos los posts
permalink: /posts/
---

# Todos los posts

{% assign valid_posts = site.posts | where_exp: "post", "post.title and post.title != '' and post.title != nil" %}
{% for post in valid_posts %}
- [{{ post.title }}]({{ site.baseurl }}{{ post.url }}) - {{ post.date | date: "%d/%m/%Y" }}
{% endfor %}


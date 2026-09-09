---
layout: default
permalink: /blog/
title: 博客
nav: true
nav_order: 1
pagination:
  enabled: true
  collection: posts
  permalink: /page/:num/
  per_page: 10
  sort_field: date
  sort_reverse: true
  trail:
    before: 1
    after: 3
translations:
  en:
    title: Blog
---

{% assign t = site.data.i18n[site.lang] %}

<header class="archive-intro">
  <p class="eyebrow">THE ARCHIVE</p>
  <h1>{{ t.notes }}</h1>
  <p>{{ t.archive_description }}</p>
</header>
<ol class="entry-list">
  {% for post in paginator.posts %}
    <li class="entry-row">
      <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: '%Y.%m.%d' }}</time>
      <div>
        <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
        <p>{{ post.description }}</p>
      </div>
      <span class="entry-arrow" aria-hidden="true">↗</span>
    </li>
  {% endfor %}
</ol>
{% include pagination.liquid %}

---
layout: default
title: 首页
permalink: /
translations:
  en:
    title: Home
---

{% assign t = site.data.i18n[site.lang] %}

<section class="notebook-intro" aria-labelledby="notebook-title">
  <div>
    <p class="eyebrow">A PERSONAL NOTEBOOK</p>
    <h1 id="notebook-title">Alchemist<span class="title-dot">.</span></h1>
    <p class="intro-subtitle">{{ t.subtitle }}</p>
  </div>
  <div class="intro-note">
    <p>{{ t.motto }}</p>
    <a class="quiet-link" href="{{ '/feed.xml' | relative_url }}">{{ t.rss }} <span aria-hidden="true">↗</span></a>
  </div>
</section>

<section class="notebook-entries" aria-labelledby="entries-title">
  <div class="section-label">
    <h2 id="entries-title">{{ t.recent }}</h2>
    <a class="quiet-link" href="{{ '/blog/' | relative_url }}">{{ t.all }} <span aria-hidden="true">↗</span></a>
  </div>
  <ol class="entry-list">
    {% for post in site.posts limit:5 %}
      <li class="entry-row">
        <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: '%Y.%m.%d' }}</time>
        <div>
          <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
          <p>{{ post.description }}</p>
        </div>
        <span class="entry-arrow" aria-hidden="true">↗</span>
      </li>
    {% endfor %}
  </ol>
</section>

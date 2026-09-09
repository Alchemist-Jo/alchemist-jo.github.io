---
layout: default
title: 首页
permalink: /
---

<section class="notebook-intro" aria-labelledby="notebook-title">
  <div>
    <p class="eyebrow">A PERSONAL NOTEBOOK</p>
    <h1 id="notebook-title">Alchemist<span class="title-dot">.</span></h1>
    <p class="intro-subtitle">研究，阅读，与思考。</p>
  </div>
  <div class="intro-note">
    <p>把问题写清楚，<br>让想法慢慢成形。</p>
    <a class="quiet-link" href="{{ '/feed.xml' | relative_url }}">订阅 RSS <span aria-hidden="true">↗</span></a>
  </div>
</section>

<section class="notebook-entries" aria-labelledby="entries-title">
  <div class="section-label">
    <h2 id="entries-title">最近的笔记</h2>
    <a class="quiet-link" href="{{ '/blog/' | relative_url }}">全部文章 <span aria-hidden="true">↗</span></a>
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

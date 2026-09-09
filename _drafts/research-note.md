---
layout: distill
title: "写作示例：研究问题与证据"
description: "草稿模板，不会在正式构建中发布。"
tags: research
categories: notes
authors:
  - name: Klein
toc:
  - name: Problem
  - name: Method
  - name: Evidence
  - name: Limitations
bibliography: references.bib
---

## Problem

用一个具体例子说明问题。区分已有证据、自己的假设，以及需要验证的预测。

## Method

下面仅展示公式排版，并非实验结论：

$$
\hat{p} = \frac{1}{N} \sum_{i=1}^{N} \mathbb{1}[\hat{y}_i = y_i].
$$

```python
correct = sum(pred == target for pred, target in pairs)
accuracy = correct / len(pairs)
```

## Evidence

| 问题         | 需要的证据               |
| :----------- | :----------------------- |
| 是否有效？   | 同一评测设置下的基线对照 |
| 为什么有效？ | 控制变量的消融实验       |

引用示例：<d-cite key="shannon1948"></d-cite>。

## Limitations

记录失败案例、适用条件和仍未验证的部分。发布前删除所有示例内容，核对图表来源与引用。

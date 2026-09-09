# Alchemist

[访问博客](https://alchemist-jo.github.io/) · [发布状态](https://github.com/Alchemist-Jo/alchemist-jo.github.io/actions/workflows/pages.yml)

Klein 的个人博客，复用 [al-folio](https://github.com/alshedivat/al-folio) v1 和 Jekyll。文章使用 Markdown，支持公式、代码高亮、目录、引用、深浅色模式、RSS 和归档。

## 日常写作

1. 复制 `_drafts/research-note.md`，修改标题和正文。
2. `bundle exec jekyll serve --drafts` 本地查看草稿。
3. 准备发布时，移动到 `_posts/YYYY-MM-DD-slug.md` 并设置准确日期。
4. 提交到 GitHub。PR 只运行检查；合并到 `main` 后自动部署到 GitHub Pages。

普通文章用 `layout: post`；研究长文用 `layout: distill`，目录在 `toc` 中配置，引用放在 `assets/bibliography/`。内部链接使用 `relative_url`，以兼容项目子路径。图片放在 `assets/img/`，写清替代文本、图注和来源。不要把密钥、未公开数据或未经核对的结论放入公开仓库；`_drafts` 不会显示在网站上，但公开仓库中的草稿源码仍然公开。

## 本地运行

Ruby 3.3、Node.js 22、ImageMagick：

```sh
bundle install
npm ci
bundle exec jekyll serve --host 127.0.0.1
```

打开 http://127.0.0.1:4000 。校验：

```sh
npm run lint:prettier
bundle exec jekyll build
python3 bin/check-site.py _site
```

## GitHub Pages

仓库为 `Alchemist-Jo/alchemist-jo.github.io`，Pages 发布来源已设为 **GitHub Actions**。推送 `main` 后会自动检查和发布。工作流自动从仓库名推导域名和子路径，不需要长期访问 token，只有部署任务获得 Pages 写入权限。

`_config.yml` 已设置正式地址 `https://alchemist-jo.github.io` 和空 `baseurl`；CI 生成 `_config.deploy.yml`，兼容个人站点和项目子路径。自定义域名可通过仓库 Actions 变量 `SITE_URL` 配置；根路径将 `SITE_BASEURL` 设为 `/`，并在 Pages 设置和 DNS 配置该域名。

## 维护

- Dependabot 每月为 gems、npm 和 Actions 创建更新 PR；检查通过后仍需审阅，不自动合并。
- Gemfile.lock、package-lock.json 固定解析结果，Actions 固定提交 SHA。
- 配置修改在 `_config.yml`，简介在 `_pages/about.md`，社交链接在 `_data/socials.yml`。
- 作者履历、头像、论文和联系方式等待本人提供，当前不展示虚构资料。
- 回滚用 GitHub Revert 或 `git revert`，让工作流重新部署；不要覆盖历史。
- 不复制主题内部实现；升级时优先更新 gem 版本。来源和许可证见 [UPSTREAM.md](UPSTREAM.md)。

初次部署已于 2026-09-09 验证成功。后续修改可在本地提交后执行 `git push origin main`；代码和依赖变更通过 PR 审阅后合并。现有 SSH key 可用于推送，无需创建新的 token。

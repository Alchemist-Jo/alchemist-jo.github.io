# Languages

Chinese is served at `/`; English at `/en/`. Navigation switches to the same page path, including articles. Static pages work without JavaScript and declare `lang`, canonical URLs and alternate language URLs. Each edition has its own feed and sitemap.

Build both editions with `bundle exec ruby bin/build-site.rb`, then run `python3 bin/check-site.py _site` and `python3 bin/check-languages.py`. CI passes `_config.yml _config.deploy.yml` to the build script for the public URL. To preview, serve `_site` as a static directory. Running Jekyll alone builds only one edition.

Interface text lives in `_data/i18n.yml`. The translation hook applies `translations.en` to page and post metadata before feed, search, pagination and archive generation. A published post must provide an English `title`, `description` and `body`; the build fails when these are absent. Preserve the existing Chinese body below front matter. English bodies may include Markdown and Liquid. Dates, tags, slugs and citations are shared. Drafts remain unpublished.

Theme overrides in header, head and post layout keep the upstream navigation controls and metadata integration; their ownership is recorded in `.al-folio-overrides.yml`. No browser-language redirect is used, so shared links preserve the chosen language.

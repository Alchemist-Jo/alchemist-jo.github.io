# Alchemist

This is Alchemist's personal blog, based on the al-folio v1 starter. This directory is an independent Git repository.

- Public site and author identity: Alchemist only. Never publish a private name or infer personal affiliations. Use the repository-local pseudonymous commit identity.
- Keep README.md byte-for-byte identical to the documented upstream README snapshot.
- Site name: Alchemist. Author: Alchemist. Do not invent affiliations, publications, links, or research findings.
- Edit content and config before considering theme overrides. Runtime belongs to pinned upstream gems.
- New research articles begin in `_drafts/`. Publish only when the user requests it by moving to `_posts/YYYY-MM-DD-slug.md`.
- Preserve upstream LICENSE and UPSTREAM.md; never push to the upstream template repository.
- Maintain matching plugin entries in Gemfile and `_config.yml` and commit lockfiles.
- Before pushing: `npm ci`, `npm run lint:prettier`, `bundle exec ruby bin/build-site.rb`, `python3 bin/check-site.py _site`.
- Verify repository owner and remote before any push. Never force push. PRs for subsequent code or dependency changes; no automatic dependency merging.
- Deploy only through `.github/workflows/pages.yml` after checks pass. Production builds never include drafts.
- If adding a gem-owned local override, document its purpose and run `bundle exec al-folio upgrade overrides audit`.

- Both languages are built by `bin/build-site.rb`. Add authored English `translations.en` (title, description, body) to every published post. Keep the same permalink in both language builds. See `docs/LANGUAGES.md`.

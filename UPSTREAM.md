# Upstream provenance

Starter: https://github.com/alshedivat/al-folio
Snapshot: c5636885aebf34cda5d971a83b00aae3e2b14478 (retrieved 2026-09-09).
Upstream MIT license preserved in LICENSE. Theme runtime stays in pinned gems; site-specific styling is layered onto the upstream Sass entrypoint.
Visual reference: https://benjamin-eecs.github.io/blog/2025/spice/
No text, images, biography or research results copied from the reference site.

README.md is copied byte-for-byte from the snapshot above.

Retained upstream: Gemfile, Gemfile.lock, library settings, blog index, 404 page, robots and formatting config.
Personalized: site settings, pages, posts, drafts, CI, documentation.
Site prose and future research assets are not automatically covered by the upstream software license.

Visual overrides: `assets/css/main.scss` loads the gem-owned Sass modules and the site-owned `_sass/_alchemist.scss`. Homepage and blog index are site-owned content. Override audit tracks the entrypoint for future gem updates.

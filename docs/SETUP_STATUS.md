# Setup status — 2026-09-09

Site: **Alchemist**. Author: **Klein**.

## Completed locally

- Independent repository using the al-folio v1 starter; upstream provenance and MIT license retained.
- Homepage, blog, starter post, and a separate research-article draft (Distill, equation, code, table, bibliography and contents).
- GitHub Actions configured for PR checks and main-only Pages deployments with job-scoped permissions and pinned Actions.
- Dependabot configured for monthly dependency PRs, without automatic merging.
- `npm ci` and Prettier passed; npm reported zero known vulnerabilities for the installed development dependencies.
- Production Jekyll build passed in Ruby 3.3 Linux with the committed lockfile.
- Seven generated HTML pages passed internal destination, feed/sitemap XML, draft exclusion and source exclusion checks.
- A second production build with a project base path `/alchemist` passed the same checks.
- Draft build passed and generated the research-note route separately from production output.
- al-folio upgrade audit: zero blocking/non-blocking issues; no local theme overrides.
- Local HTTP preview returned 200. No browser interaction or visual QA was performed.

## Pending GitHub access

GitHub CLI was not authenticated. No remote repository has been created, no push has occurred, and no live Pages deployment has been verified.

Resume after `gh auth login` and the user supplies the destination account/repository:

1. Check the authenticated account and existing repositories before creating anything.
2. Prefer `ACCOUNT/ACCOUNT.github.io` if unused. If it exists, inspect and preserve it; use a review branch/PR or a separate repository as appropriate.
3. Set `_config.yml` public `url` and `baseurl`, and the user's confirmed social links.
4. Create/connect the intended repository, enable Pages with GitHub Actions, and push this site's history.
5. Wait for the build and deploy jobs, verify the live homepage and article, and report the actual repository and site URLs.

## Known scope

The upstream notebook plugin reports missing optional Python notebook dependencies. Markdown and Distill builds pass; notebook embedding is not configured or validated. Install Jupyter/nbconvert before adding notebook posts. Public personal affiliations, a portrait, contact information and publications have not been supplied.

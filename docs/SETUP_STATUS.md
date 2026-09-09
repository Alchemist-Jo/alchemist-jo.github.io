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

## GitHub publication

- Public repository: https://github.com/Alchemist-Jo/alchemist-jo.github.io
- Live site: https://alchemist-jo.github.io/
- Existing GitHub browser session used to create the repository and select GitHub Actions as the Pages source; existing SSH key used to push.
- First deployment: https://github.com/Alchemist-Jo/alchemist-jo.github.io/actions/runs/34314058784 (completed successfully).
- Verified homepage, blog index, opening article and RSS each returned HTTP 200 with Alchemist content.
- Dependabot update jobs were activated by the repository configuration. Dependency PRs remain subject to review; automatic merging is off.
- The initial push briefly triggered GitHub's default branch-based Pages workflow before the source was switched. The custom Check and publish workflow is the active deployment path.
- Local origin uses SSH. A repository-local URL rewrite preserves SSH for this owner despite the machine's broader HTTPS rewrite.

## Known scope

The upstream notebook plugin reports missing optional Python notebook dependencies. Markdown and Distill builds pass; notebook embedding is not configured or validated. Install Jupyter/nbconvert before adding notebook posts. Public personal affiliations, a portrait, contact information and publications have not been supplied.

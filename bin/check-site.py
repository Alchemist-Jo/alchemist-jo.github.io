"""Check built routes, leaked source/drafts, and local links without network requests."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlparse, unquote
import sys
import xml.etree.ElementTree as ET

root = Path(sys.argv[1] if len(sys.argv) > 1 else '_site').resolve()

class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.links = []
        self.canonical = None
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'link' and attrs.get('rel') == 'canonical':
            self.canonical = attrs.get('href')
        for key in ('href', 'src'):
            if key in attrs:
                self.links.append(attrs[key])

errors = []
for name in ('index.html', 'blog/index.html', '404.html', 'feed.xml', 'sitemap.xml'):
    if not (root / name).is_file():
        errors.append(f'Missing required output: {name}')
if errors:
    sys.exit('\n'.join(errors))
for name in ('feed.xml', 'sitemap.xml'):
    ET.parse(root / name)
front = Page((root / 'index.html').read_text())
if not front.canonical:
    sys.exit('Homepage has no canonical URL')
site = urlparse(front.canonical)
base = site.path.rstrip('/')
for filename in ('Gemfile', 'Gemfile.lock', 'README.md', 'AGENTS.md', 'UPSTREAM.md', '.env'):
    if (root / filename).exists():
        errors.append(f'Source leaked into output: {filename}')
for dirname in ('_drafts', 'bin', 'docs', 'node_modules', 'vendor'):
    if (root / dirname).exists():
        errors.append(f'Private/build directory leaked: {dirname}')
count = 0
for path in root.rglob('*.html'):
    count += 1
    text = path.read_text()
    if '写作示例：研究问题与证据' in text:
        errors.append(f'Draft leaked into production: {path.relative_to(root)}')
    page = Page(text)
    url = page.canonical or urljoin(front.canonical, str(path.relative_to(root)))
    for link in page.links:
        parsed = urlparse(urljoin(url, link))
        if parsed.scheme not in ('http', 'https') or parsed.netloc != site.netloc:
            continue
        target_path = unquote(parsed.path)
        if base:
            if not target_path.startswith(base + '/') and target_path != base:
                errors.append(f'Link escapes project base: {path.relative_to(root)} -> {link}')
                continue
            target_path = target_path[len(base):]
        target = root / target_path.lstrip('/')
        if not target.is_file() and not (target / 'index.html').is_file():
            errors.append(f'Broken local link: {path.relative_to(root)} -> {link}')
if errors:
    sys.exit('\n'.join(sorted(set(errors))))
print(f'Checked {count} HTML pages, internal destinations, feed/sitemap XML and draft/source exclusions.')

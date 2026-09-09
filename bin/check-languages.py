"""Verify paired pages, language metadata, reciprocal switches and translated feeds."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse, unquote
import xml.etree.ElementTree as ET
import sys

root = Path(sys.argv[1] if len(sys.argv) > 1 else '_site')
class Document(HTMLParser):
    def __init__(self, text):
        super().__init__(); self.lang = None; self.canonical = None; self.alternates = {}; self.switch = None
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'html': self.lang = a.get('lang')
        if tag == 'link' and a.get('rel') == 'canonical': self.canonical = a.get('href')
        if tag == 'link' and a.get('rel') == 'alternate' and 'hreflang' in a: self.alternates[a['hreflang']] = a['href']
        if tag == 'a' and 'language-switch' in a.get('class', '').split(): self.switch = a.get('href')

def normalized(url):
    return unquote(urlparse(url).path).replace('/index.html', '/')

count = 0
for english in (root / 'en').rglob('*.html'):
    relative = english.relative_to(root / 'en')
    chinese = root / relative
    assert chinese.is_file(), f'Missing Chinese counterpart: {relative}'
    zh, en = [Document(p.read_text()) for p in (chinese, english)]
    assert zh.lang == 'zh-CN' and en.lang == 'en', relative
    assert normalized(zh.switch) == normalized(en.canonical), relative
    assert normalized(en.switch) == normalized(zh.canonical), relative
    for doc in (zh, en):
        assert normalized(doc.alternates['zh-CN']) == normalized(zh.canonical), relative
        assert normalized(doc.alternates['en']) == normalized(en.canonical), relative
    count += 1
assert count >= 4, 'English edition missing'
assert 'Research, reading, and reflection.' in (root/'en/index.html').read_text()
assert 'Some questions need to be written down' in (root/'en/blog/2026/hello/index.html').read_text()
assert '有些问题需要写下来' in (root/'blog/2026/hello/index.html').read_text()
ns = {'a': 'http://www.w3.org/2005/Atom'}
for prefix, title in [('', '开篇'), ('en/', 'A beginning')]:
    feed = ET.parse(root / prefix / 'feed.xml')
    assert title in [e.text for e in feed.findall('a:entry/a:title', ns)]
    ET.parse(root / prefix / 'sitemap.xml')
print(f'{count} language pairs verified, including reciprocal links, metadata, article translation and RSS.')

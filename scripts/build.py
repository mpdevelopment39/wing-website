#!/usr/bin/env python3
"""Generate Wing's buildless product and legal website for GitHub Pages."""
from html import escape
from pathlib import Path
import json
from content import FEATURES, EXTRAS, FAQ
from legal_content import PRIVACY, TERMS

ROOT = Path(__file__).resolve().parents[1]
URL = 'https://mpdevelopment39.github.io/wing-app'
COPY = json.loads((ROOT / 'scripts/site_copy.json').read_text())
VERSION = '4'


def header(lang, kind='', depth=1):
    c = COPY[lang]
    up = '../' * depth
    other = 'en' if lang == 'es' else 'es'
    route = f'{kind}/' if kind else ''
    nav_label = 'Navegación principal' if lang == 'es' else 'Main navigation'
    language_label = 'Read in English' if other == 'en' else 'Leer en español'
    return f'''<a class="skip" href="#main">{c['skip']}</a>
<header class="header wrap">
  <a class="brand" href="{up}{lang}/" aria-label="Wing"><img src="{up}assets/wing-icon.jpg" width="44" height="44" alt=""><span class="wordmark">Wing</span></a>
  <nav aria-label="{nav_label}">
    <a class="desktop-link" href="{up}{lang}/#discover">{c['features']}</a>
    <a class="desktop-link" href="{up}{lang}/#questions">{c['questions']}</a>
    <a href="mailto:info@legal-assistant-ai.com">{c['support']}</a>
    <a class="language" href="{up}{other}/{route}" lang="{other}" aria-label="{language_label}">{other.upper()}</a>
  </nav>
</header>'''


def footer(lang, depth=1):
    c = COPY[lang]
    up = '../' * depth
    return f'''<footer class="footer wrap"><div class="footer-top">
  <a class="brand" href="{up}{lang}/"><img src="{up}assets/wing-icon.jpg" width="44" height="44" alt=""><span class="wordmark">Wing</span></a>
  <nav class="footer-links" aria-label="{'Información legal' if lang == 'es' else 'Legal information'}"><a href="{up}{lang}/privacy-policy/">{c['privacy']}</a><a href="{up}{lang}/terms-and-conditions/">{c['terms']}</a><a href="mailto:info@legal-assistant-ai.com">{c['support']}</a></nav>
</div><p class="copyright">© 2026 Wing. {c['rights']} · NIF B26788224</p></footer>'''


def page(lang, title, description, body, route='', depth=1, script=False):
    up = '../' * depth
    return f'''<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
  <meta name="color-scheme" content="light"><meta name="theme-color" content="#123c34">
  <title>{escape(title)}</title><meta name="description" content="{escape(description, quote=True)}">
  <link rel="canonical" href="{URL}/{lang}/{route}">
  <link rel="alternate" hreflang="es" href="{URL}/es/{route}"><link rel="alternate" hreflang="en" href="{URL}/en/{route}"><link rel="alternate" hreflang="x-default" href="{URL}/en/{route}">
  <meta property="og:type" content="website"><meta property="og:title" content="{escape(title, quote=True)}"><meta property="og:description" content="{escape(description, quote=True)}"><meta property="og:url" content="{URL}/{lang}/{route}"><meta property="og:image" content="{URL}/assets/wing-icon.jpg"><meta property="og:image:alt" content="Wing">
  <link rel="icon" href="{up}assets/favicon.png"><link rel="stylesheet" href="{up}styles.css?v={VERSION}">
  {f'<script src="{up}site.js?v={VERSION}" defer></script>' if script else ''}
</head><body>{body}</body></html>'''


def screen(lang, feature, hero=False):
    c = COPY[lang]
    name = feature['id']
    alt = escape(feature['alt'], quote=True)
    label = escape(c['expand'] + ': ' + feature['label'], quote=True)
    loading = 'fetchpriority="high"' if hero else 'loading="lazy"'
    return f'''<a class="screen-link device device-{name}" href="../assets/screens/{name}.jpg" data-screen aria-label="{label}"><img src="../assets/screens/{name}.jpg" width="1000" height="2174" alt="{alt}" {loading}><span class="screen-expand" aria-hidden="true">↗</span></a>'''


def feature_section(lang, feature, index):
    c = COPY[lang]
    details = ''.join(f'<li><h3>{title}</h3><p>{body}</p></li>' for title, body in feature['details'])
    return f'''<section class="feature-section wrap {'reverse' if index % 2 else ''}" id="{feature['id']}" aria-labelledby="title-{feature['id']}">
  <div class="feature-copy"><span class="eyebrow"><span class="section-number">0{index + 1}</span>{feature['label']}</span>
    <h2 id="title-{feature['id']}">{feature['title']}</h2><p class="feature-intro">{feature['intro']}</p>
    <ul class="feature-details">{details}</ul><p class="feature-note">{feature['note']}</p>
  </div>
  <figure class="feature-visual stage-{feature['id']}"><div class="screen-stage">{screen(lang, feature)}</div><figcaption>{c['gallerynote']} <span aria-hidden="true">·</span> {c['expand']} ↗</figcaption></figure>
</section>'''


def home(lang):
    c = COPY[lang]
    features = FEATURES[lang]
    shortcuts = ''.join(f'<a href="#{f["id"]}"><span>0{i + 1}</span>{f["label"]}<b aria-hidden="true">↗</b></a>' for i, f in enumerate(features))
    sections = ''.join(feature_section(lang, feature, index) for index, feature in enumerate(features))
    extra = ''.join(f'<article class="extra"><span class="eyebrow">{f["label"]}</span><h3>{f["title"]}</h3><p>{f["text"]}</p><p class="extra-detail">{f["detail"]}</p></article>' for f in EXTRAS[lang])
    faq = ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in FAQ[lang])
    body = header(lang) + f'''
<main id="main">
  <section class="hero wrap">
    <div class="hero-copy"><span class="eyebrow">{c['eyebrow']}</span><h1>{c['headline']}</h1><p class="hero-intro">{c['intro']}</p><a class="button" href="#discover">{c['explore']}<span aria-hidden="true">↗</span></a><p class="availability">{c['soon']}</p></div>
    <div class="hero-stage"><span class="hero-label">WING / {'EN TU IPHONE' if lang == 'es' else 'ON YOUR IPHONE'}</span><div class="hero-phones"><div class="hero-primary">{screen(lang, features[0], True)}</div><div class="hero-secondary">{screen(lang, features[3], True)}</div></div><p class="hero-caption">{c['gallerynote']}</p></div>
  </section>
  <section class="feature-index wrap" id="discover" aria-labelledby="feature-index-title">
    <div class="index-heading"><span class="eyebrow">{'ASÍ ES WING' if lang == 'es' else 'MEET WING'}</span><h2 id="feature-index-title">{c['introtitle']}</h2><p>{c['introbody']}</p></div>
    <nav class="feature-shortcuts" aria-label="{c['features']}">{shortcuts}</nav>
  </section>
  <div class="feature-story">{sections}</div>
  <section class="extras wrap" aria-label="{'Más funciones de Wing' if lang == 'es' else 'More Wing features'}">{extra}</section>
  <section class="faq-section wrap" id="questions"><div><span class="eyebrow">{'LO QUE QUIERES SABER' if lang == 'es' else 'GOOD TO KNOW'}</span><h2>{c['faqtitle']}</h2></div><div class="faq">{faq}</div></section>
  <section class="closing wrap"><span class="eyebrow">WING</span><h2>{c['closing']}</h2><p>{c['closingbody']}</p><span class="coming-soon">{c['soon']}</span></section>
  <div class="credits wrap"><details><summary>{c['credits']}</summary><p>{'Interfaz y capturas: MPER STUDIO S.L. Las imágenes de aves conservan las licencias de sus autores. Las capturas se han reducido y comprimido para esta web.' if lang == 'es' else 'Interface and screenshots: MPER STUDIO S.L. Bird photographs retain their authors’ licenses. Screenshots have been resized and compressed for this website.'}</p><ul>{photo_credits(lang)}</ul></details></div>
</main>
<dialog class="screenshot-dialog" aria-labelledby="screenshot-caption"><div class="dialog-bar"><p id="screenshot-caption"></p><button type="button" data-close aria-label="{c['close']}">{c['close']} <span aria-hidden="true">×</span></button></div><div class="dialog-image"><img alt=""></div></dialog>
''' + footer(lang)
    return page(lang, c['title'], c['desc'], body, script=True)


def photo_credits(lang):
    path = ROOT / 'scripts/photo-credits.json'
    if not path.exists():
        return ''
    credits = json.loads(path.read_text())
    return ''.join(f'<li><em>{escape(f["species"])}</em> — {escape(f["author"])} · <a href="{escape(f["source"], quote=True)}">{("Fuente" if lang == "es" else "Source")}</a> · <a href="{escape(f["license_url"], quote=True)}">{escape(f["license"])}</a></li>' for f in credits)


def legal(lang, kind, sections):
    c = COPY[lang]
    privacy = kind == 'privacy-policy'
    title = c['privacy'] if privacy else c['terms']
    intro = c['privintro'] if privacy else c['termsintro']
    summary = c['privsummary'] if privacy else c['termssummary']
    toc = ''.join(f'<a href="#{identifier}">{escape(heading)}</a>' for identifier, heading, _ in sections)
    content = ''.join(f'<section id="{identifier}"><h2>{escape(heading)}</h2>{copy}</section>' for identifier, heading, copy in sections)
    body = header(lang, kind, 2) + f'<main id="main" class="wrap"><div class="legal-hero"><div class="wrap"><span class="eyebrow">Wing</span><h1>{title}</h1><p>{intro}</p><p class="legal-date">{c["updated"]}</p></div></div><div class="legal-layout"><nav class="toc" aria-label="{c["contents"]}"><h2>{c["contents"]}</h2>{toc}</nav><article class="legal-copy"><div class="legal-summary"><p>{summary}</p></div>{content}</article></div></main>' + footer(lang, 2)
    return page(lang, title + ' — Wing', intro, body, kind + '/', 2)


for lang in COPY:
    out = ROOT / lang
    (out / 'index.html').write_text(home(lang))
    for kind, sections in [('privacy-policy', PRIVACY[lang]), ('terms-and-conditions', TERMS[lang])]:
        (out / kind / 'index.html').write_text(legal(lang, kind, sections))

(ROOT / 'index.html').write_text(f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="Wing — Discover the birds around you. Descubre las aves que te rodean."><title>Wing — Bird Identifier</title><link rel="stylesheet" href="styles.css?v={VERSION}"><link rel="icon" href="assets/favicon.png"><link rel="alternate" hreflang="en" href="{URL}/en/"><link rel="alternate" hreflang="es" href="{URL}/es/"></head><body><main class="language-home"><a class="brand" href="en/"><img src="assets/wing-icon.jpg" width="52" height="52" alt=""><span class="wordmark">Wing</span></a><h1>Every song, a story.</h1><p>Cada canto, una historia.</p><nav aria-label="Language / Idioma"><a class="button" href="es/" lang="es">Español ↗</a><a class="button" href="en/" lang="en">English ↗</a></nav></main></body></html>''')
(ROOT / '.nojekyll').touch()
(ROOT / 'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {URL}/sitemap.xml\n')
routes = [''] + [f'{lang}/{kind}' for lang in COPY for kind in ['', 'privacy-policy/', 'terms-and-conditions/']]
(ROOT / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + ''.join(f'<url><loc>{URL}/{route}</loc></url>' for route in routes) + '</urlset>')
print('Generated bilingual feature pages and legal pages.')

# Wing website

Public product and legal website for Wing: Bird Identifier, by MPER STUDIO S.L.

Live: https://mpdevelopment39.github.io/wing-app/es/

This repository contains only public website files. The iOS repository remains private.

## Edit and preview

Product copy lives in `scripts/content.py` and `scripts/site_copy.json`; page structure in `scripts/build.py`; styles in `styles.css`; legal text in `scripts/legal_content.py`. Run:

```sh
python3 scripts/build.py
python3 -m http.server 8765 --bind 127.0.0.1
```

Open http://127.0.0.1:8765/es/. No package installation is required. GitHub Pages serves the generated HTML from the main branch root. Commit both generated pages and their sources.

The Spanish and English landing pages present sound identification, widgets and quick access, the bird guide, species details, the journal and learning. Additional sections explain nearby observations and backups. There is no pricing or subscription-plan section on the landing pages. Subscription information remains in the legal terms.

`site.js` progressively enhances screenshot links with a keyboard-accessible image viewer. Links open the full image when JavaScript is unavailable. There are no tracking scripts, remote fonts or analytics cookies.

## Screenshots and credits

The six images in `assets/screens/` come from the original Spanish app captures used for the Wing AppScreens project, not the exported store graphics. The source mapping is recorded in `scripts/screenshot-sources.json`. Images were resized to 1,000 pixels wide and JPEG-compressed without altering the UI. The journal contains a fictional sample encounter. Both site languages label screenshots as Spanish.

Interface and branding: MPER STUDIO S.L. Bird photographs retain their original licenses. Creator attribution, source and license links are recorded in `scripts/photo-credits.json` and displayed in the expandable photograph credits at the bottom of each landing page.

## Legal pages

Privacy and terms remain available at `/en/privacy-policy/`, `/es/privacy-policy/`, `/en/terms-and-conditions/` and `/es/terms-and-conditions/` beneath the repository URL. Keep both languages aligned with the shipped app.

Company details and support contact come from the developer’s Legal Assistant AI website, as requested by its owner. Availability remains “Coming to the App Store” until the released listing can be verified.

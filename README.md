# Wing website

Public product and legal website for Wing: Bird Identifier, by MPER STUDIO S.L.

Live: https://mpdevelopment39.github.io/wing-app/es/

This repository contains only public website files. The iOS source repository remains private.

## Edit and preview

Edit `styles.css`, `scripts/build.py` (layout and bilingual product copy), or `scripts/legal_content.py` (legal copy), then run:

```sh
python3 scripts/build.py
python3 -m http.server 8765 --bind 127.0.0.1
```

Open http://127.0.0.1:8765/es/. No npm packages, build service, tracking scripts or remote fonts are needed. HTML is generated before commit; GitHub Pages serves the main branch root. Commit generated HTML alongside its sources.

Legal pages are available at `/en/privacy-policy/`, `/es/privacy-policy/`, `/en/terms-and-conditions/` and `/es/terms-and-conditions/` beneath the repository URL. Keep both languages synchronized with app functionality.

## Content credits

Wing branding and app screenshots: MPER STUDIO S.L. Screenshots show the app in Spanish and include their on-screen species imagery.

The full-width Eurasian hoopoe photograph and the corresponding app screenshot: Greg Schechter from San Francisco, USA, [original](https://commons.wikimedia.org/wiki/File:Israel._Eurasian_Hoopoe_(6497645007).jpg), [CC BY 2.0](https://creativecommons.org/licenses/by/2.0/). The photograph has been resized, compressed and cropped in the layout. Attribution appears beside the photograph.

Support and company details are taken from the developer’s existing Legal Assistant AI website, as requested by the owner. The page does not imply that Wing is already released in App Store. Update the availability text and add the verified App Store download link after release.

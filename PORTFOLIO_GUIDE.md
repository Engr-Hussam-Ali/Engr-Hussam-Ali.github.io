# Portfolio guide: how this site works and how to edit it

This file is for whoever edits the site next: Hussam, or an AI assistant working for him.

- **Read it before changing anything.**
- **Keep it up to date** when you change the structure.

- **Live site:** https://engr-hussam-ali.github.io/
- **Repository:** https://github.com/Engr-Hussam-Ali/Engr-Hussam-Ali.github.io (GitHub Pages serves the `main` branch root)
- **Local copy:** `D:\Hussam\1. My Portfolio\Portfolio Files\`
- **Owner:** Shah Syed Hussam Ali, simulation engineer (FEA, thermal-structural analysis, design optimisation)
- **Purpose:** job hunting for full-time CAE, FEA and simulation roles.
- **Location:** do not name target countries anywhere on the site; opportunities anywhere are welcome.
- **Links:** when the site or a profile points people to his GitHub, link the portfolio (https://engr-hussam-ali.github.io/), not the repository.

---

## 1. Files

```
index.html                 Home: hero, selected results, case studies, how I work, skills, experience, contact
tilt-sensor.html           Case study 1: thermal-structural FEA and layout optimisation of an IoT tilt-sensor package
settlement-dataset.html    Case study 2: automated Abaqus settlement pipeline, 108 buildings, GNN Studio 1.0
404.html                   Not-found page (GitHub Pages uses it automatically; it uses absolute "/" paths on purpose)
assets/css/site.css        The only stylesheet. Tokens at the top.
assets/js/site.js          Mobile menu, click-to-enlarge figure viewer, contents highlighting. The site works without it.
assets/fonts/              Self-hosted Archivo and Source Serif 4 (woff2) + their SIL OFL licences
assets/img/                Figures (fig-x-y.webp), hero render, OG image, favicon
robots.txt, sitemap.xml    Search engines. Add every new page to sitemap.xml.
.nojekyll                  Tells GitHub Pages to serve files as they are
PORTFOLIO_GUIDE.md         This file
tools/render_hero.py       Re-creates the hero render from the Abaqus result export (PyVista)
README.md                  Short description shown on GitHub
```

There is no build step and no framework: plain HTML, one CSS file and one small JS file. Keep it that way, so that any editor can change it safely.

---

## 2. Design system

The identity comes from the subject: finite-element results. The accent colours are the viridis contour scale used in the result plots, and the hero is a real deformed-shape render with its contour legend. Do not swap these for a generic template look.

| Token (site.css) | Value | Use |
|---|---|---|
| `--paper` | #F2F4F3 | Page background (cool grey-green, not cream) |
| `--paper-deep` | #E6ECEA | Alternate section bands (`.band`) |
| `--sheet` | #FFFFFF | Figure mounts, tables |
| `--ink` | #15232D | Text |
| `--graphite` | #4D5B66 | Secondary text, captions, labels |
| `--rule` | #C9D1D4 | Hairlines |
| `--accent` / `--accent-ink` | #17716D / #0E4F4C | Links, buttons, focus ring (viridis teal, darkened for WCAG AA) |
| `--field` | viridis gradient | Only the contour legend in the hero and the favicon |

### Type

- **Headings, navigation, labels, numbers:** Archivo (variable width). Headings use `font-stretch` 106–118 %, which gives the wide, engineering-drawing feel.
- **Reading text:** Source Serif 4, at 1.0625 rem with line-height 1.62 and a measure of at most 66 characters.
- **Numbers in tables:** Archivo with `tabular-nums`.

### Rules that keep it from looking templated

- No ALL-CAPS eyebrow labels.
- No "→" appended to links.
- No emoji icons.
- No identical card grids.
- No monospace labels.

### Numbering and motion

- Numbered markers appear only where the content really is a sequence: the five phases (`.phase-no`) and the eight pipeline steps (`ol.steps`).
- There is only one load animation: the contour legend fills from 0 to 440 µm and the render fades in. `prefers-reduced-motion` switches all motion off. Do not add scroll-reveal effects.

### Quality floor

- Pages are responsive down to 360 px.
- Keyboard focus is always visible.
- Every image has alt text and width/height attributes.
- Figures below the fold use `loading="lazy"`.

### Fonts

The fonts are self-hosted on purpose. Loading Google Fonts from Google's servers has been ruled a GDPR violation by a German court (LG München, 2022), and many readers are in the EU. Never add a `fonts.googleapis.com` link.

---

## 3. Content rules (important)

1. **Every number comes from the project reports.**
   - **Sources:** the KRISS 2026 annual report (English v4: `D:\Hussam\3. Tilt-Sensor\Review\Final_Report\KRISS_2026\Review01\Report_EN_Review01_v4.docx`) and its number register.
   - **No new numbers:** do not round differently, invent numbers or add new ones.
   - **Figure source:** the figures are the English report figures (`KRISS_2026\figures\Fig_x-y.png`).
2. **No compliance claims.** Never say a building or design is code-compliant or non-compliant. The settlement models use design rules of thumb, and the page says so.
3. **The GNN itself is future work.** The settlement case study builds and verifies the GNN's training data. Do not claim that a GNN was trained or that sensor placement was optimised.
4. **Absolute values versus rankings.** The sensor model ranks fixing conditions reliably; its absolute values are not accurate (small residual of large rotations). Keep that caveat wherever results are quoted.
5. **Phase 2 is a separate model.** The 97.8 % reduction comes from the Phase 2 layout-optimisation model. It is not carried into the fixing-condition models; say "in the optimisation model" where needed.
6. **Write plainly.**
   - **Style:** active voice and sentence case; British spelling (optimisation, modelling, colour), since most readers are international.
   - **Number format:** thousands are written with commas (10,692) on the site, even though the reports use thin spaces.
7. **National institutions.** Always make clear that his experience is with two national institutions:
   - **KRISS:** the Korea Research Institute of Standards and Science, South Korea's national measurement standards laboratory. The sensor and settlement projects are KRISS's Safety IoT project, done through Sejong University (2025 – 2027).
   - **POF:** Pakistan Ordnance Factories, Pakistan's state-owned national defence manufacturer. He was Member, Technical Committee there from 2020 to 2024.
   - **Where this appears:** the hero text, the strip under the hero (`section.orgs`), the case-study standfirsts and the Experience entries.
8. **Personal details.** Only add facts Hussam has confirmed: degree, dates, employer titles, language levels. Do not guess.

---

## 4. How to add a case study

1. **Copy the page.** Copy `tilt-sensor.html` to a new name, for example `harfm.html`, and keep the `<head>`, header, `.study-head`, `.study` grid, `dialog.viewer`, footer and script.
2. **Update the `<head>`:** `<title>`, `meta description`, `canonical`, `og:*`.
3. **Update the header and contents list.**
   - **Header:** fill `.study-head` (h1, standfirst, `dl.study-meta`).
   - **Contents list:** replace the sections. Each `<section>` needs an `id` that matches a link in `nav.toc`.
4. **Use this figure markup** (click-to-enlarge works automatically):

   ```html
   <figure class="fig">
     <button type="button" aria-label="Enlarge figure"><img src="assets/img/fig-3-1.webp" width="1800" height="600" loading="lazy" alt="Describe what the figure shows."></button>
     <figcaption><b>Short title.</b> Caption text, with (a), (b) panel letters as in the report.</figcaption>
   </figure>
   ```

   Add `class="fig narrow"` for small charts.
5. **Use this table markup:** `<div class="table-scroll"><table class="data"><caption><b>Title.</b> note</caption>…</table></div>`. Put numbers in `<td class="n">`.
6. **Link the new page in five places:**
   - the home page `#work` section: add an `article.case`, and alternate `class="case flip"` so the figure switches sides;
   - the nav of every page;
   - the `next-study` links at the bottom of the case studies;
   - `sitemap.xml`;
   - the "Selected results" table, if the project has a headline number.

---

## 5. Images

- **Format:** figures are WebP, at most 1800 px wide, quality 86. To convert a report PNG:

  ```bash
  python -c "from PIL import Image; im=Image.open('Fig_3-1.png').convert('RGB'); im.thumbnail((1800,1800)); im.save('assets/img/fig-3-1.webp','WEBP',quality=86,method=6)"
  ```

- **Naming:** lower-case `fig-<chapter>-<number>.webp`, matching the report numbering.
- **Hero render:** `hero-package.webp` was rendered with PyVista from the Abaqus results of model C13_V_ARA_FP, step THERM: deformation ×30, viridis colour map, |U| from 0 to 440 µm, transparent background.
  - **Script:** `tools/render_hero.py`. It needs the exported surface (`surf_V_ARA_FP.npz`) and displacement files (`U_V_ARA_FP_THERM`) from `2. Project Control\04_REPORTS\KRISS_2026\tools\out`.
  - **Matching legend:** if the render changes, update the legend ticks in `index.html` (`.legend-ticks`) to match.
- **Social preview:** `og-image.png` (1200 × 630) is the preview shown when the link is shared on LinkedIn.

---

## 6. Deploying

GitHub Pages publishes the repository root of `main`.

1. Copy the changed files into the repository.
2. Commit and push.
3. Wait one or two minutes, then check https://engr-hussam-ali.github.io/.

The files in `D:\Hussam\1. My Portfolio\Portfolio Files\` and in the repository should stay identical. Old versions of pages are kept in `Portfolio Files\_archive\`.

### Checks before every push

- [ ] All links work, including `index.html#contact` style anchors.
- [ ] The page renders at 390 px width without horizontal scrolling.
- [ ] Tab through the page: focus is visible, and the menu opens on mobile.
- [ ] Every new number is traceable to the report.
- [ ] `sitemap.xml` lists every page.

---

## 7. Open items

These need Hussam's input:

- **Education:** degree, field, university and years. The Experience section has no education entry yet.
- **POF role (2020–2024):** the Member, Technical Committee entry at Pakistan Ordnance Factories has no bullet points yet; add two or three confirmed responsibilities or achievements.
- **LinkedIn:** add the profile URL to `#contact` on `index.html` and to `sameAs` in the JSON-LD.
- **Photo:** none is used. Some European employers expect one on a CV, but on a website it is optional.
- **CV:** add a downloadable CV PDF (`assets/cv/…pdf`) and a button in the hero, if he wants one.
- **Other work:** for example the HARFM (hybrid axial–radial flux machine) research, as a third case study once there are results he is happy to publish.
- **Permission:** confirm with the professor / KRISS that the project figures may be shown publicly.

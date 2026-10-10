<p align="center">
  <a><img src="assets/banner.svg" alt="amorphose — Aperture Cosmology: metaphysics, astrophysics, psychophysics" width="100%"/></a>
</p>

<p align="center">
  <a href="https://aperturecosmology.com/"><img src="assets/badge-path.svg" alt="Choose Your Path"/></a>
  <a href="https://aperturecosmology.com/solar-system/"><img src="assets/badge-sse.svg" alt="Solar System Explorer"/></a>
  <a href="https://aperturecosmology.com/laniakea/"><img src="assets/badge-lfg.svg" alt="Laniakea Field Guide"/></a>
</p>

I build [interactive maps](#-solar-system-explorer) of the universe, the
[small tools](#%EF%B8%8F-vera-rubin-analytics-bot) that keep them current, and a
philosophical framework that tries to explain who is looking. Most of it lives at
**[aperturecosmology.com](https://aperturecosmology.com/)**. My day job is medical billing, where I
write tools like [OWCP AutoFill](#-owcp-autofill) to cut down on manual claim entry. I'm always
open to collaborating, especially on projects that stretch my skills in directing AI.

---

## 🌌 Aperture Cosmology

<a href="https://aperturecosmology.com/"><img src="assets/aperture-cosmology-banner.jpg" alt="Choose Your Path: three hyperbolic grids in blue, red and violet meeting at a point" width="100%"/></a>

An independent research and creative project that approaches reality from three directions.
The portal asks you to **choose your path**:

- **Metaphysics** · a formal ontology of consciousness experiencing a static, higher-dimensional
  structure through localized apertures, developed across five connected essays, with an
  eight-episode podcast and a short film alongside them.
- **Astrophysics** · interactive scientific references, including the two projects below.
- **Psychophysics** · experiential instruments: the *Aperture Dial* (binaural and isochronic
  synthesis with kaleidoscopic visuals) and a *Ganzflicker* simulator.

<table>
  <tr>
    <td width="50%"><a href="https://aperturecosmology.com/#ep1"><img src="assets/ac-podcast.jpg" alt="A translucent figure walking through a web of glowing filaments toward a smaller figure"/></a></td>
    <td width="50%"><a href="https://www.youtube.com/watch?v=YEd3X3QK2xg"><img src="assets/ac-film.jpg" alt="A head in silhouette filled with a violet nebula, set against bright rings of light"/></a></td>
  </tr>
  <tr>
    <td align="center"><sub>Podcast · <i>The Aperture Transmissions</i></sub></td>
    <td align="center"><sub>Short film · <i>The Endosymbiotic Horizon</i></sub></td>
  </tr>
</table>

<sub>Standalone HTML pages · vanilla JS · Cloudflare Workers + D1</sub>

## 🪐 Solar System Explorer

<a href="https://aperturecosmology.com/solar-system/"><img src="assets/sse-orbits.gif" alt="Solar System Explorer: the inner solar system animating, with Mercury, Venus, Earth and Mars orbiting through the asteroid belt" width="100%"/></a>

An atlas of **2,012 objects** drawn on their real orbits: planets, dwarf planets, natural
satellites, near-Earth objects, the asteroid belt, Trojans, centaurs, the Kuiper belt, the
scattered disc and detached objects, comets and all three known interstellar visitors. The atlas
keeps itself current: a daily GitHub Actions job parses the IAU's WGSBN Bulletin and swaps
provisional designations for official names as they're announced. Zoom from the inner planets out
to the detached objects, click any world to inspect its orbital elements, drop into a planet's
moon system, or switch to a sortable, searchable table of the whole database. Everything is drawn
on a plain 2D canvas with no libraries.

<table>
  <tr>
    <td width="50%"><img src="assets/sse-table-earth.jpg" alt="Table view of the database with Earth's detail panel and its Wikipedia summary"/></td>
    <td width="50%"><img src="assets/sse-outer-system.jpg" alt="Outer view: the Kuiper belt as a blue ring of orbits around the giant planets"/></td>
  </tr>
  <tr>
    <td align="center"><sub>Table view and the detail panel</sub></td>
    <td align="center"><sub>Out to Neptune and the Kuiper belt</sub></td>
  </tr>
  <tr>
    <td width="50%"><img src="assets/sse-mars.jpg" alt="Mars's satellite view with Phobos selected in the detail panel and its Wikipedia summary"/></td>
    <td width="50%"><img src="assets/sse-scattered-disc.jpg" alt="Scattered Disc view: the Kuiper belt ring wrapped in the pink orbits of the scattered disc"/></td>
  </tr>
  <tr>
    <td align="center"><sub>Satellite view and the detail panel</sub></td>
    <td align="center"><sub>Out to the Scattered Disc</sub></td>
  </tr>
</table>

## 🔭 Laniakea Field Guide

A field guide to our home supercluster, built on my paper
**[A Hierarchical Framework for Organizing the Laniakea Basin](https://aperturecosmology.com/laniakea/downloads/Bianchini_2026_Laniakea_Framework.pdf)**
(Bianchini, 2026; 86 peer-reviewed references including the Cosmicflows program). It organizes
the local universe by cosmic-web topology rather than distance or brightness:
**4 superclusters · 27 structural regions · 128 galaxy groups**, across roughly 500 million
light-years, with an interactive chart and a dedicated page for every supercluster.

<table>
  <tr>
    <td width="50%"><a href="https://aperturecosmology.com/laniakea/"><img src="assets/lfg-basin.jpg" alt="The Laniakea Basin elevation view, galaxy groups coloured by supercluster"/></a></td>
    <td width="50%"><a href="https://aperturecosmology.com/laniakea/virgo/"><img src="assets/lfg-virgo.jpg" alt="The Virgo Supercluster section with the Virgo Cluster"/></a></td>
  </tr>
  <tr>
    <td align="center"><sub>The basin, galaxy groups by supercluster</sub></td>
    <td align="center"><sub>Virgo, one of four supercluster lobes</sub></td>
  </tr>
  <tr>
    <td width="50%"><a href="https://aperturecosmology.com/laniakea/virgo/#local-sheet"><img src="assets/lfg-local-sheet.jpg" alt="The Local Sheet section of the Virgo Supercluster page, with the Andromeda Galaxy and the start of the article"/></a></td>
    <td width="50%"><a href="https://aperturecosmology.com/laniakea/#gallery"><img src="assets/lfg-gallery.jpg" alt="The Field Guide Gallery, a grid of galaxy images grouped by supercluster"/></a></td>
  </tr>
  <tr>
    <td align="center"><sub>Local Sheet, home of the Milky Way</sub></td>
    <td align="center"><sub>The Field Guide Gallery</sub></td>
  </tr>
</table>

## 🛰️ Vera Rubin Analytics Bot

A daily GitHub Actions job that watches the Minor Planet Center's TNO and Centaur lists for new
possible dwarf planets, cross-checks sizes against JPL SBDB and Johnston's Archive, and opens an
alert when something might be 190 km in radius or more. Its findings feed the Solar System
Explorer. Most new finds now come from the Vera C. Rubin Observatory. This is the live watchlist:

<!-- watchlist:start -->
<div align="center">

| Object | Status | Radius (km) | H | a (AU) | Found | By |
|---|---|--:|--:|--:|---|---|
| **2025 NE552** | 🟡 likely | ~302 | 4.33 | 53.5 | 2025-07-04 | Rubin Observatory |
| **2025 EA16** | 🟡 likely | ~273 | 4.55 | 40.6 | 2025-03-10 | DECam, Cerro Tololo |
| **2025 MZ348** | 🟡 likely | ~258 | 4.67 | 47.8 | 2025-06-30 | Rubin Observatory |
| **2025 MT387** | 🟡 likely | ~231 | 4.91 | 54.9 | 2025-06-21 | Rubin Observatory |
| **2025 MB349** | 🟡 likely | ~201 | 5.21 | 50.2 | 2025-06-21 | Rubin Observatory |

</div>

<details><summary>9 more on the watchlist</summary>

<div align="center">

| Object | Status | Radius (km) | H | a (AU) | Found | By |
|---|---|--:|--:|--:|---|---|
| **2025 MD350** | ⚪ watched | ~183 | 5.41 | 61.1 | 2025-06-21 | Rubin Observatory |
| **2025 UP145** | ⚪ watched | ~180 | 5.45 | 56.0 | 2025-10-29 | Magellan-Baade Telescope |
| **2025 NY190** | ⚪ watched | ~180 | 5.45 | 47.7 | 2025-07-02 | Rubin Observatory |
| **2015 HT198** | ⚪ watched | ~174 | 5.53 | 43.5 | 2015-04-18 | DECam, Cerro Tololo |
| **2025 OF345** | ⚪ watched | ~166 | 5.62 | 43.0 | 2025-07-18 | Rubin Observatory |
| **2025 MJ352** | ⚪ watched | ~165 | 5.64 | 46.1 | 2025-06-21 | Rubin Observatory |
| **2025 NE189** | ⚪ watched | ~157 | 5.75 | 138.5 | 2025-07-02 | Rubin Observatory |
| **2025 NK190** | ⚪ watched | ~155 | 5.77 | 46.2 | 2025-07-02 | Rubin Observatory |
| **2025 NX193** | ⚪ watched | ~152 | 5.82 | 64.4 | 2025-07-01 | Rubin Observatory |

</div>
</details>

<sub>14 objects tracked, 11 of them discovered by Rubin Observatory. ~ marks a size estimated from brightness (H) at albedo 0.09. Last change 06 Oct 2026.</sub>
<!-- watchlist:end -->

<p align="center">
  <img src="https://img.shields.io/badge/Python-0d0d10?style=flat-square&logo=python&logoColor=3776AB" alt="Python"/>
  <img src="https://img.shields.io/badge/GitHub_Actions-0d0d10?style=flat-square&logo=githubactions&logoColor=2088FF" alt="GitHub Actions"/>
</p>

## 🩺 OWCP AutoFill

<img src="assets/owcp-pipeline.svg" alt="OWCP AutoFill: a batch of CMS-1500 claims is parsed and reviewed in the desktop app, then typed into the OWCP portal" width="100%"/>

A desktop tool that turns a batch of CMS-1500 (HCFA) PDFs into filled OWCP portal bill entries.
It parses each claim locally, lets you review it, then fills the form for a manual submit.
No patient data is transmitted, stored or logged.

<p align="center">
  <img src="https://img.shields.io/badge/Python-0d0d10?style=flat-square&logo=python&logoColor=3776AB" alt="Python"/>
  <img src="https://img.shields.io/badge/Selenium-0d0d10?style=flat-square&logo=selenium&logoColor=43B02A" alt="Selenium"/>
  <img src="https://img.shields.io/badge/Tkinter-0d0d10?style=flat-square&logo=python&logoColor=c9a84c" alt="Tkinter"/>
</p>

## 📊 Languages and tools

<p align="center">
  <img src="assets/top-languages.svg" alt="Most used languages across my repositories"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/JavaScript-0d0d10?style=flat-square&logo=javascript&logoColor=F7DF1E" alt="JavaScript"/>
  <img src="https://img.shields.io/badge/HTML5-0d0d10?style=flat-square&logo=html5&logoColor=E34F26" alt="HTML5"/>
  <img src="https://img.shields.io/badge/CSS-0d0d10?style=flat-square&logo=css&logoColor=663399" alt="CSS"/>
  <img src="https://img.shields.io/badge/Python-0d0d10?style=flat-square&logo=python&logoColor=3776AB" alt="Python"/>
  <img src="https://img.shields.io/badge/Cloudflare_Workers-0d0d10?style=flat-square&logo=cloudflareworkers&logoColor=F38020" alt="Cloudflare Workers"/>
  <img src="https://img.shields.io/badge/GitHub_Actions-0d0d10?style=flat-square&logo=githubactions&logoColor=2088FF" alt="GitHub Actions"/>
</p>

<p align="center"><sub>Language card counts inline &lt;script&gt; and &lt;style&gt; as JavaScript and CSS, and skips vendored data. Refreshed weekly by <a href=".github/workflows/refresh-profile.yml">a workflow</a> in this repo.</sub></p>

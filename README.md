# Junming Zhang — personal website

English portfolio for applied AI roles and PhD opportunities, published at <https://junming3702-cmyk.github.io/>.

## Pages and materials

- [`index.html`](index.html): personal positioning, education, quantity-surveying experience, four research directions, selected projects, methods and direct contact.
- [`tendering.html`](tendering.html): independent AI-project contributions, separate IPV01 outcomes, public synthetic examples and implementation evidence.
- [`bim-vr.html`](bim-vr.html): individual MSc dissertation and interactive-prototype brief; demonstration materials are not yet public.
- [`qgis.html`](qgis.html): co-authored Community Living Circle study, original maps, historical findings and source-verified individual contribution.
- [Public CV](assets/docs/Junming_Zhang_Public_CV.pdf): two-page professional / academic summary with portfolio links.
- [Coursework report excerpts](assets/docs/Community_Living_Circle_Report_Excerpts.pdf): selected original pages with attribution and contribution table.

The manuscript remains submitted and private. Task-level IPV01 records are not public. Functional tests, synthetic retrieval results and practitioner appraisal are distinct evidence types. Example tabs remain readable without JavaScript; legacy project anchors redirect to the tendering case study.

## Development

Plain HTML, CSS and a small progressive-enhancement script, with no build step, third-party runtime, analytics or external font dependency.

```sh
python3 -m http.server 8765
```

Open `http://localhost:8765`. GitHub Pages serves the `main` branch root.

Optional document maintenance requires ReportLab and pypdf:

```sh
python scripts/build_public_cv.py
python scripts/extract_qgis_evidence.py /path/to/source-report.pdf
```

The original coursework report is owner-supplied and is not required to serve the site. The extraction script reproduces original pages and embedded figures without redrawing results.

## Design and attribution

The approved design uses warm white, graphite and sage, Times New Roman, a faint Jiangnan background and architectural concept images. `styles-light.css` layers over the base and profile styles. Earlier archive and water-town treatments remain as history but are not loaded.

The Tom avatar and wordmark are retained. Generated artwork is labeled as conceptual; original coursework maps are distinguished and credited to the group. No concept illustration is presented as a prototype screenshot or measured result.

Facts come from owner-supplied CVs and explicit corrections. The 28 November 2026 update confirms the BIM–VR prototype from the owner's statement, adds report-grounded QGIS roles and artifacts, separates IPV01 endpoints and publishes a curated CV without private phone numbers or identifiers.

- [Content evidence and attribution](docs/CONTENT_EVIDENCE.md)
- [Light visual style](docs/LIGHT_STYLE.md)
- [Historical image prompts](docs/IMAGE_PROMPTS.md)
- [Historical water-town design](docs/WATER_TOWN_DESIGN.md)
- [Chinese architectural illustrations](docs/CHINESE_ARCHITECTURE_ASSETS.md)

# Junming Zhang — personal website

English portfolio for applied AI roles and PhD opportunities, published at <https://junming3702-cmyk.github.io/>.

## Content

- Personal homepage: education, quantity-surveying experience in Hong Kong and mainland China, research interests, selected work, methods and opportunities.
- Selected work includes the AI tendering prototype, BIM–VR master's research for modular integrated construction, and a collaborative QGIS study of Hong Kong community living circles.
- PhD research interests: industry digitalization, evidence-grounded decision support, human–AI collaboration, and future cross-sector transfer.
- Dedicated case study: [`tendering.html`](tendering.html), retaining the research summary, independent contributions, IPV01 study summary, public synthetic example tabs and verification links.
- The homepage's existing `#project` link leads to selected work; former contribution and example anchors continue to the case study through progressive enhancement.

Research interests and intended productivity improvements are presented as future evaluation goals. The current project manuscript is submitted and is not published on this website.

## Development

The site uses plain HTML, CSS, SVG and a small progressive-enhancement script. It has no build step, third-party runtime, analytics or external font dependency.

```sh
python3 -m http.server 8765
```

Open `http://localhost:8765`. Deploy the `main` branch root through GitHub Pages.

## Design and provenance

The current design restores the earlier top navigation and vertical portfolio layout. It uses Times New Roman, dark frosted-glass panels and restrained amber and jade accents. The decorative red seal was removed at the owner’s request. A photorealistic GPT Image Jiangnan canal scene in dark rain and mist fills the background. The new treatment is in `styles-water.css`, layered over the existing base styles. The previous archive stylesheet remains in the repository as design history and is not loaded.

The project cover and four research-interest illustrations use a consistent GPT Image treatment: traditional Chinese timber architecture, modern photorealistic rendering, structural layers and restrained jade evidence/workflow lines. The approved project cover links an exploded hall to three public synthetic review examples; these visual connections are conceptual, not a claim of implemented BIM-to-contract tracing. The supplied Tom avatar remains beside an equally tall Tom wordmark. No third-party biography, qualifications or institutional affiliation is reused. The backdrop is generated from the owner's written scene description and is credited in the footer.

Project descriptions derive from the owner's confirmed contribution statements and the linked public repository. The verification count is explicitly dated and refers to the existing public verification record, not a new website test.

The case-study page includes a public research summary and three accessible example tabs: source retrieval, independent evidence-gate fixtures, and a document-visibility record. All examples remain readable without JavaScript. The examples are separate component checks, not a fabricated end-to-end LLM run. The page distinguishes the IPV01 summary from the publicly available synthetic records.

The 27 November 2026 revision makes personal background and multiple projects the homepage's organizing structure. `styles-profile.css` adds responsive layouts in the existing palette and typography; the water-town backdrop and approved illustrations are retained. Education, employment and earlier academic work come from the owner's existing CV documents, with newer explicit statements taking precedence over older project-role and manuscript-status wording. No CV file or private study records are published by this revision.

- [Content evidence and attribution](docs/CONTENT_EVIDENCE.md)
- [Final image prompts and provenance](docs/IMAGE_PROMPTS.md)

- [Water-town visual design and background prompt](docs/WATER_TOWN_DESIGN.md)

- [Chinese architectural illustrations and source-grounded case labels](docs/CHINESE_ARCHITECTURE_ASSETS.md)

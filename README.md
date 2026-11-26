# Junming Zhang — personal website

English portfolio for applied AI roles and PhD opportunities, published at <https://junming3702-cmyk.github.io/>.

## Content

- PhD research interests: industry digitalization, evidence-grounded decision support, human–AI collaboration, and future cross-sector transfer.
- Featured project: [Evidence-grounded AI for construction tendering](https://github.com/junming3702-cmyk/-LLM).
- Direct links to public synthetic examples, generated outputs and verification records.
- A contribution statement distinguishing the author's role, AI-assisted implementation and expert participation.

Research interests and intended productivity improvements are presented as future evaluation goals. The current project manuscript is submitted and is not published on this website.

## Development

The site uses plain HTML, CSS, SVG and a small progressive-enhancement script. It has no build step, third-party runtime, analytics or external font dependency.

```sh
python3 -m http.server 8765
```

Open `http://localhost:8765`. Deploy the `main` branch root through GitHub Pages.

## Design and provenance

The current design restores the earlier top navigation and vertical portfolio layout. It uses Times New Roman, dark frosted-glass panels, restrained amber and jade accents, and a small decorative red seal. A photorealistic GPT Image Jiangnan canal scene fills the background. The new treatment is in `styles-water.css`, layered over the existing base styles. The previous archive stylesheet remains in the repository as design history and is not loaded.

Five existing GPT Image research illustrations retain their navy, grey-green and ivory palette. The supplied Tom avatar remains beside an equally tall Tom wordmark. No third-party biography, qualifications or institutional affiliation is reused. The backdrop is generated from the owner's written scene description and is credited in the footer.

Project descriptions derive from the owner's confirmed contribution statements and the linked public repository. The verification count is explicitly dated and refers to the existing public verification record, not a new website test.

The project section includes a public research summary and three accessible example tabs: source retrieval, independent evidence-gate fixtures, and a document-visibility record. All examples remain readable without JavaScript. The examples are separate component checks, not a fabricated end-to-end LLM run.

- [Content evidence and attribution](docs/CONTENT_EVIDENCE.md)
- [Final image prompts and provenance](docs/IMAGE_PROMPTS.md)

- [Water-town visual design and background prompt](docs/WATER_TOWN_DESIGN.md)

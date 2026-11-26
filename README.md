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

The current design follows the owner's supplied editorial portfolio reference: a warm paper background, monospaced typography, fine rules and three desktop columns for profile, research/work, and public records. The central reading order and existing evidence-based content remain intact. At smaller widths the archive moves below the main content, then the profile and content form a single reading column. The stylesheet is `styles-archive.css`.

Five GPT Image illustrations retain the earlier navy, grey-green and ivory palette. The supplied Tom avatar sits beside an equally tall Tom wordmark. Reference images inform visual style only; no third-party identity, biography, qualifications or institutional affiliation is reused.

Project descriptions derive from the owner's confirmed contribution statements and the linked public repository. The verification count is explicitly dated and refers to the existing public verification record, not a new website test.

The project section includes a public research summary and three accessible example tabs: source retrieval, independent evidence-gate fixtures, and a document-visibility record. All examples remain readable without JavaScript. The examples are separate component checks, not a fabricated end-to-end LLM run.

- [Content evidence and attribution](docs/CONTENT_EVIDENCE.md)
- [Final image prompts and provenance](docs/IMAGE_PROMPTS.md)

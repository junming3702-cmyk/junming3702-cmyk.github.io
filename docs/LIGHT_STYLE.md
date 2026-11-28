# Light visual refresh — 28 November 2026

This is a presentation-only revision based on the owner's approved light portfolio preview. The existing English copy, accessibility labels, section IDs and navigation behavior are retained. The personal homepage and the separate tendering case study share the same light color system and Times New Roman typography.

## Visual system

- Warm white `#fafbf9`, graphite `#20302f`, sage `#416656`, thin dividers and restrained corners.
- An exploded Chinese timber-building hero connects construction knowledge with digital methods. Work thumbnails are conceptual illustrations, not project outputs or research evidence.
- The original Jiangnan backdrop remains as a faint watermark so its existing attribution stays accurate. Original dark artwork and CSS remain available in the repository.
- Four research icons extend the repository's SVG illustration system with light architectural outlines; their existing alternative descriptions are retained.

## Generated assets

Built-in GPT Image was used, with the approved preview `exec-53b91ac0-44e2-4f0e-b958-335643745046.png` as the style reference. Originals remain in the image-generation output directory. The following JPEG copies are optimized for the website without altering the generated composition:

| Asset | Repository file |
| --- | --- |
| Hero | `assets/light/hero-v1.jpg` |
| Tendering | `assets/light/tendering-v1.jpg` |
| BIM and VR | `assets/light/bim-vr-v1.jpg` |
| Spatial analysis | `assets/light/qgis-v1.jpg` |

## Validation

- Compared against `d00cbac28ecfa4c43505214ed9ead6e69b0c40f4`: all 138 homepage text nodes and 169 case-study text nodes are unchanged after whitespace normalization.
- Existing section IDs, headings, ARIA attributes, alternative text and navigation links are preserved. The full-size hero-artwork link follows the new asset.
- `script.js` is byte-identical to the previous release.
- Browser checks at 1440, 768, 390 and 320 px: no horizontal overflow; loaded assets and readable light styling verified.
- Verified homepage / case-study navigation, example tabs, keyboard navigation, Chinese-input disclosure and legacy `#example-gate` redirection.
- Browser console showed no errors during the checks.

## Prompts

### hero

```text
Use case: precise-object-edit / website illustration extraction. The reference is an approved personal portfolio mockup. Extract and recreate ONLY its large upper-right exploded Chinese timber building illustration as a high-resolution standalone square artwork. Preserve the exact approved light architectural visualization: floating dark grey tiled roof, timber roof frame and column/beam layers, off-white lower courtyard building, pale stone platform, a few quiet sage data nodes and very fine grid lines, subtle trees. No website UI, browser chrome, text, letters, avatar, badges, borders or unrelated content. Soft diffuse daylight, fine architectural detailing, white/very light grey background #F8FAF8 that reaches the edges; understated warm wood and desaturated sage accents. Center the whole complete building with breathing room, all roof and foundation visible. This asset will be the hero artwork of a real website. Do not include the rest of the webpage. Opaque background.
```

### tendering

```text
Use case: precise-object-edit / website illustration extraction. From the approved webpage reference, recreate ONLY the illustration in the lower-left Selected work card as one high-resolution standalone LANDSCAPE 3:2 artwork. A miniature contemporary concrete frame building model on a pale slab, linked by two subtle sage lines to several floating off-white tender document sheets with understated grey rules and pale sage highlights. Preserve the preview's clean photoreal architectural model style, soft light grey and white materials, diffuse daylight, quiet shadows, desaturated sage. Pure soft white #F8FAF8 background. No webpage, borders, labels, letters, numbers, logos, interface, claims or buttons; the document linework must remain abstract. Entire composition visible and centered, 10 percent margin. This is a conceptual illustration, not a real project or result.
```

### bim

```text
Use case: precise-object-edit / website illustration extraction. From the approved webpage reference, recreate ONLY the illustration in the lower-middle Selected work card as one high-resolution standalone LANDSCAPE 3:2 artwork. A crisp pale-white miniature modular building of stacked rectangular units, one upper module lifted slightly above it on fine crane cables, and a small understated translucent grey VR headset to one side connected by light dashed projection lines. Match the preview's fine architectural model style, soft grey windows, subtle wood detail, diffuse daylight, gentle ambient shadows, #F8FAF8 background. No webpage, text, letters, numbers, labels, logos, buttons, borders or diagrams with invented results. All elements fit comfortably within the image, clean generous margins. Conceptual BIM/VR research illustration.
```

### qgis

```text
Use case: precise-object-edit / website illustration extraction. From the approved webpage reference, recreate ONLY the illustration in the lower-right Selected work card as one high-resolution standalone LANDSCAPE 3:2 artwork. A clean abstract top-down urban street network in thin white lines over very pale grey city blocks, a quiet pale blue river near one side, and one translucent sage-green walking catchment circle centered on a small white location node with fine white radial connections. Elegant restrained geographic analysis visual, clear simple geometry, very light grey/sage/blue palette matching the approved page. No text, numbers, street labels, legend, actual place claims, browser, UI, card border or button. This must remain an explicitly schematic illustration with no real data or fabricated statistics. High-resolution edge-to-edge flat map artwork.
```


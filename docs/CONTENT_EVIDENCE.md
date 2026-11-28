# Content evidence and attribution

## Portfolio evidence improvements — 28 November 2026

The owner accepted the recruiter / prospective-supervisor review and requested completion. This update retains the light visual style, Times New Roman, personal-homepage-first structure and example behavior. The content authorization supersedes the previous visual-only boundary.

### Positioning and public CV

The owner-supplied `Junming_Zhang_Academic_CV_Oct2026.docx` and `Junming_Zhang_Academic_CV_Nov2026_Revised.docx` support the education, employment, tools, languages, professional email and February 2026 start of independent AI research. The new two-page `assets/docs/Junming_Zhang_Public_CV.pdf` is a curated portfolio version, not an upload of either private original. Phone numbers, grades, student identifiers and unrelated private material are omitted. Its source is `scripts/build_public_cv.py`.

The hero connects quantity-surveying experience to designing and evaluating AI-assisted construction workflows. The four research directions pose future questions about information bottlenecks, traceability under change, expert corrections and cross-sector transfer. No current affiliation or doctoral enrollment is inferred.

### BIM–VR

The academic CV records the dissertation title, support concept, lifting-path / spatial / logistics scope and qualitative practitioner-feedback analysis. On 28 November 2026 the owner confirmed that an **interactive VR prototype was implemented**, with materials on another computer. This supersedes the earlier concept-only description. Prototype existence is owner-reported; the executable, screenshots, hardware configuration and demonstration were not inspected.

`bim-vr.html` provides a research brief, individual contribution and material-availability statement. The illustration is identified as a concept, not a prototype screenshot. No effectiveness metric, deployment, participant count or unverified software stack is added.

### Community Living Circle coursework

The complete 19-page `15分钟生活圈.pdf` was read and relevant pages visually checked. Authors: Chen Xinying, Qu Shiyan, Xu Junyi and Zhang Junming; CA6241 Group 9, City University of Hong Kong, April 2024.

| Claim / asset | Original evidence and boundary |
| --- | --- |
| 103 centres, walking isochrones and separate 1 km buffers | Methodology, printed pp. 9–10. Walking-time areas and circular buffers are distinct analyses. |
| Walking-circle and service-distribution maps | Figures 3 and 5, printed pp. 10 and 12. Embedded images extracted byte-for-byte, not AI-generated or redrawn. |
| 74 healthcare and 71 education communities below the study's overall per-capita benchmark | Printed p. 13, out of 103 communities. Historical group findings; no new computation or current-city claim. |
| Junming's contribution | Contribution table, printed p. 18: conclusions, implications and limitations; corresponding presentation/report sections; interim-report presentation integration. Column alignment was visually verified. Maps, data preparation and analysis remain group outputs. |
| Limits | Printed p. 16: source coverage, sample representativeness, implementation challenges and measured access versus lived experience/use. |

`qgis.html` links original figures and a seven-page excerpt: a new attribution cover plus unchanged source PDF physical pages 1, 11, 13, 14, 17 and 19. Original printed page numbers remain visible. `scripts/extract_qgis_evidence.py` rebuilds it from a supplied source path without embedding a private filesystem location. It is coursework, not a peer-reviewed publication.

### Tendering evidence

The first results panel now precedes functional tests and synthetic metrics. It separates **24/30 delivery**, **23/24 traceability passes by each evaluator**, and **21/24 and 16/24 professional acceptance**. It does not assert that the same 23 records passed both evaluators, calculate overall accuracy, or claim full-tender deployment, productivity gains or generalization.

The original research summary is retained with a clarification of the per-evaluator denominator. No task-level IPV01 data or private manuscript is published. Synthetic examples remain independent component demonstrations.

Design rationale was checked against `phase2_public/ARCHITECTURE.md` and the linked implementation. The hierarchy controls eligibility before within-level BM25/dense ranking; prompts and temperature 0.1 are design choices, while explicit gates validate release conditions. No causal temperature benefit is claimed. Research contributions are expressed as record design, paired appraisal and case-derived judgment-preservation / continuation requirements, separately from established retrieval components.

The public `phase2_public/evaluation/expert_review/README.md` describes a planned protocol. It supports evaluation planning only and is **not proof that IPV01 appraisal data have been published**.

Earlier dated records below are superseded where this update changes publication or prototype status.

## Personal background and portfolio structure — 27 November 2026

The owner requested a personal homepage with broader background and multiple works, retaining the established visual style, and selected a separate page for the detailed LLM project case study.

Education, employment dates, geographical context, earlier academic work, tools and language proficiency were checked against the owner's existing `Junming_Zhang_Academic_CV_Oct2026.docx` and the 24 November 2026 role-specific Chinese CV. These are owner-supplied biographical records, not independently authenticated credentials. Neither CV is uploaded by this update.

| Homepage statement | Source and boundary |
| --- | --- |
| MSc in Construction Management, City University of Hong Kong, 2023–2024 | Academic CV; dissertation concerns BIM-based VR support for MiC. The work is described as a support concept and practitioner-feedback analysis, not an independently verified deployed system. |
| BEng in Quantity Surveying, Chengdu University, 2018–2022 | Academic CV; undergraduate thesis concerns VR in architectural education. |
| Assistant Quantity Surveyor, Currie & Brown (China) Limited, Sep 2024–Sep 2025 | Both CVs identify the experience as Hong Kong. The firm's identity does not imply employment in the UK. |
| Assistant Quantity Surveyor, RongHui Project Management Co., Ltd, Jun 2022–Jun 2023 | Both CVs; work described as mainland China, without adding an unverified city or client. |
| BIM–VR master's research | Academic CV; individual dissertation work, with no invented performance or adoption metrics. |
| 15-minute Community Living Circle, April 2024 | Both CVs; collaborative course study using QGIS, POI and demographic data across 103 Hong Kong community centres. Co-authorship is preserved. |
| Tools, professional methods and language proficiency | Academic CV; listed as experience, without adding mastery levels, certifications or new achievements. |

The 26 November owner clarification of independent AI-project authorship and submitted manuscript status overrides older CV wording. A role-specific CV's industry-only positioning is not reused: the owner explicitly keeps employment and PhD opportunities equally important. No current doctoral enrollment, admission announcement, personal contact details or employer outcome metric is inferred.

The existing tendering summary, contributions and examples are retained in `tendering.html`. Its added availability sentence reflects the 26 November repository audit: the public repository provides synthetic examples and verification records but does not contain task-level IPV01 study records. No private study material is uploaded or newly characterized as public.

Updated 26 November 2026. Source repository: [Evidence-grounded AI for construction tendering](https://github.com/junming3702-cmyk/-LLM), reviewed at commit `fc820494cf730f154a5039cc8fe0080fd7e06923`.

## Personal contribution

Authorship and design responsibility follow the owner's clarification on 26 November 2026: Junming Zhang independently conceived, designed and developed the project. This includes defining its purpose and research questions, designing the complete program architecture, the legal-authority RAG hierarchy, BM25 + dense retrieval, the ordered L1–L4 cascade, the reasoning scheme and gate rules, and completing implementation, output acceptance, refinement and evaluation planning. This clarification supersedes the earlier architecture-support attribution.

AI tools assisted code implementation and experimental table preparation under the owner's direction. Domain practitioners appraised outputs and contributed interview feedback to evaluation design.

The following public artifacts support the described mechanisms and settings. Design authorship is attributed from the owner's explicit statement.

| Design contribution | Public implementation evidence |
| --- | --- |
| Complete program architecture | [System workflow](https://github.com/junming3702-cmyk/-LLM#for-product-and-applied-ai-teams) |
| Legal-authority hierarchy, ordered retrieval and BM25 + dense ranking | [Hierarchy retriever](https://github.com/junming3702-cmyk/-LLM/blob/main/phase2_public/src/hierarchy_cascade_retriever.py), including `LEVEL_ORDER`, level/phase partitions and hybrid scoring; [ordered execution](https://github.com/junming3702-cmyk/-LLM/blob/main/phase2_public/src/run_hierarchy_gated_llm_smoke.py) |
| Source-bound reasoning with temperature 0.1 | [Reasoning runner](https://github.com/junming3702-cmyk/-LLM/blob/main/phase2_public/src/run_hierarchy_gated_llm_smoke.py), including its evidence-constrained prompts and request configuration |
| Deterministic release gates and gap conditions | [Evidence gate](https://github.com/junming3702-cmyk/-LLM/blob/main/phase2_public/src/llm_abstention_gate.py), [task gate](https://github.com/junming3702-cmyk/-LLM/blob/main/phase2_public/src/task_subconclusion_v1.py) and [gap protocol](https://github.com/junming3702-cmyk/-LLM/blob/main/phase2_public/src/task_gap_protocol_v1.py) |
| Evaluation planning and output review | [Expert-review protocol](https://github.com/junming3702-cmyk/-LLM/blob/main/phase2_public/evaluation/expert_review/README.md) and [public output examples](https://github.com/junming3702-cmyk/-LLM/blob/main/docs/portfolio/sample-results/RESULTS.md) |

The low-temperature setting is described as part of a reasoning design intended to limit overgeneralization of legal provisions. It is not presented as a standalone guarantee of correct legal interpretation or as a measured causal effect. This attribution update does not change research results or claim commercial deployment or productivity gains.

## Project summary

On 26 November 2026, the owner supplied replacement wording for the research-summary headline and the Question, Approach and Evidence paragraphs. The website reproduces that wording, including ordered regulatory retrieval (`L1–L4`), deterministic release gates, five appraisal dimensions and the `IPV01` project results.

The owner-provided summary reports 24 delivered records from 30 selected tasks; source-traceability passes on 23 of 24 delivered records by each of two domain evaluators; acceptance of 21 and 16 records respectively; and case analyses `IPV-U10`, `IPV-U14` and `IPV-U02/U22`. This is the source for the newly stated project-specific results. They were not independently recomputed during this website text update. The public synthetic examples below remain separate component demonstrations. No private manuscript or evaluation workbook was uploaded. Manuscript status remains **submitted**, based on the owner's statement.

## Example views

| Website view | Source | Fields shown and interpretation |
| --- | --- | --- |
| Source retrieval | [retrieval.json](https://github.com/junming3702-cmyk/-LLM/blob/main/docs/portfolio/sample-results/retrieval.json) | Synthetic input, 20-chunk corpus, ranks, source locators, BM25 scores, first chunk ID and stored source version. English explanatory text summarizes the stored Chinese sample, without asserting current legal applicability. |
| Evidence checks | [review.json](https://github.com/junming3702-cmyk/-LLM/blob/main/docs/portfolio/sample-results/review.json) | Independent `DEMO-REVIEW` and `DEMO-UNKNOWN-SOURCE` fixtures, corrected statuses, final conclusion types and empty evidence for the unregistered-source fixture. These responses were not generated from the retrieval example. |
| Review record | [task-result.json](https://github.com/junming3702-cmyk/-LLM/blob/main/docs/portfolio/sample-results/task-result.json) | Observed narrative, locator `p186-b6`, pending chart, partial task completion, unavailable legal conclusion and required human review. No human review decision is invented. |

## Evaluation evidence

- **Functional verification:** 97 core + 28 bundle unittest cases, with five additional script suites reported separately; [26 November 2026 verification record](https://github.com/junming3702-cmyk/-LLM/blob/main/docs/portfolio/VERIFICATION.md).
- **Historical retrieval:** 98.08% hierarchical Evidence Hit@5 and MRR 0.9135 on 52 supported synthetic issues; [metric definitions](https://github.com/junming3702-cmyk/-LLM/blob/main/phase2_public/evaluation/retrieval/metrics.md). These were not rerun for this website revision and are not substituted for real-project effectiveness.
- **Expert evaluation:** the website links the [public expert-review protocol](https://github.com/junming3702-cmyk/-LLM/blob/main/phase2_public/evaluation/expert_review/README.md) without publishing private workbooks or claiming an unreported aggregate score.

## Research interests and imagery

Industry digitalization is the overarching goal, evidence-grounded decision support is the technical approach, and human–AI collaboration includes evaluation and feedback. Cross-sector transfer is explicitly a longer-term direction. Quality, efficiency, adoption and productivity improvements remain research goals.

The generated illustrations are labeled as concepts. They do not depict an implemented user interface, a named project, real study participants or measured results. The [image prompt record](IMAGE_PROMPTS.md) identifies their production method and style brief.

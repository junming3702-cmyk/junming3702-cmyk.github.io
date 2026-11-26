# Content evidence and attribution

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

# Content evidence and attribution

Updated 26 November 2026. Source repository: [Evidence-grounded AI for construction tendering](https://github.com/junming3702-cmyk/-LLM), reviewed at commit `fc820494cf730f154a5039cc8fe0080fd7e06923`.

## Personal contribution

The owner confirmed these responsibilities: assisting program architecture design; reviewing and accepting outputs; adjusting and optimizing the program; and developing evaluation plans. AI tools assist code implementation and experimental table preparation. Expert participants help check effectiveness and inform evaluation design through interviews.

The website preserves that scope. Linked project artifacts illustrate related system behavior and evaluation material. They are not presented as proof that the owner individually authored every component, devised each gate rule, or independently implemented the code. No unverified project duration, commercial deployment, productivity improvement or individual design decision is added.

## Project summary

The public research summary describes the problem, implementation approach and observable sample behavior documented in the [main README](https://github.com/junming3702-cmyk/-LLM/blob/main/README.md). It is a portfolio overview, not the private manuscript abstract. Manuscript status remains **submitted**, based on the owner's statement.

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

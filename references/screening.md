# Reference Screening Rules

## Goal

Download and read multiple candidate PDFs first, then select the papers that best support the user's paper. The number of downloaded papers is usually larger than the number of final cited papers.

## Scoring Dimensions

| Dimension | Prefer | Reject |
|---|---|---|
| Authenticity | Searchable on CNKI; detail page opens | Not found on CNKI or metadata mismatch |
| PDF status | `PDF下载` exists and PDF downloads successfully | No PDF, failed download, or only non-PDF formats |
| Full-text readability | PDF body is readable and evidence sentences can be extracted | Garbled, missing pages, or cannot parse |
| Relevance | Directly supports a specific paper claim | Only title, abstract, or keywords look similar |
| Technical specificity | Matches modules, methods, system structure, or implementation | Vague background with no support for concrete text |
| Source quality | Meets user requirements such as Core, CSCD, EI, theses, or recent years | Violates explicit user quality constraints |
| Non-duplication | Supports a distinct section or claim | Duplicates another selected paper's support role |

## Acceptable Support Roles

- Background: explains significance and application context.
- Related work: describes common components or research trends.
- Scheme justification: supports choosing a module, chip, communication method, or algorithm.
- Hardware design: supports controller, communication module, motor driver, sensor, power, etc.
- Software design: supports command parsing, PWM control, state machine, communication flow, upper-computer interaction, etc.
- Experiment/testing: supports simulation, physical debugging, and verification methods.
- Conclusion/outlook: supports future extension directions.

## Rejection Reasons

Record rejection reasons in the tracking table:

- Not found on CNKI.
- No PDF download entry.
- Only non-PDF formats.
- Download failed.
- PDF cannot be parsed.
- Topic mismatch.
- Only abstract-level relevance.
- Duplicates an already selected paper.
- Does not satisfy user requirements such as Core, recent years, or thesis type.
- PDF body cannot support the target paper sentence.

## PDF Evidence Sentence Rule

Every final cited reference must have a complete sentence from the PDF full text. Evidence may come from body text, figure/table notes, design methods, experiment/testing sections, or conclusions.

Do not copy long PDF passages into the paper body. The paper body should be paraphrased naturally; the original evidence sentence belongs in the verification notes and tracking table.

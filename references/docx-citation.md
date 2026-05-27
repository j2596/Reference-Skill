# Word Citation Rules

## Before Editing

1. Extract the full DOCX text, headings, and paragraph order.
2. Record paragraph indexes or stable text snippets for citation insertion points.
3. Check whether body citation numbers already exist.
4. Check whether a bibliography already exists.
5. If references already exist, complete CNKI authenticity checks and PDF full-text verification first.

## Body Citations

- Citation numbers must follow first appearance in the body.
- Default to at most one citation number per paragraph.
- Place the citation number near the specific supported claim.
- Avoid citation piles such as `[1][2][3]`.
- Rewrite the original sentence when needed so the paper's argument and PDF evidence fit naturally.
- Avoid repetitive wording like "X et al. pointed out"; use concise academic phrasing when the user wants natural writing.
- Do not paste long PDF original text into the body. Keep original PDF evidence sentences in the verification notes.

## Bibliography

The final bibliography must contain only PDF-verified references. Prefer GB/T 7714-2025 entries exported from CNKI's `li.btn-quote[title="引用"]` button.

Rules:

1. Bibliography numbers must match body citation numbers exactly.
2. References must be ordered by first body citation.
3. Each paper appears only once.
4. Remove references not cited in the body unless the user asks to keep them.
5. Remove papers that were not downloaded as PDFs, were not read as full text, only offered non-PDF formats, failed to download, or could not be found on CNKI.
6. If the user provides a school template, follow it. Otherwise, prioritize content correctness over typography.

## Saving

- Save as a new file; do not overwrite the user's original.
- Suggested suffix: `_知网参考文献已插入.docx`.
- Preserve headings, chapters, body order, acknowledgements, appendices, and unrelated content.

## Optional Formatting

If the user requests formatting, normalize:

- Chinese font: SimSun.
- English font: Times New Roman.
- Font size, indentation, and line spacing according to the school template or original style.
- Bibliography may use hanging indent.

---
name: cnki-reference-writer
description: Use the user's logged-in Chrome CNKI account with PDF download access to verify, replace, and add references for Chinese theses, graduation papers, course designs, and technical reports. Use when Codex must search CNKI, download PDF-only candidate papers, obtain GB/T 7714-2025 citation entries, read full PDFs, screen suitable references, rewrite or add body text so citations match PDF evidence, insert verified citations into DOCX files, rebuild bibliographies, and produce reference verification notes.
---

# CNKI Reference Writer

Turn a Chinese paper with missing, insufficient, fake, weak, or unverifiable references into a Word document with CNKI PDF-verified citations.

## Required Confirmation

Before controlling Chrome or downloading from CNKI, confirm:

1. Chrome is already logged in to CNKI.
2. The account or institution has PDF download permission.
3. The user can manually handle slider verification, permission prompts, blocked downloads, or payment prompts if they appear.
4. The paper DOCX path, output folder, PDF folder, and desired reference count or range are clear.
5. Source-quality preferences are clear, such as Peking University Core, CSCD, EI, master's or doctoral theses, recent-five-year journals, or ordinary journals.
6. The task is PDF-only: papers without downloadable PDFs are skipped and recorded.

## Non-Negotiable Rules

- Use the user's Chrome session for CNKI because login state, institution access, and download permission live there.
- When the `chrome:Chrome` skill is available, use its Node REPL bootstrap path first: load the Chrome plugin `scripts/browser-client.mjs`, call `setupBrowserRuntime({ globals: globalThis })`, then use `agent.browsers.get("extension")`. Do not assume Chrome is unavailable just because no dedicated Chrome tool appears in tool search.
- Final citation evidence must come from PDF full text only.
- Do not use CNKI abstracts, keywords, titles, search snippets, HTML reading pages, reference lists, or AI summaries as final evidence.
- Download PDFs only from the article detail page selector `a#pdfDown[name="pdfDown"]`.
- If the detail page has no PDF download entry, or only offers non-PDF entries, skip the paper and record the reason.
- Use CNKI's quote button `li.btn-quote[title="引用"]` to obtain GB/T 7714-2025 citation entries when available.
- Before writing CNKI citation entries into the paper, bibliography, tracking table, or verification notes, remove `DOI:` and everything after it. Example: `[1]程翔,许正荣,张昆明.基于物联网的智能家居控制系统设计[J].传感器与微系统,2021,40(3):106-108+111.DOI:...` becomes `[1]程翔,许正荣,张昆明.基于物联网的智能家居控制系统设计[J].传感器与微系统,2021,40(3):106-108+111.`
- Use CNKI search filters in `#ModuleGroupFilter` when quality, year, source, document type, or subject constraints are required.
- Do not cite weakly related papers just to reach a target count.
- Do not replace user-specified references without explaining why and getting confirmation, unless the user already authorized replacement.
- Do not insert a citation number into an unchanged sentence unless that sentence already directly matches the PDF evidence. Rewrite or add nearby body text so the citation supports the exact claim being made.
- Pause for login, verification, permission, payment, or download problems. Do not bypass access controls.

## Standard Workflow

1. Read the DOCX and extract headings, paragraph order, existing citation numbers, existing bibliography entries, and claims that need support.
2. If references already exist, verify them on CNKI before searching for additions or replacements.
3. Plan CNKI searches from the paper topic, modules, methods, and paragraph-level claims.
4. Search CNKI in Chrome, apply filters, open candidate detail pages, copy citation entries, close citation popups, and download PDFs.
5. Save PDFs in a task-specific folder with traceable filenames such as `01_Title_FirstAuthor.pdf`.
6. Read each downloaded PDF and extract at least one complete full-text evidence sentence for every final cited paper.
7. Screen references for authenticity, PDF availability, readability, relevance, source quality, and non-duplication.
8. Insert body citations into the DOCX, defaulting to at most one citation number per paragraph. Rewrite or add concise body text when needed so every citation maps to a real PDF evidence sentence.
9. Rebuild the bibliography with only PDF-verified references, ordered by first appearance.
10. Produce `知网参考文献整理.md`, `引用对应核验说明.md`, and a final processing summary.

## Reference Files

Load these files only when their details are needed:

| File | Use when |
|---|---|
| `references/workflow.md` | Need the full process for no-reference, insufficient-reference, or existing-reference scenarios. |
| `references/cnki-chrome.md` | Need Chrome/CNKI selectors, Chrome bootstrap behavior, quote dialog behavior, PDF download fallback behavior, filter selectors, or pause conditions. |
| `references/screening.md` | Need screening criteria, quality filters, rejection reasons, or PDF evidence sentence rules. |
| `references/docx-citation.md` | Need body citation placement, evidence-aligned rewriting, numbering, bibliography rebuild, saving, or formatting rules. |
| `references/templates.md` | Need templates for `知网参考文献整理.md`, `引用对应核验说明.md`, or final summaries. |
| `references/qa-checklist.md` | Need final quality checks before delivery. |

## Script

Use `scripts/validate_cnki_reference_table.py` to validate the final `知网参考文献整理.md` table fields and local PDF paths:

```bash
python scripts/validate_cnki_reference_table.py path/to/知网参考文献整理.md
```

Add `--csv-out path/to/output.csv` when a CSV export is useful.

## Final Response

When completing a real CNKI reference task, include:

- Modified Word file path.
- `知网参考文献整理.md` path.
- `引用对应核验说明.md` path.
- PDF full-text folder path.
- Counts for downloaded-and-read PDFs, no-PDF papers, failed downloads, unreadable PDFs, final cited references, and rejected candidates.
- Short citation-change summary covering first-appearance order, removed citation piles, removed unverified references, and body text adjusted to match verified PDF evidence.

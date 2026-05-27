# CNKI Chrome Operation Rules

Use the `@chrome` plugin because the user's CNKI login state, cookies, institution access, and download permission live in their Chrome profile.

## Confirm Before Use

Before controlling Chrome, confirm:

1. Chrome is logged in to CNKI.
2. The current account or institution can download PDFs.
3. The user can manually handle slider verification, permission prompts, download blocking, or payment prompts.
4. The reference count range is clear.
5. Source-quality requirements are clear.
6. The task is PDF-only.

## Search Page

1. Open the CNKI search page.
2. Enter search terms.
3. Review the result list.
4. Apply quality filters in `#ModuleGroupFilter` when required.

Common filter locations:

- Topic: `groupid="ZYZT|||CYZT"` for main and secondary topics.
- Source category: `groupid="LYBSM"` for Peking University Core, CSCD, EI, WJCI, etc.
- Year: `groupid="YE"` for recent five years or specified years.
- Document type: `groupid="WXLX"` for journal papers, theses, conference papers, etc.
- Subject: `groupid="CCL"`.
- Source title: `groupid="WXLY"`.

Open candidate detail pages after filtering.

## Article Detail Page

On a CNKI article detail page such as `https://kns.cnki.net/kcms2/article/abstract?...`:

1. Get the citation entry:
   - Click `li.btn-quote[title="引用"]`.
   - Use GB/T 7714-2025.
   - Observed behavior: the detail page opens a `.quote-pop` quote dialog. GB/T 7714-2025 is in the first row, and the citation text is in `.quote-pop tr:first-child textarea.text`.
   - Example format: `[1]路锐,范善斌,张庆华,等.基于多传感器融合的变电站开关柜智能搬运小车研究[J].物联网技术,2026,16(7):104-108.DOI:10.16667/j.issn.2095-1302.2026.07.024.`
   - Write the citation into the tracking table and final bibliography.

2. Download the PDF:
   - Click only `a#pdfDown[name="pdfDown"]`.
   - The link often has `onclick="WriteKrsDownLog()"` and visible text `PDF下载`.
   - Observed link shape: `https://bar.cnki.net/bar/download/order?...`.
   - Wait for the download to complete.
   - Move/save the PDF into the task PDF folder.

3. Forbidden:
   - Do not use any non-PDF download entry.
   - Do not use HTML reading pages as final evidence.
   - Do not click recommendation, advertisement, or `#recommend` PDF links.
   - Do not use abstract-page content as final evidence.

## Pause Conditions

Pause and explain if any of these occur:

- Slider verification appears.
- Login expires.
- No download permission.
- CNKI shows payment or institution-permission prompts.
- Browser blocks the download.
- The detail page has no `#pdfDown`.
- Only non-PDF download entries exist.
- The PDF opens but cannot be saved.

Do not bypass permission controls or ask for passwords. Ask the user to handle visible Chrome issues manually, then continue after confirmation.

## Download File Management

- Use a separate PDF folder per task.
- Use traceable filenames, such as `01_Title_FirstAuthor.pdf`.
- Do not overwrite same-name files unless it is confirmed to be the same paper redownloaded.
- If Chrome downloads to the default Downloads folder, move completed PDFs into the task PDF folder.

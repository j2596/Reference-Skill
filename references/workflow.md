# Standard Workflow

## 1. Intake

Confirm these items before starting:

- Paper DOCX path.
- Output folder.
- PDF full-text folder.
- Reference tracking Markdown path.
- Target reference count or range.
- Source-quality requirements.
- PDF-only rule: download only PDF files; skip papers without downloadable PDFs.
- Chrome is logged in to CNKI and has PDF download permission.

## 2. Determine the Paper's Reference State

### No references

1. Read the paper body.
2. Extract claims that need literature support.
3. Generate CNKI search terms.
4. Download more candidate PDFs than the target reference count.
5. Read, screen, and order references.
6. Rewrite or add body text where needed, then insert citations and rebuild the bibliography by first appearance.

### Insufficient references

1. Verify existing references on CNKI first.
2. Download and read PDFs for existing references where possible.
3. Keep only usable references.
4. Search, download, and screen added references for the gap.
5. Renumber all final references by first appearance.

### Existing references may be fake or unusable

1. Search each reference on CNKI.
2. Record whether a real matching entry is found.
3. Open the detail page and check for a PDF download entry.
4. If the paper cannot be found, has no PDF, fails to download, or only offers non-PDF formats, record the reason and skip it.
5. If replacement is needed, explain the reason and wait for user confirmation unless replacement was already authorized.

## 3. CNKI Search Strategy

Extract search terms from:

- Topic and object, such as `STM32 WiFi remote control car`.
- Core modules, such as `ESP8266`, `motor driver`, `PWM speed control`, `Proteus simulation`.
- Paragraph claims, such as `wireless communication module upper computer vehicle`.
- Method/design terms, such as `scheme comparison`, `control system design`, `line tracking obstacle avoidance`.

Start narrow for precision, then expand with synonyms and broader concepts. Do not use weakly related papers to fill a count.

If the user has quality requirements, filter in the search page panel `#ModuleGroupFilter`:

- Source category `groupid="LYBSM"`: Peking University Core, CSCD, EI, WJCI, etc.
- Year `groupid="YE"`: recent five years or specified years.
- Document type `groupid="WXLX"`: journals, master's/doctoral theses, conference papers, etc.
- Topic `groupid="ZYZT|||CYZT"`: main topic and secondary topic.
- Subject `groupid="CCL"`: narrow by subject area.

## 4. Detail-Page Citation and PDF Download

Every candidate paper must be opened on its CNKI article detail page.

Citation entry:

- Click `li.btn-quote[title="引用"]`.
- Copy the GB/T 7714-2025 entry.
- Remove `DOI:` and everything after it.
- Use the cleaned entry as the preferred source for the tracking table and final bibliography.
- Close the `.quote-pop` citation dialog before clicking the PDF download button.

PDF download:

- Before clicking, record the newest `.pdf` and `.crdownload` files in the user's Downloads folder.
- Click only the visible selector `a#pdfDown[name="pdfDown"]:visible`.
- Wait 5-15 seconds, then check the user's Downloads folder for a new `.pdf` file or active `.crdownload`.
- If a new PDF appears, move or copy it into the task PDF folder with a traceable filename.
- Use `downloadMedia()` only as a last fallback; it may trigger `docdown.cnki.net` / `ERR_BLOCKED_BY_CLIENT`.
- Do not click any non-PDF download entry.
- Do not click recommendation, advertisement, or unrelated PDF links.

If the detail page has no `#pdfDown`, or the account lacks permission, record `无PDF` or `权限不足` and skip the paper.

## 5. PDF Full-Text Verification

For every downloaded PDF:

1. Confirm the file exists and opens.
2. Extract body text.
3. Read the full text or enough complete body sections to evaluate the paper.
4. Extract a complete sentence that truly exists in the PDF.
5. Map it to the specific paper chapter/section, paragraph, and claim it supports.
6. Explain why it supports that claim.

Do not use abstracts, keywords, titles, search snippets, reference lists, or AI summaries as citation evidence.

## 6. Write Into the Paper

- Decide the final cited papers before editing the DOCX.
- Number references by first appearance in the body.
- Default to at most one citation per paragraph.
- Avoid citation piles.
- Rewrite nearby body text when needed so the citation is natural and evidence-based.
- Do not leave the body unchanged if the chosen PDF only supports a more specific or different claim. Make the smallest useful rewrite or addition so the final cited sentence is genuinely supported by the PDF evidence.
- Record the nearest chapter/section heading for every citation in `引用对应核验说明.md`; if the paper has no headings, record a stable paragraph location.
- Rebuild the bibliography.
- Save as a new Word file rather than overwriting the original.

## 7. Deliver

Deliver:

- Modified Word file.
- `知网参考文献整理.md`.
- `引用对应核验说明.md`.
- PDF full-text folder.
- Reference processing summary.

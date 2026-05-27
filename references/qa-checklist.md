# Final QA Checklist

1. Chrome CNKI login and PDF download permission were confirmed before browser control.
2. Existing references, if any, were searched and verified on CNKI before adding replacements.
3. Every final reference has a real local PDF path.
4. Every final reference has PDF read status `已阅读全文.
5. Every final reference has at least one complete PDF evidence sentence.
6. Every final PDF was downloaded from the article detail page `a#pdfDown[name="pdfDown"]`.
7. No final citation is based only on title, abstract, keywords, snippets, HTML reading pages, reference lists, or AI summaries.
8. Body citation numbers increase by first appearance.
9. Bibliography numbers match body citation numbers exactly.
10. Each final reference appears only once.
11. No uncited references remain in the final bibliography unless the user explicitly requested retention.
12. No body citation points to a missing bibliography item.
13. Citation piles such as `[1][2][3]` were removed unless the user explicitly requested them.
14. Papers without downloadable/readable PDFs, failed downloads, or only non-PDF formats did not enter the final bibliography.
15. The tracking table records CNKI URLs, PDF paths, download/read status, source quality, PDF evidence sentences, paper locations, and reasons.
16. The final response includes all required file paths and processing counts.

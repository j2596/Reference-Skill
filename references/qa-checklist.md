# Final QA Checklist

1. Chrome CNKI login and PDF download permission were confirmed before browser control.
2. Existing references, if any, were searched and verified on CNKI before adding replacements.
3. Every final reference has a real local PDF path.
4. Every final reference has PDF read status `已阅读全文`.
5. Every final reference has at least one complete PDF evidence sentence.
6. Every final PDF was downloaded from the article detail page `a#pdfDown[name="pdfDown"]`.
7. No final citation is based only on title, abstract, keywords, snippets, HTML reading pages, reference lists, or AI summaries.
8. Body citation numbers increase by first appearance.
9. Bibliography numbers match body citation numbers exactly.
10. Each final reference appears only once.
11. Final bibliography and tracking-table reference entries do not contain `DOI:` or DOI values.
12. No uncited references remain in the final bibliography unless the user explicitly requested retention.
13. No body citation points to a missing bibliography item.
14. Citation piles such as `[1][2][3]` were removed unless the user explicitly requested them.
15. Papers without downloadable/readable PDFs, failed downloads, or only non-PDF formats did not enter the final bibliography.
16. The tracking table records CNKI URLs, PDF paths, download/read status, source quality, PDF evidence sentences, paper locations, and reasons.
17. Each final citation has a recorded chapter/section location or stable paragraph location in `引用对应核验说明.md`.
18. Each final citation records the original text snippet, the revised final paper sentence, the PDF evidence sentence, and the support relationship.
19. If the original text did not directly match the PDF evidence, the paper body was rewritten or supplemented so the citation is genuine.
20. The final response includes all required file paths and processing counts.

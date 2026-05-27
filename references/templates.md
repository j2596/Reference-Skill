# Output Templates

## `知网参考文献整理.md`

Use this table structure:

| 序号 | 参考文献条目(GB/T 7714-2025) | 知网链接 | 本地PDF路径 | PDF下载状态 | PDF阅读状态 | 来源质量/筛选条件 | 适合引用的PDF原文完整句子 | 对应论文位置 | 使用理由 | 备注 |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 |  |  |  |  |  |  |  |  |  |  |

Recommended status values:

- PDF download status: `已下载`, `无PDF`, `下载失败`, `权限不足`, `非PDF跳过`.
- PDF read status: `已阅读全文`, `无法解析`, `缺页`, `未完成`, `不建议使用`.

Rows may include rejected papers. Clearly distinguish final cited references from rejected candidates in `备注`.

## `引用对应核验说明.md`

Use this entry format:

```markdown
## [1] Reference short title

* Final paper sentence:
* PDF evidence sentence:
* CNKI citation entry:
* Local PDF:
* CNKI detail URL:
* Reason:
```

Rules:

- `PDF evidence sentence` must come from the PDF body, figure/table note, or another verifiable full-text location.
- `Reason` must explain why the PDF evidence supports the final paper sentence.
- If a reference is rejected, record it in the tracking table rather than the final verification notes.

## Final Summary

```markdown
Modified Word file:
Reference tracking table:
Citation verification notes:
PDF full-text folder:

Counts:
- Downloaded and fully read PDFs:
- No PDF:
- PDF download failed:
- PDF unreadable:
- Final cited references:
- Rejected candidates:

Citation changes:
- Ordered by first appearance:
- Citation piles removed:
- Unverified references removed:
- Body text adjusted to match PDF evidence:
```

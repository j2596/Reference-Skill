# Output Templates

## `知网参考文献整理.md`

Use this table structure:

| 序号 | 参考文献条目(GB/T 7714-2025) | 知网链接 | 本地PDF路径 | PDF下载状态 | PDF阅读状态 | 来源质量/筛选条件 | 适合引用的PDF原文完整句子 | 对应论文位置 | 使用理由 | 备注 |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 |  |  |  |  |  |  |  |  |  |  |

Recommended status values:

- PDF下载状态: `已下载`, `无PDF`, `下载失败`, `权限不足`, `非PDF跳过`.
- PDF阅读状态: `已阅读全文`, `无法解析`, `缺页`, `未完成`, `不建议使用`.

Rows may include rejected papers. Clearly distinguish final cited references from rejected candidates in `备注`.

## `引用对应核验说明.md`

Use Chinese labels for all reader-facing fields. Do not use English labels such as `Final paper sentence`, `PDF evidence sentence`, `CNKI citation entry`, `Local PDF`, `CNKI detail URL`, or `Reason`.

Use this entry format:

```markdown
## [1] 参考文献简称或题名

* 论文位置: 第X章/第X节/段落说明
* 原文片段: 修改前的论文句子或段落摘录；如果原文已经完全契合证据，写“未修改，原文已契合证据”。
* 修改后论文句子: 插入正文中的最终句子，包含引用编号。
* PDF证据句: 来自PDF正文、图表注释、方法、设计、测试或结论部分的完整句子。
* CNKI引用条目: 从知网引用按钮获取的GB/T 7714-2025条目。
* 本地PDF: PDF全文文件路径。
* 知网详情页: CNKI文章详情页URL。
* 支撑关系说明: 说明PDF证据如何支撑修改后的论文句子。
```

Rules:

- `论文位置` must include the nearest chapter/section heading when the paper has headings. If the paper has no headings, use a stable paragraph location such as `正文第3段`.
- `修改后论文句子` must be the actual text written into the DOCX.
- `PDF证据句` must come from the PDF body, figure/table note, method/design/test section, or conclusion.
- `支撑关系说明` must explain why the PDF evidence supports the final paper sentence.
- If a reference is rejected, record it in the tracking table rather than the final verification notes.

## Final Summary

```markdown
修改后Word文件:
参考文献整理表:
引用对应核验说明:
PDF全文文件夹:

处理统计:
- 已下载并阅读全文PDF:
- 无PDF:
- PDF下载失败:
- PDF不可读:
- 最终引用文献:
- 拒绝候选文献:

引用修改摘要:
- 按正文首次出现排序:
- 已移除引用堆叠:
- 已移除未核验参考文献:
- 已为匹配PDF证据而修改/补写正文:
```

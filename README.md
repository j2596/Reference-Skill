# Reference Skill

用已登录的 Chrome 知网权限，把中文论文里的参考文献变成可下载、可阅读、可核验的 PDF 证据链。

本 Skill 面向中文毕业论文、课程设计、技术报告等场景。当正文没有参考文献、参考文献太少、来源不可验证，或者已有条目疑似虚假时，它会使用用户已登录的 Chrome 知网账号搜索候选文献、下载 PDF、读取全文、筛选证据，并把可验证引用写回 Word 文档。

## 安装

把仓库地址交给 Codex 的 `skill-installer`，或手动安装：

```powershell
python "${HOME}\.codex\skills\.system\skill-installer\scripts\install-skill-from-github.py" --repo j2596/Reference-Skill --path . --name cnki-reference-writer
```

## 使用前确认

- Chrome 已经登录知网。
- 当前账号或机构有 PDF 下载权限。
- 可以手动处理滑块验证、下载拦截、权限弹窗或付费提示。
- 已准备论文 DOCX 路径、输出文件夹、PDF 保存文件夹。
- 已明确目标参考文献数量，以及期刊、硕博、近五年、北大核心、CSCD、EI 等质量偏好。
- 只下载 PDF；没有 PDF 的文献会跳过并记录。

## 推荐工作流

1. 读取 DOCX，提取标题、章节、正文段落、已有引用编号和参考文献表。
2. 如果已有参考文献，先在知网验证真实性和 PDF 可下载性。
3. 根据论文主题、模块、方法和段落级论点规划检索词。
4. 使用 Chrome 打开知网，筛选候选文献，复制 GB/T 7714-2025 引文条目，并只从详情页 PDF 入口下载。
5. 关闭知网引用弹窗后再点击 PDF 下载，避免 `.quote-pop` 遮挡下载按钮。
6. 如果普通下载事件捕获不到，使用 Chrome skill 的 `downloadMedia()` 兜底，并检查用户 Downloads 文件夹。
7. 阅读本地 PDF 全文，抽取能支撑正文论点的完整证据句。
8. 修改或补写正文，使引用句真实匹配 PDF 证据；除非原文已经非常契合，否则不能只追加引用编号。
9. 按正文首次出现顺序插入引用编号，避免堆叠式引用。
10. 重建参考文献表，只保留 PDF 全文核验过的条目。
11. 输出 `知网参考文献整理.md`、`引用对应核验说明.md` 和最终处理摘要。

## 关键约束

- 最终引用必须来自 PDF 全文证据，不使用摘要、关键词、搜索片段、HTML 阅读页或 AI 总结作为最终证据。
- 只从知网详情页的 `a#pdfDown[name="pdfDown"]` 获取 PDF。
- 不为凑数量引用弱相关文献。
- 不绕过登录、权限、验证码或付费限制。
- 引用编号按正文首次出现顺序排列，参考文献表与正文编号必须一致。
- `引用对应核验说明.md` 必须使用中文字段，并写明第几章第几节或稳定段落位置。

## 常用脚本

校验最终的参考文献整理表字段、本地 PDF 路径和基本状态：

```bash
python scripts/validate_cnki_reference_table.py path/to/知网参考文献整理.md
```

同时导出 CSV：

```bash
python scripts/validate_cnki_reference_table.py path/to/知网参考文献整理.md --csv-out output.csv
```

## 目录结构

```text
cnki-reference-writer/
├── SKILL.md
├── README.md
├── LICENSE
├── agents/
│   └── openai.yaml
├── references/
│   ├── cnki-chrome.md
│   ├── docx-citation.md
│   ├── qa-checklist.md
│   ├── screening.md
│   ├── templates.md
│   └── workflow.md
└── scripts/
    └── validate_cnki_reference_table.py
```

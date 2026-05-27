<div align="center">

# Reference Skill

> 用已登录的 Chrome 知网权限，把中文论文里的参考文献变成可下载、可阅读、可核验的 PDF 证据链。

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-F7C948)
![Codex](https://img.shields.io/badge/Codex-Skill-111111)
![CNKI](https://img.shields.io/badge/CNKI-PDF%20Verified-0A7EFA)
![GB/T 7714](https://img.shields.io/badge/Citation-GB%2FT%207714--2025-16A34A)

面向中文毕业论文、课程设计、技术报告的知网参考文献核验与补写 Skill。

当正文没有参考文献、参考文献太少、来源不可验证，或者已有条目疑似虚假时，本 Skill 会使用用户已登录的 Chrome 知网账号搜索候选文献、下载 PDF、读取全文、筛选证据，并把可验证引用写回 Word 文档。

[安装](#安装) · [快速使用方式](#快速使用方式) · [推荐工作流](#推荐工作流) · [当前能力](#当前能力) · [常用脚本](#常用脚本) · [目录结构](#目录结构)

</div>

## 安装

### 方式 1：使用 Codex skill-installer 安装

```powershell
python "${HOME}\.codex\skills\.system\skill-installer\scripts\install-skill-from-github.py" --repo j2596/Reference-Skill --path . --name cnki-reference-writer
```

### 方式 2：手动克隆到本地 skills 目录

```powershell
git clone https://github.com/j2596/Reference-Skill.git "${HOME}\.codex\skills\cnki-reference-writer"
```

安装后重启 Codex，即可让它发现这个 skill。

## 快速使用方式

推荐优先在 Codex 中使用本 Skill。

第一次使用前请确认：

- Chrome 已经登录知网。
- 当前账号或机构有 PDF 下载权限。
- 可以手动处理滑块验证、下载拦截、权限弹窗或付费提示。
- 已准备论文 DOCX 路径、输出文件夹、PDF 保存文件夹。
- 已明确目标参考文献数量或范围，以及期刊、硕博、近五年、北大核心、CSCD、EI 等质量偏好。

示例指令：

```text
使用 cnki-reference-writer，帮我给这篇论文补充 15 篇知网 PDF 可验证参考文献，并写回 Word。
```

## 推荐工作流

1. 读取 DOCX，提取标题、正文段落、已有引用编号和参考文献表。
2. 如果已有参考文献，先在知网验证真实性和 PDF 可下载性。
3. 根据论文主题、模块、方法和段落级论点规划检索词。
4. 使用 Chrome 打开知网，筛选候选文献，复制 GB/T 7714-2025 引文条目，并只下载 PDF。
5. 阅读本地 PDF 全文，抽取能支撑正文论点的完整证据句。
6. 筛选掉无 PDF、下载失败、不可读、相关性弱或重复的文献。
7. 按正文首次出现顺序插入引用编号，避免堆叠式引用。
8. 重建参考文献表，只保留 PDF 全文核验过的条目。
9. 输出参考文献整理表、引用对应核验说明和最终处理摘要。

## 当前能力

- 知网候选文献检索策略规划
- Chrome 登录态复用和知网页面操作约束
- PDF-only 下载规则
- GB/T 7714-2025 引文条目采集
- PDF 全文证据句核验
- 参考文献真实性、相关性和来源质量筛选
- Word 正文引用编号插入与参考文献表重建
- 引用对应核验说明和处理摘要模板
- 参考文献整理 Markdown 表格校验脚本

## 设计原则

1. 最终引用必须来自 PDF 全文证据，不使用摘要、关键词、搜索片段或 AI 总结作为最终证据。
2. 只从知网详情页的 PDF 下载入口获取全文，跳过无 PDF 或非 PDF 资源。
3. 不为凑数量引用弱相关文献。
4. 不绕过登录、权限、验证码或付费限制，需要用户处理时暂停等待。
5. 引用编号按正文首次出现顺序排列，参考文献表与正文编号必须一致。

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

## 常用脚本

校验最终的参考文献整理表字段、本地 PDF 路径和基本状态：

```bash
python scripts/validate_cnki_reference_table.py path/to/知网参考文献整理.md
```

需要同时导出 CSV：

```bash
python scripts/validate_cnki_reference_table.py path/to/知网参考文献整理.md --csv-out output.csv
```

## 当前限制

- 需要用户自己的 Chrome 知网登录态和 PDF 下载权限。
- 遇到验证码、权限不足、付费提示或下载拦截时，需要用户手动处理。
- 没有 PDF、PDF 下载失败、PDF 不可读或仅有非 PDF 资源的文献不能进入最终参考文献表。
- 本 Skill 只定义流程、约束和校验脚本，不提供知网账号、下载权限或权限绕过能力。


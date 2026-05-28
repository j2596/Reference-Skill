#!/usr/bin/env python3
"""Validate a CNKI reference Markdown table for basic delivery checks."""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path


REQUIRED_COLUMNS = {
    "序号",
    "参考文献条目(GB/T 7714-2025)",
    "知网链接",
    "本地PDF路径",
    "PDF下载状态",
    "PDF阅读状态",
    "来源质量/筛选条件",
    "适合引用的PDF原文完整句子",
    "对应论文位置",
    "使用理由",
}


def parse_markdown_table(text: str) -> list[dict[str, str]]:
    rows: list[list[str]] = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|") or not stripped.endswith("|"):
            continue
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if all(re.fullmatch(r":?-{3,}:?", c.replace(" ", "")) for c in cells):
            continue
        rows.append(cells)
    if not rows:
        return []
    header = rows[0]
    return [dict(zip(header, row)) for row in rows[1:] if len(row) == len(header)]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("markdown", type=Path, help="Path to 知网参考文献整理.md")
    parser.add_argument("--csv-out", type=Path, help="Optional CSV export path")
    args = parser.parse_args()

    text = args.markdown.read_text(encoding="utf-8-sig")
    rows = parse_markdown_table(text)
    if not rows:
        print("ERROR: no Markdown table rows found", file=sys.stderr)
        return 2

    missing_cols = REQUIRED_COLUMNS - set(rows[0])
    errors: list[str] = []
    warnings: list[str] = []
    if missing_cols:
        errors.append(f"missing columns: {', '.join(sorted(missing_cols))}")

    seen_refs: set[str] = set()
    for idx, row in enumerate(rows, start=1):
        ref = row.get("参考文献条目(GB/T 7714-2025)", "")
        if re.search(r"\bdoi\s*:", ref, flags=re.IGNORECASE):
            errors.append(f"row {idx}: reference entry must remove DOI and following content")
        if ref in seen_refs:
            warnings.append(f"row {idx}: duplicate reference entry")
        seen_refs.add(ref)

        status = row.get("PDF下载状态", "")
        read_status = row.get("PDF阅读状态", "")
        pdf_path = row.get("本地PDF路径", "").strip("` ")
        evidence = row.get("适合引用的PDF原文完整句子", "")
        location = row.get("对应论文位置", "")

        if status == "已下载" and pdf_path and not Path(pdf_path).exists():
            errors.append(f"row {idx}: PDF path does not exist: {pdf_path}")
        if status == "已下载" and read_status == "已阅读全文" and not evidence:
            errors.append(f"row {idx}: verified PDF row has no evidence sentence")
        if status == "已下载" and read_status == "已阅读全文" and not location:
            errors.append(f"row {idx}: verified PDF row has no paper location")
        if status != "已下载" and read_status == "已阅读全文":
            warnings.append(f"row {idx}: read status says 已阅读全文 but download status is {status}")

    if args.csv_out:
        with args.csv_out.open("w", encoding="utf-8-sig", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)

    print(f"rows={len(rows)}")
    print(f"errors={len(errors)}")
    print(f"warnings={len(warnings)}")
    for item in errors:
        print(f"ERROR: {item}", file=sys.stderr)
    for item in warnings:
        print(f"WARNING: {item}", file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
import argparse
import re
import statistics
import subprocess
import tempfile
from pathlib import Path
import xml.etree.ElementTree as ET


def normalize_text(text: str) -> str:
    text = text.replace("\u00a0", " ").replace("\xad", "")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def is_noise(text: str, top: float, page_h: float, width: float, page_w: float) -> bool:
    if not text:
        return True
    if re.fullmatch(r"\d+", text) and len(text) <= 3:
        return True
    if len(text) == 1 and text in {"|", "·", "•"}:
        return True
    # Typical footer page numbers.
    if top > page_h * 0.90 and re.fullmatch(r"\d+", text) and width < page_w * 0.08:
        return True
    return False


def run_pdftohtml_xml(pdf_path: Path, xml_out: Path) -> None:
    subprocess.run(
        [
            "pdftohtml",
            "-xml",
            "-nodrm",
            "-i",
            "-noframes",
            "-q",
            str(pdf_path),
            str(xml_out),
        ],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def parse_xml_lines(xml_path: Path):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    pages = []
    all_sizes = []

    for page in root.findall("page"):
        pnum = int(page.attrib.get("number", "0"))
        pwidth = float(page.attrib.get("width", "0"))
        pheight = float(page.attrib.get("height", "0"))

        fonts = {}
        for f in page.findall("fontspec"):
            fonts[f.attrib["id"]] = float(f.attrib.get("size", "0"))

        raw_lines = []
        for t in page.findall("text"):
            top = float(t.attrib.get("top", "0"))
            left = float(t.attrib.get("left", "0"))
            width = float(t.attrib.get("width", "0"))
            height = float(t.attrib.get("height", "0"))
            f_id = t.attrib.get("font", "")
            size = fonts.get(f_id, 0.0)

            text = normalize_text("".join(t.itertext()))
            if is_noise(text, top, pheight, width, pwidth):
                continue

            bold = any(el.tag == "b" for el in t.iter())

            raw_lines.append(
                {
                    "page": pnum,
                    "top": top,
                    "left": left,
                    "width": width,
                    "height": height,
                    "size": size,
                    "bold": bold,
                    "text": text,
                }
            )
            if size > 0:
                all_sizes.append(size)

        pages.append({"number": pnum, "width": pwidth, "height": pheight, "lines": raw_lines})

    return pages, all_sizes


def order_page_lines(page):
    lines = page["lines"]
    if not lines:
        return []

    w = page["width"]

    def crosses_midline(ln):
        return ln["left"] < 0.5 * w and (ln["left"] + ln["width"]) > 0.5 * w

    colish = [ln for ln in lines if 0.22 * w <= ln["width"] <= 0.48 * w]
    left_count = sum(
        1 for ln in colish if (ln["left"] + (ln["width"] / 2.0)) < 0.45 * w
    )
    right_count = sum(
        1 for ln in colish if (ln["left"] + (ln["width"] / 2.0)) > 0.55 * w
    )

    two_col = len(colish) >= 20 and left_count >= 8 and right_count >= 8

    if not two_col:
        return sorted(lines, key=lambda x: (x["top"], x["left"]))

    right_lines = [
        ln
        for ln in colish
        if (ln["left"] + (ln["width"] / 2.0)) > 0.55 * w and not crosses_midline(ln)
    ]
    col_top = min((ln["top"] for ln in right_lines), default=0)

    preamble = [ln for ln in lines if ln["top"] < col_top - 8]
    body = [ln for ln in lines if ln not in preamble]

    left = [ln for ln in body if (ln["left"] + (ln["width"] / 2.0)) < 0.5 * w]
    right = [ln for ln in body if (ln["left"] + (ln["width"] / 2.0)) >= 0.5 * w]

    preamble = sorted(preamble, key=lambda x: (x["top"], x["left"]))
    left = sorted(left, key=lambda x: (x["top"], x["left"]))
    right = sorted(right, key=lambda x: (x["top"], x["left"]))

    return preamble + left + right


def build_markdown(ordered_lines, body_size):
    md = []
    current = ""
    prev = None

    def flush_para():
        nonlocal current
        if current.strip():
            md.append(current.strip())
            md.append("")
        current = ""

    def is_heading(ln):
        txt = ln["text"]
        if len(txt) > 120:
            return False
        if "@" in txt or "orcid" in txt.lower():
            return False
        if re.fullmatch(r"[A-Za-z]+\s+\d{4}", txt):
            return False
        if re.fullmatch(r"\d+(?:\.\d+)*", txt):
            return False
        if txt.lower() in {"abstract", "introduction", "keywords:"}:
            return True
        if ln["size"] >= body_size * 1.45:
            return True
        if ln["bold"] and ln["size"] >= body_size * 1.05 and len(txt) <= 90:
            return True
        if re.match(r"^\d+(?:\.\d+)*\s+\S+", txt) and len(txt) <= 90:
            return True
        return False

    def heading_prefix(ln):
        if ln["size"] >= body_size * 2.0:
            return "#"
        if ln["size"] >= body_size * 1.55:
            return "##"
        return "###"

    for ln in ordered_lines:
        txt = ln["text"]

        if prev is not None:
            if ln["page"] != prev["page"]:
                flush_para()
            elif ln["top"] - prev["top"] > max(prev["height"], ln["height"]) * 1.8:
                flush_para()
            elif (
                ln["left"] - prev["left"] > 10
                and ln["text"][:1].isupper()
                and not prev["text"].endswith("-")
            ):
                flush_para()
            elif (
                prev["text"].rstrip().endswith((".", "?", "!", ":"))
                and ln["top"] - prev["top"] > max(prev["height"], ln["height"]) * 1.2
            ):
                flush_para()

        if is_heading(ln):
            flush_para()
            md.append(f"{heading_prefix(ln)} {txt}")
            md.append("")
            prev = ln
            continue

        if not current:
            current = txt
        else:
            if current.endswith("-") and not current.endswith(" -"):
                current = current[:-1] + txt
            else:
                current += " " + txt

        prev = ln

    flush_para()

    # Light cleanup for common PDF artifacts.
    out = "\n".join(md)
    out = re.sub(r"\n{3,}", "\n\n", out)
    out = re.sub(r"\s+([,.;:?!])", r"\1", out)
    return out.strip() + "\n"


def convert_pdf(pdf: Path, out_md: Path):
    with tempfile.TemporaryDirectory() as td:
        xml_path = Path(td) / "out.xml"
        run_pdftohtml_xml(pdf, xml_path)
        pages, sizes = parse_xml_lines(xml_path)

    if not pages:
        out_md.write_text("", encoding="utf-8")
        return

    body_size = statistics.median(sizes) if sizes else 12.0

    ordered = []
    for page in pages:
        ordered.extend(order_page_lines(page))

    markdown = build_markdown(ordered, body_size)
    out_md.write_text(markdown, encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="Convert PDFs to readable markdown.")
    parser.add_argument("pdfs", nargs="+", help="PDF files to convert")
    args = parser.parse_args()

    for pdf_arg in args.pdfs:
        pdf = Path(pdf_arg)
        if not pdf.exists() or pdf.suffix.lower() != ".pdf":
            continue
        out_md = pdf.with_suffix(".md")
        convert_pdf(pdf, out_md)
        print(f"wrote {out_md}")


if __name__ == "__main__":
    main()

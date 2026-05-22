#!/usr/bin/env python3
import re
import shutil
import subprocess
import tempfile
from pathlib import Path


def image_entries_from_pdf(pdf: Path):
    proc = subprocess.run(
        ["pdfimages", "-list", str(pdf)],
        check=True,
        capture_output=True,
        text=True,
    )
    entries = []
    for line in proc.stdout.splitlines():
        m = re.match(
            r"^\s*(\d+)\s+(\d+)\s+(\w+)\s+(\d+)\s+(\d+)\s+", line
        )
        if not m:
            continue
        page = int(m.group(1))
        num = int(m.group(2))
        kind = m.group(3)
        if kind == "image":
            entries.append((page, num))
    entries.sort()
    return entries


def extract_images(pdf: Path, out_dir: Path):
    out_dir.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as td:
        prefix = Path(td) / "img"
        subprocess.run(
            ["pdfimages", "-png", "-p", str(pdf), str(prefix)],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        entries = image_entries_from_pdf(pdf)
        extracted = []
        for i, (page, num) in enumerate(entries, start=1):
            src = Path(f"{prefix}-{page:03d}-{num:03d}.png")
            if not src.exists():
                continue
            dst = out_dir / f"figure-{i:02d}.png"
            shutil.copy2(src, dst)
            extracted.append(dst)
    return extracted


def insert_images_at_captions(md_path: Path, image_paths):
    if not md_path.exists() or not image_paths:
        return False

    text = md_path.read_text(encoding="utf-8")

    # Remove prior auto-inserted image lines from this script.
    text = re.sub(r"\n!\[Figure \d+\]\([^\n]*?/figure-\d+\.png\)\n", "\n", text)

    lines = text.splitlines()
    caption_idx = [
        i for i, ln in enumerate(lines) if re.match(r"^Figure\s+\d+\s*:", ln.strip())
    ]

    if not caption_idx:
        return False

    rel_dir = image_paths[0].parent.relative_to(md_path.parent)

    inserts = []
    for i, idx in enumerate(caption_idx):
        if i >= len(image_paths):
            break
        rel_img = (rel_dir / image_paths[i].name).as_posix()
        fig_num = i + 1
        inserts.append((idx + 1, f"![Figure {fig_num}](./{rel_img})"))

    offset = 0
    for pos, img_line in inserts:
        lines.insert(pos + offset, "")
        lines.insert(pos + offset + 1, img_line)
        offset += 2

    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return True


def process_pdf(pdf: Path):
    md_path = pdf.with_suffix(".md")
    if not md_path.exists():
        return

    entries = image_entries_from_pdf(pdf)
    if not entries:
        return

    img_dir = pdf.parent / f"{pdf.stem}_images"
    images = extract_images(pdf, img_dir)
    if not images:
        return

    insert_images_at_captions(md_path, images)
    print(f"updated {md_path} with {len(images)} image(s)")


def main():
    pdfs = subprocess.run(
        ["rg", "--files", "-g", "*.pdf", "-g", "*.PDF"],
        check=True,
        capture_output=True,
        text=True,
    ).stdout.splitlines()

    for rel in pdfs:
        process_pdf(Path(rel))


if __name__ == "__main__":
    main()

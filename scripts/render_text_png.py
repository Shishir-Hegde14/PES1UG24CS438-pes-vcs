#!/usr/bin/env python3
"""Render terminal/text output into a screenshot-style PNG."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


def load_font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = [
        Path(r"C:\Windows\Fonts\consola.ttf"),
        Path(r"C:\Windows\Fonts\cour.ttf"),
    ]
    for font_path in candidates:
        if font_path.exists():
            return ImageFont.truetype(str(font_path), size=size)
    return ImageFont.load_default()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", type=Path)
    parser.add_argument("output_file", type=Path)
    parser.add_argument("--title", default="")
    parser.add_argument("--font-size", type=int, default=20)
    args = parser.parse_args()

    text = args.input_file.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines() or [""]

    font = load_font(args.font_size)
    line_height = int(args.font_size * 1.4)
    pad = 24

    max_line = max(lines + ([args.title] if args.title else []), key=len)
    sample = max_line if max_line else " "

    dummy = Image.new("RGB", (10, 10))
    draw = ImageDraw.Draw(dummy)
    text_width = int(draw.textlength(sample, font=font))

    header_lines = 2 if args.title else 0
    width = max(1200, text_width + pad * 2)
    height = max(700, (len(lines) + header_lines + 1) * line_height + pad * 2)

    img = Image.new("RGB", (width, height), "#0f172a")
    draw = ImageDraw.Draw(img)

    y = pad
    if args.title:
        draw.text((pad, y), args.title, font=font, fill="#93c5fd")
        y += line_height
        draw.line((pad, y, width - pad, y), fill="#1e293b", width=2)
        y += line_height // 2

    for line in lines:
        draw.text((pad, y), line, font=font, fill="#e2e8f0")
        y += line_height

    args.output_file.parent.mkdir(parents=True, exist_ok=True)
    img.save(args.output_file)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Text Extractor - Extract text from image files using OCR.
"""

import sys
import os
import argparse
from PIL import Image
import pytesseract


def extract_text_from_image(image_path: str) -> str:
    """Extract text from an image file using OCR.

    Args:
        image_path: Path to the image file.

    Returns:
        Extracted text as a string.

    Raises:
        FileNotFoundError: If the image file does not exist.
        ValueError: If the file is not a supported image format.
    """
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"Image file not found: {image_path}")

    try:
        image = Image.open(image_path)
    except Exception as e:
        raise ValueError(f"Could not open image file '{image_path}': {e}") from e

    text = pytesseract.image_to_string(image)
    return text


def main():
    parser = argparse.ArgumentParser(
        description="Extract text from image files using OCR."
    )
    parser.add_argument(
        "image_files",
        nargs="+",
        metavar="IMAGE",
        help="Path(s) to image file(s) to extract text from.",
    )
    parser.add_argument(
        "-o",
        "--output",
        metavar="FILE",
        help="Write extracted text to FILE instead of stdout.",
    )

    args = parser.parse_args()

    results = []
    errors = []

    for image_path in args.image_files:
        try:
            text = extract_text_from_image(image_path)
            if len(args.image_files) > 1:
                results.append(f"=== {image_path} ===\n{text}")
            else:
                results.append(text)
        except (FileNotFoundError, ValueError) as e:
            errors.append(str(e))

    if errors:
        for error in errors:
            print(f"Error: {error}", file=sys.stderr)

    if results:
        output_text = "\n".join(results)
        if args.output:
            with open(args.output, "w", encoding="utf-8") as f:
                f.write(output_text)
            print(f"Text written to {args.output}")
        else:
            print(output_text)

    if errors and not results:
        sys.exit(1)


if __name__ == "__main__":
    main()

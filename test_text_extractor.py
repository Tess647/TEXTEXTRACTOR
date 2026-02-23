"""
Tests for text_extractor.py
"""

import os
import tempfile
import unittest
from unittest.mock import patch
from PIL import Image, ImageDraw

from text_extractor import extract_text_from_image


def create_test_image(text: str, path: str):
    """Create a simple white image with black text for testing."""
    img = Image.new("RGB", (400, 100), color="white")
    draw = ImageDraw.Draw(img)
    draw.text((10, 30), text, fill="black")
    img.save(path)


class TestExtractTextFromImage(unittest.TestCase):

    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            extract_text_from_image("/nonexistent/path/image.png")

    def test_invalid_image_file(self):
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as f:
            f.write(b"not an image")
            tmp_path = f.name
        try:
            with self.assertRaises(ValueError):
                extract_text_from_image(tmp_path)
        finally:
            os.unlink(tmp_path)

    def test_extract_returns_string(self):
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as f:
            tmp_path = f.name
        try:
            create_test_image("Hello", tmp_path)
            result = extract_text_from_image(tmp_path)
            self.assertIsInstance(result, str)
        finally:
            os.unlink(tmp_path)

    def test_extract_text_content_mocked(self):
        """Use mock to verify pytesseract is called and its result is returned."""
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as f:
            tmp_path = f.name
        try:
            create_test_image("anything", tmp_path)
            with patch("text_extractor.pytesseract.image_to_string", return_value="MOCKED TEXT"):
                result = extract_text_from_image(tmp_path)
            self.assertEqual(result, "MOCKED TEXT")
        finally:
            os.unlink(tmp_path)


if __name__ == "__main__":
    unittest.main()

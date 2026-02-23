# TEXTEXTRACTOR

A command-line tool to extract text from image files using OCR (Optical Character Recognition).

## Prerequisites

- Python 3.7+
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) installed on your system
  - **Ubuntu/Debian:** `sudo apt-get install tesseract-ocr`
  - **macOS:** `brew install tesseract`
  - **Windows:** Download the installer from the [Tesseract GitHub releases](https://github.com/UB-Mannheim/tesseract/wiki)

## Setup

### 1. Create a virtual environment

```bash
python3 -m venv venv
```

### 2. Activate the virtual environment

- **Linux/macOS:**
  ```bash
  source venv/bin/activate
  ```
- **Windows (Command Prompt):**
  ```cmd
  venv\Scripts\activate.bat
  ```
- **Windows (PowerShell):**
  ```powershell
  venv\Scripts\Activate.ps1
  ```

Once activated, your terminal prompt will change to show `(venv)`.

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Deactivate the virtual environment

When you are done, you can deactivate the virtual environment by running:

```bash
deactivate
```

## Usage

Extract text from a single image:

```bash
python text_extractor.py image.png
```

Extract text from multiple images:

```bash
python text_extractor.py image1.png image2.jpg
```

Save extracted text to a file:

```bash
python text_extractor.py image.png -o output.txt
```
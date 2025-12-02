# DNG to JPG GUI Converter

A simple Python GUI tool for converting a folder of **DNG (Digital Negative)** raw image files into **JPEG** images on Ubuntu.  
The application uses a minimal Tkinter interface to let you select a folder, then converts all `.dng` files it finds into `.jpg` files in the **same folder**.

This is intended as a lightweight utility for quick conversions, not a full-featured photo editor or raw processing suite.

---

## Features

- Simple GUI built with Tkinter
- Select a folder and convert all `.dng` files in that folder to `.jpg`
- Writes JPEGs to the **same folder** as the DNG files
- Option to overwrite existing JPGs or skip them
- Logs progress and basic error messages in a scrollable text box

---

## What this tool can do

- Load DNG files using `rawpy`
- Convert each DNG to an RGB image
- Save each converted image as a JPEG file using `Pillow`
- Provide a minimal GUI for non-command-line usage

---

## What this tool does **not** do

This is intentionally simple. It **does not**:

- Perform advanced colour grading or film emulation
- Apply detailed noise reduction, sharpening, or lens corrections beyond `rawpy` defaults
- Handle colour profiles (ICC) or soft-proofing
- Recursively scan subfolders (it only processes files directly in the chosen folder)
- Allow choosing a different output folder (JPGs are written next to the DNG files)
- Support every possible raw format (it is designed specifically for `.dng` files)

For serious photo workflows, use a dedicated raw editor (e.g. darktable, RawTherapee, etc.) and treat this as a quick utility.

---

## Requirements

Tested on **Ubuntu** with:

- Python **3.8+**
- Tkinter
- `rawpy`
- `Pillow`

You will also need system libraries for `rawpy` / LibRaw.

### System packages (Ubuntu)

```bash
sudo apt update
sudo apt install python3 python3-tk python3-pip libraw-dev
```

### Python packages

Install the required Python libraries:

```bash
pip install rawpy Pillow
```

If you use a virtual environment, activate it before running the above `pip` command.

---

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/<your-username>/dng-to-jpg-gui.git
   cd dng-to-jpg-gui
   ```

2. (Optional but recommended) Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install rawpy Pillow
   ```

   Ensure `python3-tk` and `libraw-dev` are installed via your package manager as shown above.

---

## Usage

1. Make sure you are in the project directory:

   ```bash
   cd dng-to-jpg-gui
   ```

2. Run the GUI application:

   ```bash
   python3 dng_to_jpg_gui.py
   ```

3. In the GUI:

   - Click **“Browse…”** and select the folder containing your `.dng` files.
   - (Optional) Tick **“Overwrite existing JPG files”** if you want to replace existing `.jpg` files with new conversions.
   - Click **“Convert DNG → JPG”**.
   - Watch the log area for progress, skipped files, and any errors.

4. After completion, the application will show a summary dialog and the log will list details of the conversion.

---

## Restrictions, limitations & notes

- **File types**: Only `.dng` (case-insensitive) files are processed.
- **Folder depth**: Only files in the **selected folder** are processed. Subfolders are ignored.
- **Memory usage**: Very large DNG files or huge batches may use significant RAM and CPU time.
- **Performance**: Conversion is CPU-bound and single-process. There is no GPU acceleration or parallel processing.
- **Error handling**: Files that cannot be read or converted will be logged as errors and skipped; the rest of the batch will continue.
- **Cross-platform**: The tool is developed and tested on Ubuntu. It may run on other platforms with Python, Tkinter, `rawpy` and `Pillow` installed, but this is not guaranteed or officially supported.
- **Data safety**: The tool writes JPG files into the same folder as the source DNGs. If **“Overwrite existing JPG files”** is enabled, existing JPEGs with the same name will be replaced. Use this option with care.

Use this tool at your own risk. Do not run it on irreplaceable originals without having a backup.

---

## Project structure

A minimal layout might look like this:

```text
dng-to-jpg-gui/
├── dng_to_jpg_gui.py   # Main GUI application
├── README.md           # This file
└── (optional) LICENSE  # MIT license file
```

---

## Acknowledgements

This project relies on the following libraries:

- [Python](https://www.python.org/) and the standard library, including **Tkinter** for the GUI
- [rawpy](https://github.com/letmaik/rawpy): a Python wrapper for LibRaw used to read and process DNG files
- [Pillow](https://python-pillow.org/): the friendly fork of PIL used to save images as JPEG

Thanks to the authors and maintainers of these projects.

---

## License

This project is licensed under the **MIT License**.

You are free to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the software, subject to the conditions below.

### MIT License

Copyright (c) 2025 Shaun Dunmall

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

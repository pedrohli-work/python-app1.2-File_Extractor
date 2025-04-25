# ZIP Archive Extractor

## Overview

This project provides a Python utility for extracting ZIP archives to a specified directory. It uses the built-in `zipfile` module in Python to handle ZIP file extraction.

The module defines a function `extract_archive()` that opens a ZIP file and extracts all of its contents to a target directory. If executed as a standalone script, it extracts a sample ZIP file to a predefined location.

## Features

- **Simple ZIP file extraction**: Extracts all contents of a ZIP archive to a specified directory.
- **Reusable function**: The `extract_archive()` function can be used in other projects to automate ZIP extraction.
- **Minimal dependencies**: This script relies only on Python's built-in `zipfile` module, so there are no external dependencies.

## Usage

### Extract ZIP File from Script

If you run the script directly, it will extract the contents of the ZIP file `compressed.zip` located in the current directory to the folder `Users/files`:

```bash
python extract_archive.py

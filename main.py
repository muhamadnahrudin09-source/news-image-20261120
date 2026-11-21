#!/usr/bin/env python3
"""
main.py - Copies entry.png to /output/entry.png for make.fun contest.
Python 3.13 standard library only (shutil, pathlib, os).
"""

import os
from pathlib import Path
import shutil

def main():
    script_dir = Path(__file__).resolve().parent
    source_png = script_dir / "entry.png"
    output_dir = Path("/output")
    target_png = output_dir / "entry.png"

    if not source_png.exists():
        raise FileNotFoundError(f"Source image not found: {source_png}")

    output_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source_png, target_png)

    file_size = target_png.stat().st_size
    print(f"Successfully copied {source_png.name} to {target_png}")
    print(f"File size: {file_size} bytes")

if __name__ == "__main__":
    main()

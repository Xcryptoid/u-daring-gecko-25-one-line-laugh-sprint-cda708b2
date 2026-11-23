#!/usr/bin/env python3
"""Entrypoint: copy the pre-written one-liner to the output directory.

Standard library only. Deterministic: every run writes the same bytes.
Run: MAKEFUN_OUTPUT_DIR=out python3 -P -s main.py
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.txt")
    path = os.path.join(out_dir, "entry.txt")
    shutil.copyfile(src, path)
    print("wrote %s (%d bytes)" % (path, os.path.getsize(path)))


if __name__ == "__main__":
    main()

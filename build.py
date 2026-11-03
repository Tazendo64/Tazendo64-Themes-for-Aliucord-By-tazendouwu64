#!/usr/bin/env python3
"""Validate the theme suite and build a GitHub Pages site and ZIP package."""

import json
import re
import shutil
import sys
import zipfile
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "build"
SITE = OUTPUT / "site"
PACKAGE = OUTPUT / "waddledee-theme-suite.zip"
PACKAGE_FILES = ("README.md", "LICENSE", "index.html", "assets", "themes")


def fail(message):
    print(f"Build error: {message}", file=sys.stderr)
    raise SystemExit(1)


def validate():
    theme_path = ROOT / "themes/android/theme-waddledee.json"
    try:
        theme = json.loads(theme_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        fail(f"{theme_path.relative_to(ROOT)}: {error}")

    background_url = theme.get("background", {}).get("url", "")
    parsed_url = urlparse(background_url)
    if parsed_url.scheme != "https" or not parsed_url.netloc:
        fail(f"{theme_path.relative_to(ROOT)}: background URL must use HTTPS")

    sources = (
        ROOT / "index.html",
        ROOT / "themes/pc-linux/waddledee-pc.theme.css",
    )
    reference_pattern = re.compile(
        r"""(?:url\(\s*['"]?|new Audio\(\s*['"])([^)'"]+)"""
    )
    for source in sources:
        try:
            text = source.read_text(encoding="utf-8")
        except OSError as error:
            fail(f"{source.relative_to(ROOT)}: {error}")
        for reference in reference_pattern.findall(text):
            if urlparse(reference).scheme in ("http", "https", "data"):
                continue
            asset = (source.parent / reference).resolve()
            if not asset.is_relative_to(ROOT) or not asset.is_file():
                fail(f"{source.relative_to(ROOT)}: missing or invalid asset {reference}")

    for relative_path in PACKAGE_FILES:
        if not (ROOT / relative_path).exists():
            fail(f"required package path is missing: {relative_path}")


def build():
    validate()
    if SITE.exists():
        shutil.rmtree(SITE)
    SITE.mkdir(parents=True)

    for relative_path in PACKAGE_FILES:
        source = ROOT / relative_path
        destination = SITE / relative_path
        if source.is_dir():
            shutil.copytree(source, destination)
        else:
            shutil.copy2(source, destination)

    OUTPUT.mkdir(parents=True, exist_ok=True)
    if PACKAGE.exists():
        PACKAGE.unlink()
    with zipfile.ZipFile(
        PACKAGE, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6
    ) as archive:
        for path in sorted(SITE.rglob("*")):
            if path.is_file():
                relative_path = path.relative_to(SITE).as_posix()
                info = zipfile.ZipInfo(relative_path, date_time=(2020, 1, 1, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = (path.stat().st_mode & 0xFFFF) << 16
                archive.writestr(info, path.read_bytes(), compress_type=zipfile.ZIP_DEFLATED)

    print(f"Site: {SITE.relative_to(ROOT)}/")
    print(f"ZIP:  {PACKAGE.relative_to(ROOT)} ({PACKAGE.stat().st_size:,} bytes)")


if __name__ == "__main__":
    build()

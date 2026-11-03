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

    background = theme.get("background", {})
    if not isinstance(background, dict):
        fail(f"{theme_path.relative_to(ROOT)}: background must be an object")

    background_url = background.get("url", "")
    parsed_url = urlparse(background_url)
    if parsed_url.scheme != "https" or not parsed_url.netloc:
        fail(f"{theme_path.relative_to(ROOT)}: background URL must use HTTPS")

    overlay_alpha = background.get("overlay_alpha")
    if type(overlay_alpha) is not int or not 0 <= overlay_alpha <= 255:
        fail(f"{theme_path.relative_to(ROOT)}: background.overlay_alpha must be an integer from 0 to 255")
    blur_radius = background.get("blur_radius")
    if (
        isinstance(blur_radius, bool)
        or not isinstance(blur_radius, (int, float))
        or not 0 <= blur_radius <= 25
    ):
        fail(f"{theme_path.relative_to(ROOT)}: background.blur_radius must be from 0 to 25")
    if "alpha" in background or "blur" in background:
        fail(f"{theme_path.relative_to(ROOT)}: use Themer's overlay_alpha and blur_radius fields")

    simple_colors = theme.get("simple_colors")
    if not isinstance(simple_colors, dict) or not {
        "background",
        "background_secondary",
    }.issubset(simple_colors):
        fail(f"{theme_path.relative_to(ROOT)}: simple_colors must define background and background_secondary")

    for section in ("simple_colors", "colors"):
        color_values = theme.get(section, {})
        if not isinstance(color_values, dict):
            fail(f"{theme_path.relative_to(ROOT)}: {section} must be an object")
        for color_name, color_value in color_values.items():
            if type(color_value) is not int or not -(2**31) <= color_value < 2**31:
                fail(
                    f"{theme_path.relative_to(ROOT)}: {section}.{color_name} "
                    "must be a signed 32-bit ARGB integer"
                )

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

#!/usr/bin/env python3
"""Validate the Noctalia Lyrics plugin structure and manifest.

Mirrors the essential checks performed by the noctalia-dev/community-plugins
CI so contributors can verify changes before opening a pull request.
"""

import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REQUIRED_FILES = [
    "plugin.toml",
    "lyrics.luau",
    "lyrics_service.luau",
    "README.md",
    "LICENSE",
    "thumbnail.webp",
]
REQUIRED_DIRS = ["translations", "screenshots"]

ERRORS = []


def error(msg: str) -> None:
    ERRORS.append(msg)


def check_files() -> None:
    for name in REQUIRED_FILES:
        path = os.path.join(ROOT, name)
        if not os.path.isfile(path):
            error(f"missing required file: {name}")
    for name in REQUIRED_DIRS:
        path = os.path.join(ROOT, name)
        if not os.path.isdir(path):
            error(f"missing required directory: {name}")


def check_plugin_toml() -> dict | None:
    path = os.path.join(ROOT, "plugin.toml")
    if not os.path.isfile(path):
        return None
    data: dict = {}
    section = None
    has_service = False
    has_widget = False
    with open(path, encoding="utf-8") as fh:
        for ln, raw in enumerate(fh, 1):
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            if line.startswith("[[") and line.endswith("]]"):
                section = line[2:-2].strip()
                if section == "service":
                    has_service = True
                if section == "widget":
                    has_widget = True
                continue
            if "=" in line and section is None:
                key = line.split("=", 1)[0].strip()
                val = line.split("=", 1)[1].strip().strip('"')
                data[key] = val
    for key in ("id", "name", "version", "plugin_api", "author", "license"):
        if key not in data:
            error(f"plugin.toml missing field: {key}")
    if data.get("plugin_api") != "3":
        error("plugin.toml plugin_api must be 3 for current community CI")
    if "min_noctalia" in data:
        error("plugin.toml must not define deprecated min_noctalia")
    if not has_service:
        error("plugin.toml missing [[service]]")
    if not has_widget:
        error("plugin.toml missing [[widget]]")
    return data


def check_translations() -> None:
    tdir = os.path.join(ROOT, "translations")
    en = os.path.join(tdir, "en.json")
    if not os.path.isfile(en):
        error("translations/en.json is required")
        return
    try:
        with open(en, encoding="utf-8") as fh:
            json.load(fh)
    except json.JSONDecodeError as exc:
        error(f"translations/en.json is not valid JSON: {exc}")


def check_screenshots() -> None:
    sdir = os.path.join(ROOT, "screenshots")
    for name in ("widget.webp", "settings.webp"):
        if not os.path.isfile(os.path.join(sdir, name)):
            error(f"screenshots/{name} is required")


def main() -> int:
    check_files()
    check_plugin_toml()
    check_translations()
    check_screenshots()
    if ERRORS:
        for msg in ERRORS:
            print(f"FAIL: {msg}")
        print(f"\n{len(ERRORS)} validation error(s)")
        return 1
    print("OK: plugin structure and manifest valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
# SPDX-License-Identifier: MPL-2.0
"""Insert SPDX-License-Identifier headers into repository files."""
from __future__ import annotations

import argparse
import pathlib
from typing import Iterable

SPDX_LINE = "SPDX-License-Identifier: MPL-2.0"

HASH_EXTENSIONS = {
    ".py",
    ".sh",
    ".bash",
    ".zsh",
    ".yml",
    ".yaml",
    ".toml",
    ".cfg",
    ".ini",
    ".txt",
    ".rst",
    ".env",
}
SLASH_EXTENSIONS = {
    ".ts",
    ".tsx",
    ".js",
    ".jsx",
    ".c",
    ".h",
    ".cpp",
    ".hpp",
    ".java",
    ".go",
}
BLOCK_EXTENSIONS = {
    ".css",
}
HTML_EXTENSIONS = {
    ".html",
    ".htm",
    ".xml",
    ".md",
    ".markdown",
}

SPECIAL_HASH_NAMES = {
    "Makefile",
    "Dockerfile",
    "Justfile",
}

SKIP_DIRECTORIES = {
    "third_party",
    "site",
    "assets",
    "data",
    "docs/_build",
}

SKIP_SUFFIXES = {
    ".json",
    ".lock",
    ".ipynb",
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".svg",
    ".woff",
    ".woff2",
    ".ttf",
    ".eot",
    ".ico",
    ".pdf",
}


def should_skip(path: pathlib.Path) -> bool:
    if any(part in SKIP_DIRECTORIES for part in path.parts):
        return True
    if path.suffix in SKIP_SUFFIXES:
        return True
    if path.is_dir():
        return True
    if path.name in {"LICENSE", "NOTICE"}:
        return True
    return False


def comment_style(path: pathlib.Path) -> str | None:
    if path.suffix in HASH_EXTENSIONS or path.name in SPECIAL_HASH_NAMES:
        return "hash"
    if path.suffix in SLASH_EXTENSIONS:
        return "slash"
    if path.suffix in BLOCK_EXTENSIONS:
        return "block"
    if path.suffix in HTML_EXTENSIONS:
        return "html"
    if path.suffix == ".ps1":
        return "ps1"
    return None


def render_header(style: str) -> list[str]:
    if style == "hash":
        return [f"# {SPDX_LINE}\n"]
    if style == "slash":
        return [f"// {SPDX_LINE}\n"]
    if style == "block":
        return [f"/* {SPDX_LINE} */\n"]
    if style == "html":
        return [f"<!-- {SPDX_LINE} -->\n"]
    if style == "ps1":
        return [f"# {SPDX_LINE}\n"]
    raise ValueError(f"Unknown comment style: {style}")


def insert_header(path: pathlib.Path, style: str) -> bool:
    try:
        content = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return False

    if SPDX_LINE in content.splitlines():
        return False

    lines = content.splitlines(keepends=True)
    header = render_header(style)

    insert_at = 0
    if lines and lines[0].startswith("#!"):
        insert_at = 1

    new_lines = lines[:insert_at] + header + lines[insert_at:]
    path.write_text("".join(new_lines), encoding="utf-8")
    return True


def iter_paths(paths: Iterable[str]) -> Iterable[pathlib.Path]:
    for input_path in paths:
        path = pathlib.Path(input_path)
        if path.is_dir():
            yield from iter_paths(str(p) for p in path.iterdir())
        else:
            yield path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "paths",
        nargs="*",
        default=["."],
        help="Paths to scan. Defaults to the repository root.",
    )
    args = parser.parse_args()

    for path in iter_paths(args.paths):
        if should_skip(path):
            continue
        style = comment_style(path)
        if style is None:
            continue
        insert_header(path, style)


if __name__ == "__main__":
    main()

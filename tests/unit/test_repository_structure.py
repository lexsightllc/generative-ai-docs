# SPDX-License-Identifier: MPL-2.0
"""Smoke tests that validate the repository scaffolding stays intact."""

from __future__ import annotations

import pathlib


def test_readme_exists() -> None:
    """Ensure the top-level README remains present."""

    assert (pathlib.Path(__file__).resolve().parents[2] / "README.md").exists()


def test_scripts_directory_present() -> None:
    """The canonical scripts toolbelt should exist for contributors."""

    assert (pathlib.Path(__file__).resolve().parents[2] / "scripts").is_dir()

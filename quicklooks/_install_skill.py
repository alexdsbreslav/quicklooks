"""Install the quicklooks Cursor skill to the user's home directory."""

from __future__ import annotations

import shutil
from pathlib import Path


def install_skill() -> None:
    """Copy the quicklooks Cursor skill to ``~/.cursor/skills/ql-viz/``.

    Run this once after ``pip install quicklooks`` to make the skill available
    across all projects in Cursor.
    """
    src = Path(__file__).parent / "skill"
    dst = Path.home() / ".cursor" / "skills" / "ql-viz"

    if not src.exists():
        raise FileNotFoundError(
            "Skill files not found in the quicklooks package. "
            "Try reinstalling: pip install --force-reinstall quicklooks"
        )

    dst.mkdir(parents=True, exist_ok=True)
    shutil.copytree(src, dst, dirs_exist_ok=True)

    print(f"quicklooks skill installed to {dst}")
    print("Restart Cursor for the skill to take effect.")

"""Install the quicklooks skill for Cursor and/or Claude Code."""

from __future__ import annotations

import shutil
from pathlib import Path


def install_skill() -> None:
    """Install the quicklooks skill to every AI agent found on this machine.

    - **Cursor** (``~/.cursor/`` exists): copies skill files to
      ``~/.cursor/skills/ql-viz/``. Restart Cursor to activate.
    - **Claude Code** (``~/.claude/`` exists): copies skill files to
      ``~/.claude/quicklooks/`` and appends an ``@``-import line to
      ``~/.claude/CLAUDE.md`` so Claude Code loads the skill globally.

    Safe to run multiple times — re-running updates the skill files and
    skips the CLAUDE.md append if the import is already present.
    """
    src = Path(__file__).parent / "skill"
    if not src.exists():
        raise FileNotFoundError(
            "Skill files not found in the quicklooks package. "
            "Try reinstalling: pip install --force-reinstall quicklooks"
        )

    installed = []

    # ── Cursor ────────────────────────────────────────────────────────────
    cursor_home = Path.home() / ".cursor"
    if cursor_home.exists():
        dst = cursor_home / "skills" / "ql-viz"
        dst.mkdir(parents=True, exist_ok=True)
        shutil.copytree(src, dst, dirs_exist_ok=True)
        installed.append(f"  Cursor  → {dst}\n          Restart Cursor to activate.")

    # ── Claude Code ───────────────────────────────────────────────────────
    claude_home = Path.home() / ".claude"
    if claude_home.exists():
        dst = claude_home / "quicklooks"
        dst.mkdir(parents=True, exist_ok=True)
        shutil.copytree(src, dst, dirs_exist_ok=True)

        # Append @-import to ~/.claude/CLAUDE.md (idempotent)
        claude_md = claude_home / "CLAUDE.md"
        import_line = f"@{dst / 'SKILL.md'}"
        existing = claude_md.read_text() if claude_md.exists() else ""
        if import_line not in existing:
            with claude_md.open("a") as f:
                f.write(f"\n\n## quicklooks\n{import_line}\n")

        installed.append(f"  Claude Code → {dst}\n              Import added to {claude_md}")

    if installed:
        print("quicklooks skill installed:\n")
        print("\n".join(installed))
    else:
        print(
            "No supported AI agent found (~/.cursor/ or ~/.claude/ must exist).\n"
            "Install Cursor or Claude Code first, then run ql.install_skill() again."
        )

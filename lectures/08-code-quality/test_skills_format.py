"""Checks every skill in .agents/skills/ and .github/skills/ against the Agent Skills format.

OpenCode reads .agents/skills/ and Copilot reads .github/skills/, so each skill
needs an identical copy in both folders.
"""

import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
FOLDERS = [ROOT / ".agents" / "skills", ROOT / ".github" / "skills"]
NAME_PATTERN = re.compile(r"[a-z0-9]+(-[a-z0-9]+)*")


def skill_files() -> list[Path]:
    return sorted(path for folder in FOLDERS for path in folder.glob("*/SKILL.md"))


def frontmatter(path: Path) -> dict[str, str]:
    """Read the `key: value` lines between the two `---` lines at the top."""
    lines = path.read_text().splitlines()
    assert lines and lines[0] == "---", f"{path} must start with a --- line"
    assert "---" in lines[1:], f"{path} needs a closing --- line after the frontmatter"
    end = lines.index("---", 1)
    fields = {}
    for line in lines[1:end]:
        key, _, value = line.partition(":")
        fields[key.strip()] = value.strip().strip("\"'")
    return fields


@pytest.mark.parametrize("path", skill_files(), ids=lambda p: str(p.relative_to(ROOT)))
def test_skill_frontmatter(path: Path) -> None:
    fields = frontmatter(path)
    name = fields.get("name", "")
    description = fields.get("description", "")
    folder = path.parent.name

    assert NAME_PATTERN.fullmatch(name), (
        f"name {name!r}: use only lowercase letters, numbers, and single hyphens"
    )
    assert len(name) <= 64, f"name {name!r} is longer than 64 characters"
    assert name == folder, f"name {name!r} must match its folder name {folder!r}"
    assert 1 <= len(description) <= 1024, "description must be 1 to 1024 characters"


def test_skill_copies_match() -> None:
    agents, github = FOLDERS
    for path in skill_files():
        name = path.parent.name
        a, g = agents / name / "SKILL.md", github / name / "SKILL.md"
        assert a.exists() and g.exists(), (
            f"skill {name!r} needs a copy in both .agents/skills/ and .github/skills/"
        )
        assert a.read_text() == g.read_text(), (
            f"the two copies of skill {name!r} are different; copy the one you edited over the other"
        )

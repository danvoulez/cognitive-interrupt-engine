from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def test_markdown_local_links_exist():
    markdown_files = list(ROOT.glob("*.md")) + list((ROOT / "docs").glob("*.md")) + list((ROOT / "rfcs").glob("*.md"))
    broken = []
    for path in markdown_files:
        text = path.read_text()
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
            target = target.split("#", 1)[0]
            if not target or "://" in target or target.startswith("mailto:"):
                continue
            if not (path.parent / target).resolve().exists():
                broken.append((str(path.relative_to(ROOT)), target))
    assert not broken, broken


def test_no_placeholder_schema_ids_remain():
    for path in (ROOT / "schemas").glob("*.json"):
        assert "example.invalid" not in path.read_text()

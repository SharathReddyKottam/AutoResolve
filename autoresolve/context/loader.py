from pathlib import Path

KNOWLEDGE_DIR = Path(__file__).parent / "knowledge"


def load_chunks() -> list[str]:
    chunks = []
    for file in sorted(KNOWLEDGE_DIR.glob("*.md")):
        text = file.read_text(encoding="utf-8")
        title = text.splitlines()[0].removeprefix("# ").strip()
        for section in text.split("\n## ")[1:]:
            heading, _, body = section.partition("\n")
            chunks.append(f"{title} → {heading.strip()}\n{body.strip()}")
    return chunks
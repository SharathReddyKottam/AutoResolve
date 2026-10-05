import yaml
from pathlib import Path

def load_config() -> dict:
    """Load settings from config.yaml next to this file."""
    return yaml.safe_load((Path(__file__).parent / "config.yaml").read_text())

config = load_config()

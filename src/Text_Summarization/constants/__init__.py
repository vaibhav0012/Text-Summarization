from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
CONFIG_FILE_PATH = BASE_DIR / "config" / "config.yaml"
PARAMS_FILE_PATH = Path("params.yaml")
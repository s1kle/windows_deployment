from pathlib import Path
from typing import Any

import yaml


def load_yaml(file: Path) -> Any:
    with file.open(encoding='UTF-8') as input:
        return yaml.safe_load(input)
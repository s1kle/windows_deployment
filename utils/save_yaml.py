import yaml

from typing import Any
from pathlib import Path


yaml.SafeDumper.add_representer(
    type(None),
    lambda dumper, _: dumper.represent_scalar(u'tag:yaml.org,2002:null', '')
)

def save_yaml(file: Path, data: Any):
    with file.open('w', encoding='UTF-8') as output:
        data = (yaml.safe_dump(data, allow_unicode=True))
        output.writelines(data.replace('- ', '  '))
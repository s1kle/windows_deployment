import yaml

def load_yaml(file):
    with file.open() as f:
        return yaml.safe_load(f)
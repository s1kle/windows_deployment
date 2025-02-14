import yaml

def save_yaml(file, data):
    with file.open('w') as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True)
"""config_loader.py
Simple YAML config loader (placeholder).
"""

import yaml


def load_config(path):
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


if __name__ == "__main__":
    print("config_loader placeholder")

from tomllib import load
from pathlib import Path

def load_config(path="config/config.toml"):
    root = Path(__file__).parent.parent
    config_path = root / path
    
    with open(config_path, "rb") as f:
        return load(f) 

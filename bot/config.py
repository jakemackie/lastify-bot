from tomllib import load

def load_config(path="config.toml"):
    with open(path, "rb") as f:
        return load(f) 
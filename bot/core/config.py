from dataclasses import dataclass, field
from typing import List, Final
from tomllib import load
from pathlib import Path
import logging
from os import getenv
from dotenv import load_dotenv

@dataclass(frozen=True)
class LoggingConfig:
    level: Final[str] = "INFO"
    format: Final[str] = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    file_path: Final[str] = "debug.log"

    def __post_init__(self):
        if not getattr(logging, self.level, None):
            raise ValueError(f"Invalid logging level: {self.level}")

@dataclass(frozen=True)
class BotConfig:
    token: str
    owner_ids: List[int] = field(default_factory=list)
    default_prefix: str = ","

    def __post_init__(self):
        if not self.token:
            raise ValueError("Bot token cannot be empty")
        if not self.owner_ids:
            raise ValueError("At least one owner ID must be specified")

@dataclass(frozen=True)
class Config:
    bot: BotConfig
    logging: LoggingConfig = field(default_factory=LoggingConfig)

def load_config(path="config/config.toml") -> Config:
    load_dotenv()
    
    root = Path(__file__).parent.parent.parent
    config_path = root / path
    
    with open(config_path, "rb") as f:
        raw_config = load(f)
        
    token = getenv("TOKEN")
    if not token:
        raise ValueError("TOKEN environment variable is not set")
        
    return Config(
        bot=BotConfig(
            token=token,
            owner_ids=[int(id) for id in raw_config["bot"]["owner_ids"]],
            default_prefix=raw_config["bot"].get("default_prefix", ",")
        ),
        logging=LoggingConfig(
            level=raw_config.get("logging", {}).get("level", "INFO"),
            format=raw_config.get("logging", {}).get("format", "%(asctime)s - %(name)s - %(levelname)s - %(message)s"),
            file_path=raw_config.get("logging", {}).get("file_path", "debug.log")
        )
    ) 

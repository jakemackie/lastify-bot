from dataclasses import dataclass, field
from typing import List, Final
from tomllib import load
from pathlib import Path
from logging import getLevelName

@dataclass(frozen=True)
class LoggingConfig:
    level: Final[str] = "INFO"
    format: Final[str] = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    file_path: Final[str] = "debug.log"

    def __post_init__(self):
        if not getLevelName(self.level):
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
    root = Path(__file__).parent.parent.parent
    config_path = root / path
    
    with open(config_path, "rb") as f:
        raw_config = load(f)
        
    return Config(
        bot=BotConfig(
            token=raw_config["bot"]["token"],
            owner_ids=[int(id) for id in raw_config["bot"]["owner_ids"]],
            default_prefix=raw_config["bot"].get("default_prefix", ",")
        ),
        logging=LoggingConfig(
            level=raw_config.get("logging", {}).get("level", "INFO"),
            format=raw_config.get("logging", {}).get("format", "%(asctime)s - %(name)s - %(levelname)s - %(message)s"),
            file_path=raw_config.get("logging", {}).get("file_path", "debug.log")
        )
    ) 

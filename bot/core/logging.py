from logging import basicConfig, FileHandler, StreamHandler
from bot.core.config import Config

def logging_init(config: Config):
    basicConfig(
        level=config.logging.level,
        format=config.logging.format,
        handlers=[
            FileHandler(config.logging.file_path),
            StreamHandler()
        ]
    )

from logging import basicConfig, INFO, FileHandler, StreamHandler

def logging_init():
    basicConfig(
        level=INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            FileHandler("debug.log"),
            StreamHandler()
        ]
    )

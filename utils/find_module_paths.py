import os
from logging import getLogger

logger = getLogger(__name__)

async def find_module_paths(dir_path: str) -> list[str]:
    """Helper function to walk through directories and find Python files."""
    module_paths = []
    for item in os.listdir(dir_path):
        item_path = os.path.join(dir_path, item)
        if os.path.isfile(item_path) and item.endswith(".py"):
            module_path = item_path[:-3].replace(os.path.sep, ".")
            module_paths.append(module_path)
        elif os.path.isdir(item_path):
            module_paths.extend(await find_module_paths(item_path))
    return module_paths

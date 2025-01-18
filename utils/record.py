import time
import functools
from typing import TypeVar, Callable, Any, Coroutine

T = TypeVar("T", bound=Callable[..., Coroutine[Any, Any, Any]])

def record_time(func: T) -> T:
    @functools.wraps(func)
    async def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.perf_counter()
        result = await func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"{func.__name__} took {execution_time:.2f}s")
        return result
    return wrapper

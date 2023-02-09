# https://github.com/python/typing/issues/270#issuecomment-1346124813
import functools
from collections.abc import Callable
from typing import Any, Concatenate, ParamSpec, TypeVar

P = ParamSpec("P")
T = TypeVar("T")


def copy_callable_signature(
    source: Callable[P, T]
) -> Callable[[Callable[..., T]], Callable[P, T]]:
    def wrapper(target: Callable[..., T]) -> Callable[P, T]:
        @functools.wraps(source)
        def wrapped(*args: P.args, **kwargs: P.kwargs) -> T:
            return target(*args, **kwargs)

        return wrapped

    return wrapper


def copy_method_signature(
    source: Callable[Concatenate[Any, P], T]
) -> Callable[[Callable[..., T]], Callable[Concatenate[Any, P], T]]:
    def wrapper(target: Callable[..., T]) -> Callable[Concatenate[Any, P], T]:
        @functools.wraps(source)
        def wrapped(self: Any, /, *args: P.args, **kwargs: P.kwargs) -> T:
            return target(self, *args, **kwargs)

        return wrapped

    return wrapper

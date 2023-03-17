from typing import TypeVar

T = TypeVar('T')


def validate_fields(obj, *names: str) -> None:
    for name in names:
        validate_field(obj, name)


def validate_field(obj, name: str) -> None:
    value = getattr(obj, name, None)
    if not value:
        raise ValueError(f'You must set `{name}` for {obj}')


def listify(obj: T | list[T]) -> list[T]:
    if isinstance(obj, list):
        return obj
    return [obj]

import os
import typing

from dotenv import load_dotenv

load_dotenv()

T = typing.TypeVar('T')


class Env:

    @staticmethod
    def get(var_name: str, default: T = ...) -> str | T:
        return parse(var_name, default)

    @staticmethod
    def get_int(var_name: str, default: T = ...) -> int | T:
        return parse(var_name, default, int)


def parse(var_name: str, default=..., cast_func=lambda x: x):
    if var_name in os.environ:
        return cast_func(os.environ[var_name])
    if default is ...:
        raise ValueError(f'Environment variable "{var_name}" not set')
    return default


env = Env()

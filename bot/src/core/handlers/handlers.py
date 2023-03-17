from __future__ import annotations

from typing import Iterator

from .handler import Handler

HandlerClass = type[Handler]


class Handlers:
    def __init__(self, *items: HandlerClass | Handlers):
        self._items = items

    def __iter__(self) -> Iterator[HandlerClass]:
        for item in self._items:
            if isinstance(item, Handlers):
                yield from item
            else:
                yield item

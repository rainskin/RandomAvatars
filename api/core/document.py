import json
import typing

import mongoengine as me

DocT = typing.TypeVar('DocT', bound='BaseDocument')


class Document(me.Document):
    meta = {
        'abstract': True,
    }

    @classmethod
    def find_doc(cls: type[DocT], *args, **kwargs) -> DocT | None:
        return cls.objects(*args, **kwargs).first()

    @classmethod
    def find_docs(cls: type[DocT], *args, **kwargs) -> list[DocT]:
        return list(cls.objects(*args, **kwargs))

    def to_dict(self) -> dict:
        return json.loads(self.to_json())

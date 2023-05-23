from collections.abc import Collection

from fluent.runtime import FluentLocalization, FluentResourceLoader


class Texts:
    def __init__(
        self,
        path: str = "locales",
        locales: Collection[str] = {"ru"},
        files: Collection[str] = {"main.ftl"},
    ) -> None:
        loader = FluentResourceLoader(f"{path}/{{locale}}")
        self._l10n = FluentLocalization(list(locales), list(files), loader)

    def get(self, key: str, **kwargs: str | int) -> str:
        return self._l10n.format_value(key, kwargs)


t = Texts()

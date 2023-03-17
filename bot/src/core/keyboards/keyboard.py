from core.helpers import validate_fields
from .types import ReplyMarkup, AnyButton


class Keyboard:
    buttons: list[AnyButton] = None
    row_width: int = 1

    def build(self) -> ReplyMarkup:
        raise NotImplementedError()

    @property
    def _prepared_buttons(self) -> list[list[AnyButton]]:
        buttons = self._built_buttons
        row_width = self.row_width
        return [buttons[i:i + row_width] for i in range(0, len(buttons), row_width)]

    @property
    def _built_buttons(self) -> list[AnyButton]:
        validate_fields(self, 'buttons')
        return [self._build_button(b) for b in self.buttons]

    @staticmethod
    def _build_button(button: AnyButton) -> AnyButton:
        return button

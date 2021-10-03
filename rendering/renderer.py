import time
from typing import Optional

from terminal import Terminal
from .colors import color_control_sequence, RESET_COLOR_CONTROL_SEQUENCE


class Renderer:
    def __init__(self, terminal: Terminal):
        self._terminal = terminal

    def clear_screen(self) -> None:
        self._terminal.clear_screen()

    def show_text(self, text: str) -> None:
        print(text, end="")

    def show_text_animated(self, text: str, chars_per_second: Optional[float] = 10) -> None:
        for character in text:
            print(character, end="")
            time.sleep(1 / chars_per_second)

    def change_terminal_color(self, text_color: str) -> None:
        print(color_control_sequence(text_color), end="")

    def reset_terminal_color(self) -> None:
        print(RESET_COLOR_CONTROL_SEQUENCE, end="")

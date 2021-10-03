from queue import Queue
from . import *
from .change_color_command import ChangeColorCommand
from .reset_color_command import ResetColorCommand


class CommandQueue(Queue):
    def animate_text(self, text: str) -> None:
        self.put(AnimateTextCommand(text))

    def show_text(self, text: str) -> None:
        self.put(ShowTextCommand(text))

    def wait(self, seconds: float) -> None:
        self.put(WaitCommand(seconds))

    def clear_screen(self) -> None:
        self.put(ClearScreenCommand())

    def stop(self) -> None:
        self.put(StopCommand())

    def show_colored_text(self, text: str, text_color: str) -> None:
        self.put(ChangeColorCommand(text_color))
        self.put(ShowTextCommand(text))
        self.put(ResetColorCommand())

    def show_colored_animated_text(self, text: str, text_color: str) -> None:
        self.put(ChangeColorCommand(text_color))
        self.put(AnimateTextCommand(text))
        self.put(ResetColorCommand())

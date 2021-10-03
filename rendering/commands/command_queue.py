from queue import Queue
from . import *


class CommandQueue(Queue):
    def animate_text(self, text: str) -> None:
        self.put(AnimateTextCommand(text))

    def show_text(self, text: str) -> None:
        self.put(ShowTextCommand(text))

    def wait(self, seconds: float) -> None:
        self.put(WaitCommand(seconds))

    def clear_screen(self):
        self.put(ClearScreenCommand())

    def stop(self):
        self.put(StopCommand())

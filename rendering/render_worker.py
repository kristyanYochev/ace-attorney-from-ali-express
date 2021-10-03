from threading import Thread

from .commands import CommandQueue
from .renderer import Renderer
from .stop_thread import StopThread


class RenderWorker(Thread):
    def __init__(self, renderer: Renderer, commands: CommandQueue):
        super(RenderWorker, self).__init__()
        self._commands = commands
        self._renderer = renderer

    def run(self) -> None:
        while True:
            try:
                command = self._commands.get(block=True)
                command.execute(self._renderer)
            except StopThread:
                break

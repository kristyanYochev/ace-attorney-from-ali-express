from queue import Queue
from threading import Thread

from .renderer import Renderer
from .commands import RenderCommand
from .stop_thread import StopThread


class RenderWorker(Thread):
    def __init__(self, renderer: Renderer, commands: Queue[RenderCommand]):
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

import time

from rendering.commands.render_command import RenderCommand
from rendering.renderer import Renderer


class WaitCommand(RenderCommand):
    def __init__(self, seconds: float):
        self.seconds = seconds

    def execute(self, renderer: Renderer) -> None:
        time.sleep(self.seconds)

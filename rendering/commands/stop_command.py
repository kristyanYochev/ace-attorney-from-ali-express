from rendering.commands.render_command import RenderCommand
from rendering.renderer import Renderer
from rendering.stop_thread import StopThread


class StopCommand(RenderCommand):
    def execute(self, renderer: Renderer) -> None:
        raise StopThread()

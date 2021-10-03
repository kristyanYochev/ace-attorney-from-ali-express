from rendering.commands.render_command import RenderCommand
from rendering.renderer import Renderer


class ClearScreenCommand(RenderCommand):
    def execute(self, renderer: Renderer) -> None:
        renderer.clear_screen()

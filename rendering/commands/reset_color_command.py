from rendering import Renderer
from rendering.commands import RenderCommand


class ResetColorCommand(RenderCommand):
    def execute(self, renderer: Renderer) -> None:
        renderer.reset_terminal_color()

from rendering import Renderer
from .render_command import RenderCommand


class ChangeColorCommand(RenderCommand):
    def __init__(self, color: str):
        self.color = color

    def execute(self, renderer: Renderer) -> None:
        renderer.change_terminal_color(self.color)

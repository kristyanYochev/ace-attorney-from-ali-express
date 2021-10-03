from rendering.commands.render_command import RenderCommand
from rendering.renderer import Renderer


class ShowTextCommand(RenderCommand):
    def __init__(self, text: str):
        self.text = text

    def execute(self, renderer: Renderer) -> None:
        renderer.show_text(self.text)

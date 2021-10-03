from rendering.renderer import Renderer


class RenderCommand:
    def execute(self, renderer: Renderer) -> None:
        raise NotImplementedError()

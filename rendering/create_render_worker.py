from . import RenderWorker, Renderer
from .commands import CommandQueue
from terminal import Terminal


def create_render_worker(terminal: Terminal) -> (CommandQueue, RenderWorker):
    renderer = Renderer(terminal)
    command_queue = CommandQueue()
    worker = RenderWorker(renderer, command_queue)

    return command_queue, worker

from queue import Queue

from rendering.commands import *
from rendering import Renderer, RenderWorker
from terminal import Terminal


def main():
    with Terminal() as terminal:
        renderer = Renderer(terminal)
        commands_queue = Queue()
        render_worker = RenderWorker(renderer, commands_queue)

        commands_queue.put(ShowTextCommand("Hello there!"))
        commands_queue.put(AnimateTextCommand("This text should be animated!"))
        commands_queue.put(WaitCommand(2))
        commands_queue.put(ClearScreenCommand())
        commands_queue.put(ShowTextCommand("This text should be on it's own screen"))
        commands_queue.put(StopCommand())

        render_worker.start()
        render_worker.join()


if __name__ == '__main__':
    main()

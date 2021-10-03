from rendering import create_render_worker
from terminal import Terminal


def main():
    with Terminal() as terminal:
        commands_queue, render_worker = create_render_worker(terminal)

        commands_queue.show_text("Hello there!")
        commands_queue.animate_text("This text should be animated!")
        commands_queue.wait(2)
        commands_queue.clear_screen()
        commands_queue.show_text("This text should be on it's own screen.")
        commands_queue.stop()

        render_worker.start()
        render_worker.join()


if __name__ == '__main__':
    main()

from Game import Game
from rendering import create_render_worker
from terminal import Terminal


def main():
    with Terminal() as terminal:
        terminal.clear_screen()
        commands_queue, render_worker = create_render_worker(terminal)
        game = Game(commands_queue, terminal)

        render_worker.start()

        game.play_case()

        commands_queue.stop()
        render_worker.join()


if __name__ == '__main__':
    main()

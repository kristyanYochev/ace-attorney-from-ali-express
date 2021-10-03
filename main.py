from rendering import create_render_worker
from statement import Statement
from statement_list import StatementList
from terminal import Terminal


def main():
    with Terminal() as terminal:
        commands_queue, render_worker = create_render_worker(terminal)

        render_worker.start()

        statements = StatementList([
            Statement("He is guilty", "Prosecutor"),
            Statement("No, he is not", "Defense Attorney"),
            Statement("But this piece of evidence points to him", "Prosecutor")
        ])

        for statement in statements:
            statement.animate(commands_queue)

        running = True
        while running:
            pressed_key = terminal.get_character()
            if pressed_key == 'w':
                statements.highlight_prev()
            if pressed_key == 's':
                statements.highlight_next()
            if pressed_key == 'q':
                running = False

            commands_queue.clear_screen()
            for statement in statements:
                statement.show(commands_queue, statement is statements.highlighted_statement)

        commands_queue.stop()
        render_worker.join()


if __name__ == '__main__':
    main()

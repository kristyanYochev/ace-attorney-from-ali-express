from typing import List, Optional

from rendering import create_render_worker
from statement import Statement
from terminal import Terminal


def clamp(value: int, min: int, max: int) -> int:
    if value < min:
        return min
    if value > max:
        return max
    return value


class StatementList(list[Statement]):
    def __init__(self, statements: List[Statement]):
        super(StatementList, self).__init__(statements)
        self._highlighted_statement_index = None

    @property
    def highlighted_statement(self) -> Optional[Statement]:
        if self._highlighted_statement_index is None:
            return None
        return self[self._highlighted_statement_index]

    def highlight_next(self):
        if self._highlighted_statement_index is None:
            self._highlighted_statement_index = 0
            return
        self._highlighted_statement_index = clamp(self._highlighted_statement_index + 1, 0, len(self) - 1)

    def highlight_prev(self):
        if self._highlighted_statement_index is None:
            self._highlighted_statement_index = 0
            return
        self._highlighted_statement_index = clamp(self._highlighted_statement_index - 1, 0, len(self) - 1)


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

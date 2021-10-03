from game import Game
from rendering import create_render_worker
from statement import Statement
from statement_list import StatementList
from terminal import Terminal
import FileReader


def main():
    # chars = FileReader.read_characters(0)
    # stages = FileReader.read_script(0)

    with Terminal() as terminal:
        # commands_queue, render_worker = create_render_worker(terminal)
        #
        # render_worker.start()
        #
        # running = True
        # statements = StatementList([])
        #
        # new_statements = StatementList([])
        #
        # new_statements.append(Statement("", chars[stages[0].speeches[0].speaker]['CharacterName']))
        # for line in stages[0].speeches[0].statements:
        #     new_statements.append(Statement(line, ""))
        #
        # for statement in new_statements:
        #     statement.animate(commands_queue)
        #
        # statements.extend(new_statements)
        # speech = 1
        #
        # while running:
        #     pressed_key = terminal.get_character()
        #     if pressed_key == 'w':
        #         statements.highlight_prev()
        #     if pressed_key == 's':
        #         statements.highlight_next()
        #     if pressed_key == 'q':
        #         running = False
        #     if pressed_key == 'e':
        #
        #         new_statements = StatementList([])
        #         new_statements.append(Statement("", chars[stages[0].speeches[speech].speaker]['CharacterName']))
        #         for statement in stages[0].speeches[speech].statements:
        #             new_statements.append(Statement(statement, ""))
        #
        #         for statement in new_statements:
        #             statement.animate(commands_queue)
        #
        #         statements.extend(new_statements)
        #         speech += 1
        #
        #     commands_queue.clear_screen()
        #     for statement in statements:
        #         statement.show(commands_queue, statement is statements.highlighted_statement)
        #
        # commands_queue.stop()
        # render_worker.join()

        game = Game()


if __name__ == '__main__':
    main()

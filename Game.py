import FileReader
from SpeechBlock import SpeechBlock
from rendering.commands import CommandQueue
import re

__all__ = [
    "Game"
]

import Stage
from statement import Statement
from statement_list import StatementList
from terminal import Terminal


def parse(line: str, characters: list[dict]):
    res = line

    matches = re.findall(r"\[\d+]", line)
    character_ids = map(lambda text: int(text[1:-1]), matches)
    for cid in character_ids:
        res = res.replace(f"[{cid}]", characters[cid]["CharacterName"])

    return res


class Game:
    def __init__(self, commands_queue: CommandQueue, terminal: Terminal):
        self.commands_queue = commands_queue
        self.terminal = terminal
        self.case = 0
        self.statements = StatementList([])

    def play_case(self):
        characters = FileReader.read_characters(self.case)
        stages = FileReader.read_script(self.case)

        for stage in range(len(stages)):
            self.play_stage(characters, stages[stage])

    def play_stage(self, characters: list[dict], stage: Stage):
        self.write_speech(stage.speeches[0], characters)
        speech_index = 1

        running = True
        while running:
            pressed_key = self.terminal.get_character()
            if pressed_key == 'w':
                self.statements.highlight_prev()
            if pressed_key == 's':
                self.statements.highlight_next()
            if pressed_key == 'e':
                self.write_speech(stage.speeches[speech_index], characters)
                speech_index += 1
            if pressed_key == 'z':
                self.statements.select_currently_highlighted()
            if pressed_key == 'c':
                self.statements.clear_selection()

            self.commands_queue.clear_screen()
            for i, statement in enumerate(self.statements):
                statement.show(self.commands_queue,
                               statement is self.statements.highlighted_statement,
                               i in self.statements.selected_items)

    def write_speech(self, block: SpeechBlock, chars: list[dict]):
        new_statements = StatementList([])
        new_statements.append(Statement("", chars[block.speaker]['CharacterName']))
        for line in block.statements:
            new_statements.append(Statement(parse(line, chars), ""))

        for statement in new_statements:
            statement.animate(self.commands_queue)
        self.statements.extend(new_statements)
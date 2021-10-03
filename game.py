import json
import os.path
from dataclasses import dataclass
from typing import List, Set


@dataclass
class Character:
    name: str
    name_color: str


@dataclass
class Stage:
    lines: []


@dataclass
class Case:
    characters: List[Character]


class Game:
    _case: Case

    def __init__(self):
        self.load_case(0)

    def load_characters(self, case_number: int) -> List[Character]:
        character_filename = os.path.join(str(case_number), "Characters.json")
        with open(character_filename) as character_file:
            characters_json = json.load(character_file)
        characters = list(map(lambda char_json: Character(**char_json), characters_json))
        return characters

    def load_stages(self, case_number: int, characters: List[Character]) -> None:
        stage_filenames = os.listdir(
            os.path.join(str(case_number), "Stages")
        )

        for filename in stage_filenames:
            path = os.path.join(str(case_number), "Stages", filename)
            with open(path) as stage_file:
                answer_key = stage_file.readline()
                while stage_file:
                    line = stage_file.readline()
                    if line[0] == "<":
                        character_number_string = line[1:-2]
                        character_number = int(character_number_string)
                        character = characters[character_number]



    def load_case(self, case_number: int) -> None:
        characters = self.load_characters(case_number)
        self.load_stages(case_number, characters)

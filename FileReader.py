import json
import os
from Stage import Stage


def read_characters(case_id: int) -> list[dict]:
    return json.load(open(str(case_id) + "\\Charters.json"))["Charters"]


def read_script(case_id: int) -> list[Stage]:
    stages = []
    files = os.listdir(str(case_id) + "\\Stages")
    for file in files:
        lines = open(str(case_id) + "\\Stages\\" + file).read().split('\n')
        stages.append(Stage(lines))
    return stages

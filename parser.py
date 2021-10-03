from typing import List
import re


def parser(line: str, characters: List[str]):
    res = line

    matches = re.findall(r"\[\d+]", line)
    character_ids = map(lambda text: int(text[1:-1]), matches)
    for cid in character_ids:
        res = res.replace(f"[{cid}]", characters[cid])

    return res
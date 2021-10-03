from SpeechBlock import SpeechBlock

__all__ = [
    "Stage"
]


class Stage:
    def __init__(self, file: list[str]):
        self.speeches = []
        self.correct = set(map(lambda n: int(n), file[0].split(", ")))

        speech = SpeechBlock()

        for i in range(1, len(file)):
            if file[i][:1] == "<":
                speech = SpeechBlock()
                self.speeches.append(speech)
                speech.speaker = int(file[i][1:len(file[i]) - 1])
            else:
                self.speeches[len(self.speeches) - 1].statements.append(file[i])
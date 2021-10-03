from SpeechBlock import SpeechBlock

__all__ = [
    "Stage"
]


class Stage:
    def __init__(self, file: list[str]):
        self.speeches = []
        self.win_speech = []
        self.loss_speech = []
        self.correct = set(map(lambda n: int(n), file[0].split(", ")))

        write_speech = self.speeches
        speech = SpeechBlock()

        for i in range(1, len(file)):
            if file[i][:1] == "<":
                speech = SpeechBlock()
                write_speech.append(speech)
                speech.speaker = int(file[i][1:len(file[i]) - 1])
            elif file[i] == "{WIN}":
                write_speech = self.win_speech
            elif file[i] == "{FAIL}":
                write_speech = self.loss_speech
            else:
                speech.statements.append(file[i])
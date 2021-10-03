import os
import sys
from typing import Optional

try:
    import msvcrt
except ImportError:
    # POSIX
    import termios
    import tty


class Terminal:
    """A basic terminal interface.
    Usage for input:

    >>> with Terminal() as terminal:
    >>>     while True:
    >>>         char = terminal.get_character()
    >>>         print(char)
    >>>         if char == 'q':
    >>>             break
    """

    _ANSI_CODE_CLEAR_SCREEN = "\033[2J"
    _ANSI_CODE_MOVE_CURSOR_TOP_LEFT = "\033[1;1H"

    def __init__(self, ansi_escape_codes_supported: Optional[bool] = False):
        if os.name == "posix":
            self.posix = True
        elif os.name == "nt":
            self.posix = False
        else:
            raise RuntimeError("Supporting only POSIX and NT systems")

        self._ansi_escape_codes_supported = ansi_escape_codes_supported
        self._prepare()

    def _prepare(self) -> None:
        if not self.posix:
            return

        self._saved_terminal_options = termios.tcgetattr(sys.stdin)
        tty.setcbreak(sys.stdin)

    def clear_screen(self) -> None:
        if self._ansi_escape_codes_supported:
            print(self._ANSI_CODE_CLEAR_SCREEN)
            print(self._ANSI_CODE_MOVE_CURSOR_TOP_LEFT, end="")
        elif self.posix:
            os.system("clear")
        else:
            os.system("cls")

    def get_character(self) -> str:
        if self.posix:
            return sys.stdin.read(1)
        return msvcrt.getch().decode()

    def finalize(self) -> None:
        if self.posix:
            termios.tcsetattr(
                sys.stdin,
                termios.TCSANOW,
                self._saved_terminal_options
            )

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.finalize()

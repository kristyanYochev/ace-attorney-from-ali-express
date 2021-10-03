from typing import List, Optional

from math_utils import clamp
from statement import Statement


class StatementList(list[Statement]):
    def __init__(self, statements: List[Statement]):
        super(StatementList, self).__init__(statements)
        self._highlighted_statement_index = None
        self.selected_items = []

    @property
    def highlighted_statement(self) -> Optional[Statement]:
        if self._highlighted_statement_index is None:
            return None
        return self[self._highlighted_statement_index]

    def select_currently_highlighted(self) -> None:
        self.selected_items.append(self._highlighted_statement_index)

    def clear_selection(self) -> None:
        self.selected_items = []

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
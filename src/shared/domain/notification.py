from dataclasses import dataclass
from typing import List


@dataclass
class Notification:
    def __init__(self) -> None:
        self._errors: List[str] = []

    def add_error(self, error: str) -> None:

        if error is not None:
            self._errors.append(error)

    @property
    def messages(self) -> str:
        return ",".join(self._errors)

    @property
    def has_errors(self) -> bool:
        return bool(self._errors)

    def __str__(self) -> str:
        return self.messages

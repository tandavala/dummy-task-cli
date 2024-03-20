from dataclasses import dataclass
from typing import List


@dataclass
class Notification:
    def __init__(self) -> None:
        self._errors: List[str] = []

    def add_errors(self, error: str) -> None:
        self._errors.append(error)

    @property
    def messages(self) -> str:
        return ",".join(self._errors)

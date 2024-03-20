from dataclasses import dataclass
from datetime import datetime

from src.tasks.domain.value_objects.priority import Priority


@dataclass
class Task:
    title: str
    description: str
    due_date: datetime = datetime.now()
    priority: Priority = Priority.NORMAL

    def set_due_date(self, due_date: datetime):
        self.due_date = due_date

    def set_priority(self, priority: Priority):
        self.priority = priority

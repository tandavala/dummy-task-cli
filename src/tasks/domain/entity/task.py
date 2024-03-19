from datetime import datetime

from src.tasks.domain.value_objects.priority import Priority


class Task:

    def __init__(
        self,
        title: str,
        description: str,
        due_date: datetime = datetime.now(),
        priority: Priority = Priority.NORMAL,
    ) -> None:
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority

    def set_due_date(self, due_date: datetime):
        self.due_date = due_date

    def set_priority(self, priority: Priority):
        self.priority = priority

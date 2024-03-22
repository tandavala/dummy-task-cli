from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from src.tasks.domain.value_objects.priority import Priority
from src.shared.domain.entity import Entity


@dataclass
class Task(Entity):
    title: str
    description: Optional[str] = ""
    due_date: datetime = datetime.now()
    priority: Priority = Priority.NORMAL

    def __post_init__(self):
        self.validate()

    def set_due_date(self, due_date: datetime):
        self.due_date = due_date

    def set_priority(self, priority: Priority):
        self.priority = priority

    def validate(self):
        if len(self.title) > 255:
            self.notification.add_error("title cannot be longer than 255")

        if not self.title:
            self.notification.add_error("title cannot be empty")

        if len(self.description) > 1024:
            self.notification.add_error("description cannot be longer than 1024")

        if self.notification.has_errors:
            raise ValueError(self.notification.messages)




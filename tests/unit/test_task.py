from datetime import datetime
import pytest
from src.tasks.domain.entity.task import Task
from src.tasks.domain.value_objects.priority import Priority


class TestTask:
    def test_can_create_task_with_default_values(self, task_dto):
        title = task_dto.get('title')
        description = task_dto.get('description')

        task = Task(title=title, description=description)
        assert task.title == title
        assert task.description == description
        assert task.due_date.date() == datetime.now().date()
        assert task.priority == Priority.NORMAL

    def test_can_create_task_with_high_priority(self, task_dto):
        pass

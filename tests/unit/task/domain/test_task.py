from datetime import datetime
import pytest
from src.tasks.domain.entity.task import Task
from src.tasks.domain.value_objects.priority import Priority


class TestTask:
    def test_can_create_task_with_default_values(self, task_dto):
        title = task_dto.get("title")
        description = task_dto.get("description")

        task = Task(title=title, description=description)
        assert task.title == title
        assert task.description == description
        assert isinstance(task.due_date, datetime)
        assert task.priority == Priority.NORMAL

    def test_can_create_task_with_high_priority(self, task_dto):
        title = task_dto.get("title")
        description = task_dto.get("description")

        task = Task(title, description, priority=Priority.HIGH)
        assert task.title == title
        assert task.description == description
        assert isinstance(task.due_date, datetime)
        assert task.priority == Priority.HIGH

    def test_can_create_task_with_low_priority(self, task_dto):
        title = task_dto.get("title")
        description = task_dto.get("description")

        task = Task(title, description, priority=Priority.LOW)
        assert task.title == title
        assert task.description == description
        assert task.priority == Priority.LOW
        assert isinstance(task.due_date, datetime)

    def test_task_title_validation(self):
        with pytest.raises(ValueError, match="^title cannot be empty$") as excinfo:
            Task(title="")

    def test_task_description_validation(self):
        with pytest.raises(
            ValueError, match="^description cannot be longer than 1024$"
        ) as excinfo:
            Task(title="valid title", description="a" * 1025)

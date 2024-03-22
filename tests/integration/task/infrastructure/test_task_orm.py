
from datetime import datetime
from sqlalchemy import text

from src.tasks.domain.entity.task import Task
from src.tasks.domain.value_objects.priority import Priority


def test_task_mapper_can_load_tasks(session, task_dto):
    curr = datetime.now()
    session.execute(
        text(
            "INSERT INTO tasks (title, description, due_date, priority) "
            "VALUES (:title, :description, :due_date, :priority)"
        ),
        {
            "title": task_dto.get("title"),
            "description": task_dto.get("description"),
            "due_date": curr,
            "priority": Priority.NORMAL.value,  # Use enum's underlying value
        },
    )
    expected = [
        Task(
            title=task_dto.get("title"),
            description=task_dto.get("description"),
            due_date=curr,
            priority=Priority.NORMAL,  # Use enum directly
        )
    ]

    assert session.query(Task).all() == expected

   

    



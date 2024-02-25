import sys
sys.path.append("..")

# fmt: off
import pytest
from src.tasks.task import Task
# fmt: on


def test_add_return_valid_id(tasks_db):
    """task.add(<valid_id>) should return an integer"""
    # GIVEN an initialized tasks db
    # WHEN a new task id added
    # THEN returned task_id is of type int
    task_id = Task.add(Task('do something'))
    assert isinstance(task_id, int)


@pytest.mark.smoke
def test_added_task_has_id_set():
    """Make sure the task_id filed is set by tasks.add()"""
    # GIVEN an initialized tasks db
    # AND a new task is added

    new_task = Task('sit in chair', owner='me', done=True)
    task_id = Task.add(new_task)

    # WHEN task is retrieved
    task_from_db = Task.get(task_id)

    # THEN task_id matches id field
    assert task_from_db.id == task_id


def test_add_increases_count(db_with_3_tasks):
    """Test Task.add() affect on Task.count()"""
    # GIVEN a db with 3 tasks
    # WHEN another task is added
    Task.add(Task('throw a party'))

    # THEN the count increase by 1
    assert Task.count() == 6

import sys
sys.path.append("..")

# fmt: off
import pytest
from src.tasks.task import Task 
# fmt: on


def test_add_raise():
    """add() should raise an exception with wrong type param"""
    with pytest.raises(TypeError):
        Task.add(task="not a task object")


def test_start_tasks_db_raises():
    """Make sure unsupported db raises an exception"""
    with pytest.raises(ValueError) as excinfo:
        Task.start_tasks_db('some/great/path', 'mysql')
        exception_msg = excinfo.value.args[0]
        assert exception_msg == "db_type must be a 'tiny' or 'mongo'"


@pytest.mark.smoke
def test_list_raises():
    """list() should raise an exception with wrong type param."""
    with pytest.raises(TypeError):
        Task.list_tasks(owner=123)


@pytest.mark.get
@pytest.mark.smoke
def test_get_raises():
    """get() should raise an exception with wrong param."""
    with pytest.raises(TypeError):
        Task.get(task_id='123')

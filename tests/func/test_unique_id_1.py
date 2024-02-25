import sys
sys.path.append("..")

# fmt: off
import pytest
from src.tasks.task import Task
# fmt: on


def initialized_tasks_db(tempdir):
    """Connect to db before testing, disconnect after"""
    # Setup: start db
    Task.start_tasks_db(str(tempdir), 'tiny')
    yield
    Task.stop_tasks_db()


@pytest.mark.skipif(Task.__version__ < '1.0.0', reason='Task Version is less than 1.0.0')
def test_unique_id_1():
    """Calling unique_id() twice should return different numbers"""

    id_1 = Task.unique_id()
    id_2 = Task.unique_id()
    assert id_1 != id_2


def test_unique_id_2():
    ids = []
    ids.append(Task.add(Task('One')))
    ids.append(Task.add(Task('Two')))
    ids.append(Task.add(Task('Three')))

    uid = Task.unique_id()

    assert uid not in ids


@pytest.mark.xfail(Task.__version__ > '1.0.0', reason='reason why')
def test_xfail():
    id_1 = Task.unique_id()
    id_2 = Task.unique_id()
    assert id_1 != id_2


@pytest.mark.xfail()
def test_unique_id_not_a_duck():
    """Demonstrate xpass"""
    uid = Task.unique_id()
    assert uid != 'a duck'

import pytest


@pytest.fixture
def task_dto():
    return {"title": "Task # 1", "description": "Description task # 1"}

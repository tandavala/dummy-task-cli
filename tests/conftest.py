import pytest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, clear_mappers

from src.tasks.infrastructure.sqlalchemy_orm.task_orm import (
    mapper_registry,
    start_mappers,
)


@pytest.fixture
def task_dto():
    return {"title": "Task # 1", "description": "Description task # 1"}


@pytest.fixture
def in_memory_db():
    engine = create_engine("sqlite:///:memory:")
    mapper_registry.metadata.create_all(engine)
    return engine


@pytest.fixture
def session_factory(in_memory_db):
    start_mappers()
    yield sessionmaker(bind=in_memory_db)
    clear_mappers()


@pytest.fixture
def session(session_factory):
    return session_factory()

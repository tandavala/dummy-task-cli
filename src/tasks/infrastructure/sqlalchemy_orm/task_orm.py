from datetime import datetime
from sqlalchemy import Table, Column, Integer, String, Date, Enum
from sqlalchemy.orm import registry

from src.tasks.domain.entity.task import Task
from src.tasks.domain.value_objects.priority import Priority

mapper_registry = registry()

tasks = Table(
    'tasks',
    mapper_registry.metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('title', String(255)),
    Column('description', String),
    Column('due_date', Date),
    Column('priority', Enum(Priority)),
    Column('created_at', Date, default=datetime.now())
)

def start_mappers():
    mapper_registry.map_imperatively(Task, tasks)
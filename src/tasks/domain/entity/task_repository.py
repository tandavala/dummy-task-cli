from abc import ABC, abstractclassmethod

from src.tasks.domain.entity.task import Task


class TaskRepository(ABC):

    @abstractclassmethod
    def save(self, task: Task) -> Task:
        raise NotImplementedError

    @abstractclassmethod
    def get_by_id(self, id: int) -> Task:
        raise NotImplementedError

    @abstractclassmethod
    def delete(self, id: int) -> None:
        raise NotImplementedError

    @abstractclassmethod
    def list(self) -> list[Task]:
        raise NotImplementedError

    @abstractclassmethod
    def update(self, task: Task) -> None:
        raise NotADirectoryError

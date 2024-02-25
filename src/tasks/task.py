class Task:
    __version__ = '1.0.1'
    last_assigned_id = 0
    tasks = {}

    def __init__(self, summary: str = None, owner: str = None, done: bool = False) -> None:
        self.id = None
        self.summary = summary
        self.owner = owner
        self.done = done

    @classmethod
    def add(cls, task) -> int:
        if not isinstance(task, Task):
            raise TypeError("Param 'task' must be an object of class Task")
        task.id = cls.unique_id()
        cls.tasks[task.id] = task
        return task.id

    @classmethod
    def get(cls, task_id):
        if not isinstance(task_id, int):
            raise TypeError("Param 'task_id' must be an integer")
        return cls.tasks.get(task_id)

    @classmethod
    def list_tasks(owner=None):
        if not isinstance(owner, (str, type(None))):
            raise TypeError("Para 'owner must be a'")

    @classmethod
    def count(cls):
        return len(cls.tasks)

    @classmethod
    def update(cls, task_id, task):
        if not isinstance(task_id, int):
            raise TypeError("Param 'task_id' must be an integer")
        result = cls.tasks.get(task_id)
        cls.tasks[task_id] = task

    @classmethod
    def delete(task_id):
        pass

    @classmethod
    def unique_id(cls):
        cls.last_assigned_id += 1
        return cls.last_assigned_id

    @staticmethod
    def start_tasks_db(db_path, db_type):
        if db_type not in ['tiny', 'mongo']:
            raise ValueError("db_type must be 'tiny' or 'mongo'")
        pass

    @staticmethod
    def stop_tasks_db():
        pass

    @staticmethod
    def delete_all():
        pass

    def to_dict(self):
        return self.__dict__

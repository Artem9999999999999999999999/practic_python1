# practic_python2

Университетский курс по Питону. Задачи, которые могут быть полезны на собеседовании


+ [Task manager](#Task-manager)


## Task manager


```python
from typing import Dict, Generic, TypeVar

class TaskStatus(enum.Enum):
    OPEN = 1
    IN_PROGRESS = 2
    DONE = 3


class Task:
    def __init__(self, id: int = None, name: str = "", description: str = ""):
        self.id = id
        self.name = name
        self.description = description
        self.status = TaskStatus.OPEN

    def mark_in_progress(self):
        if self.status == TaskStatus.OPEN:
            self.status = TaskStatus.IN_PROGRESS
        else:
            raise WrongTaskStatusError()

    def mark_done(self):
        if self.status == TaskStatus.IN_PROGRESS:
            self.status = TaskStatus.DONE
        else:
            raise WrongTaskStatusError()


class Subtask(Task):
    def __init__(self, parent_id: int = None, id: int = None, name: str = "", description: str = ""):
        super().__init__(id, name, description)
        self.parent_id = parent_id


class ComplexTask(Task):
    def __init__(self, id: int = None, name: str = "", description: str = "", subtasks=None):
        super().__init__(id, name, description)
        self.subtasks = subtasks or []

    def add_subtask(self, subtask: Subtask):
        if subtask.parent_id != self.id:
            raise WrongSubtaskError(f"Subtask has incorrect parent id: {self.id} != {subtask.parent_id}")
        self.subtasks.append(subtask)

    def mark_in_progress(self):
        super().mark_in_progress()
        for subtask in self.subtasks:
            subtask.mark_in_progress()

    def mark_done(self):
        super().mark_done()
        for subtask in self.subtasks:
            subtask.mark_done()


InnerContainerType = TypeVar("InnerContainerType", bound=Task)


class TaskContainer(Generic[InnerContainerType]):
    def __init__(self):
        self.tasks: Dict[int, InnerContainerType] = {}

    def add(self, task: InnerContainerType):
        self.tasks[task.id] = task

    def get_by_id(self, id):
        return self.tasks.get(id, None)

    def get_all(self):
        return list(self.tasks.values())

    def remove_by_id(self, id):
        return self.tasks.pop(id)

    def remove_all(self):
        return self.tasks.clear()


class TaskManager:
    def __init__(self):
        self.task_counter = 0
        self.tasks: TaskContainer[Task] = TaskContainer()
        self.subtasks: TaskContainer[Subtask] = TaskContainer()
        self.complex_tasks: TaskContainer[ComplexTask] = TaskContainer()

    def __get_new_id(self) -> int:
        self.task_counter += 1
        return self.task_counter

    def __create_task(self, task_container: TaskContainer, task: Task) -> int:
        task.id = self.__get_new_id()
        task_container.add(task)
        return task.id

    def create_task(self, task: Task):
        return self.__create_task(self.tasks, task)

    def create_subtask(self, subtask: Subtask):
        return self.__create_task(self.subtasks, subtask)

    def create_complex_task(self, complex_task: ComplexTask):
        return self.__create_task(self.complex_tasks, complex_task)

    @staticmethod
    def __get_tasks(task_container: TaskContainer):
        return task_container.get_all()

    def get_tasks(self):
        return self.__get_tasks(self.tasks)

    def get_subtasks(self):
        return self.__get_tasks(self.subtasks)

    def get_complex_tasks(self):
        return self.__get_tasks(self.complex_tasks)

    @staticmethod
    def __get_tasks_by_id(task_container: TaskContainer, id: int):
        return task_container.get_by_id(id)

    def get_tasks_by_id(self, id: int):
        return self.__get_tasks_by_id(self.tasks, id)

    def get_subtasks_by_id(self, id: int):
        return self.__get_tasks_by_id(self.subtasks, id)

    def get_complex_tasks_by_id(self, id: int):
        return self.__get_tasks_by_id(self.complex_tasks, id)

    @staticmethod
    def __remove_tasks(task_container: TaskContainer):
        return task_container.remove_all()

    def remove_tasks(self):
        return self.__remove_tasks(self.tasks)

    def remove_subtasks(self):
        return self.__remove_tasks(self.subtasks)

    def remove_complex_tasks(self):
        return self.__remove_tasks(self.complex_tasks)

    @staticmethod
    def __remove_task_by_id(task_container: TaskContainer, id: int):
        return task_container.remove_by_id(id)

    def remove_task_by_id(self, id: int):
        return self.__remove_task_by_id(self.tasks, id)

    def remove_subtask_by_id(self, id: int):
        return self.__remove_task_by_id(self.subtasks, id)

    def remove_complex_task_by_id(self, id: int):
        return self.__remove_task_by_id(self.complex_tasks, id)

    @staticmethod
    def mark_in_progress(task: Task):
        return task.mark_in_progress()

    @staticmethod
    def mark_done(task: Task):
        return task.mark_done()

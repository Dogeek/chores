from pathlib import Path
import json


class TaskStatus:
    PENDING = 0
    STARTED = 1
    PAUSED = 2
    COMPLETED = 3


class Task:
    def __init__(self, name, description="", status=None):
        if status is None:
            status = TaskStatus.PENDING

        self.name = name
        self.description = description
        try:
            self._status = int(status)
        except ValueError:
            self._status = status

    def __str__(self):
        if self.description:
            return f"({self.status_string}) {self.name} : {self.description}"
        else:
            return f"({self.status_string}) {self.name}"

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        if isinstance(value, str):
            if value.upper() not in TaskStatus.__dict__.keys():
                raise ValueError
            self._status = TaskStatus.__dict__.get(value.upper(), 0)
        elif isinstance(value, int):
            self._status = value
        else:
            raise TypeError

    @property
    def status_string(self):
        for key, value in [(k, v) for k, v in TaskStatus.__dict__.items() if k.isupper()]:
            if self._status == value:
                return key
        return "UNDEFINED"

    def serialize(self):
        return {
            "name": self.name,
            "description": self.description,
            "status": self._status,
        }


class TaskList:
    def __init__(self):
        self.tasks = []
        self.filename = None

    def __getitem__(self, item):
        return self.tasks[item]

    def load(self, filename=None):
        if filename is None:
            filename = Path.home().joinpath(".chores")

        self.filename = filename

        if not Path(filename).exists():
            return

        with open(filename) as f:
            data = json.load(f)
            self.tasks = [Task(**d) for d in data]

    def add_task(self, task):
        if len(self.tasks) <= 10:
            self.tasks.append(task)
        else:
            print("Task list is full, please delete a task before adding any more.")
            exit(1)

    def get_task(self, task_name):
        for t in self:
            if t.name.lower() == task_name.lower():
                return t
        print(f"Task {task_name} does not exist.")
        exit(1)

    def get_task_index(self, task_name):
        task = self.get_task(task_name)
        return self.tasks.index(task)

    def serialize(self):
        return [t.serialize() for t in self.tasks]

import json

import ipywidgets as widgets
from IPython.display import display


class TaskList(object):

    @classmethod
    def from_json(cls, path):
        with open(path, 'r') as f:
            tasks = json.load(f)
        return cls(tasks)

    def __init__(self, tasks):
        if isinstance(tasks, list):
            tasks = {task: False for task in tasks}
        self._boxes = []
        for task, state in tasks.items():
            if not isinstance(task, str):
                raise ValueError('All tasks must be strings')
            if not isinstance(state, bool):
                raise ValueError('All values must be boolean type')
            box = widgets.Checkbox(
                value=state,
                description=task,
                disabled=False,
            )
            self._boxes.append(box)

    def __repr__(self):
        out = '{\n'
        for task, value in self.tasks.items():
            if "'" in task:
                quotes = '"'
            else:
                quotes = "'"
            out += f'    {quotes}{task}{quotes}: {value},\n'
        out += '}'
        return out

    def display(self):
        for box in self._boxes:
            display(box)

    def sort_tasks(self, by_task=True, by_state=False):
        if not by_task and not by_state:
            raise ValueError('Must be by task or by state')

        def key(box):
            if by_task and by_state:
                return (not box.value, box.description)
            elif by_task and not by_state:
                return box.description
            elif not by_task and by_state:
                return not box.value

        self._boxes = sorted(self._boxes, key=key)

    def new_task(self, task, state=False):
        if task in self.tasks:
            raise ValueError('Cannot have two of the same tasks')
        new_box = widgets.Checkbox(
            value=state,
            description=task,
            disabled=False,
        )
        self._boxes.append(new_box)

    def remove_task(self, task):
        new_boxes = []
        for box in self._boxes:
            if task != box.description:
                new_boxes.append(box)
        self._boxes = new_boxes

    @property
    def tasks(self):
        return {box.description: box.value for box in self._boxes}

    def to_json(self, path):
        with open(path, 'w') as f:
            json.dump(self.tasks, f, indent=4)

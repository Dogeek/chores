from .models import Task


def add(task_list, args):
    task = Task(args.task_name, args.description)
    task.status = args.status
    task_list.add_task(task)
    return

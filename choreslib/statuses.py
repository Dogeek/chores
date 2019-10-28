def _set_status(task_list, task_name, status):
    task = task_list.get_task(task_name)
    task.status = status


def done(task_list, args):
    _set_status(task_list, args.task, "completed")
    return


def start(task_list, args):
    _set_status(task_list, args.task, "started")
    return


def pause(task_list, args):
    _set_status(task_list, args.task, "paused")
    return


def remove(task_list, args):
    task = task_list.get_task(args.task)
    task_list.tasks.remove(task)
    return

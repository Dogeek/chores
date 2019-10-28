def remove(task_list, args):
    if args.task == "ALL":
        task_list.tasks = []
        return

    task = task_list.get_task(args.task)
    task_list.tasks.remove(task)
    return

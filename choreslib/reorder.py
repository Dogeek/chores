def reorder(task_list, args):
    from_index = task_list.get_task_index(args.task_from)
    to_index = task_list.get_task_index(args.task_to)
    task_list.tasks.insert(to_index, task_list.tasks.pop(from_index))
    return

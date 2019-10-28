def _format(task_list, task, view_indices):
    if view_indices:
        return f"{task_list.tasks.index(task) + 1} : {str(task)}"
    else:
        return str(task)


def view(task_list, args):
    if args.status_filter == "all":
        for task in task_list:
            print(_format(task_list, task, args.view_indices))
    else:
        for task in [t for t in task_list if t.status_string.lower() == args.status_filter]:
            print(_format(task_list, task, args.view_indices))
    return

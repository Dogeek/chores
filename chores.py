# FEATURES
# Add up to 10 (ten) tasks
# Reorder tasks
# Start/Pause/Done tasks
# View last 10 completed tasks
import argparse
import choreslib


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--tasklist", default=None, type=str,
                        help="Specifies a file path to an existing task list")
    subparsers = parser.add_subparsers()

    # ADD TASK ACTION PARSER
    add_parser = subparsers.add_parser("add", help="Add a task to the task list",
                                       aliases=["a"])
    add_parser.add_argument("task_name", help="The name of the task",
                            type=str)
    add_parser.add_argument("--description", help="A description for this task",
                            type=str, default="")
    add_parser.add_argument("--status", help="Optional status to set the task to.",
                            choices=["pending", "started", "paused", "completed"],
                            type=str, default="pending")
    add_parser.set_defaults(func=choreslib.add)

    # REMOVE TASK ACTION PARSER
    rm_parser = subparsers.add_parser("remove", aliases=["rm"],
                                      help="Remove a task from the task list")
    rm_parser.add_argument("task", type=str, help="Task to remove, 'ALL' to remove every task")
    rm_parser.set_defaults(func=choreslib.remove)

    # REORDER ACTION PARSER
    reorder_parser = subparsers.add_parser("reorder", help="The reorder command help",
                                           aliases=["ro"])
    reorder_parser.add_argument("task_from", help="Task name to move", type=str)
    reorder_parser.add_argument("task_to", help="Task name to exchange with.", type=str)
    reorder_parser.set_defaults(func=choreslib.reorder)

    # START ACTION PARSER
    start_parser = subparsers.add_parser("start", help="Start a task",
                                         aliases=["s"])
    start_parser.add_argument("task", help="The task to start",
                              type=str)
    start_parser.set_defaults(func=choreslib.start)

    # PAUSE ACTION PARSER
    pause_parser = subparsers.add_parser("pause", help="Pause a task",
                                         aliases=["p"])
    pause_parser.add_argument("task", help="The task to pause",
                              type=str)
    pause_parser.set_defaults(func=choreslib.pause)

    # DONE ACTION PARSER
    done_parser = subparsers.add_parser("done", help="Set a task as done",
                                        aliases=["d"])
    done_parser.add_argument("task", help="The task to complete",
                             type=str)
    done_parser.set_defaults(func=choreslib.done)

    # VIEW ACTION PARSER
    view_parser = subparsers.add_parser("view", help="View the last 10 completed tasks",
                                        aliases=["v"])
    view_parser.add_argument("--status_filter", help="Filters tasks to view by status.",
                             choices=["pending", "started", "paused", "completed", "all"],
                             type=str, default="all")
    view_parser.add_argument("--view-indices", "-i", help="Show task indices",
                             type=bool, default=False, dest="view_indices", const=True, nargs="?")
    view_parser.set_defaults(func=choreslib.view)

    # PARSE THE ARGS AND EXECUTE
    args = parser.parse_args()
    task_list = choreslib.TaskList()
    task_list.load(args.tasklist)
    args.func(task_list, args)

    choreslib.save(task_list)


if __name__ == "__main__":
    main()

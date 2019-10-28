import json


def save(task_list):
    filename = task_list.filename

    with open(filename, "w") as f:
        json.dump(task_list.serialize(), f)
    return

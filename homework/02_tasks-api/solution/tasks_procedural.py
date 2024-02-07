"""Procedural task store

Note:
    It is best to avoid declaring variables outside functions, classes,
    and control flow statements. Global variables make it difficult to
    debug and test code. Instead, use classes to encapsulate the state
    of the application.
"""

tasks = {}  # avoid this
counter = 1  # avoid this


def create_uid():
    global counter  # avoid this
    uid = counter
    counter += 1
    return uid


def create_task(name, due=None):
    uid = create_uid()
    new_task = {"uid": uid, "name": name, "due": due}
    tasks[uid] = new_task
    return new_task


def get_task(uid):
    return tasks[uid]


def delete_task(uid):
    tasks.pop(uid)

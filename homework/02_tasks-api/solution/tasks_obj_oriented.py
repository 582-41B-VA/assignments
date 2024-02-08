"""Object-oriented task store

Note:
    Unlike the procedural version, the state of the store in this
    object-oriented version is encapsulated in the scope of the class.
    There are no global variables, which makes the code easier to test
    and maintain.
"""


class TaskStore:
    def __init__(self):
        self.tasks = {}
        self._counter = 1

    def _create_uid(self):
        uid = self._counter
        self._counter += 1
        return uid

    def create_task(self, name, due=None):
        uid = self._create_uid()
        new_task = {"uid": uid, "name": name, "due": due}
        self.tasks[uid] = new_task
        return new_task

    def get_task(self, uid):
        return self.tasks[uid]

    def delete_task(self, uid):
        return self.tasks.pop(uid)

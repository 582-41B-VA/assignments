"""Server module for a tasks management application."""

from http.server import BaseHTTPRequestHandler, HTTPServer

from form_urlencoded import get_POST_data
from taskstore import TaskStore


class Router(BaseHTTPRequestHandler):
    """A router."""

    taskstore = TaskStore()

    def do_GET(self):
        """Handle GET requests."""
        if self.path == "/":
            body = str(self.taskstore.tasks)
            self._respond(200, body)
        elif self.path.startswith("/task/"):
            task_uid = self._uid_from_path()
            task = self.taskstore.get_task(task_uid)
            body = str(task)
            self._respond(200, body)
        else:
            self._respond(404, "Page Not Found")

    def do_POST(self):
        """Handle POST requests."""
        if self.path == "/task":
            task_data = get_POST_data(self)
            task_name = task_data["name"]
            task_due = task_data["due"] if "due" in task_data else None
            self.taskstore.create_task(task_name, task_due)
            self._respond(200, "Task created.")
        else:
            self._respond(405, "Method Not Allowed")

    def do_DELETE(self):
        """Handle DELETE requests."""
        if self.path.startswith("/task/"):
            task_uid = self._uid_from_path()
            self.taskstore.delete_task(task_uid)
            body = f"Task {task_uid} deleted."
            self._respond(200, body)
        else:
            self._respond(405, "Method Not Allowed")

    def _respond(self, code, body):
        """Send response to client, including headers and body.

        Args:
            code (int): Response code (e.g., 200, 404, etc.)
            body (str): Body of the response.
        """
        self.send_response(code)
        self.end_headers()
        body = body + "\n"
        self.wfile.write(body.encode())

    def _uid_from_path(self):
        """Return UID (int) from the current URL path."""
        path_segments = self.path.split("/")
        task_uid = int(path_segments[-1])
        return task_uid


address = ("localhost", 8080)
server = HTTPServer(address, Router)
print(
    f"Server listening at http://{address[0]}:{address[1]} ...\n"
    "Press CTRL + C to stop."
)
server.serve_forever()

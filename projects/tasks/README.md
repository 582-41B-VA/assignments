# Project: Tasks

Now that you have written the task management application's interface,
the last step is to expose its functions to clients. To do so, you will implement a simple HTTP server using Python's standard library.

## Requirements

-   The server must use the `HTTPServer` and `BaseHTTPRequestHandler`
    classes from the [`http.server` standard module][doc].
-   It must be possible to get all tasks, get a specific task, add
    a new task, and delete a task.
-   Requests with unknown URLs should receive a 404 response code with a
    "page not found" error message.
-   The source code must be formatted using [Black][].
-   The source code must be linted with [Pylint][].
-   Modules, classes and functions (including parameters) must be
    documented using the style guide seen in class.

[doc]: https://docs.python.org/3/library/http.server.html
[Black]: https://pypi.org/project/black/
[Pylint]: https://pypi.org/project/pylint/

Use the following `curl` commands to test your server:

```sh
# should return all tasks
curl localhost:8080

# should return the task corresponding to the ID (1, 2, 3, etc.)
curl localhost:8080/task/1

# should delete the task corresponding to the ID (1, 2, 3, etc.)
curl localhost:8080/task/1 -X DELETE

# should add a new task
curl localhost:8080/task -d "name=Buy+milk&due=2017-06-01"
```

The curl program can be downloaded [here][curl download], or through the
package manager of your choice.

[curl download]: https://curl.se/download.html

## Tips

-   Start by listing all possible *routes*. A route is the combination
    of an HTTP verb (GET, POST, PUT, DELETE, etc.), a URL path/pattern,
    and a function that is called to handle that pattern.
-   Unsure how to parse the URL to get the ID? Take a look at the [built-in
    string methods][].

[built-in string methods]: https://docs.python.org/3/library/stdtypes.html#string-methods

## Extra

-   Use decorators to define routes.
-   Add a route for updating tasks.

## Grading [10]

-   Requirements are met.
-   Requests are well-formed (including headers).
-   Program is free of dead code (unused variables and functions).
-   Naming is descriptive and consistant.
-   Prose is correct and helpful.
-   Program flow is decomposed into manageable, logical pieces.
-   Common code is unified, and not duplicated.
-   No global variables are used.
-   Data structure is appropriate.
-   Constant values are assigned to variables.

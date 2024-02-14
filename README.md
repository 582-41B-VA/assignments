# Assignment Submission Guidelines

All assignments for this course must be submitted using GitHub
Classroom.

## Homework

Homework must be submitted in your GitHub Classroom repository of the
project related to said homework: "tasks-username" for week 1,
"newspaper-username" for week 2 and 3.

Submissions must be identified by an [annotated Git tag][] pointing to a
commit on the "main" branch. The tag's name must identify the submission
using a **minor** version number: "v0.1", "v0.2", "v0.3" for homework of
weeks 1 and 2, "v1.1", "v1.2", "v1.3" for homework of week 3.

## Projects

Project submissions must also be identified by an [annotated Git tag][],
but its name must be a **major** version number: "v1.0" for Tasks,
"v1.0" for part 1 of Newspaper and "v2.0" for part 2 of Newspaper.

## LIA

The learning integration assessment must be submitted in the GitHub
Classroom repository named "lia-username". The submission must be
identified with an [annotated Git tag][] named "v1.0".

[annotated Git tag]: https://git-scm.com/book/en/v2/Git-Basics-Tagging

## Example

Here is an example of how to submit an assignment once it is done.
Replace `<placeholders>` with the appropriate values.

```sh
git add <files to submit>
git commit -m "<Describe changes made>"
git tag <tag name> -m "Submit <assignment name>"
git push --follow-tags
```
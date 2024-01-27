# Homework: Git Classroom

Your first homework is to accept the GitHub Classroom assignment for the
Task project. In order to do so, click on this [invitation link][GitHub
Classroom assignment] and follow the instructions:

[GitHub Classroom assignment]: https://classroom.github.com/a/8usUq9vd

1.  Once you have accepted the assignment, a Git repository will be
    created for you. Its name should be "task" followed by your GitHub
    username. For instance, "task-maxime-pigeon". [Clone][git clone]
    this repository on your computer.

[git clone]: https://git-scm.com/docs/git-clone

2.  Add a "README" file at the root of your [working tree][], and
    [commit][] your change on the "main" branch of the repository.
    Remember to always write [well formed commit messages][].

[working tree]: https://git-scm.com/docs/gitglossary#Documentation/gitglossary.txt-aiddefworkingtreeaworkingtree
[commit]: https://git-scm.com/docs/git-commit
[well formed commit messages]: https://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html

3.  Add an [annotated tag][] pointing to the commit created above. The
    tag's name must be "v0.1".

[annotated tag]: https://git-scm.com/book/en/v2/Git-Basics-Tagging

4.  Finally, to submit your homework, [push][] your commit and your tag
    to the GitHub remote repository with the following command:

    ```sh
    git push --follow-tags
    ```

    To make sure your homework has been correctly submitted, verify that
    the GitHub remote repository contains both the commit and the tag.

[push]: https://git-scm.com/docs/git-push

## Learning Git

If you feel uncomfortable using Git, the best learning resource is the
*Pro Git* book, written by Scott Chacon and Ben Straub. The book is
available for free in multiple languages [here][Pro Git].

[Pro Git]: https://git-scm.com/book/en/v2

Learning Git's command-line interface without understanding its
underlying data model can lead to a lot of confusion. Once the data
model is understood, the commands can be better comprehended in terms of
how they manipulate the underlying structure. Although *Pro Git* has a
[chapter on Git's internals][Git internals], I strongly recommend [Anish
Athalye's lecture][] on the subject.

[Git internals]: https://git-scm.com/book/en/v2/Git-Internals-Plumbing-and-Porcelain
[Anish Athalye's lecture]: https://missing.csail.mit.edu/2020/version-control/
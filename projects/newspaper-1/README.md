# Project: Newspaper part 1

In class, you have created a Django project named "newspaper", as well
as an application called "polls". Any newspaper without a proper
newsroom is not worth the name. Accordingly, for this first submission
of the Newspaper project, you are asked to create a "news" application.

## Requirements

-   The application has a homepage view at the URL "/news".
-   The homepage must dynamically lists all the news articles.
-   Each article has a view that lists the title, the text, as well as
    the author of the article.
-   Each article also dynamically lists other articles written by the
    same author, excluding the current article.
-   It is possible to create and modify articles and authors from the
    admin panel.

## Tips

-   Re-read [part 2 of the tutorial][].
-   [How to make queries in Django][Making queries].
-   [URL dispatcher][].

[part 2 of the tutorial]: https://docs.djangoproject.com/en/5.0/intro/tutorial02/
[Making queries]: https://docs.djangoproject.com/en/5.0/topics/db/queries/
[URL dispatcher]: https://docs.djangoproject.com/en/5.0/topics/http/urls/

## Grading [10]

-   Requirements are met.
-   Program is free of dead code (unused variables and functions).
-   Naming is descriptive and consistant.
-   Prose is correct and helpful.
-   Program flow is decomposed into manageable, logical pieces.
-   Common code is unified, and not duplicated.
-   APIs are used correctly.
-   Models are properly displayed in the admin panel.
-   Code is properly formatted and linted.

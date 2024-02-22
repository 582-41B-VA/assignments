# Project: Pig latin translator

Pig Latin is a made-up children's language that's intended to be
confusing. It obeys a few simple rules (below), but when it's spoken
quickly it's really difficult for non-children (and non-native speakers)
to understand.

## Rules

1.  If a word begins with a vowel sound, add an "ay" sound to the end of
    the word (e.g. "eat" = "eatay", "omelet" = "omeletay", "are" = "areay").

2.  "xr" and "yt" at the beginning of a word make vowel sounds (e.g.
    "xray" = "xrayay", "yttria" = "yttriaay").

2.  If a word begins with a consonant sound, move it to the end of the
    word and then add an "ay" sound to the end of the word (e.g. "pig" =
    "igpay", "latin" = "atinlay", "banana" = "ananabay"). Consonant sounds
    can be made up of multiple consonants, such as the "ch" in "chair"
    or "st" in "stand" (e.g. "chair" = "airchay").

3.  If a word starts with a consonant sound followed by "qu", move it to
    the end of the word, and then add an "ay" sound to the end of the
    word (e.g. "square" = "aresquay").

4.  If a word contains a "y" after a consonant cluster or as the second
    letter in a two letter word it makes a vowel sound (e.g. "rhythm" =
    "ythmrhay", "my" = "ymay").

## Instructions

-   Implement a program that translates sentences from English to Pig
    Latin.
-   The program must take input from the terminal.
-   The program must be tested using the [unittest module][].

[unittest module]: https://docs.python.org/3/library/unittest.html

## Tips

-   Start by defining your test cases, then build the program.
-   The [`input()` built-in function][] returns input from the terminal.

[`input()` built-in function]: https://docs.python.org/3/library/functions.html#input

## Submission

The project must be submitted using [GitHub Classroom][]. Accept the assignment, clone the repository, and push your changes to submit.

[GitHub Classroom]: https://classroom.github.com/a/Pr9wthIB

## Grading [10]

-   Requirements are met.
-   Program is free of dead code (unused variables and functions).
-   Naming is descriptive and consistant.
-   Modules are properly documented, and prose is correct and
    helpful.
-   Program flow is decomposed into manageable, logical pieces.
-   Common code is unified, and not duplicated.
-   Code is properly formatted (Black) and linted (Pylint).
-   Tests are well written and cover all the source code.

def madlib():
    programming_language = input("Enter a programming language: ")
    noun1 = input("Enter a noun: ")
    verb1 = input("Enter a verb: ")
    adjective1 = input("Enter an adjective: ")
    noun_plural_1 = input("Enter a plural noun: ")
    verb_past_tense = input("Enter a verb in past tense: ")
    adjective2 = input("Enter another adjective: ")
    noun2 = input("Enter another noun: ")
    tool = input("Enter a tool used by programmers: ")
    adjective3 = input("Enter another adjective: ")

    madlib = f"In the world of programming, every {programming_language} programmer dreams of writing the perfect {noun1}. \
But in reality, they often end up having to {verb1} {adjective1} {noun_plural_1} just to meet deadlines. \
Once, they {verb_past_tense} a {adjective2} {noun2} using only a {tool} and it was surprisingly {adjective3}."

    print(madlib)

madlib()
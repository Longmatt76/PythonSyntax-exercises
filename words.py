words = ['hello', "whatup", "yoskies", "digitbra", "ponyface"]

for word in words:
    print(word.upper())


def print_upper_words(wordslist):
    """takes a list of words and prints an uppercase version of the list """
    for word in wordslist:
        print(word.upper())


def print_upper_e_words(wordslist):
    """takes a list of words and prints an uppercase version of any "e" word on the list """
    for word in wordslist:
        if word.startswith("e"):
            print(word.upper())


def print_upper_words_that_start_with(wordslist,starts):
    """take a list of words and returns an uppercase version of any word that starts with the letters
    dennoted in the set """
    for word in wordslist:
        for s in starts:
            if word.startswith(s):
                print(word.Upper())
                break
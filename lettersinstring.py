def count_letters(word):
    no_spaces = word.strip()
    length = len(no_spaces)
    return length

def get_word():
    word = input("Enter a word: ")
    length = count_letters(word)
    print(f"{word.strip()} is {length} letters long.")

get_word()
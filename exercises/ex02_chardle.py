"""Making a game like Wordle"""

__author__: str = "730663107"


"""Main function to call other functions"""


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


def input_word() -> str:
    user_word: str = input("Enter a 5-charcter word: ")
    if len(user_word) != 5:  # testing the length of the word
        print("Error: Word must contain 5 charcters.")
        print(user_word)
        exit()
    else:
        print(user_word)
    return user_word


def input_letter() -> str:
    user_letter: str = input("Enter a single character: ")
    if len(user_letter) != 1:  # testing the length of charcter
        print("Error: Character must be a single character.")
        print(user_letter)
        exit()  # function used to stop the program after error
    else:
        print(user_letter)
    return user_letter


"""This function goes through each index an tracks how many times a letter is repeated"""


def contains_char(word: str, letter: str) -> None:
    print("Searching for " + str(letter) + " in " + str(word))
    match_count: int = 0
    if word[0] == letter:  # Searching the index for matching letters
        print(str(letter) + " found at index 0")
        match_count += 1
    if word[1] == letter:
        print(str(letter) + " found at index 1")
        match_count += 1
    if word[2] == letter:
        print(str(letter) + " found at index 2")
        match_count += 1
    if word[3] == letter:
        print(str(letter) + " found at index 3")
        match_count += 1
    if word[4] == letter:
        print(str(letter) + " found at index 4")
        match_count += 1
    if match_count == 0:
        print("No instances of " + str(letter) + " found in " + str(word))
    else:
        print(
            str(match_count) + " instances of " + str(letter) + " found in " + str(word)
        )


if __name__ == "__main__":
    main()

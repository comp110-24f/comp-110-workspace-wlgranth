"""While Loops Challenge Question"""

__author__: str = "730663107"


def num_instances(phrase: str, search_char: str) -> int:
    count: int = 0
    index: int = (
        1  # since the len() of a string and indexing start at different values I had to find a way to balance them
    )
    while index <= len(phrase):
        if (
            phrase[index - 1] == search_char
        ):  # since the index of a string starts at 0 I had to change to index -1
            count += 1
            index += 1
        else:
            index += 1
    return count


"""This function takes any phrase and outputs how many times any given letter occurs in the phrase"""

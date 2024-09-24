"""Challenge Question"""

__author__ = "730663107"


"""Defining function mimic"""


def mimic(message: str) -> str:
    return message


"""Main Function Pulls Together Other Functions"""


def main() -> None:
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()

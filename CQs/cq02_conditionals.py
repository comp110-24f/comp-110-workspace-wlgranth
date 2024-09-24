"""Simple Number Guessing Game"""

__author__: str = "730663107"


def guess_a_number() -> None:  # defining function with no return or parameters
    secret: int = 7
    x: str = input("Guess a number:")  # assigns variable as a user input
    print("Your guess was " + str(x))
    if int(x) == 7:
        print("You got it!")
    elif int(x) > 7:
        print("Your guess was too high! The secret number is " + str(secret))
    else:
        print("Your guess was too low! The secret number is " + str(secret))


"""Conditional statement based of users guess"""

if __name__ == "__main__":
    guess_a_number()

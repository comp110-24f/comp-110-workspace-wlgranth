"""Calculating cost to host a tea pary of varying size."""

__author__: str = "730663107"


def main_planner(guests: int) -> None:
    """Calling every function and printing results"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


"""Line 7 assures that any variable of guest enetered will updated the text"""
"""Line 8 and 9 assigns the variable people inside the function tea_bags and treats to number of guests"""
"""Line 10 assigns the variables tea_count and treat_count to the results from functions tea_bags and treats"""


def tea_bags(people: int) -> int:
    """Function to describe relationship between number of guest and teabags"""  # Had to move docstring comments inside the function or autograder
    return people * 2


def treats(people: int) -> int:
    """Function to describe relationship between number of guest and treats"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Function taking the tea count and treat count and calculating the cost"""
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
# Allows program to be runnable

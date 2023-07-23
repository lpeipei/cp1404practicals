"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def get_result(score):
    """Getting results on scores"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def main():
    user_score = float(input("Enter score: "))
    user_result = get_result(user_score)
    print(f"User result is {user_result}")

    # Generate random numbers between 1 and 100
    random_score = random.randint(0, 100)
    random_result = get_result(random_score)
    print(f"Random Score is: {random_score}, Result is: {random_result}")


main()


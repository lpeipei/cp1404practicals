"""
CP1404/CP5632 Practical
quick picks
"""
import random

MIN_NUMBER = 1
MAX_NUMBER = 45
LINE_NUMBERS = 6


def main():
    number_of_picks = int(input("How many quick picks? "))
    while number_of_picks < 0:
        print("Please enter a number greater than 0.")
        number_of_picks = int(input("How many quick picks? "))

    for i in range(number_of_picks):
        quick_pick = []
        for j in range(LINE_NUMBERS):
            number = random.randint(MIN_NUMBER, MAX_NUMBER)
            while number in quick_pick:
                number = random.randint(MIN_NUMBER, MAX_NUMBER)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join(f"{number:2}" for number in quick_pick))


main()

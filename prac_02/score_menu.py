def get_valid_score():
    """Getting and checking score"""
    score = int(input("Enter your score: "))
    while 0 > score > 100:
        print("Please enter a score between 0 and 100.")
        score = int(input("Enter your score: "))
    return score


def get_result(score):
    """Getting score results"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def print_asterisks(score):
    """print as many stars as the score"""
    print("*" * score)


def display_menu():
    """display the menu list"""
    print("Menu")
    print("(G)et a valid score")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")


def main():
    print("Hello!")
    user_score = get_valid_score()
    user_result = get_result(user_score)
    print(f"user score is {user_score}， result is {user_result}")

    while True:
        display_menu()
        choice = input("Enter your choice: ").upper()
        if choice == "G":
            user_score = get_valid_score()
            user_result = get_result(user_score)
        elif choice == "P":
            print(f"user score is {user_score}, result is {user_result}")
        elif choice == "S":
            print_asterisks(user_score)
        elif choice == "Q":
            print("Thank you. Goodbye!")
            break
        else:
            print("Invalid choice.")


main()

"""
CP1404/CP5632 - Practical
Shop Calculator
"""

DISCOUNT = 0.9


def main():
    total_price = 0
    number_items = int(input("Number of items: "))
    while number_items <= 0:
        print("Invalid number of items!")

        number_items = int(input("Number of items: "))

    for i in range(number_items):
        price = float(input("Price of item: "))
        total_price = total_price + price

    if total_price > 100:
        total_price = total_price * DISCOUNT

    print(f"Total price for {number_items} items is ${total_price:.2f}")


main()

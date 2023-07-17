"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
UNDER_RATE = 0.1
OVER_RATE = 0.15

sales = float(input("Enter sales: $"))

while sales >= 0:
    if sales < 1000:
        bonus = sales * UNDER_RATE
    else:
        bonus = sales * OVER_RATE
    # If the decimal point is not preserved, as in the example
    # then when 0.1,0.2 is entered, the result will be 0, so two decimal places are preserved
    print(f"Bonus: ${bonus:.2f}")

    sales = float(input("Enter sales: $"))

print("Invalid sales")



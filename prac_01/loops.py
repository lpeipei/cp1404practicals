"""
CP1404/CP5632 - Practical
Loops
"""
# question a: count in 10s from 0 to 100
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# question b: count down from 20 to 1
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# question c: print n stars
number_stars = int(input("Number of stars: "))
for i in range(number_stars):
    print('*', end='')
print()

# question d: print n lines of increasing stars
for i in range(1, number_stars + 1):
    print('*' * i)

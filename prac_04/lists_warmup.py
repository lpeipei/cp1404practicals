numbers = [3, 1, 4, 1, 5, 9, 2]
"""
numbers[0]
 console: 3
numbers[-1]
  console: 2
numbers[3]
  console: 1
numbers[:-1]
  console: [3, 1, 4, 1, 5, 9]
numbers[3:4]
  console: 1
5 in numbers
  console: True
7 in numbers
  console: False
"3" in numbers
  console: False
numbers + [6, 5, 3]
  console: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
"""

# question 1
numbers[0] = "ten"

# question 2
numbers[-1] = 1

# question 3
print(numbers[2:])

# question 4
print(isinstance(numbers[5], int))

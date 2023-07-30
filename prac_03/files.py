# question 1.
name = input("Enter your name: ")
out_file = open("name.txt", "w")
out_file.write(name)
out_file.close()

# question 2.
in_file = open("name.txt", "r")
name = in_file.read().strip()
print(f"Your name is {name}")
in_file.close()

# question 3.
in_file = open("numbers.txt", "r")
numbers = in_file.readlines()
print(int(numbers[0]) + int(numbers[1]))
in_file.close()

# question 4.
in_file = open("numbers.txt", "r")
numbers = in_file.readlines()

total = 0
for number in numbers:
    total += int(number)
in_file.close()
print(total)






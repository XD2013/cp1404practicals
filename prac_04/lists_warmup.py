numbers = [3, 1, 4, 1, 5, 9, 2]

# numbers[0]
# This is 3

# numbers[-1]
# This is 2

# numbers[3]
# This is 1

# numbers[:-1]
# 3, 1, 4, 1, 5, 9

# numbers[3:4]
# This is 1

# 5 in numbers
# True

# 7 in numbers
# False

# "3" in numbers
# False

# numbers + [6, 5, 3]
# 3, 1, 4, 1, 5, 9, 2, 6, 5, 3

numbers[0] = "ten"
print(numbers[0])

numbers[-1] = 1
print(numbers[-1])

print(numbers[2:7])

print(9 in numbers)

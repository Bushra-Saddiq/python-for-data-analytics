# Task: Using a list comprehension, create a list of the squares of
# all numbers from 1 to 10 that are even.
# Topics: list comprehensions

squares = [x * x for x in range(1, 11) if x % 2 == 0]
print(squares)

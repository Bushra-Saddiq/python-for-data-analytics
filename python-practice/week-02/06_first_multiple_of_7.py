# Task: Find and print the first number greater than 50 that is
# divisible by 7, searching starting from 51 upward.
# Topics: for loop, break, modulus operator

for num in range(51, 1000):
    if num % 7 == 0:
        break
print(num)

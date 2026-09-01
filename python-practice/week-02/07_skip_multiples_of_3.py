# Task: Loop through numbers 1 to 20. Print each number, but skip
# printing any number that's a multiple of 3.
# Topics: for loop, continue, modulus operator

for num in range(1, 21):
    if num % 3 == 0:
        continue
    print(num)

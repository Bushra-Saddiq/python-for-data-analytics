# Task: Take a sentence from the user and print:
# (1) the sentence stripped of extra spaces
# (2) the sentence in uppercase
# (3) the first word only
# Topics: string methods (.strip(), .upper(), .split()), list indexing

sentance = input()

print(sentance.strip())
print(sentance.upper())
print(sentance.split()[0])

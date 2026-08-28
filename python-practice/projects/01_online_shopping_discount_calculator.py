# Task: Online Shopping Discount Calculator
# Uses if/elif/else and a NESTED if to calculate the final amount
# of an online shopping purchase, based on shopping amount tiers
# and an additional discount for Premium Members.
# Topics: if / elif / else, nested if, arithmetic operators, f-strings

Total_Amount = int(input("What's the total amount?: "))
Membership = input("Are you premium member y/n?: ")

if Total_Amount >= 10000:
    Regular_Discount = 0.20
    if Membership == "y":
        Premium_Discount = 0.05
    else:
        Premium_Discount = 0

elif Total_Amount >= 5000:
    Regular_Discount = 0.10
    if Membership == "y":
        Premium_Discount = 0.05
    else:
        Premium_Discount = 0

elif Total_Amount >= 2000:
    Regular_Discount = 0.05
    if Membership == "y":
        Premium_Discount = 0.05
    else:
        Premium_Discount = 0

else:
    Regular_Discount = 0
    if Membership == "y":
        Premium_Discount = 0.05
    else:
        Premium_Discount = 0

# Calculations happen after the whole if/elif/else block finishes,
# once the discount percentages have been decided
Regular_Discount_Amount = Total_Amount * Regular_Discount
Premium_Discount_Amount = Total_Amount * Premium_Discount
Total_Discount = Regular_Discount_Amount + Premium_Discount_Amount
Final_Amount_To_Pay = Total_Amount - Total_Discount

print("Original Shopping Amount: ", Total_Amount)
print("Regular Discount: ", Regular_Discount_Amount)
print("Premium Discount: ", Premium_Discount_Amount)
print("Total Discount is: ", Total_Discount)
print("Amount to pay now is: ", Final_Amount_To_Pay)

# Using if, elif and else statement
# WAP to find whether a number is zero, positive or negative

# Getting user input
user_input = int(input("Enter a number: "))

# Classifying the number and print the appropriate statement
if user_input < 0:
    print("The number is negative.")
elif user_input == 0:
    print("The number is zero.")
else:
    print("The number is positive.")


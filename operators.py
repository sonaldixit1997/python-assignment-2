num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Step 2: Perform operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# To avoid division by zero error
if num2 != 0:
    division = num1 / num2
else:
    division = "Undefined (cannot divide by zero)"

# Step 3: Display results
print("\n\n")
print(f"Addition:{addition}") # remember this if we want input value to be printed
print(f"Subtraction:{subtraction}")
print(f"Multiplication:{multiplication}")
print(f"Division:{division}")

# ----------------------------
# Project 1: BMI Category Checker
# ----------------------------

# Get user input
height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))

# Calculate BMI
bmi = weight / (height ** 2)

# Display BMI value
print(f"\nYour BMI is: {bmi:.2f}")

# Determine and print category
if bmi >= 30:
    print("Category: Obesity")
elif 25 <= bmi < 30:
    print("Category: Overweight")
elif 18.5 <= bmi < 25:
    print("Category: Normal")
else:
    print("Category: Underweight")

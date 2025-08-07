
# Project 1: Store value of pi and check its data type

pi = 22 / 7
print("1. Value of pi:", pi)
print("   Data type of pi:", type(pi))  # Output: <class 'float'>



# Project 2: Try to use 'for' as a variable name (will cause error)

print("\n2. Trying to use 'for' as a variable name...")
try:
    exec("for = 4") 
except SyntaxError:
    print("   ❌ Error: 'for' is a reserved keyword in Python and cannot be used as a variable name.")
except Exception as e:
    print("   ❌ Exception occurred:", e)



# Project 3: Calculate Simple Interest

# Inputs
principal = 10000  # Principal amount in Rupees
rate = 5           # Interest rate in percent
time = 3           # Time in years

# Formula for Simple Interest
simple_interest = (principal * rate * time) / 100

# Output
print("\n3. Simple Interest Calculation:")
print("   Principal:", principal)
print("   Rate of Interest:", rate)
print("   Time:", time)
print("   Simple Interest:", simple_interest)

# ----------------------------
# Project 2: City to Country Checker
# ----------------------------

# Define cities by country
australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
uae = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
india = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

# Get user input (case-insensitive)
city = input("\nEnter a city name: ").strip()

# Normalize capitalization for matching
city_title = city.title()

# Check and print result
if city_title in australia:
    print(f"{city_title} is in Australia.")
elif city_title in uae:
    print(f"{city_title} is in UAE.")
elif city_title in india:
    print(f"{city_title} is in India.")
else:
    print(f"{city_title} is not in our list.")

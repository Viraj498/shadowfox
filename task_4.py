# ----------------------------
# Project: Check if two cities belong to the same country
# ----------------------------

# Define cities grouped by country
countries = {
    "Australia": ["Sydney", "Melbourne", "Brisbane", "Perth"],
    "UAE": ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"],
    "India": ["Mumbai", "Bangalore", "Chennai", "Delhi"]
}

# Function to find country of a city
def find_country(city_name):
    city_title = city_name.title()
    for country, cities in countries.items():
        if city_title in cities:
            return country
    return None

# User input for two cities
city1 = input("Enter the first city: ").strip()
city2 = input("Enter the second city: ").strip()
# Find countries of both cities
country1 = find_country(city1)
country2 = find_country(city2)

# Determine and display the result
if country1 and country2:
    if country1 == country2:
        print(f"Both cities are in {country1}.")
    else:
        print("They don't belong to the same country.")
else:
    if not country1:
        print(f"{city1.title()} is not in our list.")
    if not country2:
        print(f"{city2.title()} is not in our list.")

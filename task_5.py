# ----------------------------
# Task 1: Use format() function
# ----------------------------

def format_number(value, format_type):
    formatted = format(value, format_type)
    print(f"1. Formatted result of {value} with format '{format_type}': {formatted}")
    return formatted

# Call the function with 145 and 'o' (octal)
format_number(145, 'o')  # 'o' = octal representation

# ----------------------------
# Task 2: Pond area and water volume
# ----------------------------

def pond_water_volume(radius, pi=3.14, water_per_sqm=1.4):
    # Calculate area of the pond
    area = pi * radius ** 2
    print(f"\n2. Area of the circular pond (πr²): {area:.2f} square meters")

    # Calculate total water volume
    total_water = int(area * water_per_sqm)  # cast to int to remove decimal
    print(f"   Total water in the pond: {total_water} liters (rounded)")

    return area, total_water

# Given radius of the pond = 84 meters
pond_water_volume(84)

# ----------------------------
# Task 3: Calculate speed
# ----------------------------

def calculate_speed(distance_meters, time_minutes):
    time_seconds = time_minutes * 60  # Convert minutes to seconds
    speed = int(distance_meters / time_seconds)  # Cast to int to remove decimal
    print(f"\n3. Speed while crossing a {distance_meters} meter street in {time_minutes} minutes:")
    print(f"   Speed: {speed} meters/second")

    return speed

# Given: 490 meters, 7 minutes
calculate_speed(490, 7)

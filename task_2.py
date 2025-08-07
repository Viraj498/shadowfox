# Initial List of Justice League members
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
print("Initial Justice League:", justice_league)

# 1. Calculate the number of members
print("\n1. Number of members in Justice League:", len(justice_league))

# 2. Add Batgirl and Nightwing
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("\n2. After adding Batgirl and Nightwing:", justice_league)

# 3. Move Wonder Woman to the beginning
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("\n3. After moving Wonder Woman to the front (new leader):", justice_league)

# 4. Separate Aquaman and Flash by inserting Superman or Green Lantern in between
# Let's insert "Superman" between them
aquaman_index = justice_league.index("Aquaman")
flash_index = justice_league.index("Flash")

# Remove Superman from old position
justice_league.remove("Superman")

# Insert Superman between Aquaman and Flash
# Ensure Flash is after Aquaman
if aquaman_index < flash_index:
    justice_league.insert(flash_index, "Superman")
else:
    justice_league.insert(aquaman_index + 1, "Superman")

print("\n4. After inserting Superman between Aquaman and Flash:", justice_league)

# 5. Crisis! Replace entire list with new members
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("\n5. New Justice League after crisis:", justice_league)

# 6. Sort alphabetically, new leader is at index 0
justice_league.sort()
print("\n6. Justice League sorted alphabetically:", justice_league)
print("New Leader:", justice_league[0])

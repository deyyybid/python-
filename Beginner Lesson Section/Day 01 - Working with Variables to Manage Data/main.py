# Improved using f-strings & .title() for cleaner formatting.
print("Welcome to the Band Name Generator")

cityName = input("What's the name of the city you grew up in?\n")
petName = input("What's your pet's name?\n")

print(f"\nYour band name could be \"{cityName.title()} {petName.title()}\"")
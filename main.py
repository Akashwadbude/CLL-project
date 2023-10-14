# Get the user's name
name = input("What is your name? ")

# Greet the user
print(f"Hello Mr. , {name}!")

# Get the user's age
age = int(input("How old are you? "))

# Check if the user is of legal drinking age
if age >= 21:
    print("You are of legal drinking age. Enjoy responsibly!")
else:
    print("You are not of legal drinking age. Please refrain from drinking alcohol.")

# Ask user for their name
name = input("What's your name? ")

# remove whitespace from str and capitalize user's name
name= name.strip().title()

# Say hello to user
print(f"hello, {name}")

# Write a Python program that asks the user to enter a username. Display the username's length, first three characters, last three characters,
# and whether the username is empty after removing whitespace. 

username = input("Enter your username: ")

print(f"Username length: {len(username)}")
print(f"First three characters: {username[:3]}")
print(f"Last three characters: {username[-3:]}")
print(f"Username is empty: {username.strip() == ''}")

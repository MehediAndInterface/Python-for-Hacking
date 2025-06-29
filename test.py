"""
Simple Login: Create variables for a username and password. Ask the user for theirs and check if they match.
"""
username = "admin"
password = "password123"

user_input_username = input("Please enter your username: ")
user_input_password = input("Please enter your password: ")

if user_input_username == username and user_input_password == password:
    print(f"\nLogin successful! Welcome, {username}")
else:
    print("\nError: Incorrect username or password.")
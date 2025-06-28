"""
Simple Login: Create variables for a username and password. Ask the user for theirs and check if they match.
# 1. Define the correct username and password.
# 2. Ask the user for their username.
# 3. Ask the user for their password.
# 4. Check if the entered username and password match the correct ones.
# 5. If they match, print a success message.
# 6. If they don't match, print an error message.
"""
username = "admin"
password = "password123"

user_input_username = input("Please enter your username: ")
user_input_password = input("Please enter your password: ")

if user_input_username == username and user_input_password == password:
    print(f"\nLogin successful! Welcome, {username}")
else:
    print("\nError: Incorrect username or password")
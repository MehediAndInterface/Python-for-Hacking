"""
Type Conversion: Ask the user for their age (as a string), convert it to an integer, and calculate the year they were born.
"""
from datetime import date

current_year = date.today().year

age_str = input("Enter your age: ")
age_int = int(age_str)

born_year = current_year - age_int

print(f"You were born in approximately {born_year}.")

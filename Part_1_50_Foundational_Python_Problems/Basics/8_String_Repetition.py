"""
String Repetition: Ask the user for a word and a number, then print the word repeated that many times.
"""
word = input("Enter a word: ")
num = int(input("Enter a number: "))

try:
    print(word * num)
except ValueError:
    print("Error: You did not enter a valid whole number.")


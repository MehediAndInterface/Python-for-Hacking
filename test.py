"""
String Repetition: Ask the user for a word and a number, then print the word repeated that many times.
"""
word = input("Enter a word: ")
num = input("Enter a number: ")

try:
    repeat_num = int(num)
    print(word * repeat_num)
except ValueError:
    print("Error: you did not enter a valid whole number.")
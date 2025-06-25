"""
Simple Mad Libs: Ask the user for a noun, a verb, and an adjective, and print a short story using them.
"""
noun = input("Enter a noun: ")
verb = input("Enter a verb (past tense): ")
adjective = input("Enter an adjective: ")

story = (f"The {adjective} {noun} decided to {verb} across the field."
         f"Everyone thought the {noun} was very brave, but also a little bit silly.")

print("\n--- Here is your story! ---")
print(story)
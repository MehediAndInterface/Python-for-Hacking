"""
Age Group Classifier: Ask for an age and classify the person as a "Child," "Teenager," "Adult," or "Senior."
"""
while True:
    age = input("Please enter age: ")

    if age.lower() == 'exit':
        break

    try:
        age_int = int(age)

        if age_int < 0:
            print("Age cannot be negative. Please enter a valid age.")
        elif age_int <= 12:
            print("You are a Child")
        elif age_int <= 18:
            print("You are a Teenager.")
        elif age_int <= 40:
            print("you are an Adult")
        else:
            print("You are a Senior")
    except ValueError:
        print("Invalid input. Please enter a whole number for age.")

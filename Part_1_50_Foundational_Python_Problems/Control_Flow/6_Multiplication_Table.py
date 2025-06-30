"""
Multiplication Table: Ask for a number and print its multiplication table up to 10.
Product = Multiplicand × Multiplier
"""
multiplicand = int(input("Enter a number to see its multiplication table: "))

print(f"--- Multiplication Table for {multiplicand} ---")

for multiplier in range (1, 11):
    product = multiplicand * multiplier

    print(f"{multiplicand} x {multiplier} = {product}")














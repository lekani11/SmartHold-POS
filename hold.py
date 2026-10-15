
print("=============================================")
print("              SMART HOLD POS")
print("=============================================")
print()

cashier_name = input("Please enter your name: ").strip()

while not cashier_name:
    print("Name cannot be empty. Please try again.")
    cashier_name = input("Please enter your name: ").strip()

print()
print(f"Welcome, {cashier_name}!")
print("Your till is ready.")
print()
# f-string removes the need for concatenation and makes the code cleaner and more readable.
# f is used for string interpolation, allowing the variable cashier_name to be inserted into the string.
print(f"Logged-in cashier: {cashier_name}")
print("Role: Cashier")
print("Till: 01")

print()
print("1. Add product")
print("2. View basket")
print("3. Hold transaction")
print("4. Resume transaction")
print("5. Exit")
print()
print("SmartHold POS is starting...")

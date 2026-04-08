"""age = int(input("Enter your age : "))

if age < 0 or age > 150:
    print("Invalid age")
elif age < 13:
    print("Child - no access")
elif age < 17:
    print("Teenager - limited access")
elif age < 64:
    print("Adult - full access")
else:
    print("Senior - full access with discounts")"""

"""bal = 10000
pin = "1234"
user_pin = input("Enter your PIN: ")
if pin == user_pin:
    print("PIN accepted")
    amount = float(input("Enter amount to withdraw: "))
    if amount > bal:
        print("Insufficient funds")
    else:
        bal -= amount
        print(f"Withdrawal successful. Remaining balance: {bal}")""" 

age = int(input("Age: "))
has_ticket = input("Have ticket? (yes/no): ")
has_id = input("Have ID? (yes/no): ")
 
if age < 18:
    print("Must be 18 or older")
elif has_ticket == "yes":
    print("You need a ticket")
elif has_id == "yes":
    print("ID required for entry")
else:
    print("Welcome to the event!")

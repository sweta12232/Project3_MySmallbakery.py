print("Welcome to Sweta's Bakery")

def place_order(item, price):
    print(f"Your order is placed for {item.capitalize()}")
    return price

choice = input("Here is our Menu:\n 1. Black Forest = Nrs. 65 \n 2. White Forest = Nrs. 70 \n 3. Pineapple = Nrs. 45.\nPlease enter your choice: ").lower()
total = 0

if choice == "pineapple":
    total += place_order("pineapple", 45)
elif choice == "white forest":
    total += place_order("white forest", 70)
elif choice == "black forest":
    total += place_order("black forest", 65)
else:
    print("Sorry! It is not available")

choice2 = input("Do you want to add anything else? (yes/no): ").lower()
if choice2 == "yes":
    choice = input("Please enter your choice: ").lower()
    if choice == "pineapple":
        total += place_order("pineapple", 45)
    elif choice == "white forest":
        total += place_order("white forest", 70)
    elif choice == "black forest":
        total += place_order("black forest", 65)
    else:
        print("Sorry! It is not available")

print(f"Thank your for ordering😊🧁. Your total bill is: Nrs. {total}")


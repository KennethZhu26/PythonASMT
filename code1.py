#Shopping Cart Program - V1

available_items = {
    "1kg apple": 3.99,
    "1kg banana": 2.99,
    "bread": 3.99,
    "1l milk": 8.99,
    "1kg orange": 6.99
}

grocery_list = []

print('-------------------------------------')
print("Welcome user, please enter your name")
name = input("Enter your name : ")
print('-------------------------------------')

while True:
    print("\n--- Grocery Shopping Menu ---")
    print("1. Add item")
    print("2. View items")
    print("3. Remove item")
    print("4. Exit")
    print("-----------------------------")
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        print("\nAvailable items:")
        for item, price in available_items.items():
            print(f"- {item} (${price:.2f})")
        item = input("Enter item to add: ")
        grocery_list.append(item)
        print(f"'{item}' has been added to your list.")

    elif choice == "2":
        print("\nYour grocery list:")
        total = 0
        for i, item in enumerate(grocery_list, 1):
            price = available_items[item]
            total += price
            print(f"{i}. {item} - ${price:.2f}")
        print(f"Total: ${total:.2f}")

    elif choice == "3":
        item = input("Enter item to remove: ")
        grocery_list.remove(item)
        print(f"'{item}' has been removed.")

    elif choice == "4":
        print("Goodbye!")
        break

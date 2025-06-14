#Shopping Cart Program - V1

#Dictionary of valiable items
available_items = {
    "1kg apple": 3.99,
    "1kg banana": 2.99,
    "bread": 3.99,
    "1l milk": 8.99,
    "1kg orange": 6.99
}

#Empty list waiting for items to be entered
grocery_list = []

#Print statement to welcome user
print('-------------------------------------')
print("Welcome user, please enter your name")
name = input("Enter your name : ")
print('-------------------------------------')

#While loop asking user for their input
while True:
    print("\n--- Grocery Shopping Menu ---")
    print("1. Add item")
    print("2. View items")
    print("3. Remove item")
    print("4. Exit")
    print("-----------------------------")
    choice = input("Choose an option (1-4): ")

    #If user decides to add item
    if choice == "1":
        #Prints avaliable items from grocery list
        print("\nAvailable items:")
        #Prints item and price to 2 decimal points
        for item, price in available_items.items():
            print(f"- {item} (${price:.2f})")
        item = input("Enter item to add: ")
        #Adds item to list
        grocery_list.append(item)
        print(f"'{item}' has been added to your list.")

    #If user decides to view grocery list
    elif choice == "2":
        #Prints user's current grocery list
        print("\nYour grocery list:")
        #Sets total to 0
        total = 0
        #Give index of the item starting from 1
        for i, item in enumerate(grocery_list, 1):
            #Calculate price of cart
            price = available_items[item]
            total += price
            print(f"{i}. {item} - ${price:.2f}")
        print(f"Total: ${total:.2f}")

    #If user decides to remove item
    elif choice == "3":
        item = input("Enter item to remove: ")
        #Removes item
        grocery_list.remove(item)
        print(f"'{item}' has been removed.")

    #If user decides to exit program
    elif choice == "4":
        print("Goodbye!")
        break

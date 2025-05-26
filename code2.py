#Grocery Shopping Program

#Function to print initial menu
def print_menu():
    print("\n--- Grocery Shopping Menu ---")
    print("1. Add item")
    print("2. View items")
    print("3. Remove item")
    print("4. Exit")
    print("-----------------------------")

#Function to add item to grocery list
def add_item(grocery_list):
    item = input("Enter item to add: ")
    if item:
        grocery_list.append(item)
        print(f"'{item}' has been added to your list.")
    else:
        print("No item entered.")

#Function to view grocery items
def view_items(grocery_list):
    if grocery_list:
        print("\nYour grocery list:")
        for i, item in enumerate(grocery_list, 1):
            print(f"{i}. {item}")
    else:
        print("Your grocery list is empty.")

#Function to remove grocery item
def remove_item(grocery_list):
    item = input("Enter item to remove: ")
    if item in grocery_list:
        grocery_list.remove(item)
        print(f"'{item}' has been removed.")
    else:
        print(f"'{item}' is not in your list.")

#Function to select appropriate function
def main():
    grocery_list = []
    while True:
        print_menu()
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_item(grocery_list)
        elif choice == "2":
            view_items(grocery_list)
        elif choice == "3":
            remove_item(grocery_list)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

#Ensures the main function is called only when the program is directly ran.
if __name__ == "__main__":
    main()

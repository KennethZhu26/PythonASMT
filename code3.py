#Shopping Cart Program - V3

#Imports easygui for GUI
from easygui import*

#Dictionary of available items and prices
available_items = {
    "Apple": 0.50,
    "Banana": 2.99,
    "Bread": 3.99,
    "Milk": 8.99,
    "Orange": 0.99
}

#Function to print home menu, sends result of buttonbox back to function
def print_menu():
    #Buttonbox used to display inital mennu
    return buttonbox(
        msg="Grocery Shopping Menu",
        choices=["Add item", "View items", "Remove item", "Exit"]
    )

#Function to add an item
def add_item(grocery_list):
    #Buttonbox for user to choose an item from the available grocery items
    item = buttonbox("Select an item to add:", "Add Item", choices=list(available_items.keys()))
    #If user decides to cancel program
    if not item:
        msgbox("Action has been cancelled.")
        #Ends function early
        return

    #Enterbox to ask user quantity they would like to purchase
    quantity_input = enterbox(f"How many '{item}' would you like to buy?", "Enter Quantity")
    #If user decides to cancel program
    if quantity_input is None:
        msgbox("Action has been cancelled.")
        #Ends function early
        return

    #Validates user's input by checking if it is a positive whole number above 0
    if quantity_input.isdigit() and int(quantity_input) > 0:
        #Converts string into integer
        quantity = int(quantity_input)
        if item in grocery_list:
            #If item is in list, increases its quantity
            grocery_list[item] += quantity
        else:
            #If item is not in list, adds it with the quantity
            grocery_list[item] = quantity
        #Message box to inform user that item has been added to cart
        msgbox(f"{quantity} x '{item}' has been added to your list.")
    else:
        #Message to inform user their input is invalid
        msgbox("Please enter a whole number greater than 0.")

#Function to view grocery items
def view_items(grocery_list):
    if grocery_list:
        #Sets inital total value of shopping cart to 0
        total = 0
        #Item numbering starts from 1
        count = 1
        message = "Your grocery list:\n\n"
        #Calculates cart cost by multiplying item amount with cost
        for item in grocery_list:
            #Gets quantity of item from list
            quantity = grocery_list[item]
            #Gets price of item from avaliable items
            price = available_items[item]
            item_total = quantity * price
            message += f"{count}. {item} x {quantity} = ${item_total:.2f}\n"
            #Adds item total to total cost
            total += item_total
            count += 1
        #Informs user's total cart value
        message += f"\nTotal: ${total:.2f}"
        msgbox(message)
    else:
        #Message to inform user cart is empty
        msgbox("Your grocery cart is empty.")

#Function to remove item
def remove_item(grocery_list):
    #Informs user that cart is empty and items cannot be removed
    if not grocery_list:
        msgbox("Your grocery cart is empty, no items can be removed.")
        #Ends function early
        return

    #Takes keys from grocery list and converts to list which are able to be accessed by buttonbox
    items = list(grocery_list.keys())

    #Allows user to choose item to remove
    item = buttonbox("Select an item to remove:", "Remove Item", choices=items)
    #If user cancels removal
    if not item:
        msgbox("Action has been cancelled.")
        #Ends function early
        return

    #Ask how many to remove where quantity to be removed must be =< quantity in cart
    max_quantity = grocery_list[item]
    quantity_input = enterbox(f"How many '{item}' would you like to remove? (Max: {max_quantity})", "Remove Quantity")
    #If user cancels quantity input
    if quantity_input is None:
        msgbox("Action has been cancelled.")
        #Ends function early
        return

    #Validates quantity input by checking if it is positive whole number not exceeding total quantity in cart
    if quantity_input.isdigit() and 0 < int(quantity_input) <= max_quantity:
        #Converts string to integer
        quantity_to_remove = int(quantity_input)
        #Confirmation box before final removal
        confirm = ynbox(f"Are you sure you want to remove {quantity_to_remove} x '{item}' from your cart?", "Confirm Removal")
        if confirm:
            #Removes selected quantity from quantity in cart originally
            grocery_list[item] -= quantity_to_remove
            #Remove item completely if quantity reaches 0
            if grocery_list[item] == 0:
                #Removes item
                del grocery_list[item]
            #Message informing user items and quantity has been removed
            msgbox(f"Removed {quantity_to_remove} x '{item}' from your cart.")
        else:
            #Message informing user that removal process has been cancelled
            msgbox("Removal cancelled.")
    else:
        #Message to inform user their input is invalid
        msgbox(f"Please enter a whole number between 1 and {max_quantity}.")

#Function to checkout
def checkout(grocery_list):
    if grocery_list:
        #Sets inital total value of shopping cart to 0
        total = 0
        #Item numbering starts from 1
        count = 1
        message = "Your final grocery list:\n\n"
        #Calculates cart cost by multiplying item amount with cost
        for item in grocery_list:
            #Gets quantity of item from list
            quantity = grocery_list[item]
            #Gets price of item from avaliable items
            price = available_items[item]
            item_total = quantity * price
            message += f"{count}. {item} x {quantity} = ${item_total:.2f}\n"
            #Adds item total to total cost
            total += item_total
            count += 1
        #Informs user's total cart value
        message += f"\nTotal: ${total:.2f}"
        msgbox(message, title="Checkout")
    else:
        #Message to inform user cart is empty
        msgbox("Your grocery cart is empty. Nothing to checkout.", title="Checkout")

#Main function
def main():
    grocery_list = {}
    #Asks for user's name
    while True:
        name = enterbox("Welcome user, please enter your name:")
        if name is None:
            msgbox("Goodbye!")
            #Ends function early
            return
        #If input is not in alphabetical characters
        if name.isalpha():
            break
        else:
            #Informs user that they need to re-enter
            msgbox("Please use only letters for your name.")
    #Greets user to program
    msgbox(f"Hi {name}, let's begin shopping!")

    #While loop to ask user's action
    while True:
        choice = print_menu()
        #If user decides to exit program
        if choice is None or choice == "Exit":
            #Checkout auto displays on exit
            checkout(grocery_list)
            msgbox("Goodbye!")
            break
        #If user decides to add item
        elif choice == "Add item":
            add_item(grocery_list)
        #If user decides to view item
        elif choice == "View items":
            view_items(grocery_list)
        #If user decides to remove item
        elif choice == "Remove item":
            remove_item(grocery_list)
        else:
            #If user enters input which is not avaliable
            msgbox("Invalid choice.")

#Runs the program and ensures program is directly ran from file
if __name__ == "__main__":
    main()

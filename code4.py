#Shopping Cart Program - V4

#Imports easygui for GUI
from easygui import*
#Imports json for json file use
import json
#Imports os so that program can interact with operating system
import os
#Imports matplotlib for data visualization
import matplotlib.pyplot as plt

#Dictionary of available items and prices
available_items = {
    "Apple": 0.50,
    "Banana": 2.99,
    "Bread": 3.99,
    "Milk": 8.99,
    "Orange": 0.99
}

#Json file to store user's data
USER_FILE = "users.json"

#Function to load user details from json file
def load_users():
    #Check if the user data file exists
    if os.path.exists(USER_FILE):
        #If it exists, open the file in read mode
        with open(USER_FILE, "r") as f:
            #Load and return the json data as a dictionary
            return json.load(f)
    #If the file doesn't exist, return to an empty dictionary
    return {}

#Function to save user data to a json file
def save_users(users):
    #Open the user data file in write mode
    with open(USER_FILE, "w") as f:
        #Write the user data dictionary to the file in json format with indentation
        json.dump(users, f, indent=4)

#Function to print home menu, sends result of buttonbox back to function
def print_menu():
    #Buttonbox used to display initial menu
    return buttonbox(
        msg="Grocery Shopping Menu",
        choices=["Add item", "View items", "Remove item", "Exit"]
    )

#Function to add an item
def add_item(grocery_list):
    #Choicebox for user to choose an item from the available grocery items
    item = choicebox("Select an item to add:", "Add Item", choices=list(available_items.keys()))
    #If user cancels program
    if not item:
        msgbox("Action has been cancelled.")
        #Ends function early
        return

    #Sets maximum quantity per user per item
    max_per_user = 50
    #Gets current quantity of item in the user's cart
    current_quantity = grocery_list.get(item, 0)
    #If user enters a quantity beyond the limit of user's limit
    if current_quantity >= max_per_user:
        msgbox(f"You already have the maximum allowed of 50 x '{item}' in your cart.")
        #Ends function early
        return

    #Enterbox to ask user quantity they would like to purchase
    quantity_input = enterbox(f"How many '{item}' would you like to buy? (Max: {max_per_user - current_quantity})", "Enter Quantity")
    #If user decides to cancel program
    if quantity_input is None:
        msgbox("Action has been cancelled.")
        #Ends function early
        return

    #Validates user's input by checking if it is a positive whole number above 0 and does not exceed max_per_user
    if quantity_input.isdigit():
        #Converts string to integer
        quantity = int(quantity_input)
        #Checks input does not exceed maximum amount allowed
        if 0 < quantity <= (max_per_user - current_quantity):
            if item in grocery_list:
                #If item is in list, increases its quantity
                grocery_list[item] += quantity
            else:
                #If item is not in list, adds it with the quantity
                grocery_list[item] = quantity
            #Message box to inform user that item has been added to cart
            msgbox(f"{quantity} x '{item}' has been added to your list.")
        else:
            #Message to inform user that quantity exceeds the allowed amount
            msgbox(f"Please enter a whole number between 1 and {max_per_user - current_quantity}.")
    else:
        #Message to inform user their input is invalid
        msgbox("Please enter a whole number greater than 0.")

#Function to view grocery items
def view_items(grocery_list):
    if grocery_list:
        #Sets initial total value of shopping cart to 0
        total = 0
        #Item numbering starts from 1
        count = 1
        message = "Your grocery list:\n\n"
        #Empty list to store names of items
        items = []
        #Empty list to store quantites of items
        quantities = []
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
            #Adds selected item name to items list
            items.append(item)
            #Adds quantity to quantities list
            quantities.append(quantity)
            count += 1
        #Informs user's total total cart value
        message += f"\nTotal: ${total:.2f}"
        msgbox(message)

        #Implements data visualization (Graphs)
        plt.bar(items, quantities)
        #Sets x-axis to items
        plt.xlabel("Items")
        #Sets y-axis to quantity
        plt.ylabel("Quantity")
        #Sets title of graph to Items in Cart
        plt.title("Items in Cart")
        #Displays data visualization
        plt.show()
    else:
        #Message to inform user cart if cart is empty and does not display data visualization
        msgbox("Your grocery cart is empty.")

#Function to remove item
def remove_item(grocery_list):
    #Informs user that cart is empty and items cannot be removed
    if not grocery_list:
        msgbox("Your grocery cart is empty, no items can be removed.")
        #Ends function early
        return

    #Choicebox to select item to remove
    item = choicebox("Select an item to remove:", "Remove Item", choices=list(grocery_list.keys()))
    #If user cancels program
    if not item:
        msgbox("Action has been cancelled.")
        #Ends function early
        return

    #Asks user quantity where quantity to be removed must be =< quantity of items in cart
    max_quantity = grocery_list[item]
    quantity_input = enterbox(f"How many '{item}' would you like to remove? (Max: {max_quantity})", "Remove Quantity")
    #If user cancels program
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
            #Remove items completely if quantity reaches 0
            if grocery_list[item] == 0:
                #Removes item
                del grocery_list[item]
            #Informs user that items and quantity have been removed 
            msgbox(f"Removed {quantity_to_remove} x '{item}' from your cart.")
        else:
            #Informs user that removal process has been cancelled
            msgbox("Removal cancelled.")
    else:
        #Informs user that input is invalid and it must be within this range
        msgbox(f"Please enter a whole number between 1 and {max_quantity}.")

#Function to checkout
def checkout(grocery_list):
    if grocery_list:
        #Sets initial totale value of shopping cart to 0
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
        #Message to inform user cart is empty
        msgbox(message, title="Checkout")
    else:
        #Informs user cart is empty and that there are no items to be checked out
        msgbox("Your grocery cart is empty. Nothing to checkout.", title="Checkout")

#Function to show cart summary and visualization on exit
def show_summary_and_visualization(grocery_list):
    #Displays cart summary
    checkout(grocery_list)
    
    if grocery_list:
        #Extracts all item names from grocery dictionary into a list
        items = list(grocery_list.keys())
        #Creates a list of quantities that match the items in the same order
        quantities = [grocery_list[item] for item in items]

        #Display data visualization after checkout
        plt.bar(items, quantities)
        #Sets x-axis as items
        plt.xlabel("Items")
        #Sets y-axis to quantity
        plt.ylabel("Quantity")
        #Sets title of grpah to Items in Cart
        plt.title("Items in Cart")
        #Displays data visualization
        plt.show()

#Main login/signup function
def authenticate():
    #Checks users information in Json File
    users = load_users()
    while True:
        #Asks user if they would like to sign up or login
        action = buttonbox("Do you want to sign up or login?", choices=["Sign Up", "Login", "Exit"])
        #If user chooses to exit
        if action == "Exit" or action is None:
            #Ends function early
            return None

        #Asks user for username input
        username = enterbox("Enter your username:")
        if username is None:
            #Ends function early
            return None

        #Asks user for password input
        password = enterbox("Enter your password:")
        if password is None:
            #Ends function early
            return None

        #If user chooses to login
        if action == "Login":
            #Checks if username and password matches to details in Json file
            if username in users and users[username]["password"] == password:
                #If user successfully logs in, display welcome message
                msgbox(f"Welcome back, {username}!")
                #Ends function early and sends value of username to calling function
                return username
            else:
                #If username or password is invalid
                msgbox("Invalid username or password.")

        #If user chooses to sign up
        elif action == "Sign Up":
            #If user inputs username which already exists, prompts user to try logging in instead
            if username in users:
                msgbox("Username already exists. Try logging in.")
            else:
                #Asks user to confirm password if user enters new username
                confirm_password = enterbox("Confirm your password:")
                #If user exits program
                if confirm_password is None:
                    msgbox("Sign up cancelled.")
                #If user enters password in confirmation phase which does not match with initial passoword, asks them to re-try
                elif confirm_password != password:
                    msgbox("Passwords do not match. Try again.")
                else:
                    #Creates a new user entry with their password with an empty shopping cart
                    users[username] = {"password": password, "cart": {}}
                    #Adds new user details to json file
                    save_users(users)
                    #Displays message to inform user that account has been created
                    msgbox("Account created successfully!")
                    #Ends function early and sends value of username to calling function
                    return username

#Main function
def main():
    grocery_list = {}

    #Authenticates the user and calls function
    user = authenticate()
    if not user:
        msgbox("Goodbye!")
        #Ends function early
        return

    #Load user's existing cart if it exists
    users = load_users()
    #Checks if user has existing cart and loads the cart data into grocery list
    if user in users and "cart" in users[user]:
        grocery_list = users[user]["cart"]

    #While loop to ask for user's action
    while True:
        choice = print_menu()
        #If user chooses to exit
        if choice is None or choice == "Exit":
            #Shows checkout summary and data visualization before exit
            show_summary_and_visualization(grocery_list)
            #Saves cart to user's data before exiting
            users[user]["cart"] = grocery_list
            save_users(users)
            #Message displaying Goodbye
            msgbox("Goodbye!")
            break
        #If user decides to add item
        elif choice == "Add item":
            add_item(grocery_list)
        #If user decides to view cart
        elif choice == "View items":
            view_items(grocery_list)
        #If user decides to remove item
        elif choice == "Remove item":
            remove_item(grocery_list)
        else:
            #If user does not choose valid option
            msgbox("Invalid choice.")

#Runs the program and ensures program is directly ran from file
if __name__ == "__main__":
    main()

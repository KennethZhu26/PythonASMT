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

#Maximum quantity per user per item
MAX_PER_ITEM_PER_USER = 50

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
    item = choicebox("Select an item to add.", "Add Item", choices=list(available_items.keys()))
    #If user cancels
    if not item:
        msgbox("Action has been cancelled.")
        #Ends function early
        return

    #Gets current quantity of item in the user's cart
    current_quantity = grocery_list.get(item, 0)
    #If user already has max allowed amount of item
    if current_quantity >= MAX_PER_ITEM_PER_USER:
        msgbox(f"You already have the maximum allowed of {MAX_PER_ITEM_PER_USER} x '{item}' in your cart.")
        #Ends function early
        return

    #Enterbox to ask for quantity
    quantity_input = enterbox(f"How many '{item}' would you like to buy? (Max: {MAX_PER_ITEM_PER_USER - current_quantity})", "Enter Quantity")
    if quantity_input is None:
        msgbox("Action has been cancelled.")
        #Ends function early
        return

    #Checks if input is of numerical characters
    if quantity_input.isdigit():
        #Converts string to integer
        quantity = int(quantity_input)
        #Checks input does not exceed maximum limit
        if 0 < quantity <= (MAX_PER_ITEM_PER_USER - current_quantity):
            if item in grocery_list:
                #If item already exisits in list, adds to it
                grocery_list[item] += quantity
            else:
                #If not in list, adds item with quantity
                grocery_list[item] = quantity
            #Message informing user item and quantity have been added
            msgbox(f"{quantity} x '{item}' has been added to your list.")
        else:
            #Message informing user they must enter quantity inside of avaliable
            msgbox(f"Please enter a whole number between 1 and {MAX_PER_ITEM_PER_USER - current_quantity}.")
    else:
        #Informs user they must enter a whole number greater than 0
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
        #Empty list to store quantities of items
        quantities = []

        #Calculates cart cost by multiplying item amount with cost
        for item in grocery_list:
            #Gets quantity of item from list
            quantity = grocery_list[item]
            #Gets price of item from available items
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
        #Informs user's total cart value
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
        #Informs user that cart is empty
        msgbox("Your grocery cart is empty.")    

#Function to remove item (fixed version)
def remove_item(grocery_list):
    #Informs user that cart is empty and items cannot be removed
    if not grocery_list:
        msgbox("Your grocery cart is empty, no items can be removed.")
        #Ends function early
        return

    #If there is only 1 item, selects item automatically
    if len(grocery_list) == 1:
        #Retrives item by changing keys into list while accessing the first one
        item = list(grocery_list.keys())[0]
    else:
        #Choicebox to select item to remove
        item = choicebox("Select an item to remove.", "Remove Item", choices=list(grocery_list.keys()))
        #If user cancels
        if item is None:
            msgbox("Action has been cancelled.")
            #Ends function early
            return

    #Asks user quantity where quantity to be removed must be <= quantity of items in cart
    max_quantity = grocery_list[item]
    quantity_input = enterbox(f"How many '{item}' would you like to remove? (Max: {max_quantity})", "Remove Quantity")
    #If user cancels
    if quantity_input is None:
        msgbox("Action has been cancelled.")
        #Ends function early
        return

    #Checks if input is composed of numerical characters
    if quantity_input.isdigit():
        #Converts string to integer
        quantity_to_remove = int(quantity_input)
        #Checks if quantity is within range
        if 1 <= quantity_to_remove <= max_quantity:
            #Confirmation box before final removal
            confirm = ynbox(f"Are you sure you want to remove {quantity_to_remove} x '{item}' from your cart?", "Confirm Removal")
            if confirm:
                #Removes selected quantity from the item
                grocery_list[item] -= quantity_to_remove
                #Remove item completely if quantity reaches 0 or below
                if grocery_list[item] <= 0:
                    del grocery_list[item]
                #Informs user that items and quantity have been removed 
                msgbox(f"Removed {quantity_to_remove} x '{item}' from your cart.")
            else:
                #Informs user removal has been cancelled
                msgbox("Removal cancelled.")
        else:
            #Informs user to enter a whole number between the limit
            msgbox(f"Please enter a whole number between 1 and {max_quantity}.")
    else:
        #Informs user to enter a valid whole number greatwer than 0
        msgbox("Please enter a valid whole number greater than 0.")    

#Function to checkout
def checkout(grocery_list):
    if grocery_list:
        #Sets initial total value of shopping cart to 0
        total = 0
        #Item numbering starts from 1
        count = 1
        message = "Your final grocery list:\n\n"
        #Calculates cart cost by multiplying item amount with cost
        for item in grocery_list:
            #Gets quantity of item from list
            quantity = grocery_list[item]
            #Gets price of item from available items
            price = available_items[item]
            item_total = quantity * price
            message += f"{count}. {item} x {quantity} = ${item_total:.2f}\n"
            #Adds item total to total cost
            total += item_total
            count += 1
        #Informs user's total cart value
        message += f"\nTotal: ${total:.2f}"
        #Message to inform user that checkout is complete
        msgbox(message, title='Checkout')
    else:
        #Informs user that cart is empty and therefore this is nothing to be checked out
        msgbox("Your grocery cart is empty. Nothing to checkout.", title='Checkout')    

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
        #Sets title of graph to Items in Cart
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
                msgbox(f"Welcome back, {username}!")
                #Returns authenticated user's username to the main function
                return username
            else:
                msgbox("Invalid username or password.")
        #If user chooses to sign up
        elif action == "Sign Up":
            #If username already exists, prompts them to login instead
            if username in users:
                msgbox("Username already exists. Try logging in.")
            else:
                #Asks user to confirm password
                confirm_pass = enterbox("Confirm your password:")
                if confirm_pass is None:
                    #Informing user sign up has been cancelled
                    msgbox("Sign Up cancelled.")
                elif confirm_pass == password:
                    #If password matches, creates account and empty cart
                    users[username] = {"password": password, "cart": {}}
                    #Saves user's details
                    save_users(users)
                    msgbox("Account created successfully.")
                    #Returns authenticated user's username to the main function
                    return username
                else:
                    #Informs user passwords do not match and they must re-try
                    msgbox("Passwords do not match. Try again.")    

# Main function
def main():
    #Initializes an empty grocery list for the user's shopping cart
    grocery_list = {}
    
    #Authenticates the user and calls the authentication function
    user = authenticate()

    #If authentication fails or the user exits
    if not user:
        #Displays goodbye message and exits
        msgbox("Goodbye.")
        #Ends function early
        return

    #Loads users from the json file
    users = load_users()

    #If the user already exists and has a shopping cart, loads it
    if user in users and "cart" in users[user]:
        grocery_list = users[user]["cart"]

    #Loop to keep asking the user for their action until they choose to exit
    while True:
        #Prints the main menu and gets the user's choice
        choice = print_menu()

        #If the user exits or clicks "Exit"
        if choice is None or choice == "Exit":
            #Shows a summary of the user's grocery list and data visualization
            show_summary_and_visualization(grocery_list)
            #Saves the user's updated cart back into json file
            users[user]["cart"] = grocery_list
            save_users(users)
            #Displays goodbye message
            msgbox("Goodbye.")
            break

        #If the user chooses to add an item
        elif choice == "Add item":
            add_item(grocery_list)
        #If the user chooses to view their items
        elif choice == "View items":
            view_items(grocery_list)
        #If the user chooses to remove an item
        elif choice == "Remove item":
            remove_item(grocery_list)
        #If the user enters an invalid choice
        else:
            msgbox("Invalid choice.") 
  
#Runs the program and ensures it runs directly from the file
if __name__ == "__main__":
    main()

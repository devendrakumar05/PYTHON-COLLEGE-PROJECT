# Shopping List Program

# Function to display the menu
def display_menu():
    print("\n1. Add item to the list")
    print("2. Remove item from the list")
    print("3. View the list")
    print("4. Clear the list")
    print("5. Exit")

# Function to add an item to the list
def add_item(item, shopping_list):
    shopping_list.append(item)
    print(item, "added to the list.")

# Function to remove an item from the list
def remove_item(item, shopping_list):
    if item in shopping_list:
        shopping_list.remove(item)
        print(item, "removed from the list.")
    else:
        print(item, "is not in the list.")

# Function to view the shopping list
def view_list(shopping_list):
    print("\nShopping List:")
    for item in shopping_list:
        print("-", item)

# Function to clear the shopping list
def clear_list(shopping_list):
    shopping_list.clear()
    print("Shopping list cleared.")

# Main function
def main():
    shopping_list = []

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the item to add: ")
            add_item(item, shopping_list)
        elif choice == '2':
            item = input("Enter the item to remove: ")
            remove_item(item, shopping_list)
        elif choice == '3':
            view_list(shopping_list)
        elif choice == '4':
            clear_list(shopping_list)
        elif choice == '5':
            print("Thank you for using the shopping list program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Calling the main function
'''if _name_ == "_main_":'''
main()

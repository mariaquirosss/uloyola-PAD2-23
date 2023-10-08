##Shopping list: Create a shopping list where users can add and remove items and display the
##final list

def show_menu():
    print("Shopping List Menu:")
    print("1. Add item to the list")
    print("2. Remove item from the list")
    print("3. Show the shopping list")
    print("4. Quit")

def add_item(shopping_list, item):
    shopping_list.append(item)
    print(f"{item} has been added to the shopping list.")

def remove_item(shopping_list, item):
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} has been removed from the shopping list.")
    else:
        print(f"{item} is not in the shopping list.")

def show_shopping_list(shopping_list):
    if not shopping_list:
        print("The shopping list is empty.")
    else:
        print("Shopping List:")
        for index, item in enumerate(shopping_list, start=1):
            print(f"{index}. {item}")

def main():
    shopping_list = []

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the item to add: ")
            add_item(shopping_list, item)
        elif choice == '2':
            item = input("Enter the item to remove: ")
            remove_item(shopping_list, item)
        elif choice == '3':
            show_shopping_list(shopping_list)
        elif choice == '4':
            print("Thank you for using the Shopping List program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option (1-4).")

if __name__ == "__main__":
    main()
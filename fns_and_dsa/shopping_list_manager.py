def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            list_item = input("Enter item name to add to the list: ")
            shopping_list.append(list_item)
            print()
        elif choice == '2':
            # Prompt for and remove an item
            list_item = input("Enter item name to remove on the list: ")
            shopping_list.remove(list_item)
            print()
        elif choice == '3':
            # Display the shopping list1
            for item in shopping_list:
                print(item)
            print()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
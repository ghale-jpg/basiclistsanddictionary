contacts = {
    "Ram": "9841000000",
    "Sita": "9851000000",
    "Hari": "9861000000"
}

while True:
    print("\n====Contact Book====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display All Contacts")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        name = input("Enter contact name: ")
        number = input("Enter contact number: ")
        contacts[name] = number
        print(f"Contact {name} added successfully.")

    elif choice == "2":
        name = input("Enter contact name to search: ")
        if name in contacts:
            print(f"{name}: {contacts[name]}")
        else:
            print(f"Contact {name} not found.") 

    elif choice == "3":
        name = input("Enter contact name to update: ")
        if name in contacts:
            number = input("Enter new contact number: ")
            contacts[name] = number
            print(f"Contact {name} updated successfully.")
        else:
            print(f"Contact {name} not found.")

    elif choice == "4":
        name = input("Enter contact name to delete: ")
        if name in contacts:
            del contacts[name]
            print(f"Contact {name} deleted successfully.")
        else:
            print(f"Contact {name} not found.")

    elif choice == "5":
        print("\nAll Contacts:")
        for name, number in contacts.items():
            print(f"{name}: {number}")

    elif choice == "6":
        print("Exiting Contact Book.")
        break

    else:
        print("Invalid choice. Please try again.")
"""
Contact Book program
"""

TypeContact = dict[str, dict[str, str]]

contacts: TypeContact = {}

while True:
    print("1. Create Contact")
    print("2. Update Contact")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. View Contacts")
    print("6. Count Contacts")
    print("7. Exit")

    choice = input("> ")

    if choice == "1":
        name = input("Enter name: ")
        email = input("Enter email: ")
        mobile = input("Enter phone number: ")
        contacts[name] = {"name": name, "email": email, "mobile": mobile}
        print("Contact added successfully")
    elif choice == "2":
        name = input("Enter name to update contact: ")
        if name in contacts:
            email = input("Enter email: ")
            mobile_num = input("Enter phone number: ")
            contacts[name].update({"email": email, "mobile": mobile})
            print("Contact updated successfully")

        else:
            print("Contact not found!")
    elif choice == "3":
        name = input("Enter name to search: ")
        if name in contacts:
            print(contacts[name])
        else:
            print("Contact not found!")
    elif choice == "4":
        name = input("Enter contact name to delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found!")
    elif choice == "5":
        if contacts:
            print(contacts)
        else:
            print("No contacts yet!")
    elif choice == "6":
        if contacts:
            print(f"No. of contacts: {len(contacts)}")
        else:
            print("No contacts yet!")
    elif choice == "7":
        print("Contact book closed")
        break
    else:
        print("Invalid command!")

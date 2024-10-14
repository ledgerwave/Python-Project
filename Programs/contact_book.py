"""
Contact Book program
"""

TypeContact = dict[str, str]

TypeContacts = dict[str, TypeContact]


class ContactBook:
    """
    Contact book class
    """

    def __init__(self):
        self.__contacts = {}

    def __str__(self):
        return f"Contact book: Total contacts {len(self.__contacts)}"

    def create_contact(self, contact: TypeContact) -> None:
        """
        Creates a new contact

        Args:
            contact (dict) : New contact dictionary
        """
        name, email, phone = contact["name"], contact["email"], contact["phone"]
        if name in self.__contacts:
            print("Contact name already exists!")
        else:
            self.__contacts[name] = {"name": name, "email": email, "phone": phone}
            print("Contact added successfully")

    def view_contacts(self) -> None:
        """
        View contacts
        """
        if self.__contacts:
            print(f"Contacts: {self.__contacts}")
        else:
            print("Empty contact list!")

    def update_contact(self, name: str, contact: TypeContact) -> None:
        """
        Updates the contact with the given name
        """
        if name in self.__contacts:
            self.__contacts[name].update(contact)
            print("Contact updated successfully")
        else:
            print("Contact not found!")

    def search_contact(self, name: str) -> TypeContact | None:
        """
        Searchs for a contact in list by given name
        """
        if name in self.__contacts:
            return self.__contacts[name]
        print("Contact not found!")
        return None

    def delete_contact(self, name: str) -> None:
        """
        Deletes a contact in list by given name
        """
        if name in self.__contacts:
            del self.__contacts[name]
        else:
            print("Contact not found!")


def main():
    """
    Main function
    """

    contact_book = ContactBook()

    while True:
        print("1. Create Contact")
        print("2. Update Contact")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. View Contacts")
        print("6. Exit")

        command = input("> ")

        if command == "1":
            name = input("Enter name: ")
            email = input("Enter email: ")
            phone = input("Enter phone: ")
            contact_book.create_contact({"name": name, "email": email, "phone": phone})
        elif command == "2":
            name = input("Enter name to update contact: ")
            email = input("Enter email: ")
            phone = input("Enter phone: ")
            contact_book.update_contact(
                name, {"name": name, "email": email, "phone": phone}
            )
        elif command == "3":
            name = input("Enter name to update contact: ")
            contact = contact_book.search_contact(name)
            print(contact)
        elif command == "4":
            name = input("Enter name to update contact: ")
            contact_book.delete_contact(name)
        elif command == "5":
            contact_book.view_contacts()
        elif command == "6":
            print("Contact book closed")
            break


if __name__ == "__main__":
    main()

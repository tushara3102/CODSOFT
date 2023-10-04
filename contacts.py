contacts = []

def add_contact():
    print("\nAdding a New Contact")
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email address: ")
    address = input("Enter the contact's address: ")
    contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
    contacts.append(contact)
    print("Contact added successfully.")

def view_contacts():
    print("\nViewing Contact List")
    if not contacts:
        print("No contacts found.")
    else:
        print("Contact List:")
        for index, contact in enumerate(contacts, start=1):
            print(f"{index}. Name: {contact['Name']}, Phone: {contact['Phone']}")

def search_contact():
    print("\nSearching for a Contact")
    search_term = input("Enter a name or phone number to search for: ")
    found_contacts = []
    for contact in contacts:
        if search_term.lower() in contact['Name'].lower() or search_term in contact['Phone']:
            found_contacts.append(contact)
    if found_contacts:
        print("Search results:")
        for index, found_contact in enumerate(found_contacts, start=1):
            print(f"{index}. Name: {found_contact['Name']}, Phone: {found_contact['Phone']}")
    else:
        print("No matching contacts were found.")

def update_contact():
    print("\nUpdating a Contact")
    view_contacts()
    if not contacts:
        return
    try:
        index = int(input("Enter the index of the contact to update: ")) - 1
        if 0 <= index < len(contacts):
            name = input("Enter the new name: ")
            phone = input("Enter the new phone number: ")
            email = input("Enter the new email address: ")
            address = input("Enter the new address: ")
            contacts[index] = {"Name": name, "Phone": phone, "Email": email, "Address": address}
            print("Contact updated successfully.")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input. Please enter a valid index.")

def delete_contact():
    print("\nDeleting a Contact")
    view_contacts()
    if not contacts:
        return
    try:
        index = int(input("Enter the index of the contact to delete: ")) - 1
        if 0 <= index < len(contacts):
            deleted_contact = contacts.pop(index)
            print(f"Contact '{deleted_contact['Name']}' deleted successfully.")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input. Please enter a valid index.")

def main():
    while True:
        print("\nContact Management System")
        print("1. Add a New Contact")
        print("2. View Contacts")
        print("3. Search for a Contact")
        print("4. Update a Contact")
        print("5. Delete a Contact")
        print("6. Quit")

        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

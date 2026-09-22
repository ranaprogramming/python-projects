

import json

DATA_FILE = "contacts.json"


def load_contacts(filename=DATA_FILE):
    
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        print("Warning: contacts file was corrupted. Starting fresh.")
        return {}


def save_contacts(contacts, filename=DATA_FILE):
    """Write the current contacts dict to disk as JSON."""
    with open(filename, "w") as f:
        json.dump(contacts, f, indent=2)


def add_contact(contacts, name, phone, email):
    if not name:
        print("Name cannot be empty.")
        return
    if phone and not phone.replace("-", "").isdigit():
        print("Phone number should contain only digits and dashes.")
        return
    contacts[name] = {"phone": phone, "email": email}
    print(f"Added {name}.")


def search_contact(contacts, name):
    if name in contacts:
        info = contacts[name]
        print(f"{name}: {info['phone']}, {info['email']}")
    else:
        print(f"No contact found for '{name}'.")


def delete_contact(contacts, name):
    if name in contacts:
        del contacts[name]
        print(f"Deleted {name}.")
    else:
        print(f"No contact found for '{name}'.")


def list_contacts(contacts):
    if not contacts:
        print("Contact book is empty.")
        return
    print(f"\n{len(contacts)} contact(s):")
    for name, info in sorted(contacts.items()):
        print(f"  {name}: {info['phone']}, {info['email']}")


def print_menu():
    print("\n--- Contact Book ---")
    print("1. Add contact")
    print("2. Search contact")
    print("3. Delete contact")
    print("4. List all contacts")
    print("5. Save and exit")


def main():
    contacts = load_contacts()

    while True:
        print_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            name = input("Name: ").strip()
            phone = input("Phone: ").strip()
            email = input("Email: ").strip()
            add_contact(contacts, name, phone, email)

        elif choice == "2":
            name = input("Name to search: ").strip()
            search_contact(contacts, name)

        elif choice == "3":
            name = input("Name to delete: ").strip()
            delete_contact(contacts, name)

        elif choice == "4":
            list_contacts(contacts)

        elif choice == "5":
            save_contacts(contacts)
            print("Saved. Goodbye!")
            break

        else:
            print("Invalid option, please choose 1-5.")


if __name__ == "__main__":
    main()
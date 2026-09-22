print("=" * 50)
print("          CONTACT MANAGEMENT SYSTEM")
print("=" * 50)

contacts = []

while True:

    print("1: Add Contact")
    print("2: View All Contacts")
    print("3: Search Contact")
    print("4: Update Contact")
    print("5: Delete Contact")
    print("6: Exit Contact")

    choice = input("Enter a choice")

    if choice == "1":
        name = input("Enter Name: ")
        phone_no = int(input("Enter Phone Number: "))
        email = input("Enter Email: ")

        contact = {
            "name" : name,
            "phone_no" : phone_no,
            "Email" : email
        }
        contacts.append(contact)
        print("Contact Added successfully")
    elif choice == "2":
        for index,contact in enumerate(contacts, start=1):
            print(index, contact["name"], "|", contact["phone_no"], "|", contact["Email"])

    elif choice == "3":
        phoneno = int(input("Enter PhoneNo to search: "))
        for contact in contacts:
            if phoneno == contact["phone_no"]:
                print("Name:", contact["name"])
                print("Phone No:", contact["phone_no"])
                print("Email:", contact["Email"])
                break
        else:
            print("No contact Found")
    elif choice == "4":
        phoneno = int(input("Enter Phone no to Search: "))
        for contact in contacts:
            if phoneno == contact["phone_no"]:
                contact["name"] = input("Enter new Name: ")
                contact["phone_no"] = int(input("Enter new Phone no: "))
                contact["Email"] = input("Enter new Email : ")

                print("Contact updated Successfully")
                break
        else:
            print("No Contact found")

    elif choice == "5":
        phoneno = int(input("Enter Phone no to Search: "))
        for contact in contacts:
            if phoneno == contact["phone_no"]:
                contacts.remove(contact)
                print("Contact Deleted Successfully")
                break
        else: 
            print("No Contact found")
    elif choice == "6":
        print("Contact managment system Exiting....")
        break
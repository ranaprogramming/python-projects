books = []

while True:
    print("1. Add Book")
    print("2. View Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Remove Book")
    print("6. Exit")

    choice = input("Enter a choice: ")

    if choice == "1":
        bookName =  input("Enter book name: ")
        AurthorName =  input("Enter Author name: ")
        availbale = True
        book = {
            "name" : bookName,
            "Author" : AurthorName,
            "available" : availbale
        }
        books.append(book)
        print("Book added successfully!")

    elif choice == "2":
        for index, book in enumerate(books, start=1):
            print(index, book["name"], "-", book["Author"])
            if book["available"] == True:
                print("Available")
            else:
                print("Borrowed")

    elif choice == "3":
        bookNumber = int(input("Enter book Number to borrow: "))
        book = books[bookNumber - 1]
        if book["available"] == False:
            print("Book is not Available")
        else:
            book["available"] = False
            print("Book borrowed successfully")
    elif choice == "4":
            bookNumber = int(input("Enter book Number to return: "))
            book = books[bookNumber - 1]
            if book["available"] == True:
                print("Book is not borrowed")
            else:
                book["available"] = True
                print("Book return successfully")
    elif choice == "5":
        bookNumber = int(input("Enter book Number to remove: "))
        
        books.pop(bookNumber - 1)
        print("Book Remocve successfully")
    elif choice == "6":
        break
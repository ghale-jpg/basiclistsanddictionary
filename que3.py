
books = [
    {"title": "Python Basics", "author": "John Smith", "available": True},
    {"title": "Learn Java", "author": "James Gosling", "available": True},
    {"title": "Web Development", "author": "David Miller", "available": True},
    {"title": "Data Science", "author": "Sarah Wilson", "available": False},
    {"title": "Computer Networks", "author": "Andrew Tanenbaum", "available": True}
]


def search_book(title):
    for book in books:
        if book["title"].lower() == title.lower():
            return book

    raise KeyError("Book does not exist in the library.")


def borrow_book(title):
    book = search_book(title)

    if not book["available"]:
        print("Sorry, this book is already borrowed.")
    else:
        book["available"] = False
        print("Book borrowed successfully:", book["title"])


def return_book(title):
    book = search_book(title)

    if book["available"]:
        print("This book has not been borrowed.")
    else:
        book["available"] = True
        print("Book returned successfully:", book["title"])


def display_available_books():
    print("\nAvailable Books")
    print("-------------------------")

    found = False

    for book in books:
        if book["available"]:
            print(book["title"], "-", book["author"])
            found = True

    if not found:
        print("No books are currently available.")


def main():
    while True:
        print("\n===== Library Management =====")
        print("1. Search Book")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Display Available Books")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "5":
            print("Thank you for using the library system.")
            break

        if choice == "4":
            display_available_books()
            continue

        if choice in ["1", "2", "3"]:
            title = input("Enter book title: ").strip()

            try:
                if choice == "1":
                    book = search_book(title)
                    status = ("Available" if book["available"]
                              else "Already borrowed")
                    print("Title:", book["title"])
                    print("Author:", book["author"])
                    print("Status:", status)

                elif choice == "2":
                    borrow_book(title)

                elif choice == "3":
                    return_book(title)

            except KeyError as error:
                print("Error:", error)

        else:
            print("Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()
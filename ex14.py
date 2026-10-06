book = {
    "title": "Python Basics",
    "author": "John Smith",
    "year": 2025,
    "price": 500
}
print("Keys", book.keys())
print("values", book.values())
print("Items", book.items())
print("\nBook Information:")
for key, value in book.items():
    print(f"{key}: {value}")


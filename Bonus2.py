cart = ["apple", "banana", "apple", "mango"]
prices = {
    "apple": 100,
    "banana": 50,
    "mango": 150
}
total = 0
for product in cart:
    total += prices[product]
print("Shopping Cart:", cart)
print("Total =", total)
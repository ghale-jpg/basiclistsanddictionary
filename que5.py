cart = ["apple", "milk", "bread", "apple", "eggs", "milk"]

cart = list(set(cart))
cart.append("cheese")

if "bread" in cart:
    cart.remove("bread")

cart.sort()

print("Shopping cart:", cart)
print("Number of items:", len(cart))
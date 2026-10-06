product = {
    "name": "Laptop",
    "brand": "Dell",   
    "price": 75000,
    "quantity": 5,
}

print("product:", product["name"])
print("brand:", product["brand"])
print("price:", product["price"])
print("Available quantity:", product["quantity"])
total_value = product["price"] * product["quantity"]
total_value = product["price"] * product["quantity"]
print("Total value:", total_value)
product["quantity"] -= 2
print("\nAfter selling 2 laptops:")
print("Remaining quantity:", product["quantity"])
updated_value = product["price"] * product["quantity"]

print("Updated total value:", updated_value)
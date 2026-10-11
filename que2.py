
products = {
    "laptop": {"price": 75000, "quantity": 3},
    "mouse": {"price": 1500, "quantity": 10},
    "keyboard": {"price": 2500, "quantity": 8},
    "monitor": {"price": 18000, "quantity": 4},
    "headphones": {"price": 3000, "quantity": 6},
    "usb": {"price": 800, "quantity": 15}
}

cart = {}


def add_product(name, quantity):
    if name not in products:
        raise KeyError("Product does not exist.")

    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")

    available = products[name]["quantity"]
    already_in_cart = cart.get(name, 0)

    if quantity + already_in_cart > available:
        raise ValueError(
            f"Only {available - already_in_cart} more item(s) available."
        )

    cart[name] = already_in_cart + quantity


def calculate_total():
    total = 0

    for name, quantity in cart.items():
        total += products[name]["price"] * quantity

    return total


def display_cart():
    print("\nShopping Cart")
    print("-------------------------")

    if not cart:
        print("Your cart is empty.")
        return

    for name, quantity in cart.items():
        price = products[name]["price"]
        print(f"{name.title()}: {quantity} x Rs. {price}"
              f" = Rs. {quantity * price}")

    print("Total: Rs.", calculate_total())


def main():
    while True:
        print("\nAvailable Products:")

        for name, details in products.items():
            print(f"{name.title()}: Rs. {details['price']}, "
                  f"Stock: {details['quantity']}")

        name = input("\nEnter product name (or 'done'): ").strip().lower()

        if name == "done":
            break

        try:
            quantity = int(input("Enter quantity: "))
            add_product(name, quantity)
            print("Product added successfully.")

        except KeyError as error:
            print("Error:", error)

        except ValueError as error:
            print("Invalid input:", error)

    # Display the final bill and update stock.
    display_cart()

    for name, quantity in cart.items():
        products[name]["quantity"] -= quantity

    print("\nThank you for shopping!")


if __name__ == "__main__":
    main()
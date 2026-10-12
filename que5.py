

menu = {
    "momo": 180,
    "pizza": 450,
    "burger": 250,
    "chowmein": 160,
    "fried_rice": 200,
    "pasta": 350,
    "sandwich": 220,
    "coffee": 120
}

order = []
tax_rate = 13


def display_menu():
    print("\n===== RESTAURANT MENU =====")

    for item, price in menu.items():
        print(f"{item.replace('_', ' ').title()}: Rs. {price}")


def add_item(item, quantity):
    if item not in menu:
        raise KeyError("This food item is not on the menu.")

    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")

    # Add to the existing quantity if the item is ordered again.
    for entry in order:
        if entry["item"] == item:
            entry["quantity"] += quantity
            return

    order.append({"item": item, "quantity": quantity})


def calculate_bill():
    subtotal = 0

    for entry in order:
        item = entry["item"]
        quantity = entry["quantity"]
        subtotal += menu[item] * quantity

    tax = subtotal * tax_rate / 100
    final_total = subtotal + tax

    return subtotal, tax, final_total


def display_order():
    print("\n===== FINAL ORDER =====")

    if not order:
        print("No items were ordered.")
        return

    for entry in order:
        item = entry["item"].replace("_", " ").title()
        quantity = entry["quantity"]
        price = menu[entry["item"]]
        item_total = price * quantity

        print(f"{item} x {quantity} = Rs. {item_total:.2f}")

    subtotal, tax, final_total = calculate_bill()

    print("-----------------------------")
    print(f"Subtotal: Rs. {subtotal:.2f}")
    print(f"Tax ({tax_rate}%): Rs. {tax:.2f}")
    print(f"Final Bill: Rs. {final_total:.2f}")


def main():
    display_menu()

    while True:
        item = input(
            "\nEnter food item (or 'done' to finish): "
        ).strip().lower()

        if item == "done":
            break

        try:
            if item not in menu:
                raise KeyError("Food item not found. Please check the menu.")

            quantity_text = input("Enter quantity: ").strip()

            try:
                quantity = int(quantity_text)
            except ValueError:
                print("Invalid quantity. Please enter a whole number.")
                continue

            if quantity <= 0:
                print("Quantity must be greater than zero.")
                continue

            add_item(item, quantity)
            print("Item added successfully.")

        except KeyError as error:
            print("Error:", error)

    display_order()
    print("\nThank you for visiting our restaurant!")


if __name__ == "__main__":
    main()

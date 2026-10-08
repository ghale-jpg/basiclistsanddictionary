inventory = {
    "apple": 10,
    "milk": 5,
    "bread": 8,
    "eggs": 12
}

item = input("Enter item to sell: ").lower()

if item in inventory:
    quantity = int(input("Enter quantity sold: "))

    if quantity <= inventory[item]:
        inventory[item] -= quantity

        if inventory[item] == 0:
            del inventory[item]

        print("Sale completed.")
    else:
        print("Not enough stock.")
else:
    print("Item not found.")

print("Updated inventory:", inventory)
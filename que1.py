import random

full_name = input("Enter your full name: ")
name = "_".join(full_name.split()).lower()

random_number = random.randint(1000, 9999)
username = name + str(random_number)

print("Generated username:", username)
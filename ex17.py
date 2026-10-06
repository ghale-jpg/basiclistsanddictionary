fruits = {"apple", "banana", "apple", "orange", "banana", "apple", "mango", "orange", "banana"
          }
fruit_count = {}
for fruita in fruits:
    if fruita in fruit_count:
        fruit_count[fruita] += 1
    else:
        fruit_count[fruita] = 1
        
print("Fruit Counts:")
for fruit, count in fruit_count.items():
    print(fruit, ":", count)
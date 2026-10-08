marks = [45, 78, 62, 89, 55, 92, 38, 76]

highest = max(marks)
lowest = min(marks)
average = sum(marks) / len(marks)

above_average = 0
for mark in marks:
    if mark > average:
        above_average += 1

print("Highest:", highest)
print("Lowest:", lowest)
print("Average:", average)
print("Above Average:", above_average)
print("Ascending:", sorted(marks))
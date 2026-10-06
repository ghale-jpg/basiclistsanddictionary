
marks = [75, 82, 68, 90, 55, 88, 72, 95]
print("Marks:", marks)
total_marks = sum(marks)
print("Total marks:", total_marks)
average_marks = total_marks / len(marks)
print("Average marks:", average_marks)
print("Highest mark:", max(marks))
print("Lowest mark:", min(marks))
count = 0
for mark in marks:
    if mark >= 75:
        count += 1

print("Students scoring 75 or more:", count)
marks.sort(reverse=True)

print("Marks from highest to lowest:", marks)
marks = {
    "Ram": 75,
    "Sita": 88,
    "Hari": 65,
    "Gita": 92,
    "John": 55
}
print("Student Marks:")
for student, mark in marks.items():
    print(student, "-", mark)
total_marks = sum(marks.values())
print("\nTotal Marks:", total_marks)
average_marks = total_marks / len(marks)
print("Average Marks:", average_marks)
highest_mark=max(marks.values())
print("Highest Mark:", highest_mark)    
lowest_mark=min(marks.values())
print("Lowest Mark:", lowest_mark)  
highest_student = max(marks, key=marks.get)

print("student with hight mark:", highest_student)
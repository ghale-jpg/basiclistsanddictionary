students = {"Ram", "Sita", "Hari", "Gita"}
marks = {"Ram": 75, "Sita": 88, "Hari": 65, "Gita": 92}
print("Student Marks:")
for student in students:
    print(student, ":", marks[student])
print("\nStudents scoring 80 and above:")
for student in students:
    if marks[student] >= 80:
        print(student, ":", marks[student])
student = {
    "name": "Ram",
    "age": 20,
    "course": "Computer Science",
    "marks": 65
}

print("Student Information:")
print("Name:", student["name"])
print("Age:", student["age"])
print("Course:", student["course"])
print("Marks:", student["marks"])

student["marks"] += 5

if student["marks"] >= 40:
    status = "Pass"
else:
    status = "Fail"

print("\nUpdated Marks:", student["marks"])
print("Status:", status)
employee = {
    "name": "John",
    "age": 30,
    "department": "IT",
    "salary": 50000,
    "city": "Kathmandu"
}
del employee["age"]
employee.pop("city")
print("Updated employee:", employee)
employee.pop("email", None)
print("After safely removing email:", employee)
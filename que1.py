
students = [
    {"name": "Ram", "subject1": 75, "subject2": 80, "subject3": 85},
    {"name": "Sita", "subject1": 90, "subject2": 88, "subject3": 92},
    {"name": "Hari", "subject1": 65, "subject2": 70, "subject3": 72},
    {"name": "Gita", "subject1": 95, "subject2": 89, "subject3": 94},
    {"name": "John", "subject1": 60, "subject2": 68, "subject3": 75}
]


def calculate_total(student):
    subjects = ["subject1", "subject2", "subject3"]

    for subject in subjects:
        if subject not in student or student[subject] is None:
            raise ValueError("A subject mark is missing.")

    return sum(student[subject] for subject in subjects)


def calculate_percentage(total):
    maximum_marks = 300
    return (total / maximum_marks) * 100


def main():
    name = input("Enter student name: ").strip()

    try:
        student = next(
            student for student in students
            if student["name"].lower() == name.lower()
        )

        total = calculate_total(student)
        percentage = calculate_percentage(total)

        print("\nStudent Result")
        print("--------------------")
        print("Name:", student["name"])
        print("Total Marks:", total, "/ 300")
        print(f"Percentage: {percentage:.2f}%")

    except StopIteration:
        print("Error: Student does not exist.")

    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
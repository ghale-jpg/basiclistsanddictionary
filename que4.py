
employees = {
    101: {"name": "Ram", "department": "IT", "salary": 50000},
    102: {"name": "Sita", "department": "HR", "salary": 45000},
    103: {"name": "Hari", "department": "Finance", "salary": 55000},
    104: {"name": "Gita", "department": "Marketing", "salary": 48000},
    105: {"name": "John", "department": "IT", "salary": 60000}
}


def find_employee(employee_id):
    if employee_id not in employees:
        raise KeyError("Employee ID does not exist.")

    return employees[employee_id]


def calculate_yearly_salary(monthly_salary):
    return monthly_salary * 12


def increase_salary(monthly_salary, percentage):
    if percentage < 0:
        raise ValueError("Percentage cannot be negative.")

    return monthly_salary + (monthly_salary * percentage / 100)


def main():
    try:
        employee_id = int(input("Enter employee ID: "))
        employee = find_employee(employee_id)

        percentage = float(
            input("Enter salary increase percentage: ")
        )

        if percentage < 0:
            raise ValueError("Percentage cannot be negative.")

        old_salary = employee["salary"]
        new_salary = increase_salary(old_salary, percentage)

        print("\nEmployee Salary Details")
        print("----------------------------")
        print("Name:", employee["name"])
        print("Department:", employee["department"])
        print(f"Old Monthly Salary: Rs. {old_salary:.2f}")
        print(f"New Monthly Salary: Rs. {new_salary:.2f}")
        print(
            f"Yearly Salary After Increase: "
            f"Rs. {calculate_yearly_salary(new_salary):.2f}"
        )

    except ValueError as error:
        print("Invalid input:", error)

    except KeyError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
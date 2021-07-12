EMPLOYEES = [
    {
      "id": 1,
      "name": "Jeremy Baker",
      "locationId": 1
    },
    {
      "id": 2,
      "name": "Jack Bauer",
      "locationId": 2
    },
    {
      "id": 3,
      "name": "Homer Simpson",
      "locationId": 1
    },
    {
      "id": 4,
      "name": "Michael Scott",
      "locationId": 1
    },
    {
      "name": "Leggy Boy",
      "locationId": 1,
      "id": 5
    },
    {
      "name": "Dakota",
      "locationId": 3,
      "id": 6
    },
    {
      "name": "BenJAMMIN Kimball",
      "locationId": 2,
      "id": 7
    }
]

def get_all_employees():
    return EMPLOYEES

def get_single_employee(id):
    requested_employee = None

    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee

def create_employee(employee):
    max_id = EMPLOYEES[-1]["id"]

    new_id = max_id + 1

    employee["id"] = new_id

    EMPLOYEES.append(employee)

    return employee

def delete_employee(id):
    # Initial -1 value for employee index, in case one isn't found
    employee_index = -1

    # Iterate the employeeS list, but use enumerate() so that you
    # can access the index value of each item
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            # Found the employee. Store the current index.
            employee_index = index

    # If the employee was found, use pop(int) to remove it from list
    if employee_index >= 0:
        EMPLOYEES.pop(employee_index)

def update_employee(id, new_employee):
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            EMPLOYEES[index] = new_employee
            break
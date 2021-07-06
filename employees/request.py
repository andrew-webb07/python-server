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
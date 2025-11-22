import requests

BASE_URL = "http://localhost:8000"

def get_employees():
    response = requests.get(f"{BASE_URL}/employees")
    response.raise_for_status()
    return response.json()

def add_employee(employee_data):
    response = requests.post(f"{BASE_URL}/employees", json=employee_data)
    response.raise_for_status()
    return response.json()

def update_employee(employee_id, updated_data):
    response = requests.put(f"{BASE_URL}/employees/update/{employee_id}", json=updated_data)
    response.raise_for_status()
    return response.json()

def delete_employee(employee_id):
    response = requests.delete(f"{BASE_URL}/employees/delete/{employee_id}")
    response.raise_for_status()
    return response.json()

# Example usage:
if __name__ == "__main__":
    # Get all employees
    print(get_employees())

    # Add a new employee
    new_employee = {
        "id": 6,
        "name": "Frank",
        "position": "Support",
        "salary": 55000
    }
    print(add_employee(new_employee))

    # Update an employee
    updated_employee = {
        "id": 6,
        "name": "Franklin",
        "position": "Support Lead",
        "salary": 60000
    }
    print(update_employee(6, updated_employee))

    # Delete an employee
    print(delete_employee(6))
    
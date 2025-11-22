from fastapi.testclient import TestClient
from main import app

# Crea una instancia de TestClient para la aplicación
client = TestClient(app)

def test_get_employees_initially_empty():
    response = client.get("/employees")
    assert response.status_code == 200
    assert response.json() == []

def test_add_employee_success():
    employee = {"id": 1, "name": "Alice", "position": "Developer", "salary": 70000}
    response = client.post("/employees", json=employee)
    assert response.status_code == 200
    assert response.json() == employee

def test_add_employee_duplicate_id():
    employee_1 = {"id": 2, "name": "Bob", "position": "Manager", "salary": 90000}
    client.post("/employees", json=employee_1)
    response = client.post("/employees", json=employee_1)
    assert response.status_code == 400
    assert response.json()["detail"] == "Employee ID already exists."

def test_update_employee_success():
    employee = {"id": 3, "name": "Charlie", "position": "Tester", "salary": 50000}
    client.post("/employees", json=employee)
    updated_employee = {"id": 3, "name": "Charlie", "position": "Lead Tester", "salary": 60000}
    response = client.put("/employees/update/3", json=updated_employee)
    assert response.status_code == 200
    assert response.json()["position"] == "Lead Tester"
    assert response.json()["salary"] == 60000.0

def test_update_employee_not_found():
    updated_employee = {"id": 99, "name": "Ghost", "position": "None", "salary": 0}
    response = client.put("/employees/update/99", json=updated_employee)
    assert response.status_code == 404
    assert response.json()["detail"] == "Employee not found."

def test_delete_employee_success():
    employee = {"id": 4, "name": "Dave", "position": "Designer", "salary": 65000}
    client.post("/employees", json=employee)
    response = client.delete("/employees/delete/4")
    assert response.status_code == 200
    assert response.json()["detail"] == "Employee deleted."

def test_delete_employee_not_found():
    response = client.delete("/employees/delete/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Employee not found."

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Employee(BaseModel):
    id: int
    name: str
    position: str
    salary: float

employees: List[Employee] = [Employee(id=1, name="Alice", position="Developer", salary=70000),
                              Employee(id=2, name="Bob", position="Manager", salary=90000),
                              Employee(id=3, name="Charlie", position="Tester", salary=50000),
                              Employee(id=4, name="Dave", position="Designer", salary=65000),
                              Employee(id=5, name="Eve", position="Analyst", salary=60000)]

@app.get("/employees", response_model=List[Employee])
def get_employees():
    return employees

@app.post("/employees", response_model=Employee)
def add_employee(employee: Employee):
    if any(emp.id == employee.id for emp in employees):
        raise HTTPException(status_code=400, detail="Employee ID already exists.")
    employees.append(employee)
    return employee

@app.put("/employees/update/{employee_id}", response_model=Employee)
def update_employee(employee_id: int, updated_employee: Employee):
    for idx, emp in enumerate(employees):
        if emp.id == employee_id:
            employees[idx] = updated_employee
            return updated_employee
    raise HTTPException(status_code=404, detail="Employee not found.")

@app.delete("/employees/delete/{employee_id}")
def delete_employee(employee_id: int):
    for idx, emp in enumerate(employees):
        if emp.id == employee_id:
            del employees[idx]
            return {"detail": "Employee deleted."}
    raise HTTPException(status_code=404, detail="Employee not found.")
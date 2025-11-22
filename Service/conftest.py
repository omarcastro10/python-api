import pytest
from main import employees

@pytest.fixture(autouse=True)
def reset_employees():
    """Reinicia la lista de empleados antes de cada test."""
    employees.clear()
    yield
    employees.clear()

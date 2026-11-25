from employee_salary import calculate_salary

def test_salary():
    hra, da, gross = calculate_salary(10000)
    assert hra == 1500
    assert da == 900
    assert gross == 12400
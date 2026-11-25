def calculate_salary(basic):
    hra = basic * 0.15
    da = basic * 0.09
    gross = basic + hra + da
    return hra, da, gross

def main():
    print("EMPLOYEE SALARY APPLICATION")
    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    location = input("Enter Work Location: ")
    basic = float(input("Enter Basic Salary: "))

    hra, da, gross = calculate_salary(basic)

    print("\n--- EMPLOYEE DETAILS ---")
    print("Name:", name)
    print("Department:", dept)
    print("Location:", location)
    print("Basic Salary:", basic)
    print("HRA (15%):", hra)
    print("DA (9%):", da)
    print("Gross Salary:", gross)

if __name__ == "__main__":
    main()
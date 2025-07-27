def balance(salary: int) -> int:
    all_employee_cost = salary * 0.1 + salary * 0.05 + salary * 0.03
    
    if salary >= 100000 and salary <= 200000:
        tax = salary * 0.1
        final_salary = salary - all_employee_cost - tax
        return final_salary
    elif salary >= 200001 and salary <= 500000:
        tax = salary * 0.2
        final_salary = salary - all_employee_cost - tax
        return final_salary
    elif salary > 500000:
        tax = salary * 0.3
        final_salary = salary - all_employee_cost - tax
        return final_salary
    else:
        # For salary less than 100000, no tax
        final_salary = salary - all_employee_cost
        return final_salary

if __name__ == "__main__":
    print(balance(500000))

    
    

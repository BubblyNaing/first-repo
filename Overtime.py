def salary_calc(hours_worked,hourly_wage,max_h_work):
    salary = 0
    if hours_worked<= max_h_work:
       salary = hourly_wage * hours_worked
    else : # overtime
       base_salary = max_h_work * hourly_wage
       extra_hours = hours_worked - max_h_work
       extra_salary = extra_hours * hourly_wage* 1.5
       salary = extra_salary
       return salary 


    salary_week_1 = salary_calc (50,15,40)
    salary_week_2 = salary_calc (45,15,40)
    salary_week_3 = salary_calc (30,15,40)
    salary_week_4 = salary_calc (50,15,40)
    monthly_salary = salary_week_1 + salary_week_2 + salary_week_3 + salary_week_4
    print(f"your salary for this week is ${salary}")
       





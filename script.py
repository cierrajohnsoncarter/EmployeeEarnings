def employee_earnings(name, hours_worked, hourly_wage):
    weekly_earnings = hours_worked * hourly_wage
    if hours_worked == 40:
        return f'{name} earned ${str(weekly_earnings)} this week.'
    elif hours_worked > 40:
        return f'{name} earned ${str(weekly_earnings)} this week. Talk to the manager to take some days off next week.'
    else:
        return f'{name} earned ${str(weekly_earnings)} this week. You have not worked a full 40 hours.'


print(employee_earnings('Josh', 40, 65))
print(employee_earnings('Stacy', 55, 80))
print(employee_earnings('Brandon', 35, 100))
print(employee_earnings('Amanda', 25, 70))
print(employee_earnings('Skylar', 30, 30))

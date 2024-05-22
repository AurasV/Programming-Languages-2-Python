def payment(hours_worked, pay_per_hour):
    if hours_worked <= 40:
        return hours_worked * pay_per_hour

    else:
        return 40 * pay_per_hour + (hours_worked - 40) * pay_per_hour * 1.5


print(payment(41, 2))
print(payment(40, 2))

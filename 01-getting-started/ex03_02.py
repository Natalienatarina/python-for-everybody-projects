hrs = input("Enter Hours:")
hrs = float(hrs)
rate = input("Enter Rate:")
rate = float(rate)
if hrs > 40:
    regular_pay = rate * 40
    overtime = hrs - 40
    overtime_pay = overtime * rate * 1.5
    gross_pay = regular_pay + overtime_pay
else: gross_pay = hrs * rate
print(gross_pay)
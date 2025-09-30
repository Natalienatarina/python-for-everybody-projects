hrs = input("Enter Hours:")
hrs = float(hrs)
rate = input("Enter Rate:")
rate = float(rate)
def computepay(hrs, rate):
    if hrs <= 40:
        pay = hrs * rate
        return pay
    else:
        overtime = hrs - 40
        gross_pay = (rate * overtime * 1.5) + (40 * rate)
        return gross_pay
        
gross_pay = computepay(hrs, rate)

print("Pay", gross_pay)
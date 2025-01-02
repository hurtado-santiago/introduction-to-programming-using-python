# uso de módulos
import math

def process (a,b,c,d):
    r = (b/100)/12
    n = c*12
    if r == 0:
        Remaining_Loan_Balance = a*(1-(d/n))
    else:
        Remaining_Loan_Balance = a*(((1+r)**n)-((1+r)**d))/((1+r)**n-1)
    return Remaining_Loan_Balance

principal = 1000.0
annual_interest_rate = 4.5
duration = 5
number_of_payments = 12
out = process (principal, annual_interest_rate, duration, number_of_payments)
print (out)


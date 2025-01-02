# uso de módulos
import math

def process (a,b,c):
    r = (b/100)/12
    n = c*12
    if r == 0:
        monthly_payment = a/n
    else:
        monthly_payment = a*((r*(1+r)**n)/((1+r)**n-1)) 
    return monthly_payment

principal = 1000.0
annual_interest_rate = 4.5
duration = 5
out = process (principal, annual_interest_rate, duration)
print (out)


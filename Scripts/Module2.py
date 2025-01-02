# uso de módulos
import math

def process (number):
    y = abs(number**3)+math.cos(math.sqrt(3*number))
    return y

x = 2
out = process (x)
print (out)


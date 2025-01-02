# uso de módulos
import math

def process (number):
    y = math.sin(number)-math.cos(number)+math.sin(number)*math.cos(number)
    return y

x = 2
out = process (x)
print (out)


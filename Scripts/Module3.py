# uso de módulos
import math

def process (a, b):
    y = math.sqrt((list2[0]-list1[0])**2 + (list2[1]-list1[1])**2 + (list2[2]-list1[2])**2) 
    return y

list1 = [2, 3, -5]
list2 = [4, -3, 12]
out = process (list1, list2)
print (out)


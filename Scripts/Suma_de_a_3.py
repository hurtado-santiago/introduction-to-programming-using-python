x = 1
y = 2
z = 0
while x <= 1001 :
    y = y + 1
    if y == 3:
        z = z + x
        y = 0
    x = x + 1
print (z)

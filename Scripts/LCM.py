def proc (a,b):
    for search in range (1,a*b+1):
        if not search%a and not search%b:
            return search
        
number1 = 9
number2 = 18
out = proc (number1, number2)
print (out)

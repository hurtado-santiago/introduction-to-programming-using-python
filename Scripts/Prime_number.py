def proc (x):
    if x == 0 or x == 1:
        return False
    for search in range (2,x):
        if not x % search:
            return False
    return True
        
number = 10
out = proc (number)
print (out)

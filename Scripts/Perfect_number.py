def proc (x):
    perfect = 0
    for search in range (1,x):
        if not x % search:
            perfect = perfect + search
    if perfect == x:
        return True
    else:
        return False

number = 3
out = proc (number)
print (out)

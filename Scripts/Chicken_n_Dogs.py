def proc (h,l):
    chicken = 0
    dogs = 0
    if h*2>l or l%2:
        return None
    elif h*2==l:
        chicken = h
        dogs = 0
        return (chicken, dogs)
    elif h*4==l:
        chicken = 0
        dogs = h
        return (chicken, dogs)
    for n in range (1,h):
        if ((h-n)*2) + 4*n == l:
            chicken = h-n
            dogs = n
    return [chicken, dogs]
        
heads = 9
legs = 23
out = proc (heads, legs)
print (out)

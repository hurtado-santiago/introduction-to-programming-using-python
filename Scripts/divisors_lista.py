def proc (a):
    my_list = []
    for x in range(1,a+1):
        if not a%x:
            my_list.append(x)
    return my_list

k = int(input ("Integer: "))
out = proc (k)
print(out)

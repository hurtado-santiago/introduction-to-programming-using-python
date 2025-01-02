def proc (a):
    my_list = []
    for x in range(1,a):
        aux = x **(1/3)
        print (x)
        my_list.append(aux)
    return my_list

k = int(input ("Integer: "))
out = proc (k)
print(out)

def proc (a):
    my_list = []
    for x in range(1,6):
        my_list.append(x*a)
    return my_list

x = int (input ("Integer: "))
out = proc (x)
print(out)

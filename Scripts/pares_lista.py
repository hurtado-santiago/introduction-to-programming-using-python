def proc (n1, n2):
    my_list = []
    for x in range(n1,n2):
        if not x%2:
            my_list.append(x)
    return my_list

a = int (input ("Integer1: "))
b = int (input ("Integer2: "))
out = proc (a, b)
print(out)

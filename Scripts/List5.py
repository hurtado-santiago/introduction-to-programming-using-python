def proc (mylist, num):
    length = 0
    times = 0
    for element in mylist:
        length = length + 1
    for index in range (0, length):
        if mylist[index] == num:
             times = times + 1
    return times
    
my_list = [5, 4, 3]
value = 3
out = proc (my_list, value)
print (out)
#print(my_list[0:-1:3])

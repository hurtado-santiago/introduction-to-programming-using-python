def proc (mylist):
    new_list = []
    length = 0
    times = 0
    for element in mylist:
        length = length + 1
    for element in mylist:
        if element%2:
          new_list.append (element+1)
        else:
            new_list.append (element)
    return new_list
    
my_list = [5, 4, 3]
out = proc (my_list)
print (out)
#print(my_list[0:-1:3])

def proc (A):
    my_list = A[:]
    length = 0
    for element in my_list:
        length = length + 1
    unSorted = True
    while unSorted:
        unSorted = False
        for index in range(0, length-1):
            if my_list[index] > my_list[index + 1]:
                temporary_variable = my_list[index]
                my_list[index] = my_list[index + 1]
                my_list[index + 1] = temporary_variable
                unSorted = True
    return my_list
    
my_listA=[5, 4, 3]
out = proc (my_listA)
print (out)
#print(my_list[0:-1:3])

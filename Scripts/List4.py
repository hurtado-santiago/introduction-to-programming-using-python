def proc (A, B):
    new_list = A[:]
    new_list.extend(B)
    length = 0
    for element in new_list:
        length = length + 1
    unSorted = True
    while unSorted:
        unSorted = False
        for index in range(0, length-1):
            if new_list[index] < new_list[index + 1]:
                temporary_variable = new_list[index]
                new_list[index] = new_list[index + 1]
                new_list[index + 1] = temporary_variable
                unSorted = True
    return new_list
    
my_listA=[5, 4, 3]
my_listB=[6, 2, 1]
out = proc (my_listA, my_listB)
print (out)
#print(my_list[0:-1:3])

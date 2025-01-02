def proc (mylistA, mylistB):
    mylistA.extend(mylistB)
    new_list = []
    for element in mylistA:
        if element not in new_list:
            new_list.append(element)
    return new_list
    
my_listA = [5, 4, 3, 3]
my_listB = [2, 1, 1, 6]
out = proc (my_listA, my_listB)
print (out)
#print(my_list[0:-1:3])

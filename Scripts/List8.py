def proc (mylistA, mylistB):
    length = 0
    count = 0
    mylistA.extend (mylistB)
    for element in mylistA:
        if element%2:
            count = count + element
    return count
    
my_listA = [5, 4, 3]
my_listB = [2, 1, 0]
out = proc (my_listA, my_listB)
print (out)
#print(my_list[0:-1:3])

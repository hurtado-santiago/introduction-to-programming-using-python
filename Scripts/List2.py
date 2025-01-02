def proc (A, B):
    new_list = []
    sizeA = len(A)
    sizeB = len (B)
    for x in range (0,sizeA):
        new_list.append(A[x])   
    for x in range (0, sizeB):
        new_list.append(B[x])
    return new_list
    
my_listA=[5, 4, 3]
my_listB=[2, 6, 1]
out = proc (my_listA, my_listB)
print (out)
#print(my_list[0:-1:3])

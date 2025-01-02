def proc (mylistA):
    new_list = []
    length = len (mylistA)
    for index in range (0, length):
        new_list.append (mylistA[length-index-1])
    print (length)
    return new_list
    
my_listA = ['mouse', 'cat', 'dog']
out = proc (my_listA)
print (out)
#print(my_list[0:-1:3])

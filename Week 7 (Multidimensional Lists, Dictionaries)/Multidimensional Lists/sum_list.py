def sum_list(some_list):
    add=0
    
    for array in some_list:
        for j in array:
            add+=j
    return add
    
list_1 = [[1,2,3],[4,5,6]]
print(sum_list(list_1))

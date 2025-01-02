def avg_list(some_list):
    add=0
    quantity=0
    
    for array in some_list:
        for j in array:
            quantity+=1
            add+=j
    return (add/quantity)
    
list_1 = [[1,2,3],[4,5,6]]
print(avg_list(list_1))

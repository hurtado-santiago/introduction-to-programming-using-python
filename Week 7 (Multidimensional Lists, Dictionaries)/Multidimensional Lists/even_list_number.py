def even_list_number(some_list):
    even=0
        
    for array in some_list:
        for j in array:
            if j%2 == 0 and j>even:
                even = j
    if even == 0:
        return None
    else:
        return even
    
list_1 = [[1,2,3,5],[1,5,3,5]]
print(even_list_number(list_1))

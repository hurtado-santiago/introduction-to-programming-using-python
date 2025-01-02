def descending_list(some_list):
    
    for item in some_list:
        item.sort(reverse=True)
    return some_list

   
list_1 = [[35, 12, -35, -12], [0, 0, 3, 0], [0, -2, -4, 12], [11, 11, 11, 11]]
print(ascending_list(list_1))


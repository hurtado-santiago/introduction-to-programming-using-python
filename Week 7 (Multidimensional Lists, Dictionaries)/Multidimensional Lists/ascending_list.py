def ascending_list(some_list):
    cols=len(some_list)
    output_list=[]
    
    for i in range(cols):
        output_list.extend(some_list[i])
    output_list.sort()
    return output_list

   
list_1 = [[35, 12, -35, -12], [0, 0, 3, 0], [0, -2, -4, 12], [11, 11, 11, 11]]
print(ascending_list(list_1))


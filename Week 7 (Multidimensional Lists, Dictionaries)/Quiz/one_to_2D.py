def one_to_2D(some_list, rows, columns):
    long_new_list=rows*columns
    output=[]
    
    if not some_list or long_new_list == 0:
        return None

    if len(some_list)<long_new_list:
        for i in range(len(some_list), long_new_list):
            some_list.append('None')
        
    for i in range(rows):
        output.append(some_list[(i*columns):(i*columns)+columns])
    return output


lists =  [8, 2, 9, 4, 1, 6, 7, 8, 7, 10]
r, c = 2, 3
print(one_to_2D(lists, r, c))

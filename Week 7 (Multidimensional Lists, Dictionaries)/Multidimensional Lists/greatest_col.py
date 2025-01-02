def greatest_col(some_list):
    cols=len(some_list[0])
    output_list=[]
    
    for i in range(cols):
        temp=[]
        for row in some_list:
            temp.append(row[i])
        output_list.append(max(temp))
    return output_list

   
list_1 = [[35, 12, -35, -12], [0, 0, 3, 0], [0, -2, -4, 12], [11, 11, 11, 11]]
print(greatest_col(list_1))


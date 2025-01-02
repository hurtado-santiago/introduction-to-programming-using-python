def greatest_row(some_list):
    output_list=[]

    for rows in some_list:
        output_list.append(max(rows))
    return output_list

   
list_1 = [[35, 12, -35, -12], [0, 0, 3, 0], [0, -2, -4, 12], [11, 11, 11, 11]]
print(greatest_number(list_1))

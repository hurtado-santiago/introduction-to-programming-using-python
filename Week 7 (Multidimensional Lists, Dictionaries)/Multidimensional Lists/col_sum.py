def col_sum(some_list):
    cols=len(some_list[0])
    output_list=[]
        
    for i in range(cols):
        add=0
        for row in some_list:
            add += row[i]
        output_list.append(add)
    return output_list
  
list_1 = [[35, 12, -35, -12], [0, 0, 3, 0], [0, -2, -4, 12], [11, 11, 11, 11]]
print(even_odd(list_1))

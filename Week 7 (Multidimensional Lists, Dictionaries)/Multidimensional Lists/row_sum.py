def row_sum(some_list):
    output_list=[]
    
    for item in some_list:
        output_list.append(sum(item))
    return output_list
   
list_1 = [[1,2,3,5],[1,5,3,5]]
print(row_sum(list_1))

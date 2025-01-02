def multiply_vectors_no_np(l1, l2):
    output_list=[]
    if len(l1[0])!=len(l2):
        return None
    
    for item_l1 in l1:
        temp=[]
        for i in range(len(l2)):
            row=[]
            add=0
            for rows in l2:
                row.append(rows[i])
            for i in range(len(l2)):
                add+=(item_l1[i]*row[i])
            temp.append(add)
        output_list.append(temp)
    return output_list
               
a = [[2, 3, 4],
     [3, 4, 5]]

b = [[4, -3, 12],
     [1, 1, 5],
     [1, 3, 2]]
print(multiply_vectors(a, b))


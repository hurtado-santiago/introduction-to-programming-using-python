def can_multiplied(l1, l2):
    cols_l1=len(l1[0])
    rows_l2=len(l2)
    
    if cols_l1==rows_l2:
        return True
    else:
        return False

   
a = [[2, 3, 4],
     [3, 4, 5]]
b = [[4, -3, 12],
     [1, 1, 5],
     [1, 3, 2]]
print(can_multiplied(a, b))


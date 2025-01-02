def crazy_list(lists):
    until = int(len(lists)/2)
    cont = 0
    for x in range(until):
        if lists[x] == lists[-(x+1)]:
            cont += 1
        else:
            return False    
    if cont == until:
        return True
    else:
        return False
    
list_b = [5, 6, 8, 9, 'PYTHON', 9, 8, 6, 5] 
list_c = [4, 5, 6, 7, 8, 4, 5, 2]
list_a = [1, 3, 2]
print(crazy_list(list_a))

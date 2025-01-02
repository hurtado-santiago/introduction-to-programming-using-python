def even_odd(some_list):
    count_even=0
    count_odd=0

    for rows in some_list:
        row_sum = sum(rows)
        if row_sum%2 == 0:
            count_even+=1
        else:
            count_odd+=1
    return [count_even, count_odd]

   
list_1 = [[35, 12, -35, -12], [0, 0, 3, 0], [0, -2, -4, 12], [11, 11, 11, 11]]
print(even_odd(list_1))

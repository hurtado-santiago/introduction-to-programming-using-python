def MY_2D_LIST(number):
    final_list=[[1]]
    for index in range(1, number):
        some_list=[1]
        print(index)
        for j in range(1, index):
            some_list.append(final_list[index-1][j-1]+final_list[index-1][j])
        some_list.append(1)
        print('some_list: ', some_list)
        final_list.append(some_list)
        print('final_list: ', final_list)
    return(final_list)


integer = 3
print(MY_2D_LIST(integer))

def nested_list_sum(some_list):
    my_sum=0
    for item in some_list:
        if type(item)!=type([]):
            my_sum+=item
        else:
            my_sum+=nested_list_sum(item)
    return (my_sum)
    
some_list=[1, -1, [2, -2], [3, -3, [4, -4], 10]]
print(nested_list_sum(some_list))

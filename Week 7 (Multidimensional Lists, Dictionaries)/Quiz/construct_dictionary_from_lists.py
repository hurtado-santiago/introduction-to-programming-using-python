def construct_dictionary_from_lists(some_list):
    output={}
    for i, item in enumerate(some_list[0]):
        temp=[]
        for j, row in enumerate(some_list):
            if j != 0:
                temp.append(row[i])
                if j == len(some_list)-1:
                    if temp[j-1]>=60:
                        temp.append('pass')
                    else:
                        temp.append('fail')
        output['{}'.format(item)]=temp
    return output

lists =  (["paul", "saul", "steve", "chimpy"],
          [28, 59, 22, 5],
          [59, 85, 55, 60])
print(construct_dictionary_from_lists(lists))

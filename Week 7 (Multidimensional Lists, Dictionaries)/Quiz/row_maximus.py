def row_maximus(some_list):
    output={}
    for index, item in enumerate(some_list):
        highest=item[0]
        for number in item:
            if number>highest:
                highest=number
        output['row {} max'.format(index)]=highest
    return output

numbers = [[5, 0, 0, 0, 13],
          [0, 12, 0, 0],
          [20, 0, 11, 0],
          [6, 0, 0, 8]] 
print(row_maximus(numbers))

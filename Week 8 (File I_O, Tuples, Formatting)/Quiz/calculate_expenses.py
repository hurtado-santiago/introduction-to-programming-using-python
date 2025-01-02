def calculate_expenses(some_file):
    food={}
    some_list=[]
    file_pointer = open(some_file, 'r')
    data = file_pointer.readlines()
    file_pointer.close()

    for lines in data:
        lines=lines.strip().split(',')
        my_item = lines[0].strip()
        my_price = float(lines[1].strip())

        if my_item not in food:
            food[my_item]=my_price
        else:
            food[my_item]+=my_price

    keys=sorted(food.keys())
    
    for key in keys:
        some_list.append((key,"${0:.2f}".format(food[key])))
    return(some_list)

file_name = 'calculate_expenses.txt'
print(calculate_expenses(file_name))

def select_milk_bread(file_name):
    file_pointer = open(file_name, 'r')
    data = file_pointer.readlines()
    file_pointer.close()
    
    output={}
    lists_m=[]
    lists_b=[]
    
    for item in data:
        temp = item.strip('\n')
        stripped_line=temp.split(' ')
        aux=[]
        if stripped_line[0] == 'm':
            float_values=float_value(aux, stripped_line)
            lists_m.append(float_values)
            
        if stripped_line[0] == 'b':
            float_values=float_value(aux, stripped_line)
            lists_b.append(float_values)
            
    output['milk']=lists_m
    output['bread']=lists_b
    return output

def float_value(aux, line):
    aux=line[1:]
    for i, value in enumerate(aux):
        aux[i]=float(value)
    return aux


file_name = 'select_milk_bread.txt'
print(select_milk_bread(file_name))

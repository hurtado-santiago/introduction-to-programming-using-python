def key_keys(file_name):
    file_pointer = open(file_name, 'r')
    data = file_pointer.readlines()
    file_pointer.close()
    
    output={}
    lastnames={}
    
    for item in data:
        if item[0] != '#':
            first_name, last_name, age = item.strip().split(',')
            if last_name not in lastnames:
                lastnames[last_name]={first_name: int(age)}
            else:
                if first_name not in lastnames[last_name]:
                    lastnames[last_name][first_name]=int(age)
    return lastnames 
        

file_name = 'key_keys.txt'
print(list_from_file(file_name))

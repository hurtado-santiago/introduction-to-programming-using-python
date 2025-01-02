def list_from_file(file_name):
    # Make a connection to the file
    file_pointer = open(file_name, 'r')
    # You can use either .read() or .readline() or .readlines()
    data = file_pointer.readlines()
    # NOW CONTINUE YOUR CODE FROM HERE!!!
    output=[]
    for item in data:
        stripped_line=item.strip('\n')
        output.append(stripped_line)
    return output
        

file_name = 'list_from_file.txt'
print(list_from_file(file_name))

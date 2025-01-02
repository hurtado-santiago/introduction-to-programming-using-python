def calculate_grades(some_file):

    file_pointer = open(some_file, 'r')
    data = file_pointer.readlines()
    file_pointer.close()

    new_lines=[]
    pairs = []

    for lines in data:
        add=0
        if lines[0] != '#':
            lines=lines.strip().split('\n')
            new_lines.append(lines)
    new_lines=sorted(new_lines)

    for index, real_info in enumerate(new_lines):
        aux=[]
        add=0
        real_info="".join(real_info)
        real_info=real_info.split(',')
        numbers=real_info[1:len(new_lines)+1]
        for num in numbers:
            add+=int(num)
        avg=add/len(numbers)
        aux=real_info[0], avg
        pairs.append(aux)

    for index in range (0, len(pairs)):
        pairs[index]=tuple(pairs[index])
    return(tuple(pairs))


file_name = 'calculate_grades.txt'
print(calculate_grades(file_name))

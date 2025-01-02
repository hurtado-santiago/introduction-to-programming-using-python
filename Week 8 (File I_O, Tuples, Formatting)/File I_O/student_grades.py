def student_grades(file_name):
    file_pointer = open(file_name, 'r')
    data = file_pointer.readlines()
    
    output={}
    
    for item in data:
        aux=[]
        temp = item.strip('\n')
        stripped_line=temp.split(',')
        for index, value in enumerate(stripped_line):
            if index == 0:
                output[value]=''
            else:
                aux.append(float(value))
        output['{}'.format(stripped_line[0])]=aux
    return output
        

file_name = 'student_grades.txt'
print(student_grades(file_name))

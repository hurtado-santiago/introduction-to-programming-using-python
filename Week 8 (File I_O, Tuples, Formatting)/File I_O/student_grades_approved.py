def student_grades_approved(file_name):
    file_pointer = open(file_name, 'r')
    data = file_pointer.readlines()
    file_pointer.close()
    data=data[1:]
    output={}
    
    for item in data:
        aux=[]
        temp = item.strip('\n')
        stripped_line=temp.split(',')
        for index, value in enumerate(stripped_line):
            if index != 0:
                aux.append(float(value))
        if aux[0]>70.0 and aux[2]>70.0:
            output[stripped_line[0]]=aux
    return output
        

file_name = 'student_grades_approved.txt'
print(student_grades_approved(file_name))

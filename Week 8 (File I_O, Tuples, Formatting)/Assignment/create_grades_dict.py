def create_grades_dict (file_name):
    file_pointer = open(file_name, 'r')
    data = file_pointer.readlines()
    file_pointer.close()
    output={}

    for item in data:
        grades={}
        if item[0] != '#':
            student = item.strip().split(',')
            for index, value in enumerate(student):
                value=value.strip()
                if value[0]=='T':
                    grades[int(value[-1])]=int(student[index+1].strip())
            for i in range(1, 5):
                if i not in grades:
                    grades[i]=0
                    
            some_list=list(grades.values())
            some_list.append(sum(some_list)/4)
            some_list.insert(0,student[1])
            output[student[0]]=some_list
                    
    return output 

file_name = 'student_grades.txt'
print(create_grades_dict(file_name))

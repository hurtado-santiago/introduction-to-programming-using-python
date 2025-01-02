def create_grades_dict (file_name):
    file_pointer = open(file_name, 'r')
    data = file_pointer.readlines()
    file_pointer.close()
    output={}

    for item in data:
        grades={}
        some_list=[]

        if item[0] != '#':
            student = item.strip().split(',')
            for index, value in enumerate(student):
                value=value.strip()
                if value[0]=='T':
                    grades[int(value[-1])]=int(student[index+1].strip())

            for i in range(1, 5):
                if i not in grades:
                    grades[i]=0

            ordered_keys=list(sorted(grades.keys()))
            for item in ordered_keys:
                some_list.append(grades[item])
            some_list.append(sum(some_list)/4)
            some_list.insert(0,student[1])
            output[student[0]]=some_list
    return(output)


def print_grades(file_name):
    grades_dict=create_grades_dict(file_name)
    print('{0:^10s} | {1:^16s} | {2:^6s} | {3:^6s} | {4:^6s} | {5:^6s} | {6:^6s} | '.format('ID', 'Name', 'Test_1', 'Test_2', 'Test_3', 'Test_4', 'Avg.'))

    sorted_list=sorted(grades_dict)
    for item in sorted_list:
        print('{0:<10} | '.format(item), end="")
        print('{0:<16} | '.format(grades_dict[item][0]), end="")
        print('{0:>6d} | '.format(grades_dict[item][1]), end="")
        print('{0:>6d} | '.format(grades_dict[item][2]), end="")
        print('{0:>6d} | '.format(grades_dict[item][3]), end="")
        print('{0:>6d} | '.format(grades_dict[item][4]), end="")
        print('{0:>6.2f} | '.format(grades_dict[item][5]))

    return None    
    


file_name = 'student_grades.txt'
print(print_grades(file_name))

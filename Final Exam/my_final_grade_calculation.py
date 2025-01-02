#name, q1, q2, q3, q4, q5, q6, a1, a2, a3, a4, midterm, final

def my_final_grade_calculation(filename):    
    grades={}
    file_pointer = open(some_file, 'r')
    data = file_pointer.readlines()
    file_pointer.close()

    for lines in data:
        assignments=[]
        quizzes=[]
        if lines[0] != '#':
            lines=lines.strip().split(',')

            for i in range (1, 7):
                quizzes.append(int(lines[i]))
            quizzes.sort()
            quizzes=quizzes[2:]
            avg_quizzes=sum(quizzes)/len(quizzes)

            for i in range (7, 11):
                assignments.append(int(lines[i]))
            assignments.sort()
            assignments=assignments[1:]
            avg_assignments=sum(assignments)/len(assignments)
                
            midterm=int(lines[11])
            final=int(lines[12])

            total_score=(avg_quizzes+avg_assignments+midterm+final)/4
            
            if total_score>=60:
                grades[lines[0].lower()]="pass"
            else:
                grades[lines[0].lower()]="fail"

    return(grades)


some_file = "my_final_grade_calculation.txt"
print(my_final_grade_calculation(some_file))

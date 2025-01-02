def spelling_corrector(s1,s2):
    s1_list=s1.lower().split()
    for index, item in enumerate(s1_list):
        for item_correct_spells in s2:
            result_mismatch = find_mismatch(item, item_correct_spells)
            result_insert_delete = single_insert_or_delete(item, item_correct_spells)
            if result_mismatch == 1 or result_insert_delete == 1:
                s1_list[index]=item_correct_spells.lower()
                break
        print(s1_list[index], end=" ")


def find_mismatch(s1, s2):
    new_s2=s2.lower()
    mismatches=0

    if len(s1) != len(new_s2):
       return 2

    for index in range(len(s1)):
        if s1[index] != new_s2[index]:
            mismatches+=1
            if mismatches>1:
                return 2
    return mismatches


def single_insert_or_delete(s1,s2):
    new_s2=s2.lower()
    mismatches=0

    if s1==s2:
        return 0
    if abs(len(s1)-len(new_s2))!=1:
        return 2
    
    if len(s1)>len(new_s2):
        for index in range(len(new_s2)):
            if s1[index]!=new_s2[index]:
                if s1[index+1:]==new_s2[index:]:
                    return 1
                else:
                    return 2
        return 1
    else:
        for index in range(len(s1)):
            if s1[index]!=new_s2[index]:
                if s1[index:]==new_s2[index+1:]:
                    return 1
                else:
                    return 2
        return 1

#first_string = 'Thes is the Firs cas'
#first_string = 'programing is fan and eesy'
first_string = 'Thes is vary essy'
#first_string = 'Wee lpve Pythen'
#correct_spells = ['that','first','case','car']
#correct_spells = ['programming','this','fun','easy','book' ]
correct_spells = ['this', 'is', 'very', 'very', 'easy']
#correct_spells = ['we', 'Live', 'In', 'Python']
spelling_corrector(first_string, correct_spells)

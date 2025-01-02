def single_insert_or_delete(s1,s2):
    new_s1=s1.lower()
    new_s2=s2.lower()
    mismatches=0

    if new_s1==new_s2:
        return 0
    if abs(len(s1)-len(s2))!=1:
        return 2
    
    if len(new_s1)>len(new_s2):
        for index in range(len(new_s2)):
            if new_s1[index]!=new_s2[index]:
                if new_s1[index+1:]==new_s2[index:]:
                    return 1
                else:
                    return 2
        return 1
    else:
        for index in range(len(new_s1)):
            if new_s1[index]!=new_s2[index]:
                if new_s1[index:]==new_s2[index+1:]:
                    return 1
                else:
                    return 2
        return 1

first_string = 'sin'
second_string = 'sink'
print(single_insert_or_delete(first_string, second_string))

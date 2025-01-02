def find_mismatch(s1, s2):
    new_s1=s1.lower()
    new_s2=s2.lower()
    mismatches=0

    if len(new_s1) != len(new_s2):
        return 2

    for index in range(len(new_s1)):
        if new_s1[index] != new_s2[index]:
            mismatches+=1
            if mismatches>1:
                return 2
    return mismatches
    
    

first_string = 'dog'
second_string = 'Dog'
print(find_mismatch(first_string, second_string))

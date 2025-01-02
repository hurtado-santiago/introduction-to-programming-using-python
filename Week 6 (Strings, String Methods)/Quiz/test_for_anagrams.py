def test_for_anagrams(s1, s2):
    new_s1=s1.lower()
    new_s2=s2.lower()

    if sorted(new_s1) == sorted(new_s2):
        return True
    else:
        return False
    
first_string = 'Listen'
second_string = 'Silent'
print(test_for_anagrams(first_string, second_string))

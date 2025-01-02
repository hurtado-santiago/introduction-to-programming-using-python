def find_gcd(my_list):
    result = my_list[0]
    for i in range(1, len(my_list)):
        print('i: ',i)
        result = my_gcd(result, my_list[i])
    return result
  
def my_gcd(a,b):
    while b:
        print('a1: ',a)
        print('b1: ',b)
        a, b = b, a%b
        print('a2: ',a)
        print('b2: ',b)
    return a
        

#a=[12, 24, 6, 18]
a=[3, 5, 9, 11, 13]
print(find_gcd(a))

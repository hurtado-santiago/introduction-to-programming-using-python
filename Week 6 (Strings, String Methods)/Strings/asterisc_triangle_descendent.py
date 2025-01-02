def asterisc_triangle_descendent(number):
    if number>2:
        print('*'*number)
    for x in range(number, 0, -1):
        if x>2 and x<number:
            print('*'+' '*(x-2)+'*')
        if x<3:
            print('*'*x)    


n = int(input('please enter a positive integer(1 to n): '))
asterisc_triangle_descendent(n)

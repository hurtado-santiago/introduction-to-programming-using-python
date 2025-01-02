def triangNumber(number):
    for x in range(1, number+1):
        print(str(x)*x)    


n = int(input('please enter a positive integer(1 to n): '))
numberTriag(n)

def calculate_fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1 
    else:
        return calculate_fibonacci(n-1)+calculate_fibonacci(n-2)


n=10
print(calculate_fibonacci(n))

n = int (input("Integer: "))
for creciente in range (1,n+1):
    print (creciente*"*")
    if creciente == n:
        while creciente != 1 :
            creciente = creciente - 1
            print (creciente*"*")


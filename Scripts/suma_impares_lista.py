def proc (x):
    odd = 0
    for search in x:
        if search % 2:
            odd = odd + search
    return odd

my_list = [1,3,1,5,1]
out = proc (my_list)
print (out)

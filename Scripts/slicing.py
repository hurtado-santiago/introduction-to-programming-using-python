def proc (lists):
    output = []
    size = len(lists)
    output.append (lists [0])
    for x in range (1, size):
        if x%2 == 0:
            output.append (lists [x])
    return output

mylist = ["we", "love", "python", "so","much"]
out = proc (mylist)
print (out)

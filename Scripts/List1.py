def proc (lista, cadena):
    new_list = []
    size = len(lista)
    new_list.append (lista[0])
    print (size)
    for x in range (1, 4):
        new_list.insert(x, cadena)
    for x in range (4, size):
        new_list.append (lista[x]) 
    return new_list
    
my_list=['python', 3.4, 54, 'java', 82, 'c', 7.4]
string = "Brahman"
out = proc (my_list, string)
print (out)
#print(my_list[0:-1:3])

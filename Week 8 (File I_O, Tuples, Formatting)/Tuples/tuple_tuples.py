import numpy as np

def tuple_tuples(some_dict):
    output=[]

    keys = tuple(some_dict.keys())
    items = tuple(some_dict.values())
    output.append(keys)
    output.append(items)              
    return tuple(output)

input_dictionary = {1:"a", 2:"b", 3:"c", 4:"d"} 
print(tuple_tuples(input_dictionary))

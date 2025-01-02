import numpy as np

def tuple_func(some_tuple):

    mean = sum(some_tuple)/len(some_tuple)
    median = np.median(np.array(some_tuple))            
    return(mean, median)

numbers = (3, 3, 0, 1, 12, 13, 15, 16)
result = tuple_func(numbers)
print(result)

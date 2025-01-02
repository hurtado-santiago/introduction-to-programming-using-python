import numpy as np

def multiply_vectors(l1, l2):
    np_l1 = np.array(l1)
    np_l2 = np.array(l2)
    output=np_l1.dot(np_l2)
    final_output=output.tolist()
    return final_output

   
a = [[2, 3, 4],
     [3, 4, 5]]
b = [[4, -3, 12],
     [1, 1, 5],
     [1, 3, 2]]
print(multiply_vectors(a, b))


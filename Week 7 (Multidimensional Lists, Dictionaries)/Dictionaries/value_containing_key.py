
def value_containing_key(some_dict, integer):
    result=[]
    
    for keys in some_dict:
        results=some_dict.get(keys)
        if integer in results:
            result.append(keys)
            result.sort()
    return result
                        
dicctionary = {"rabbit" : [1, 2, 3],
          "kitten" : [2, 2, 6],
          "lioness": [6, 8, 9]}
print(value_containing_key(dicctionary))

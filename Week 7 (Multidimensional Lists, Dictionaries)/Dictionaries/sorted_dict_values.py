def sorted_dict_values(some_dict):
    values = list(some_dict.values())
    values.sort()
    return values

dicctionary={'name':21, 'age':12}
print(sorted_dict_values(dicctionary))

def sorted_dict(some_dict):
    keys = list(some_dict.keys())
    keys = sorted(keys)
    return keys

dicctionary={'name':'papo', 'age':12}
print(sorted_dict(dicctionary))

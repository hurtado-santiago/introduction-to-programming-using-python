def formatted_print(some_dict):
    values = some_dict.values()
    values=sorted(values, reverse=True)
    keys=some_dict.keys()

    for value in values:
        for key in keys:
            if some_dict[key]==value:
                print('{0:<10s}  {1:>6.2f}'.format(key, value))

dictionary = {'john':34.480, 'eva':88.5, 'alex':90.55, 'tim': 65.900}
print(formatted_print(dictionary))

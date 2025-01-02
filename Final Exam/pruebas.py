def reverse_dictionary(some_dict):
    output={}

    values=sorted(some_dict.values())
    keys=sorted(some_dict.keys())
    
    for key in keys:
        for item in some_dict[key]:
            if item not in output.keys():
                output[item.lower()]=[key.lower()]
            else:
                output[item.lower()].append(key.lower())
                output[item.lower()]=sorted(output[item.lower()])
    return(output)


input_dict = {'Accurate': ['exact', 'precise'], 'exact': ['precise'], 'astute': ['Smart', 'clever'], 'smart': ['clever', 'bright', 'talented']}
print(reverse_dictionary(input_dict))

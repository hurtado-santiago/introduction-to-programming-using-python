def reverse_dictionary(some_dict):
    output={}
    
    for key in some_dict:
        for item in some_dict[key]:
            if item not in output.keys():
                output[item.lower()]=[key.lower()]
            else:
                output[item.lower()].append(key.lower())
                output[item.lower()].sort()
    return(output)


input_dict = {'Accurate': ['exact', 'precise'], 'exact': ['precise'], 'astute': ['Smart', 'clever'], 'smart': ['clever', 'bright', 'talented']}
print(reverse_dictionary(input_dict))

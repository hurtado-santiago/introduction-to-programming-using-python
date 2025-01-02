def handle_concatenation_error_sample(some_list, index, string):
    try:
        some_list[index] = string
    except (IndexError, TypeError):
        return some_list
    else:
        return some_list

print(handle_concatenation_error_sample([1, 2, 3, 4, 5], 4, 'santiago'))

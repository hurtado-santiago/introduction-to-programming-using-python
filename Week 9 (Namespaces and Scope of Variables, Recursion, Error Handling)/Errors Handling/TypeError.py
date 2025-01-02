def handle_concatenation_error_sample(unknown, string):
    try:
        result = unknown + string
    except TypeError:
        return None
    else:
        return result

print(handle_concatenation_error_sample(4.56, 'hola'))

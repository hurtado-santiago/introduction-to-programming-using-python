def handle_concatenation_error_sample(float_num, unknown):
    try:
        result = float_num / unknown
    except (ZeroDivisionError, TypeError):
        return None
    else:
        return result

print(handle_concatenation_error_sample(4, 1))

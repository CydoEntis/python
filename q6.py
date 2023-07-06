def check_numeric_value(wg_int):
    return isinstance(wg_int, int)

# Verify if the string is null

def check_null_string(wg_string):
    return wg_string is not None

if __name__ == '__main__':
    wg_string = "I like dogs."  # use keyword None to test
    wg_int = 12345

    print(check_null_string(wg_string))
    print(check_numeric_value(wg_int))
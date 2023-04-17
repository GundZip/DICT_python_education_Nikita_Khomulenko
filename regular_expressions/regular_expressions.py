def compare_strings(input_str):
    input_list = input_str.split('|')
    if len(input_list) != 2:
        return False
    left, right = input_list
    if len(left) != len(right):
        return False
    for i in range(len(left)):
        if left[i] != '.' and left[i] != right[i]:
            return False
    return True

print(compare_strings('apple|apple'))  # True
print(compare_strings('.pple|apple'))  # True
print(compare_strings('appl.|apple'))  # True
print(compare_strings('.....|apple'))  # True
print(compare_strings('peach|apple'))  # False
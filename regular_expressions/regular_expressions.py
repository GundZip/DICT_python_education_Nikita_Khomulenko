def match_char(regular_exp, string):
    if regular_exp == '':
        return True
    elif string == '':
        return False
    elif regular_exp == '.':
        return True
    else:
        return regular_exp == string

print(match_char('a', 'a'))  # True
print(match_char('.', 'a'))  # True
print(match_char('', 'a'))  # False
print(match_char('a', ''))  # False
print(match_char('', ''))  # True
print(match_char('|', ''))  # True
print(match_char('|', 'a'))  # True
print(match_char('a|a', 'a'))  # True
print(match_char('.|a', 'b'))  # False
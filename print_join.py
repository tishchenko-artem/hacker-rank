def print_and_join(string: str):
    '''You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.'''
    split = string.split()
    return '-'.join(split)

test = print_and_join("this is a string")
print(test)

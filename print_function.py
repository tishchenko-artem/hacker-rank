def print_numbers(n:int):
    '''Without using any string methods, try to print the following:
    "123***n"'''
    lst = []
    for el in range(1, n+1):
        lst.append(str(el))
    return ''.join(lst)

test = print_numbers(5)
print(test)
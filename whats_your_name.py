def print_full_name(first:str, last:str):
    '''You are given the firstname and lastname of a person on two different lines.
     Your task is to read them and print the following:
     "Hello firstname lastname! You just delved into python."'''
    return 'Hello {} {}! You just delved into python.'.format(first, last)


test = print_full_name('ross', 'Taylor')
print(test)
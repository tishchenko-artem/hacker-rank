def dev(a:int, b:int):
    '''The provided code stub reads two integers, a and b, from STDIN.
    Add logic to print two lines. The first line should contain the result of integer division, a // b.
    The second line should contain the result of float division, a / b.
    No rounding or formatting is necessary.'''
    c = a // b
    d = a / b
    return c, d


test = dev(3, 5)
print(test)
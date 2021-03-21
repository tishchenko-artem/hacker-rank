def if_else(n:int):
    '''Given an integer, , perform the following conditional actions:
    If  is odd, print Weird
    If  is even and in the inclusive range of 2 to 5, print Not Weird
    If  is even and in the inclusive range of 6 to 20, print Weird
    If  is even and greater than 20, print Not Weird'''
    if n % 2 != 0:
        return 'Weird'
    elif n % 2 == 0:
        if 2 < n < 5:
            return 'Not Weird'
        elif 6 < n <= 20:
            return 'Weird'
        elif n > 20:
            return 'Not Weird'


test = if_else(3)
test1 = if_else(24)
test2 = if_else(4)
print(test)
print(test1)
print(test2)
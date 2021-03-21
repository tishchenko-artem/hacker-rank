def arithmetic(a: int, b: int):
    '''The provided code stub reads two integers from STDIN, a and b. Add code to print three lines where:
    The first line contains the sum of the two numbers.
    The second line contains the difference of the two numbers (first - second).
    The third line contains the product of the two numbers.'''
    first_action = a + b
    second_action = a - b
    third_action = a * b
    return first_action, second_action, third_action

test = arithmetic(3, 5)
print(test)
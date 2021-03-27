def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    string = ''.join(l)
    return string

test = mutate_string('abracadabra', 5, 'k')
print(test)
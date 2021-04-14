def tup(n, n1):
    lst = []
    for el in n1:
        if el != ' ':
            lst.append(int(el))
        else:
            continue
    tup = (lst[0], lst[1])
    return hash(tup)


test = tup(2, '1 2')
print(test)
def solve(s: str):
    split = s.split()
    new_list = []
    for el in split:
        new_list.append(el.capitalize())
    return ' '.join(new_list)


test = solve('chris alan')
test1 = solve('hello   world  lol')
test2 = solve('132 456 Wq  m e')
test3 = solve(
    'q w e r t y u i o p a s d f g h j  k l z x c v b n m Q W E R T Y U I O P A S D F G H J  K L Z X C V B N M')
test4 = solve('1 2 2 3 4 5 6 7 8  9')
print(test)
print(test1)
print(test2)
print(test3)
print(test4)

def leap_or_not(year:int):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

test = leap_or_not(1990)
test1 = leap_or_not(2000)
test2 = leap_or_not(2300)
test3 = leap_or_not(1992)
print(test)
print(test1)
print(test2)
print(test3)
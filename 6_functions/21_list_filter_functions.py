def check(arg):
    if (arg % 3 == 0):
        return True
    else:
        return False

L = [1,2,3,4,10,123,22]
filtered = filter(check,L)
for s in filtered:
    print(s)

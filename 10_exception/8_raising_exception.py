try:
    a = input("enter a :") # A 4
    if not a.isnumeric():
        raise TypeError
    else:
        pass
except TypeError:
    print("ValueError: invalid literal for int()\
with base 10: ",a)
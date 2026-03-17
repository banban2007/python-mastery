try:
    a = 10/0
except ValueError:
    print("Please use b as interger value !")
except ZeroDivisionError:
    print("Please use b as greater than zero !")
else:
    print("else block call")
finally:
    print("finally block call")
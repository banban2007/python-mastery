try:
    a = int(input("Enter a: ")) #4 A
    b = int(input("Enter b:")) #0
    c = a/b
    print("a/b = ",c)
except (ZeroDivisionError,ValueError):
    print("Can't divide by zero please use as greater than zero !")
else:
    print("else block call")
    
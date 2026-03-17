try:
    a = int(input("Enter a: "))
    b = int(input("Enter b:"))
    c = a/b
    print("a/b = ",c)
except Exception:
    print("Can't divide by zero please use as greater than zero !")
    
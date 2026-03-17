try:
    a = int(input("Enter a :")) #4 A
    b = int(input("Enter b :")) # 0 2
    if b == 0:
        raise ArithmeticError
    else:
        pass
except ArithmeticError:
    print("ZeroDivisionError: division by zero ")

# ArithmeticError types in python include:OverFlowError,ZeroDivisionError,FolatingPointError
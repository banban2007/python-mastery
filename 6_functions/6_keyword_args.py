#positional args
def calculator(a1,b1,c1):
    return (a + b)*c

a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))
print("Result a,c,d = ",calculator(a1=a,b1=b,c1=c))
print("Result a,b,c = ",calculator(a1=a,c1=c,b1=b))

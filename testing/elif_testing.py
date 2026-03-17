age = int(input("Enter any age ?"))
if age > 85 and age <=100:
    print("Very Old")
elif age > 60 and age <=85:
    print("Old")
elif age > 40 and age <=60:
    print("Very Adult")
elif age > 30 and age <=40:
    print("Adult")
elif age > 20 and age <=30:
    print("Young")
elif age > 10 and age <=20:
    print("Teenger")
elif age >= 1 and age <=10:
    print("Child")
else:
    print("Invalid age !")                            
print("Welcome Quzi Game")

playing = input("Do you Want to play? Yes or NO ?")

if playing.lower() != "yes":
    quit()

print("Okay! Let play :")

Q = [
    {"quiz":"3 + 4 = ","Ans":3+4},
    {"quiz":"6 + 9 = ","Ans":6+9},
    {"quiz":"11 + 8 = ","Ans":11+8},
    {"quiz":"15 + 11 = ","Ans":15+11},
    {"quiz":"31 + 48 = ","Ans":31+48},
]
coa = 0
for i in Q:
    question = i['quiz']
    ans = i['Ans']
    answer = int(input(question))
    if answer == ans:
        print("Corrend answer")
        coa+= 1
    else:
        print("Incorrect! "+str(ans)+ " is correct Answer")

print("You correct "+str(coa)+" Answer !")
   
if coa > 3:
    print("Good Job")
elif coa == 3:
    print("Not Bad!")
else:
    print("You need more hardwork!")


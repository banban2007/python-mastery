#rock_paper_scissors

import random

options =["rock","paper","scissors"]
con = True
userpoint = 0
computerpoint = 0
match = 0

while(con):
    user_input = input("Type Rock,Paper,Scissors or q to Quit !").lower()

    if user_input =="q":
        quit()
    if user_input not in options:
        continue
    
    random_number = random.randint(0,2)
    computer_pick = options[random_number]
    print("computer Pick "+computer_pick)

    if user_input == "rock" and computer_pick == "scissors" or user_input == "paper" and computer_pick == "rock" or user_input == "scissors" and computer_pick == "paper":
        print("YOU Win")
        userpoint += 1
        match += 1
    elif user_input == computer_pick:
        print("Draw")
    else:
        print("Computer Win")
        computerpoint += 1
        match += 1

    if match == 5:
        con = False
        print("Your score = ",userpoint)
        print("Computer Score = ",computerpoint)
        if userpoint > computerpoint:
            print("You win !")
        else:
            print("Computer win !")

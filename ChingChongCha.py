import random

game_cards = ["paper","scissors","rock"]

compchoice = random.randint(0,2)

playerchoice = int(input("Please enter a number between 0,2 0 being Paper,1 being Scissor,2 being Rock "))


if playerchoice == 2:

    if compchoice == 1:
        print("You have won!")
    elif compchoice == 0:
        print("You have lost.")
    elif compchoice == 2:
        print("It is a draw")
        
if playerchoice == 0:

    if compchoice == 1:
        print("You have lost.")
    elif compchoice == 2:
        print("You have won!")
    elif compchoice == 0:
        print("It is a draw")

if playerchoice == 1:
   
    if compchoice == 0:
        print("You have won!")
    elif compchoice == 2:
        print("You have lost.")
    elif compchoice == 1:
        print("It is a draw")

# rock beat scissors 
# scissors beat paper 
# paper beat rock

import random


actions = ["Rock", "Paper", "Scissors"]

def init():

    print("====== Rock-Paper-Scissors Game =======")
    print("Welcome player")
    print("****** Rules of the Game ******")
    print("Take care to read the rules: \n You are to choose between R (Rock), P (Paper), or S (Scissors). ")
    print(" * Rock beats Scissors \n * Paper beats Rock \n * Scissors beats Paper. \n If two players choose the same character, it's a tie.")
    print("*********************************************")

    input_from_player()



def input_from_player():

    player_input = input("Pick an option: R (Rock), P (Paper) or S (Scissors) \n")
    

    while True:

        cpu_input = random.choice(actions)
        

        if(player_input == "R"):
            player_input = "Rock"
            print("Player (%s) : CPU (%s)" % (player_input, cpu_input))
            break
            
        elif(player_input == "P"):
            player_input = "Paper"
            print("Player (%s) : CPU (%s)" % (player_input, cpu_input))
            break

        elif(player_input == "S"):
            player_input = "Scissors"
            print("Player (%s) : CPU (%s)" % (player_input, cpu_input))
            break 
        else:
            print("Invalid option selected") 
            return input_from_player()        
            continue
    

    
    if(player_input == cpu_input):
        print("Players selected %s. It's a tie!" % player_input)
        input_from_player()

    elif(player_input == "Rock"):
        if(cpu_input == "Scissors"):
            print("Rock smashes scissors. You win!")
        else:
            print("Paper covers rock. CPU wins!")
        

    elif(player_input == "Paper"):
        if(cpu_input =="Rock"):
            print("Paper covers rock. You win!")
        else:
            print("Scissors cut paper. CPU wins")
    elif(player_input == "Scissors"):
        if(cpu_input == "Paper"):
            print("Scissors cuts paper. You win!")
        else: 
            print("Rock smashes scissors. CPU wins")

init()

    

        






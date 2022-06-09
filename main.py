
# A Dictionnary to store the options
options = {"R":"Rock", "P":"Paper", "S":"Scissors"}

# asking the user to pick an option between "R", "P" or "S"


def player_choice():

    isValidOptionSelected = False

    print("Welcome to our Rock-Paper-Scissors game \n")
    while isValidOptionSelected == False:
        player_option = input("Choose an option between R, P and S \n")
        
        if player_option in options.keys():
            isValidOptionSelected = True
            #cpu_choice()
            return player_option 
            print("good")
        else:
             print("You have selected invalid option")         

import random   
def cpu_choice():
    
    cpu_option = random.choice(list(options.keys()))
    return cpu_option
    #who_wins()

player_option = player_choice()

def winner():
    cpu_option = cpu_choice()
    if player_option == "R" and cpu_option =="S":
        print(f"Player ({options[player_option]}) : CPU ({options[cpu_option]})\n")
        print("YOU are the winner congratulations!\n")
    elif player_option == "R" and cpu_option =="P":
        print(f"Player ({options[player_option]}) : CPU ({options[cpu_option]})\n")
        print("The winner is the CPU you loose this time!\n")
    elif player_option == "R" and cpu_option =="R":
        print(f"Player ({options[player_option]}) : CPU ({options[cpu_option]})\n")
        winner()
    elif player_option == "P" and cpu_option =="S":
        print(f"Player ({options[player_option]}) : CPU ({options[cpu_option]})\n")
        print("The winner is the CPU you loose this time!\n")
    elif player_option == "P" and cpu_option =="R":
        print(f"Player ({options[player_option]}) : CPU ({options[cpu_option]})\n")
        print("YOU are the winner congratulations!\n")
    elif player_option == "P" and cpu_option =="P":
        print(f"Player ({options[player_option]}) : CPU ({options[cpu_option]})\n")
        winner()
    elif player_option == "S" and cpu_option =="R":
        print(f"Player ({options[player_option]}) : CPU ({options[cpu_option]})\n")
        print("The winner is the CPU you loose this time!\n")
    elif player_option == "S" and cpu_option =="P":
        print(f"Player ({options[player_option]}) : CPU ({options[cpu_option]})\n")
        print("YOU are the winner congratulations!\n")
    else :
        print(f"Player ({options[player_option]}) : CPU ({options[cpu_option]})\n")
        winner()

      

winner()





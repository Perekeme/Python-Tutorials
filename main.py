import random

# Rock, Paper, Scissors Game

# This are the options for the computer to choose from
options = ["rock", "paper", "scissors"] 

# This fn gets the users input and makes sure it is correct
def get_choices():
    computer_choice = random.choice(options) #sets a random answer for the computer
    player_choice = input("Enter a choice (rock,paper,scissors):")
    if player_choice == "rock":
        choices = {"player": player_choice, "computer": computer_choice} #stores in the choices dict
    elif player_choice == "paper":
        choices = {"player": player_choice, "computer": computer_choice}
    elif player_choice == "scissors":
        choices = {"player": player_choice, "computer": computer_choice}
    else:
        player_choice = "None" # for when the input is wrong, None is stored in the choices dict instead
        choices = {"player": player_choice, "computer": computer_choice}
    return choices
    

def check_win(player, computer):
    result=""
    if player != 'None': # checking if user input is correct
        print(f" you chose  {player}  and Computer chose {computer}")
        if player == computer:
            result= "Draw"
        elif player == "rock" and computer == "paper":
            result= "you lose"
        elif player == "paper" and computer == "scissors":
            result= "you lose"
        elif player == "scissors" and computer == "rock":
            result= "you lose"
        else:
            result= "you win"
        return result
    return "Choose between rock paper or scissors"


answers = get_choices() # store choices as answers
# print(answers)     
# # for debugging

print(check_win(answers["player"], answers["computer"]))  # run game


# (fixed)  this code has bug that makes any input other than the intended ones to allow the user to win
# the code has been updated to solve the problem above. random inputs wont make u win
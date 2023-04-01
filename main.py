import random


options =["rock", "paper", "scissors"]

def get_choices():
    player_choice = input("Enter a choice (rock,paper,scissors):")
    if player_choice == "rock":
        computer_choice = random.choice(options)
        choices= {"player":player_choice,"computer":computer_choice}
        return choices
    elif player_choice== "paper":
        computer_choice = random.choice(options)
        choices= {"player":player_choice,"computer":computer_choice}
        return choices
    elif player_choice== "scissors":
        computer_choice = random.choice(options)
        choices= {"player":player_choice,"computer":computer_choice}
        return choices
    else:
        print("Choose between rock paper or scissors")
        break

def check_win(player, computer):
    print(f" you chose  {player}  and Computer chose {computer}")
    if player == computer:
        return "Draw"
    elif player=="rock" and computer == "paper":
        return "you lose"
    elif player=="paper" and computer == "scissors":
        return "you lose"
    elif player=="scissors" and computer == "rock":
        return "you lose"
    else:
        return "you win"
answers= get_choices()

print(check_win(answers["player"], answers["computer"]))
print(type("player_choicefd") == str)

# this code has bug that makes any input other than the intended ones to allow the user to win



 
 
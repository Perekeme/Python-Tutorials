import random

options =["rock", "paper", "scissors"]

def get_choices():
    player_choice = input("Enter a choice (rock,paper,scissors):")
    computer_choice = random.choice(options)
    choices= {"player":player_choice,"computer":computer_choice}
    return choices

# print(get_choices())

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





 
 
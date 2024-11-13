import random

win_count = 0
lose_count = 0
running = True
options = ['rock', 'paper', 'scissors']

def endGame():
    print(f"You won {win_count} times and lost {lose_count} times!")


def getUserInput():
    user_input = input("Type 1 for rock, 2 for paper, 3 for scissors ")
    if user_input not in ['0', '1', '2']:
        print("Invalid input. Please enter 1, 2, or 3.")
    elif (user_input == 'e'):
        endGame()
    else:
        return int(user_input)
    
def getComputerInput():
    return random.randint(0, 2)

def checkWin(computer_input, user_input):
    print(win_options[(computer_input - user_input) % 3])

while running == True:
    win_options = ['tie', 'win', 'loss']
    user_input = getUserInput()
    computer_input = getComputerInput()
    checkWin(computer_input, user_input)





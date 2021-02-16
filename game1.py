# Simple rock-paper-scissors game

import random

print('\nWelcome to Rock-Paper-Scissors game\n')
rounds = int(input("Please enter how many rounds would you like to play: "))

options = ['rock','paper','scissors']
flag = True
count = 0
score_player = 0
score_pc = 0


while flag:

    for i in range(rounds):

        print('\nPick one of the options below to play!')
        player = input('Rock, Paper or Scissors?: ').lower()
        pc = random.choice(options)

        if player == pc:
            print(f"It's a draw, You and pc both picked {player}")
            score_player += 0.5
            score_pc += 0.5
            count += 1

        elif (player == 'rock') and (pc == 'paper'):
            print(f"Pc won, You picked {player}, pc picker {pc}")
            score_player += 0
            score_pc += 1
            count += 1

        elif (player == 'rock') and (pc == 'scissors'):
            print(f"You won, You picked {player}, pc picker {pc}")
            score_player += 1
            score_pc += 0
            count += 1

        elif (player == 'scissors') and (pc == 'paper'):
            print(f"You won, You picked {player}, pc picker {pc}")
            score_player += 1
            score_pc += 0
            count += 1

        elif (player == 'scissors') and (pc == 'rock'):
            print(f"PC won, You picked {player}, pc picker {pc}")
            score_player += 0
            score_pc += 1
            count += 1

        elif (player == 'paper') and (pc == 'rock'):
            print(f"You won, You picked {player}, pc picker {pc}")
            score_player += 1
            score_pc += 0
            count += 1

        elif (player == 'paper') and (pc == 'scissors'):
            print(f"PC won, You picked {player}, pc picker {pc}")
            score_player += 0
            score_pc += 1
            count += 1

        print(f"\nScore is: player: {score_player}, pc: {score_pc}")
        
        # Ask if the player wants to continue after every 5 games 
        if count == 5:
            to_continue = input("Would you like to continue? [y/n]")
            if to_continue == 'n':
                flag = False
                print("\nThanks for playing!")
            else:
                count = 0
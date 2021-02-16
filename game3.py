# Rock-paper-scissors game
import random
import math

print("\nWelcome to the rock-paper-scissors game!\n")


while True: 

    # Ask for user input
    user = input("\nChoose between 'rock', 'scissors' and 'paper':   ")
    user_choice = user.lower()
    # PC makes random choice
    pc_choice = random.choice(['rock', 'scissors', 'paper'])

    print("\n - User has chosen '{}'".format(user_choice))
    print(" - PC has chosen '{}'\n".format(pc_choice))

    # Get the indexes from inputs
    choice_dict = {'rock': 0, 'paper': 1, 'scissors': 2}
    user_index = choice_dict.get(user_choice,3)
    pc_index = choice_dict.get(pc_choice,3) # Can leave default value for return


    res_matrix =[[0,2,1],
                [1,0,2],
                [2,1,0],
                [3,3,3]]

    res_idx = res_matrix[user_index][pc_index]
    res_messages = ['It is a tie!', 'Player wins!', 'PC wins!']
    # 0 = tie, 2 = loss, 1 = win, 3 = invalid input by user

    print(f"{res_messages[res_idx]}\n")

    to_continue = input('Do you wish to continue? (y/n)   ')
    if to_continue == 'n':
        break
import random
import math

n = int(input("Please enter how many games would you like to play: "))

def game():
    
    user = input("Please pick one, 'r' for rock,'p' for paper or 's' for scissors: ")
    user = user.lower() # lowercase the user input
    pc = random.choice(['r', 's', 'p'])

    if user == pc: 
        return (0, user, pc)
        # return f"It's a draw, You and pc both picked {user}"

    if is_win(user, pc):
        return (1, user, pc)
        # print("You picked '{}' and the pc picked '{}'. You won!".format(user, pc))
    
    # print("You have chosen {} and the pc chose {}, therefore you have lost".format(user, pc))
    return (-1, user, pc)

def is_win(user,pc):
    # Return ture if the user has won
    if (user == 'r' and pc == 's')\
        or(user == 's' and pc == 'p')\
        or (user=='p' and pc == 'r'):
        return True
    return False

def play_best_of(n):
    # Winner is determined once the best of n games have been won by one player
    user_score = 0
    pc_score = 0
    wins_necessary = math.ceil(n/2)

    while (user_score < wins_necessary) and (pc_score < wins_necessary):
        result, user, pc = game()
        if result == 0: # A Draw
            print("It's a draw. Both players chose {}.\n".format(user))
        elif result == 1: # user has won
            print("User has won this round!\n")
            user_score += 1
        else: # PC has won
            print("Pc has won this round!\n")
            pc_score += 1
    
    # Determine the winner
    if user_score > pc_score:
        print("You have won the best of {} games!".format(n))
    else:
        print("Unfortunately computer has won!")

play_best_of(n)

# if __name__ == '__main__':
#     print(play_best_of(5))
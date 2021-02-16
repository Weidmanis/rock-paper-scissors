# Rock-Paper-Scissors Game

## 3 seperate versions of the code: 

    - game1.py: Simple code with If/else loop. 
  
        -  Keeps the count of points for both, player and the pc
        -  After every 5 games it askes if the user wants to continue playing
  
    - game2.py: Sligthly more sophisticated code, mainly using functions
  
        - Asks the user to enter the number for games to be played
        - Then using fcn is_win() determine if user has won the round
        - Keep the count of who's won majority of the rounds
        - Determine the winner at the end

    - game3.py: Code does not use if statements for the game (note there is only on if statement used to exit the game if user no longer wishes to play)

        - First User inputs the choice for the round
        - PC input is generated
        - Both choices are indexed, and both indexes return an int from results_matrix wich determines if the round is tie, won or lost for the user. 
        - Results matrix is simple nested list variable
        - Rows = ['Rock', 'Paper', 'Scissors','Invalid']
        - Columns = ['Rock', 'Paper', 'Scissors']
        - Code also deals with Invalid User inputs
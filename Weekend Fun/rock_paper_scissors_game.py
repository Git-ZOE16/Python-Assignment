#Pseudocode:
    #Step1. Enter the choice of Player1, and Player2 to  ("rock", "paper", or "scissors").
    #Step2. Check if both players chose the same thing. If they did, it's a "Tie".
    #Step3. If their choices are different, use a nested if-else statement to compare Player 1's choice against Player 2's choice to see who wins.


player1 = input("Player 1, enter rock, paper, or scissors: ")
player2 = input("Player 2, enter rock, paper, or scissors: ")

if player1 == player2:
    print("Tie")
else:
     
    if player1 == "rock":
        if player2 == "scissors":
            print("Player 1 wins")
        else:
            print("Player 2 wins")
            
    
    elif player1 == "paper":
        if player2 == "rock":
            print("Player 1 wins")
        else:
            print("Player 2 wins")
            
    
    elif player1 == "scissors":
        if player2 == "paper":
            print("Player 1 wins")
        else:
            print("Player 2 wins")

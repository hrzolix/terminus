print("Rock...")
print("Paper...")
print("Scissors...")

player1 = input("Player1, make your move: ")
player2 = input("Player2, make your move: ")

if player1 == "rock" and player2 == "scissors":
    print("player1 wins!")
elif player1 == "rock" and player2 == "paper":
    print("player2 wins!")
elif player1 == "paper" and player2 == "rock":
    print("player1 wints!")
elif player1 == "paper" and player2 == "scissors":
    print("It's a tie!")
elif player1 == player2:
    print("It's a tie!")
else:
    print("Something went wrong!")
#XOX
#source code of xox
import xoxCore

gameBoard = [" "]*9
game_over = False
game_tied = False
user_turn = 0
winner = ""



#display introduction
xoxCore.display_intro()

#choosing the first player's sign 1 or 2. if 1:x, 2:o
user_turn = xoxCore.choose_sign()

#game

while not game_over and not game_tied:

	#check whick user plays
	if user_turn == 1:

		#take input move
		user_input = xoxCore.take_input("Player X")

		if gameBoard[user_input] != " ":
			print("Please enter an empty location.")
			continue
		gameBoard[user_input] = "X"
		xoxCore.display_board(gameBoard)

		#check if the game is over
		game_over = xoxCore.check_winner(gameBoard)
		if game_over:
			print("Congratulations! Player X has won the game!")
			break
		#check if the game is tied
		game_tied = xoxCore.check_tie(gameBoard)

		if game_over:
			winner = "X"

		#switch user turn
		user_turn = 2

	if user_turn == 2:

		#take input move
		user_input = xoxCore.take_input("Player O")

		if gameBoard[user_input] != " ":
			print("Please enter an empty location.")
			continue
		gameBoard[user_input] = "O"
		xoxCore.display_board(gameBoard)

		#check if the game is over
		game_over = xoxCore.check_winner(gameBoard)
		if game_over:
			print("Congratulations! Player O has won the game!")
			break
		#check if the game is tied
		game_tied = xoxCore.check_tie(gameBoard)

		if game_over:
			winner = "O"

		#switch user turn
		user_turn = 1

if game_tied and winner == 0:
	print("The game is tied!")






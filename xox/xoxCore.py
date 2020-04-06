#xox game functions

def display_board(gameBoard):
	#printing game board

	print " {} | {} | {} ".format(gameBoard[6],gameBoard[7],gameBoard[8])
	print "-----------"
	print " {} | {} | {} ".format(gameBoard[3],gameBoard[4],gameBoard[5])
	print "-----------"
	print " {} | {} | {} ".format(gameBoard[0],gameBoard[1],gameBoard[2])

def display_intro():
	#printing introduction of the game

	print("WELCOME TO XOX GAME")
	print("by Eda Bahar")

	game_start = int(input("Please press 1 to start the game.\n"))
	while game_start != 1:
		game_start = int(input("Please press 1 to start the game.\n"))

	print("This is the map of the game.")
	print("\n")
	print(" '7' | '8' | '9' ")
	print("-----------")
	print(" '4' | '5' | '6' ")	
	print("-----------")
	print(" '1' | '2' | '3' ")
	print("\n")
	print("In your turn, you should enter the location.")

def check_tie(gameBoard):
	#checking if the game tied or not

	if not " " in gameBoard:
		return True

def take_input(player):
	#taking the move of players
	try:
		location = int(input(player + " please enter your move: "))
	except ValueError:
		print("err")
	return location-1

def choose_sign():
	sign = ""
	while sign != "o" and sign != "x":
		sign = raw_input("First player, please choose your sign(X/O): ")
		if sign == "x":
			return 1
		elif sign == "o":
			return 2
		else:
			print("Please choose X or O!")
			continue

def check_winner(gameBoard):
	# horizontal
	for i in range(0,7,3):
		if gameBoard[i] == gameBoard[i+1] and gameBoard[i+1] == gameBoard[i+2] and gameBoard[i] != " ":
			return True
	#vertical
	for j in range(3):
		if gameBoard[j] == gameBoard[j+3] and gameBoard[j+3] == gameBoard[j+6] and gameBoard[j] != " ": 
			return True
	#cross-overs
	if gameBoard[0] == gameBoard[4] and gameBoard[4] == gameBoard[8] and gameBoard[0] != " ":
		return True
	elif gameBoard[2] == gameBoard[4] and gameBoard[4] == gameBoard[6] and gameBoard[2] != " ":
		return True
	else:
		return False

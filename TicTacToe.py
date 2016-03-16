# Validate User Input
def moveCheck(arr, move):
	# Check if not a number
	try:
		int(move)
	except:
		print('Please enter a valid number')
		return False
	#  Check if in board range
	if int(move) > 8:
		print('Please enter a valid board position (0-8)')
		return False
	# Check if move already taken
	for item in arr:
		if move == item:
			print('Spot %s is Already Taken, Sorry' %(move))
			return False	
	return True

# Start The Game
def playGame(moves=0, turn=True):
	moveCount = moves
	playerTurn = turn
	pastMoves = []
	gameBoard = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
	# Build the empty board to start the game
	print(gameBoard[0] + ' | ' + gameBoard[1] + ' | ' + gameBoard[2] + '\n' + '---------' + '\n' + gameBoard[3]
	      + ' | ' + gameBoard[4] + ' | ' + gameBoard[5] + '\n' + '---------' + '\n' + gameBoard[6]
	      + ' | ' + gameBoard[7] + ' | ' + gameBoard[8])

	while moveCount < len(gameBoard):
	    position = input('Please enter the position of your move: ')

	    # Prevent user from inputting a space already occupied...maybe use try catch instead here?  nested while loops are scary
	    while moveCheck(pastMoves, position) == False:
	    	position = input('Please enter the position of your move: ')

	    pastMoves.append(position);

	    # Toggle player turn with boolean
	    if playerTurn == True:
	        letter = 'X'
	    else:
	        letter = 'O'
	    
	    # Change turn to next player and track number of moves so can track game end
	    playerTurn = not playerTurn
	    moveCount = moveCount + 1
	    
	    # replace empty string with user letter
	    gameBoard[int(position)] = letter

	    print(gameBoard[0] + ' | ' + gameBoard[1] + ' | ' + gameBoard[2] + '\n' + '---------' + '\n' + gameBoard[3]
	          + ' | ' + gameBoard[4] + ' | ' + gameBoard[5] + '\n' + '---------' + '\n' + gameBoard[6]
	          + ' | ' + gameBoard[7] + ' | ' + gameBoard[8])
	else:
		# When game ends allow replay option
	    replay = input('Game Over, replay [yes, no]?: ')
	    if replay == 'yes':
	        playGame()
	    elif replay == 'no':
	        print('Thanks for playing!')
	    else:
	    	print('Invalid input, ending game')

# Start Initial Game of Tic Tac Toe
playGame()







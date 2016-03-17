def generateBoard(l):
    board = []
    for i in range(0,7,3):
        if i != 6:
            bottomLine = '---------'
        else:
            bottomLine = '' 
        print(l[i] + ' | ' + l[i+1] + ' | ' + l[i+2] + '\n' + bottomLine)

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

def checkForWinner(board):
    #Logic to check game for winner,probably a pretty important aspect of this project
    print('Check for winner')


# Start The Game
def playGame(moves=0, turn=True):
    moveCount = moves
    playerTurn = turn
    pastMoves = []
    gameBoard = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

    # Build the empty board to start the game
    generateBoard(gameBoard)

    while moveCount < len(gameBoard):
        # Check for a winner if more than 4 total moves have been made
        if moveCount > 4:
            checkForWinner(gameBoard)

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

        generateBoard(gameBoard)
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


# TODO: Forgot the win condition!!!! duh...




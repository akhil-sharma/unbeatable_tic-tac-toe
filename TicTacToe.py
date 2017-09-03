'''
TIC TAC TOE : Min - Max
'''
import math

def printBoard(board):
	print(board[0] + ' | ' + board[1] + ' | ' + board[2])
	print("--+---+--")
	print(board[3] + ' | ' + board[4] + ' | ' + board[5])
	print("--+---+--")
	print(board[6] + ' | ' + board[7] + ' | ' + board[8])
	print(emptyIndices(board))

def resetBoard():
	##implementing the board using a dictionary
	board = {0:' ',1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' '}
	return board

##return th list of empty spots on the board
def emptyIndices(board):
	emptyIndexList = [];
	for k, v in board.items():
		if(v == ' '):
			emptyIndexList.append(k)
	return emptyIndexList;

def winning(board, player):
	if (board[0] == board[1] == board[2] == player or
		board[3] == board[4] == board[5] == player or
		board[6] == board[7] == board[8] == player or
		board[0] == board[3] == board[6] == player or
		board[1] == board[4] == board[7] == player or
		board[2] == board[5] == board[8] == player or
		board[0] == board[4] == board[8] == player or
		board[2] == board[4] == board[6] == player):
		return True
	else:
		return False

def getPlayerMove(board):
	##let the player make his move
	move = -1
	while move not in emptyIndices(board):
		print('\nWhat is your next move ?\n')
		move = int(input())
	return move

def getBoardCopy(board):
	dupeBoard = board.copy()
	return dupeBoard

def makeMove(board, turn, move):
	##TODO: update the board
	board[move] = turn

def getComputerMove(board):
	dupBoard = getBoardCopy(board)
	print("\nCalculating the future...\n")
	bestMove = minmax(dupBoard, "O")
	return bestMove['index']

def minmax(board, player):
	##available spots
	availSpots = emptyIndices(board);
	##Scores for terminal positions
	if (winning(board, "X")):
		return {'score':-10}
	elif (winning(board, "O")):
		return {'score':10}
	elif (len(availSpots) == 0):
		return {'score':0}
	##list to collect all the dict objects
	moves = []
	##loop through all the available spots
	for spot in availSpots:
		move = {'index':spot}
		##set the empty spot to current player
		board[spot] = player
		##collect the score resulting from minmax
		if player == "O":
			result = minmax(board, "X")
			move['score'] = result['score']
		else:
			result = minmax(board, "O")
			move['score'] = result['score']
		##reset the spot to empty
		board[spot] = ' '
		moves.append(move)
	##if it is the computer's turn loop over the moves
	##and choose the move with the highest score
	if(player == "O"):
		bestScore = -10000
		for move in moves:
			if move['score'] > bestScore:
				bestScore = move['score']
				bestMove = move
	else:
		bestScore = 10000
		for move in moves:
			if move['score'] < bestScore:
				bestScore = move['score']
				bestMove = move
	##print(bestMove)
	return bestMove

def playAgain():
# This function returns True if the player wants to play again, otherwise it returns False.
	print('Do you want to play again? (yes or no)')
	return input().lower().startswith('y')


def main():
	print('Wecome to Tic Tac Toe')
	while True:
		#reset the board
		board = resetBoard()
		##human player
		human = 'X'
		##computer 
		artificial = 'O'
		#who goes first
		turn = human
		print("\nHuman goes first (X)\n\n")
		gameIsPlaying = True

		while gameIsPlaying:
			if turn == human:
				##humans turn
				printBoard(board)
				move = getPlayerMove(board)
				makeMove(board, turn, move)

				if winning(board, turn):
					printBoard(board)
					print('Hooray! YOU have won the game!\n--------------------------')
					gameIsPlaying = False
				else:
					if len(emptyIndices(board)) == 0:
						printBoard(board)
						print("It was a DRAW!\n-------------------------------")
						break
					else:
						turn = artificial
			else:
				##computers turn
				move = getComputerMove(board)
				print("\n" + str(move) + "\n")
				makeMove(board, turn, move)
				if winning(board, turn):
					printBoard(board)
					print('THE MACHINE has won the game!\n---------------------------')
					gameIsPlaying = False
				else:
					if len(emptyIndices(board)) == 0:
						printBoard(board)
						print("It was a DRAW!\n---------------------------")
						break
					else:
						turn = human
		if not playAgain():
			break


if __name__ == '__main__':
	main()

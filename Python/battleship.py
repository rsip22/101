from random import randint

board = []

for i in range(5):
	board.append(["O"] * 5)

def print_board(board):
	for row in board:
		print " ".join(row)

def random_row(board):
	return randint(0, len(board) - 1)

def random_col(board):
	return randint(0, len(board) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

for turn in range(4):
	print "Turn ", turn+1
	g_row = raw_input("Guess row: ")
	g_col = raw_input("Guess col: ")
	try:
		guess_row = int(g_row)
		guess_col = int(g_col)
		if guess_col == ship_col and guess_row == ship_row:
			board[guess_row][guess_col] = "X"
			print "Congratulations! You sank my battleship!"
		    	break 
		elif board[guess_row][guess_col] == "X":
			print "You guessed that one already."
		else:
			if guess_col not in range(5) or guess_row not in range(5):
				print "Oops, that's not even in the ocean."
				print_board(board)
			else:
				print "You missed my battleship!"
				board[guess_row][guess_col] = "X"
				print_board(board)
				if turn == 4:
					print "Game Over"
	except:
		print "Please enter a number!"

print "Ship row: ", ship_row
print "Ship col: ", ship_col
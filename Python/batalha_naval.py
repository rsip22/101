# -*- coding: utf-8 -*-

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
	print "Vez ", turn+1
	g_row = raw_input("Chute uma linha: ")
	g_col = raw_input("Chute uma coluna: ")
	try:
		guess_row = int(g_row)
		guess_col = int(g_col)
		if guess_col == ship_col and guess_row == ship_row:
			board[guess_row][guess_col] = "X"
			print "Parabéns! Você afundou meu navio!"
		    	break 
		elif board[guess_row][guess_col] == "X":
			print "Você já adivinhou esse."
		else:
			if guess_col not in range(5) or guess_row not in range(5):
				print "Oops, isso sequer é no oceano."
				print_board(board)
			else:
				print "Você errou meu navio!"
				board[guess_row][guess_col] = "X"
				print_board(board)
				if turn == 4:
					print "Game Over"
	except:
		print "Por favor, coloque um número!"

print "Linha do navio: ", ship_row
print "Coluna do navio: ", ship_col
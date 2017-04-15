import os
import sys
import random

theBoard = {'top-L':' ','top-M':' ', 'top-L':' ','top-R':' ','mid-L':' ', 'mid-M':' ', 'mid-L':' ','mid-R':' ', 'low-L':' ', 'low-M':' ', 'low-R':' '}

def printBoard(board):
	print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
	print('-+-+-')
	print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
	print('-+-+-')
	print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
	print('-+-+-')

turn ='X'
for i in range(9):
	printBoard(theBoard)
	print('Turn for '+ turn + '. Move on which space?')
	move = input()
	theBoard[move] = turn
	if turn == 'X':
		turn = 'O'
	else:
		turn = 'X'
printBoard(theBoard)


print('\n'*3)
print('Nested dictionary and lists')
print('\n'*3)

allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
'Bob': {'ham sandwiches': 3, 'apples': 2},
'Carol': {'cups': 3, 'apple pies': 1}}
def totalBrought(guests, item):
	numBrought = 0
	for k, v in guests.items():
		numBrought = numBrought + v.get(item, 0)
	return numBrought
print('Number of things being brought:')
print(' - Apples' + str(totalBrought(allGuests,'apples')))
print(' - Cups' + str(totalBrought(allGuests,'cups')))
print(' - Cakes' + str(totalBrought(allGuests,'cakes')))
print(' - Ham Sandwiches ' + str(totalBrought(allGuests,'ham Sandwiches')))
print(' - Apple Pies' + str(totalBrought(allGuests,'Apple Pies')))


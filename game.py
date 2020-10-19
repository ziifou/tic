import random
#Global variables
board = ['-','-','-',
         '-','-','-',
         '-','-','-']

def printBoard():
  for i in range(9):
    if(i == 3 or i == 6):
      print()
    print(f' {board[i]} |', end="")
  print()

def checkRow(board, val):
  if(val == 0 or val == 3 or val == 6):
    return board[val] == board[val+1] == board[val+2] != '-'
  elif (val == 1 or val == 4 or val == 7):
    return board[val] == board[val + 1] == board[val - 1] != '-'
  else:
    return board[val] == board[val - 1] == board[val - 2] != '-'

#check column

def checkCol(board, val):
  if(val == 0 or val == 1 or val == 2):
    return board[val] == board[val + 3] == board[val + 6] != '-'
  elif (val == 3 or val == 4 or val == 5):
    return board[val] == board[val - 3] == board[val + 3] != '-'
  else:
    return board[val] == board[val - 3] == board[val - 6] != '-'

# check checkDiago
def checkDiago(board, val):
  if val == 0 or val == 8:
    return board[0] == board[4] == board[8] != '-'
  elif val == 2 or val == 6:
    return board[2] == board [4] == board[6] != '-'
  elif val == 4:
    return board[0] == board[4] == board[8] != '-' or board[2] == board [4] == board[6] != '-'


#check for winner
def checkWin(board,val):
  row = checkRow(board,val)
  col = checkCol(board,val)
  diag = False
  if val == 0 or val == 2 or val == 6 or val == 8 or val == 4:
    diag = checkDiago(board,val)
  if row or col or diag:
    return True
  return False

# check game
def checkGame(board, val, str):
  if checkWin(board, val):
    print(f'{str} Win!')
    return True
  if not '-' in board:
    print('Game Over')
    return True
 
while(True):
  try:
    print('X turn')
    printBoard()
    val = int(input('enter a position between 1 and 9  :')) - 1
    if val < 0 or val > 9 or board[val] != '-':
      raise ValueError('')
    board[val] = 'X'
    printBoard()
    #check if win or game over
    if checkGame(board,val, 'You'):
      break
    # O turn
    print("O turn")
    computer = random.randint(0,8)
    while(board[computer] != '-'):
      computer = random.randint(0,8)
    board[computer] = 'O'
    printBoard()
    if checkGame(board,computer,'Computer'):
      break

  except ValueError:
    print('please enter a position between 1 and 9  :')





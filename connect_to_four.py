'''
Have the function ConnectFourWinner(strArr) read
the strArr parameter being passed which will represent a 6x7 Connect Four board.
The rules of the game are: two players alternate turns and place a colored disc
down into the grid from the top and the disc falls down the column until it hits
the bottom or until it hits a piece beneath it. The object of the game is to connect
four of one's own discs of the same color next to each other vertically, horizontally,
or diagonally before your opponent. The input strArr will represent a Connect Four board
and it will be structured in the following format: ["R/Y","(R,Y,x,x,x,x,x)","(...)","(...)",...)]
where R represents the player using red discs, Y represents the player using yellow discs and x
represents an empty space on the board. The first element of strArr will be either R or Y and it
represents whose turn it is. Your program should determine, based on whose turn it is, whether a
space exists that can give that player a win. If a space does exist your program should return the
space in the following format: (RxC) where R=row and C=column. If no space exists, return the string none.
The board will always be in a legal setup.'''

import copy

def ConnectFourWinner(strArr):

  player = strArr[0]

  board = [x[1:-1].split(',') for x in strArr[1:]]

  m = len(board)
  n = len(board[0])

  for i in range(n):
    move = findSpace(board, m, n, player, i)
    newBoard = copy.deepcopy(board)
    newBoard[move][i] = player
    if checkForWinner(newBoard, m, n, player):
      return '(%dx%d)' % (move + 1, i + 1)

  return 'none'


def findSpace(board, m, n, player, pos):
  if board[0][pos] != 'x': return 0
  for i in range(1, m):
    if board[i][pos] != 'x':
      return i-1
  return m-1

def checkForWinner(board, m, n, player):

  winStr = (player * 4)

  for row in board:
    strRow = ''.join(row)
    if winStr in strRow:
      return True

  for col in range(n):
    colStr = ''
    for row in range(m):
      colStr += board[row][col]
    if winStr in colStr:
      return True

  diags = [[(2,0),(3,1),(4,2),(5,3)],
          [(1,0),(2,1),(3,2),(4,2),(5,3)],
          [(0,0),(1,1),(2,2),(3,3),(4,4),(5,5)],
          [(0,1),(1,2),(2,3),(3,4),(4,5),(5,6)],
          [(0,2),(1,3),(2,4),(3,5),(4,6)],
          [(0,3),(1,4),(2,5),(3,6)],
          [(0,3),(1,2),(2,1),(3,0)],
          [(0,4),(1,3),(2,2),(3,1),(4,0)],
          [(0,5),(1,4),(2,3),(3,2),(4,1),(5,0)],
          [(0,6),(1,5),(2,4),(3,3),(4,2),(5,1)],
          [(1,6),(2,5),(3,4),(4,3),(5,2)],
          [(2,6),(3,5),(4,4),(3,5)]]

  for diag in diags:
    diaStr = ''
    for d in diag:
      diaStr += board[d[0]][d[1]]
    if winStr in diaStr:
      return True

  return False

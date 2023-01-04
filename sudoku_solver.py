import time

def hardcode_values(sudoku_board):
  sudoku_board[0][0]['text'] = "5"
  sudoku_board[0][1]['text'] = "3"
  sudoku_board[0][2]['text'] = ""
  sudoku_board[0][3]['text'] = ""
  sudoku_board[0][4]['text'] = "7"
  sudoku_board[0][5]['text'] = ""
  sudoku_board[0][6]['text'] = ""
  sudoku_board[0][7]['text'] = ""
  sudoku_board[0][8]['text'] = ""
  
  sudoku_board[1][0]['text'] = "6"
  sudoku_board[1][1]['text'] = ""
  sudoku_board[1][2]['text'] = ""
  sudoku_board[1][3]['text'] = "1"
  sudoku_board[1][4]['text'] = "9"
  sudoku_board[1][5]['text'] = "5"
  sudoku_board[1][6]['text'] = ""
  sudoku_board[1][7]['text'] = ""
  sudoku_board[1][8]['text'] = ""
  
  sudoku_board[2][0]['text'] = ""
  sudoku_board[2][1]['text'] = "9"
  sudoku_board[2][2]['text'] = "8"
  sudoku_board[2][3]['text'] = ""
  sudoku_board[2][4]['text'] = ""
  sudoku_board[2][5]['text'] = ""
  sudoku_board[2][6]['text'] = ""
  sudoku_board[2][7]['text'] = "6"
  sudoku_board[2][8]['text'] = ""
  
  sudoku_board[3][0]['text'] = "8"
  sudoku_board[3][1]['text'] = ""
  sudoku_board[3][2]['text'] = ""
  sudoku_board[3][3]['text'] = ""
  sudoku_board[3][4]['text'] = "6"
  sudoku_board[3][5]['text'] = ""
  sudoku_board[3][6]['text'] = ""
  sudoku_board[3][7]['text'] = ""
  sudoku_board[3][8]['text'] = "3"
  
  sudoku_board[4][0]['text'] = "4"
  sudoku_board[4][1]['text'] = ""
  sudoku_board[4][2]['text'] = ""
  sudoku_board[4][3]['text'] = "8"
  sudoku_board[4][4]['text'] = ""
  sudoku_board[4][5]['text'] = "3"
  sudoku_board[4][6]['text'] = ""
  sudoku_board[4][7]['text'] = ""
  sudoku_board[4][8]['text'] = "1"
  
  sudoku_board[5][0]['text'] = "7"
  sudoku_board[5][1]['text'] = ""
  sudoku_board[5][2]['text'] = ""
  sudoku_board[5][3]['text'] = ""
  sudoku_board[5][4]['text'] = "2"
  sudoku_board[5][5]['text'] = ""
  sudoku_board[5][6]['text'] = ""
  sudoku_board[5][7]['text'] = ""
  sudoku_board[5][8]['text'] = "6"
  
  sudoku_board[6][0]['text'] = ""
  sudoku_board[6][1]['text'] = "6"
  sudoku_board[6][2]['text'] = ""
  sudoku_board[6][3]['text'] = ""
  sudoku_board[6][4]['text'] = ""
  sudoku_board[6][5]['text'] = ""
  sudoku_board[6][6]['text'] = "2"
  sudoku_board[6][7]['text'] = "8"
  sudoku_board[6][8]['text'] = ""
  
  sudoku_board[7][0]['text'] = ""
  sudoku_board[7][1]['text'] = ""
  sudoku_board[7][2]['text'] = ""
  sudoku_board[7][3]['text'] = "4"
  sudoku_board[7][4]['text'] = "1"
  sudoku_board[7][5]['text'] = "9"
  sudoku_board[7][6]['text'] = ""
  sudoku_board[7][7]['text'] = ""
  sudoku_board[7][8]['text'] = "5"
  
  sudoku_board[8][0]['text'] = ""
  sudoku_board[8][1]['text'] = ""
  sudoku_board[8][2]['text'] = ""
  sudoku_board[8][3]['text'] = ""
  sudoku_board[8][4]['text'] = "8"
  sudoku_board[8][5]['text'] = ""
  sudoku_board[8][6]['text'] = ""
  sudoku_board[8][7]['text'] = "7"
  sudoku_board[8][8]['text'] = "9"

def clearSudoku(sudoku_board):
  for i in range(9):
    for j in range(9):
      sudoku_board[i][j]['text'] = ''

# master function for solving sudoku board recursively
# with visual updates to the board
def solveSudoku(sudoku_board, VISUALIZATION_SPEED):
  def validRow(row):
    seen = {}
    for i in range(9):
      cell = sudoku_board[row][i]['text']
      if ((cell != '') and (seen.get(cell)) == None):
        seen[cell] = True
      elif (cell != ''):
        return False
    return True

  def validCol(col):
    seen = {}
    for i in range(9):
      cell = sudoku_board[i][col]['text']
      if ((cell != '') and (seen.get(cell)) == None):
        seen[cell] = True
      elif (cell != ''):
        return False
    return True

  def validSquare(row, col):
    # Grab the top left corner of the subsquare based on arguments
    if row >= 6: cornerRow = 6
    elif row >= 3: cornerRow = 3
    else: cornerRow = 0

    if col >= 6: cornerCol = 6
    elif col >= 3: cornerCol = 3
    else: cornerCol = 0

    # Grab each top left corner in of the subsquare
    seen = {}
    # Loop through all 9 cells in a subsquare
    for m in range(3):
      for n in range(3):
        cell = sudoku_board[cornerRow + m][cornerCol + n]['text']
        if ((cell != '') and (seen.get(cell)) == None):
          seen[cell] = True
        elif (cell != ''):
          return False
    return True

  def isValid(row, col):
    return validRow(row) and validCol(col) and validSquare(row, col)

  def printBoard():
    for i in range(9):
      print("[", end='')
      for j in range(9):
        cell = sudoku_board[i][j]['text']
        if cell == '': cell = '_'
        print(f"{cell} ", end='')
      print(']')
    print()

  # It's necessary to use a list variable 'complete' in order to have it
  # as a global/static reference rather than just a copied value.
  # Without it being a reference, updating the variable will not be
  # noticed in previous recursive function calls.
  def recursiveSudoku(i, j, complete):
    # Check if board is complete
    if (i == 8 and j == 8 and sudoku_board[i][j]['text'] != ''):
      complete[0] = True
      return
    if complete[0]: return

    # Keep range in bounds
    elif (j == 9):
      i += 1
      j = 0

    cell = sudoku_board[i][j]['text']

    # Empty cell to fill
    if (cell == ''):
      # Loop through values 1 - 9
      for k in range(1, 10):
        if complete[0]: return
        sudoku_board[i][j]['text'] = str(k)
        sudoku_board[i][j].update()
        time.sleep(VISUALIZATION_SPEED)
        # printBoard()
        if (isValid(i, j) == True):
          if (i == 8 and j == 8):
            complete[0] = True
          recursiveSudoku(i, j + 1, complete)
      
      # Check if board is complete
      if complete[0]: return

      # If we reach here, we tried all inputs and need to
      # backtrack - so erase
      sudoku_board[i][j]['text'] = ''
      sudoku_board[i][j].update()
      time.sleep(VISUALIZATION_SPEED)
      return

    else:
      recursiveSudoku(i, j + 1, complete)

  completeStatus = [False]
  recursiveSudoku(0, 0, completeStatus)

  print(completeStatus[0])
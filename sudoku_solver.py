def hardcode_values(sudoku_board):
  sudoku_board[0][0]['text'] = "5"
  sudoku_board[0][1]['text'] = "3"
  sudoku_board[0][2]['text'] = ""
  sudoku_board[0][3]['text'] = ""
  sudoku_board[0][4]['text'] = "7"
  sudoku_board[0][5]['text'] = "1"
  sudoku_board[0][6]['text'] = ""
  sudoku_board[0][7]['text'] = ""
  sudoku_board[0][8]['text'] = ""
  
  sudoku_board[1][0]['text'] = "6"
  sudoku_board[1][1]['text'] = ""
  sudoku_board[1][2]['text'] = ""
  sudoku_board[1][3]['text'] = ""
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

# master function for solving sudoku board recursively
# with visual updates to the board
def solveSudoku(sudoku_board):
  def validRows():
    for i in range(9):
      for j in range(9):
        cell = sudoku_board[i][j]['text']
        for k in range(j + 1, 9):
          if ((cell != '') and (cell == sudoku_board[i][k]['text'])):
            sudoku_board[i][k]['fg'] = "red"
            sudoku_board[i][j]['fg'] = "red"
            return False
    return True

  def validCols():
    for i in range(9):
      for j in range(9):
        cell = sudoku_board[j][i]['text']
        for k in range(j + 1, 9):
          if ((cell != '') and (cell == sudoku_board[k][i]['text'])):
            sudoku_board[k][i]['fg'] = "red"
            sudoku_board[j][i]['fg'] = "red"
            return False
    return True

  def validSquare():
    # Grab each top left corner in of the subsquare
    for i in range(0, 9, 3):
      for j in range(0, 9, 3):
        seen = {}
        # Loop through all 9 cells in a subsquare
        for m in range(3):
          for n in range(3):
            cell = sudoku_board[i + m][j + n]['text']
            if ((cell != '') and (seen.get(cell)) == None):
              seen[cell] = True
            elif (cell != ''):
              sudoku_board[i + m][j + n]['fg'] = "red"
              return False
    return True

  def isValid():
    return validRows() and validCols() and validSquare()

  print("Solving Sudoku Board")
  isValid()


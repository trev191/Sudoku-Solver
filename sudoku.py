# sudoku.py
# Contains functions to set up and modify
# the sudoku board

import tkinter as tk
import time
import random
from event_handlers import *
from colors import CELL_COLOR, CELL_SELECT_COLOR

class Board:
  def __init__(self, masterWidget) -> None:
    self.label_cell_table = []
    self.masterWidget = masterWidget
    self.createBoard()

  def get_label_cell_table(self):
    return self.label_cell_table

  # create sudoku grid and table of label references
  def createBoard(self):
    for i in range(9):
      label_cell_row = []

      for j in range(9):
        frame_cell = tk.Frame(
          master=self.masterWidget,
          relief=tk.RAISED,
          borderwidth=1,
          background="black",
        )
        frame_cell.grid(row=i, column=j)
        label_cell = tk.Label(
          master=frame_cell,
          text='',
          width=4,
          height=2,
          bg=CELL_COLOR,
        )
        label_cell.bind("<Key>", handle_keypress)
        label_cell.bind("<Button-1>", handle_click)
        label_cell.bind("<FocusIn>", handle_focus_in)
        label_cell.bind("<FocusOut>", handle_focus_out)
        label_cell_row.append(label_cell)
        label_cell.pack()

      self.label_cell_table.append(label_cell_row)

  # clear sudoku board
  def clearSudoku(self):
    for i in range(9):
      for j in range(9):
        self.label_cell_table[i][j]['text'] = ''

  # master function for solving sudoku board recursively
  # with visual updates to the board
  def solveSudoku(self, VISUALIZATION_SPEED):
    def printBoard():
      for i in range(9):
        print("[", end='')
        for j in range(9):
          cell = self.label_cell_table[i][j]['text']
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
      if (i == 8 and j == 8 and self.label_cell_table[i][j]['text'] != ''):
        complete[0] = True
        return
      if complete[0]: return

      # Keep range in bounds
      elif (j == 9):
        i += 1
        j = 0

      cell = self.label_cell_table[i][j]['text']

      # Empty cell to fill
      if (cell == ''):
        # Loop through values 1 - 9
        for k in range(1, 10):
          if complete[0]: return
          self.label_cell_table[i][j]['text'] = str(k)
          self.label_cell_table[i][j].update()
          time.sleep(VISUALIZATION_SPEED)
          # printBoard()
          if (self.isValid(i, j) == True):
            if (i == 8 and j == 8):
              complete[0] = True
            recursiveSudoku(i, j + 1, complete)
        
        # Check if board is complete
        if complete[0]: return

        # If we reach here, we tried all inputs and need to
        # backtrack - so erase
        self.label_cell_table[i][j]['text'] = ''
        self.label_cell_table[i][j].update()
        time.sleep(VISUALIZATION_SPEED)
        return

      else:
        recursiveSudoku(i, j + 1, complete)

    completeStatus = [False]
    recursiveSudoku(0, 0, completeStatus)

  # Helper function to check if a cell is empty
  def cellIsEmpty(self, cellCoord):
    if (cellCoord == None):
      return True

    row, col = cellCoord[0], cellCoord[1]
    if (self.label_cell_table[row][col] == ''):
      return True

    else:
      return False

  # Helper function to pick a random cell in the 9x9 board
  def randomCell(self):
    cellCoord = None

    while (self.cellIsEmpty(cellCoord)):
      row = random.randint(0, 8)
      cell = random.randint(0, 8)
      cellCoord = [row, cell]

    return cellCoord

  # Helper function to validate a certain row and col
  def isValid(self, row, col):
    def validRow(row):
      seen = {}
      for i in range(9):
        cell = self.label_cell_table[row][i]['text']
        if ((cell != '') and (seen.get(cell)) == None):
          seen[cell] = True
        elif (cell != ''):
          return False
      return True

    def validCol(col):
      seen = {}
      for i in range(9):
        cell = self.label_cell_table[i][col]['text']
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
          cell = self.label_cell_table[cornerRow + m][cornerCol + n]['text']
          if ((cell != '') and (seen.get(cell)) == None):
            seen[cell] = True
          elif (cell != ''):
            return False
      return True

    return validRow(row) and validCol(col) and validSquare(row, col)

  # Randomly generate a new unique sudoku board to be solved
  def generateBoard(self):
    self.clearSudoku()
    
    # Pick ~15 random cells to fill with random, valid numbers
    random.seed()
    numRandomCells = random.randint(14, 17)
    for i in range(numRandomCells):
      row, col = self.randomCell()

      while True:
        randNum = str(random.randint(1, 9))
        self.label_cell_table[row][col]['text'] = str(randNum)

        if (self.isValid(row, col) == True):
          break

        self.label_cell_table[row][col]['text'] = ''
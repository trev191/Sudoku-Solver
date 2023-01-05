# board.py
# Contains functions to set up the sudoku board
# and cells

import tkinter as tk
from event_handlers import *
from colors import CELL_COLOR, CELL_SELECT_COLOR

class Board:
  def __init__(self, masterWidget) -> None:
    self.label_cell_table = []
    self.masterWidget = masterWidget
    self.createBoard()

  def get_label_cell_table(self):
    return self.label_cell_table

  def createBoard(self):
    # create sudoku grid and table of label references
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
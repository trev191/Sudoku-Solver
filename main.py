# main.py
# Main driver file to run the program

import tkinter as tk
from tkinter import ttk
from hardcode import *
from speedRadioBtn import *
from sudoku import *
from event_handlers import *


# create a new window
window = tk.Tk()

# frame containing the game board
frame_board = tk.Frame(
  master=window,
  padx=10,
  pady=10
)

# app title
label_title = tk.Label(
  master=window,
  text="Sudoku Solver",
  width=12,
  height=4,
)

# clicking outside of the board will remove the focus from cells
window.bind("<Button-1>", handle_click)

sudoku_board = Board(frame_board)
label_cell_table = sudoku_board.get_label_cell_table()

hardcode_values(label_cell_table)

label_title.pack()
frame_board.pack()

def handle_click_clear():
  sudoku_board.clearSudoku()

# button to solve the puzzle
def handle_click_solve():
  VISUALIZATION_SPEED = speedRadioBtn.getVisualizationSpeed()
  sudoku_board.solveSudoku(VISUALIZATION_SPEED)

frame_button_panel = tk.Frame(
  master=window,
)

button_clear = tk.Button(
  master=frame_button_panel,
  text="Clear",
  padx=5,
  command=handle_click_clear,
)
button_clear.grid(row=0, column=0)

button_solve = tk.Button(
  master=frame_button_panel,
  text="Solve",
  padx=5,
  command=handle_click_solve
)
button_solve.grid(row=0, column=1)

speedRadioBtn = visualizationSpeedRadioBtns(window)

frame_button_panel.pack()

# listen for event loop
# (without this line, the window will never appear)
window.mainloop()
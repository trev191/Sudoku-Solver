import tkinter as tk
from tkinter import ttk
from sudoku_solver import *

CELL_COLOR = "light gray"
CELL_SELECT_COLOR = "light steel blue"

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

# event handler for key press
def handle_keypress(event):
  input = (event.char)
  # clear the cell if a backspace or delete is read
  if ((input == '\x08') or (input == '')):
    event.widget['text'] = ''

  # else verify the input is a single digit 1-9
  elif (input.isnumeric()):
    intNum = int(input)
    if ((intNum > 0) and (intNum < 10)):
      event.widget['text'] = input

# event handler for clicking into a widget
def handle_click(event):
  event.widget.focus_set()

# highlight cell we are focused on
def handle_focus_in(event):
  event.widget['bg'] = CELL_SELECT_COLOR

# unhighlight cell after losing focus
def handle_focus_out(event):
  event.widget['bg'] = CELL_COLOR

# clicking outside of the board will remove the focus from cells
window.bind("<Button-1>", handle_click)

# create sudoku grid and table of label references
label_cell_table = []
for i in range(9):
  label_cell_row = []

  for j in range(9):
    frame_cell = tk.Frame(
      master=frame_board,
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

  label_cell_table.append(label_cell_row)

hardcode_values(label_cell_table)

label_title.pack()
frame_board.pack()

def handle_click_clear():
  clearSudoku(label_cell_table)

# button to solve the puzzle
def handle_click_solve():
  VISUALIZATION_SPEED = float(str_selectedSpeed.get())
  solveSudoku(label_cell_table, VISUALIZATION_SPEED)

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

# Desired speed of visualizing the solution/algorithm.
# The lower the value, the faster the speed.
frame_speed_select = tk.Frame(
  master=window,
  padx=5,
)
visualization_speeds = [
  ("Fastest", 0),
  ("Fast", .1),
  ("Medium", .2),
  ("Slow", .35),
]
str_selectedSpeed = tk.StringVar(value=0)

for speed in visualization_speeds:
  radio_speed_button = ttk.Radiobutton(
    master=frame_speed_select,
    text=speed[0],
    value=speed[1],
    variable=str_selectedSpeed,
  )
  radio_speed_button.pack()

frame_speed_select.pack()

frame_button_panel.pack()

# listen for event loop
# (without this line, the window will never appear)
window.mainloop()
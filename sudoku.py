import tkinter as tk

# create a new window
window = tk.Tk()

# frame containing the game board
frame_board = tk.Frame(
  master=window,
  padx=10,
  pady=10
)

label_title = tk.Label(
  master=window,
  text="Sudoku Solver",
  width=10,
  height=4,
)

# create sudoku grid
for i in range(9):
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
      text=f"{i},{j}",
      width=4,
      height=2,
      
    )
    label_cell.pack()

label_title.pack()
frame_board.pack()

# event handler for key press
def handle_keypress(event):
  print(event.char)

# bind keypress handler with key press event
window.bind("<Key>", handle_keypress)

# master function for solving sudoku board recursively
# with visual updates to the board
def solveSudoku():
  print("Solving Sudoku Board")

# button to solve the puzzle
def handle_click_solve():
  solveSudoku()

button_solve = tk.Button(
  master=window,
  text="Solve",
  command=handle_click_solve
)
button_solve.pack()

# listen for event loop
# (without this line, the window will never appear)
window.mainloop()

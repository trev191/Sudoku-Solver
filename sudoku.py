import tkinter as tk

# create a new window
window = tk.Tk()

frame_board = tk.Frame(
  master=window,
)

label_title = tk.Label(
  master=window,
  text="Sudoku Solver",
  width=10,
  height=5,
)

for i in range(9):
  for j in range(9):
    frame_cell = tk.Frame(
      master=frame_board,
      relief=tk.RAISED,
      borderwidth=1
    )
    frame_cell.grid(row=i, column=j)
    label_cell = tk.Label(
      master=frame_cell,
      text=f"Row {i}\nColumn {j}"
    )
    label_cell.pack()

# add the label into the window
label_title.pack()
frame_board.pack(
  # fill=tk.BOTH,
  # side=tk.LEFT,
  # expand=True
)

# listen for event loop
# (without this line, the window will never appear)
window.mainloop()

# speedRadioBtn.py
# Contains functions to set up the radio button widgets
# for selecting the visualization speed

import tkinter as tk
from tkinter import ttk

# Desired speed of visualizing the solution/algorithm.
# The lower the value, the faster the speed.
visualization_speeds = [
  ("Fastest", 0),
  ("Fast", .1),
  ("Medium", .2),
  ("Slow", .35),
]

class visualizationSpeedRadioBtns:
  def __init__(self, masterWidget) -> None:
    self.str_selectedSpeed = tk.StringVar(value=0)
    self.masterWidget = masterWidget
    self.createRadioButtons()

  def getVisualizationSpeed(self):
    return float(self.str_selectedSpeed.get())

  def createRadioButtons(self):
    frame_speed_select = tk.Frame(
      master=self.masterWidget,
      padx=5,
    )

    for speed in visualization_speeds:
      radio_speed_button = ttk.Radiobutton(
        master=frame_speed_select,
        text=speed[0],
        value=speed[1],
        variable=self.str_selectedSpeed,
      )
      radio_speed_button.pack()

    frame_speed_select.pack()





# event_handlers.py
# Contains event handler functions

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
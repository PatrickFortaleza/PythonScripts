import time
import threading
# Ensure that you have pynput installed. $ pip install pynput
# Import dependencies from pynput
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

# Setup delay
delay = 0.001
button = Button.left
# Configure toggle on/off button
start_stop_key = KeyCode(char='s')
# Configure exit key
exit_key = KeyCode(char='e')

# Create a class that inherits from threading.Thread
class ClickMouse(threading.Thread):
  # __init__ is kind of like a constructor for the class
  # We pass in self, to say that it belongs to this class
  # Also expects a delay and a button
  def __init__(self, delay, button):
    # Call super to initialize the constructor
    super(ClickMouse, self).__init__()
    # Construct the class with dependency injection
    self.delay = delay
    self.button = button
    # These variables will allow the script to check wether to run or not.
    self.running = False
    self.program_running = True

  # Next, we will define the methods that start, stop and exit the auto clicker.
  def start_clicking(self):
    self.running = True

  def stop_clicking(self):
    self.running = False

  def exit(self):
    self.stop_clicking()
    self.program_running = False
  # We'll need a method that runs the clicking too...
  # Here we'll use a while loop that will always check if the script is running.
  def run(self):
    while self.program_running:
      while self.running:
      # When program_running === true && running === true do this:
          mouse.click(self.button) # Mouse will be clicked here
          time.sleep(self.delay) # Then wait for the specified delay
      time.sleep(0.1)

# Creates the mouse controller instance and click_thread instance, and runs the script.
mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()

# Create key listeners to stop/start the auto clicker
def on_press(key):
  # Check if the key that was pressed is the start_stop_key
  if key == start_stop_key:
    if click_thread.running:
        click_thread.stop_clicking()
    else:
      click_thread.start_clicking()
  # If the key was pressed, but it was not the start_stop_key, check if it's the exit_key
  elif key == exit_key:
    click_thread.exit()
    listener.stop()

with Listener(on_press=on_press) as listener:
  listener.join()
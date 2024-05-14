## pip install pyautogui pyscreeze

import datetime
import time
# import pyautogui
import pyscreeze
import tkinter as tk

def screeshot():
  name = datetime.datetime.now()
  name = 'G:\\DOCUMENTS\\Ana\\Project perso\\lab\\python_10_projects\\scrnsht\\{}.jpg'.format(name.strftime('%y%m%d%H%M%S'))
  time.sleep(5)
  img = pyscreeze.screenshot(name)
  img.show()

# screeshot()

## GUI

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(
  frame,
  text="Take Screenshot",
  command=screeshot)
button.pack(side=tk.LEFT)

close = tk.Button(
  frame,
  text="QUIT",
  command=quit)
close.pack(side=tk.LEFT)

root.mainloop()

import tkinter as tk
from tkinter import *
from tkinter import ttk

root = tk.Tk()

# -------------- STYLING --------------
s = ttk.Style(self)
s.configure('mainFrame.TFrame', background='#164863')


# -------------- WIDGETS --------------
mainFrame = tk.Frame(root, width=250, height=250, style='mainFrame.TFrame')
mainFrame.grid()

# -------------- GRID CONFIG --------------


# root.resizeable(width=False, height=False)
root.mainloop()  # Keep the window open

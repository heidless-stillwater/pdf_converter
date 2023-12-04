import tkinter as tk
from tkinter import ttk


class NinjaDashboard(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text='Ninja Dash', font=("Arial", 50))
        label.pack()

import tkinter as tk
# import Dashboard
from constants import *

from page import Page


class PageThree(Page):

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        # label = tk.Label(self, text="This is page 3")
        label = tk.Label(self, text="Page 3", fg=TEXT_COLOR, bg=THEME_COLOR, font=("", 20, "bold"))

        # label.pack(side="top", fill="both", expand=True)
        label.grid(row=2, column=0, columnspan=1)


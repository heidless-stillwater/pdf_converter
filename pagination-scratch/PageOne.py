import tkinter as tk
# import Dashboard
from page import Page

# TEXT_COLOR = '#0cb3f0'
# BACKGROUND_COLOR = '#006666'

TEXT_COLOR = 'black'
BACKGROUND_COLOR = '#66b2b2'


class PageOne(Page):

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="HOME page", fg=TEXT_COLOR, bg=BACKGROUND_COLOR, font=("", 20, "bold"),
)
        label.pack(side="top", fill="both", expand=True)

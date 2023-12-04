import tkinter as tk
# import Dashboard
from page import Page
import pdf_ninja

# TEXT_COLOR = '#0cb3f0'
# BACKGROUND_COLOR = '#006666'

TEXT_COLOR = 'black'
BACKGROUND_COLOR = '#66b2b2'


class PageTwo(Page):

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        #
        # label = tk.Label(self, text="PDF Ninja Page", fg=TEXT_COLOR, bg=BACKGROUND_COLOR, font=("", 20, "bold"),)
        # label.pack(side="top", fill="both", expand=True)
        #
        my_app = pdf_ninja.App()




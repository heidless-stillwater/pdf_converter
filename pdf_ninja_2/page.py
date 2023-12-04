import tkinter as tk
import customtkinter
BACKGROUND_COLOR = '#006666'
# TEXT_COLOR = '#0cb3f0'
TEXT_COLOR = 'white'

STATUS_FRAME_WIDTH = 800
APP_FRAME_WIDTH = 100


class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        page_frame = tk.Frame.__init__(self, *args, **kwargs)
        # label = tk.Label(self, text="This is Page", fg=TEXT_COLOR, bg=BACKGROUND_COLOR, font=("", 10, "normal"))
        # label.config(width=APP_FRAME_WIDTH, height=5)
        # # label.pack(side="top", fill='none', expand=True)
        # # label.pack(side="top", fill='none')
        # label.grid(row=0, column=0, columnspan=1, sticky='s')

    def show(self):
        self.lift()

import tkinter as tk
import customtkinter
BACKGROUND_COLOR = '#006666'
# TEXT_COLOR = '#0cb3f0'
TEXT_COLOR = 'white'


class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        page_frame = tk.Frame.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="This is Page", fg=TEXT_COLOR, bg=BACKGROUND_COLOR, font=("", 10, "normal"))
        label.config(width=130, height=5)
        # label.pack(side="top", fill='none', expand=True)
        label.pack(side="top", fill='none')

        # # user_entry
        # self.user_entry = customtkinter.CTkEntry(
        #     master=page_frame,
        #     placeholder_text="combo filename")
        # # self.user_entry.grid(row=6, column=2, padx=(20, 0), pady=(20, 0))
        # self.user_entry.place(relx=0, rely=0, relwidth=0.5, relheight=0.15)
        # # self.user_entry.pack(side="top", fill='none')
        #


    def show(self):
        self.lift()

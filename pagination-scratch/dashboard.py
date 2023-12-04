import tkinter as tk
from customtkinter import *

from PageOne import PageOne
from pdf_ninja import PdfApp

from PageTwo import PageTwo
from PageThree import PageThree

# -------------------------- DEFINING GLOBAL VARIABLES -------------------------
NAVY_BLUE = '#05445E'
BLUE_GROTTO = '#189AB4'
BLUE_GREEN = '#75E6DA'
BABY_BLUE = '#D4F1F4'

THEME_COLOR = 'blue'
# THEME_COLOR = '#748cb3'
TEXT_COLOR = '#0cb3f0'
#
# MAIN_BACKGROUND_COLOR = 'blue'
# ICON_BACKGROUND_COLOR = 'yellow'
# SIDEBAR_BACKGROUND_COLOR = 'green'
# SELECTION_BACKGROUND_COLOR = 'yellow'
# HEADER_BACKGROUND_COLOR = 'red'
# # MAIN_BACKGROUND_COLOR = '#748cb3'
# BRANDING_BACKGROUND = 'pink'

ICON_BACKGROUND_COLOR = '#2b2b2b'
SIDEBAR_BACKGROUND_COLOR = '#2b2b2b'
SELECTION_BACKGROUND_COLOR = '#6f93c9'
HEADER_BACKGROUND_COLOR = '#1169ed'
MAIN_BACKGROUND_COLOR = '#748cb3'
BRANDING_BACKGROUND = '#144870'

# APP_DIMENSIONS = '1100x700'
APP_WIDTH = 1100
APP_HEIGHT = 700
SIDEBAR_WIDTH = 200
SIDEBAR_HEIGHT = APP_HEIGHT - 500
SELECTION_WIDTH = APP_WIDTH - SIDEBAR_WIDTH
SELECTION_HEIGHT = 100
BRAND_FRAME_HEIGHT = APP_HEIGHT

selectionbar_color = SELECTION_BACKGROUND_COLOR
sidebar_color = SIDEBAR_BACKGROUND_COLOR
header_color = HEADER_BACKGROUND_COLOR
visualisation_frame_color = "#ffffff"


class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = PageOne(self)
        p2 = PdfApp(self)
        # p2 = PageTwo(self)
        p3 = PageThree(self)

        buttonframe = tk.Frame(self)
        buttonframe.config(bg=SIDEBAR_BACKGROUND_COLOR, width=100, height=100, padx=10)
        container = tk.Frame(self)
        container.config(bg=SIDEBAR_BACKGROUND_COLOR, width=50, height=50)

        #
        # buttonframe.place(relx=0, rely=0, relwidth=0.2, relheight=1, width=SIDEBAR_WIDTH, height=10)
        # container.place(relx=10, rely=10, relwidth=0.2, relheight=1, width=SIDEBAR_WIDTH, height=10)
        #
        buttonframe.pack(side='left', fill="x", expand=False)
        container.pack(side="right", fill="both", expand=True)

        buttonframe.grid(row=1, column=0, rowspan=4, sticky="nsew")
        container.grid(row=1, column=0, rowspan=4, sticky="nsew")

        # # ---------------- HEADER ------------------------
        # self.header = tk.Frame(self, bg=header_color)
        # self.header.config(width=SELECTION_WIDTH, height=SELECTION_HEIGHT)
        # self.header.place(relx=0, rely=0, relwidth=1, relheight=1)
        #


        # #---------------- SIDEBAR -----------------------
        # # CREATING FRAME FOR SIDEBAR
        # self.sidebar = tk.Frame(self, bg=sidebar_color)
        # self.sidebar.config(width=SIDEBAR_WIDTH, height=APP_HEIGHT)
        # self.sidebar.place(relx=0, rely=0, relwidth=0.2, relheight=1)
        # # self.sidebar.grid(row=0, column=0, columnspan=1)
        #
        # buttonframe = tk.Frame(self.sidebar)
        # buttonframe.config(bg='grey')
        # container = tk.Frame(self.sidebar)
        # container.config(bg='yellow')
        # #
        # buttonframe.place(relx=0, rely=0, relwidth=0.2, relheight=1, width=SIDEBAR_WIDTH, height=10)
        # container.place(relx=10, rely=10, relwidth=0.2, relheight=1, width=SIDEBAR_WIDTH, height=10)
        # #
        # # buttonframe.pack(side='top', fill="x", expand=False)
        # # container.pack(side="top", fill="both", expand=True)
        #
        # pdf_tools = tk.Label(
        #     self.sidebar,
        #     text='PDF Ninja',
        #     bg=BRANDING_BACKGROUND,
        #     fg='white',
        #     font=("", 15, "bold")
        # )
        # pdf_tools.place(x=50, y=50, anchor="w")
        #



        # # UNIVERSITY LOGO AND NAME
        self.brand_frame = tk.Frame(self, bg=BRANDING_BACKGROUND)
        self.brand_frame.config(width=SIDEBAR_WIDTH, height=100)
        # self.brand_frame.config(width=SIDEBAR_WIDTH, height=BRAND_FRAME_HEIGHT)
        # self.brand_frame.place(relx=0, rely=0, relwidth=1, relheight=0.15)
        self.brand_frame.grid(row=2, column=1, columnspan=1, sticky='s')

        self.uni_logo = icon.subsample(9)
        logo = tk.Label(self.brand_frame, image=self.uni_logo, bg=sidebar_color)
        # logo.place(x=40, y=40)
        self.logo.grid(row=2, column=1, columnspan=1, sticky='s')


        uni_name = tk.Label(self.brand_frame,
                            text='PDF Ninja',
                            bg=BRANDING_BACKGROUND,
                            fg='#bac9e0',
                            font=("", 15, "bold"),
                            )
        # uni_name.place(x=70, y=55, anchor="w")
        self.uni_name.grid(row=3, column=1, columnspan=1, sticky='s')


        # uni_name = tk.Label(self.brand_frame,
        #                     text='Ninja',
        #                     bg=sidebar_color,
        #                     fg=TEXT_COLOR,
        #                     font=("", 15, "bold")
        #                     )
        # uni_name.place(x=55, y=60, anchor="w")
        #

        # p1.place(in_=container, x=0, y=25, relwidth=0.97, relheight=0.93)
        p1.grid(row=3, column=1, columnspan=1, sticky='s')

        # p2.place(in_=container, x=30, y=25, relwidth=0.9, relheight=0.93)
        # p3.place(in_=container, x=30, y=25, relwidth=0.9, relheight=0.93)

        b1 = CTkButton(buttonframe, text="Home", command=p1.lift)
        b2 = CTkButton(buttonframe, text="PDF Ninja", command=p2.lift)
        b3 = CTkButton(buttonframe, text="Page 3", command=p3.lift)

        # b1.pack(side="top", padx=20, pady=10)
        b1.grid(row=3, column=1, columnspan=1, sticky='s')

        #
        # b2.pack(side="top", padx=20, pady=10)
        # b3.pack(side="top", padx=20, pady=10)

        p1.show()


if __name__ == "__main__":
    root = tk.Tk()

    # ---------------- SETTINGS ------------------------
    icon = tk.PhotoImage(file='../images/LU_logo.png')
    root.iconphoto(True, icon)
    main = MainView(root)
    main.configure(background=SIDEBAR_BACKGROUND_COLOR)

    # main.pack(side="top", fill="both", expand=True)

    main.grid(row=3, column=1, columnspan=1, sticky='s')

    # root.wm_geometry("400x400")
    root.wm_geometry(f'{APP_WIDTH}x{APP_HEIGHT}')

    root.mainloop()

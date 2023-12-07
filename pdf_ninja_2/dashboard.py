import tkinter as tk
from customtkinter import *
from tkinter import ttk
from constants import *

from PageOne import PageOne
from PageThree import PageThree
from pdf_ninja import PdfApp

selectionbar_color = SELECTION_BACKGROUND_COLOR
sidebar_color = SIDEBAR_BACKGROUND_COLOR
header_color = HEADER_BACKGROUND_COLOR
visualisation_frame_color = PALETTE_DARK


class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        super().__init__()

        # -------------- STYLING --------------
        s = ttk.Style(self)
        s.configure('brandingFrame.TFrame', background=PALETTE_LIGHTEST)
        s.configure('sidebarFrame.TFrame', background=PALETTE_DARK)
        s.configure('statusFrame.TFrame', background=PALETTE_DARK)
        s.configure('AppFrame.TFrame', background=PALETTE_LIGHTEST)
        s.configure('ControlsFrame.TFrame', background=PALETTE_DARKEST)
        # s.configure('Vertical.TFrame', background=F_BACKGROUND_6)

        # -------------- WIDGETS --------------
        BrandingFrame = ttk.Frame(self, width=SIDEBAR_WIDTH, height=BRAND_FRAME_HEIGHT, style='brandingFrame.TFrame')
        BrandingFrame.grid(row=0, column=0)

        SidebarFrame = ttk.Frame(self, width=SIDEBAR_WIDTH, height=SIDEBAR_HEIGHT, style='sidebarFrame.TFrame')
        SidebarFrame.grid(row=1, column=0, rowspan=2, sticky='NSEW')

        StatusFrame = ttk.Frame(self, width=STATUS_FRAME_WIDTH , height=BRAND_FRAME_HEIGHT, style='statusFrame.TFrame')
        StatusFrame.grid(row=0, column=1)

        AppFrame = ttk.Frame(self, style='AppFrame.TFrame')
        AppFrame.grid(row=1, column=1, padx=0, sticky='NSEW')

        ControlsFrame = ttk.Frame(self, width=CONTROLS_FRAME_WIDTH, height=CONTROLS_FRAME_HEIGHT, style='ControlsFrame.TFrame')
        ControlsFrame.grid(row=2, column=1, padx=0)

        # configure style
        b_s = ttk.Style(self)
        b_s.configure('SidebarBtn.TFrame', background=PALETTE_DARKEST)

        buttonframe = tk.Frame(SidebarFrame, width=180, height=60, padx=10)
        buttonframe.configure(bg=PALETTE_DARK)

        buttonframe.grid(row=0, column=0, padx=20, pady=100, rowspan=1)

        # UNIVERSITY LOGO AND NAME
        self.brand_frame = tk.Frame(BrandingFrame, bg=PALETTE_LIGHTEST)
        self.brand_frame.config(width=SIDEBAR_WIDTH, height=100)
        self.brand_frame.grid(row=0, column=0, columnspan=1)

        self.bus_logo = heidless_icon.subsample(9)
        logo = tk.Label(self.brand_frame, image=self.bus_logo, bg=PALETTE_LIGHTEST)
        logo.place(x=20, y=20)

        bus_name = tk.Label(BrandingFrame,
                            text=BUS_NAME,
                            bg=PALETTE_LIGHTEST,
                            fg=TEXT_COLOR,
                            font=("", 15, "bold"),
                            )
        bus_name.grid(row=0, column=0, columnspan=1, sticky='N', pady=30, padx=20)

        #
        p1 = PageOne(AppFrame)
        p1.config(width=600, height=100)
        p1.grid(row=0, column=0)

        # PDF Ninja Frame
        PDFNinjaFrame = PdfApp(AppFrame)

        PDFNinjaFrame.config(width=600, height=100)
        PDFNinjaFrame.grid(row=0, column=0)

        p3 = PageThree(AppFrame)
        p3.config(width=600, height=100)
        p3.grid(row=0, column=0)

        b1 = CTkButton(buttonframe, text="Home", command=p1.lift)
        b2 = CTkButton(buttonframe, text="PDF Ninja", command=PDFNinjaFrame.lift)
        b3 = CTkButton(buttonframe, text="Page 3", command=p3.lift)

        b1.grid(row=1, column=0, columnspan=1, pady=10, padx=0, sticky='s')
        b2.grid(row=2, column=0, columnspan=1, pady=10, padx=0, sticky='s')
        b3.grid(row=3, column=0, columnspan=1, pady=10, padx=0, sticky='s')

        PDFNinjaFrame.show()


if __name__ == "__main__":
    root = tk.Tk()

    # ---------------- SETTINGS ------------------------
    heidless_icon = tk.PhotoImage(file=BUS_LOGO)
    root.iconphoto(True, heidless_icon)

    main = MainView(root)
    main.configure(background=SIDEBAR_BACKGROUND_COLOR)

    main.grid(row=0, column=0, columnspan=1, sticky='s')

    root.wm_geometry(f'{APP_WIDTH}x{APP_HEIGHT}+300+10')

    root.mainloop()

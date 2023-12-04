import tkinter as tk
from tkinter import ttk
from ninja_page_dashboard import NinjaDashboard

# -------------------------- DEFINING GLOBAL VARIABLES -------------------------

NAVY_BLUE = '#05445E'
BLUE_GROTTO = '#189AB4'
BLUE_GREEN = '#75E6DA'
BABY_BLUE = '#D4F1F4'

THEME_COLOR = '#748cb3'
TEXT_COLOR = '#0cb3f0'

ICON_BACKGROUND_COLOR = '#2b2b2b'
SIDEBAR_BACKGROUND_COLOR = '#2b2b2b'
SELECTION_BACKGROUND_COLOR = '#6f93c9'
HEADER_BACKGROUND_COLOR = '#1169ed'
MAIN_BACKGROUND_COLOR = '#748cb3'
BRANDING_BACKGROUND = '#144870'

# 6f93c9

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

# ------------------------------- ROOT WINDOW ----------------------------------


class NinjaApp(tk.Tk):
    """
     The class creates a header and sidebar for the application. Also creates
     two submenus in the sidebar, one for attendance overview with options to
     track students and modules, view poor attendance and another for
     database management, with options to update and add new modules to the
     database.
    """
    def __init__(self):
        tk.Tk.__init__(self)

        # ------------- BASIC APP LAYOUT -----------------

        self.geometry(f'{APP_WIDTH}x{APP_HEIGHT}')
        self.resizable(0, 0)
        self.title('PDF Ninja')
        self.config(background=selectionbar_color)

        icon = tk.PhotoImage(file='images\\LU_logo.png')
        self.iconphoto(True, icon)

        # ---------------- HEADER ------------------------
        self.header = tk.Frame(self, bg=header_color)
        # self.header.config(width=SELECTION_WIDTH, height=SELECTION_HEIGHT)
        self.header.place(relx=0, rely=0, relwidth=1, relheight=0.1)

        # self.header.grid(row=0, column=1, columnspan=1, sticky='n')

        # ---------------- SIDEBAR -----------------------
        # CREATING FRAME FOR SIDEBAR
        self.sidebar = tk.Frame(self, bg=sidebar_color)
        self.sidebar.config(width=SIDEBAR_WIDTH, height=APP_HEIGHT)
        self.sidebar.place(relx=0, rely=0, relwidth=0.2, relheight=1)
        # self.sidebar.grid(row=0, column=0, columnspan=1)

        # UNIVERSITY LOGO AND NAME
        self.brand_frame = tk.Frame(self.sidebar, bg=BRANDING_BACKGROUND)
        self.brand_frame.config(width=SIDEBAR_WIDTH, height=BRAND_FRAME_HEIGHT)
        self.brand_frame.place(relx=0, rely=0, relwidth=1, relheight=0.1)
        # self.brand_frame.grid(row=1, column=1, columnspan=1, sticky='s')

        self.uni_logo = icon.subsample(9)
        logo = tk.Label(self.brand_frame, image=self.uni_logo, bg=sidebar_color)
        logo.place(x=45, y=20)

        # self.logo.grid(row=0, column=0, columnspan=1)

        uni_name = tk.Label(self.brand_frame,
                            text='PDF Ninja',
                            bg=BRANDING_BACKGROUND,
                            fg='#bac9e0',
                            font=("", 15, "bold")
                            )
        uni_name.place(x=80, y=35, anchor="w")
        #
        # uni_name = tk.Label(self.brand_frame,
        #                     text='Ninja',
        #                     bg=sidebar_color,
        #                     fg=TEXT_COLOR,
        #                     font=("", 15, "bold")
        #                     )
        # uni_name.place(x=55, y=60, anchor="w")
        #
        # SUBMENUS IN SIDE BAR

        # # SUBMENU 1
        self.submenu_frame = tk.Frame(self.sidebar, bg=sidebar_color)
        self.submenu_frame.place(relx=0, rely=0.1, relwidth=1, relheight=0.85)
        submenu1 = SidebarSubMenu(self.submenu_frame,
                                  sub_menu_heading='SUBMENU 1',
                                  sub_menu_options=[
                                    # "Display Frame1",
                                    # "Display Frame2",
                                    "PDF Dashboard",
                                    ])
        # submenu1.options["Display Frame1"].config(
        #     command=lambda: self.show_frame(Frame1),
        #     fg=TEXT_COLOR
        # )
        # submenu1.options["Display Frame2"].config(
        #     command=lambda: self.show_frame(Frame2),
        #     fg=TEXT_COLOR
        # )

        submenu1.options["PDF Dashboard"].config(
            command=lambda: self.show_frame(NinjaDashboard),
            fg=TEXT_COLOR,
            font=("Arial", 15)
        )
        submenu1.place(relx=0, rely=0.025, relwidth=1, relheight=0.3)

        #
        # --------------------  MULTI PAGE SETTINGS ----------------------------
        container = tk.Frame(self)
        container.config(highlightbackground="#808080", highlightthickness=0.5)
        container.place(relx=0.20, rely=0.1, relwidth=0.8, relheight=0.9)

        self.frames = {}

        for F in (
                # Frame1,
                # Frame2,
                NinjaDashboard,
                ):
            frame = F(container, self)
            self.frames[F] = frame
            frame.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.show_frame(NinjaDashboard)

    def show_frame(self, cont):
        """
        The function 'show_frame' is used to raise a specific frame (page) in
        the tkinter application and update the title displayed in the header.

        Parameters:
        cont (str): The name of the frame/page to be displayed.
        title (str): The title to be displayed in the header of the application.

        Returns:
        None
        """
        frame = self.frames[cont]
        frame.tkraise()


# ------------------------ MULTIPAGE FRAMES ------------------------------------


class Frame1(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text='Frame 1', font=("Arial", 15))
        label.pack()


class Frame2(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text='Frame 2', font=("Arial", 15))
        label.pack()


class NinjaDashboard(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text='Ninja default Dash', font=("Arial", 20))
        label.pack()


# ----------------------------- CUSTOM WIDGETS ---------------------------------

class SidebarSubMenu(tk.Frame):
    """
    A submenu which can have multiple options and these can be linked with
    functions.
    """
    def __init__(self, parent, sub_menu_heading, sub_menu_options):
        """
        parent: The frame where submenu is to be placed
        sub_menu_heading: Heading for the options provided
        sub_menu_operations: Options to be included in sub_menu
        """
        tk.Frame.__init__(self, parent)
        self.config(bg=sidebar_color)
        self.sub_menu_heading_label = tk.Label(self,
                                               text=sub_menu_heading,
                                               bg=sidebar_color,
                                               fg="#333333",
                                               font=("Arial", 10)
                                               )
        self.sub_menu_heading_label.place(x=30, y=10, anchor="w")

        sub_menu_sep = ttk.Separator(self, orient='horizontal')
        sub_menu_sep.place(x=30, y=30, relwidth=0.8, anchor="w")

        self.options = {}
        for n, x in enumerate(sub_menu_options):
            self.options[x] = tk.Button(self,
                                        text=x,
                                        bg=sidebar_color,
                                        font=("Arial", 9, "bold"),
                                        bd=0,
                                        cursor='hand2',
                                        activebackground='#ffffff',
                                        )
            self.options[x].place(x=30, y=45 * (n + 1), anchor="w")


app = NinjaApp()
app.mainloop()

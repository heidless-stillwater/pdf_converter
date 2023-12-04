import tkinter as tk
from tkinter import ttk

F_BACKGROUND_1 = '#FF6C22'
F_BACKGROUND_2 = '#F5E8C7'
F_BACKGROUND_3 = '#2B3499'
F_BACKGROUND_4 = '#557C55'
F_BACKGROUND_5 = '#427D9D'
F_BACKGROUND_6 = '#FF5B22'


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # self.geometry('300x110')
        self.resizable(1, 1)
        self.title('Login')


        root = tk.Tk()

        # -------------- STYLING --------------
        s = ttk.Style(self)
        s.configure('mainFrame.TFrame', background=F_BACKGROUND_1)
        s.configure('Frame2.TFrame', background=F_BACKGROUND_2)
        s.configure('Frame3.TFrame', background=F_BACKGROUND_3)
        s.configure('Frame4.TFrame', background=F_BACKGROUND_4)
        s.configure('Horizontal.TFrame', background=F_BACKGROUND_5)
        s.configure('Vertical.TFrame', background=F_BACKGROUND_6)

        # -------------- WIDGETS --------------
        mainFrame = ttk.Frame(self, width=250, height=250, style='mainFrame.TFrame')
        mainFrame.grid(row=0, column=0)

        Frame2 = ttk.Frame(self, width=200 , height=200, style='Frame2.TFrame')
        Frame2.grid(row=1, column=0, padx=0, pady=0, sticky='WE')

        Frame3 = ttk.Frame(self, width=250 , height=250, style='Frame3.TFrame')
        Frame3.grid(row=0, column=1, padx=0, pady=0)

        Frame4 = ttk.Frame(self, width=150 , height=100, style='Frame4.TFrame')
        Frame4.grid(row=1, column=1, padx=0, pady=0, sticky='NSEW')

        horizontal = ttk.Frame(self, width=500 , height=100, style='Horizontal.TFrame')
        horizontal.grid(row=2, column=0, columnspan=2)

        vertical = ttk.Frame(self, width=100 , height=350, style='Vertical.TFrame')
        vertical.grid(row=0, column=2, rowspan=3, sticky='NS')

# -------------- GRID CONFIG --------------

        #
        # # UI options
        # paddings = {'padx': 5, 'pady': 5}
        # entry_font = {'font': ('Helvetica', 11)}
        #
        # # configure the grid
        # self.columnconfigure(0, weight=1)
        # self.columnconfigure(1, weight=3)
        #
        # username = tk.StringVar()
        # password = tk.StringVar()
        #
        # # username
        # username_label = ttk.Label(self, text="Username:")
        # username_label.grid(column=0, row=0, sticky=tk.W, **paddings)
        #
        # username_entry = ttk.Entry(self, textvariable=username, **entry_font)
        # username_entry.grid(column=1, row=0, sticky=tk.E, **paddings)
        #
        # # password
        # password_label = ttk.Label(self, text="Password:")
        # password_label.grid(column=0, row=1, sticky=tk.W, **paddings)
        #
        # password_entry = ttk.Entry(
        #     self, textvariable=password, show="*", **entry_font)
        # password_entry.grid(column=1, row=1, sticky=tk.E, **paddings)
        #
        # # login button
        # login_button = ttk.Button(self, text="Login")
        # login_button.grid(column=1, row=3, sticky=tk.E, **paddings)
        #
        # # configure style
        # self.style = ttk.Style(self)
        # self.style.configure('TLabel', font=('Helvetica', 11))
        # self.style.configure('TButton', font=('Helvetica', 11))


if __name__ == "__main__":
    app = App()
    app.mainloop()

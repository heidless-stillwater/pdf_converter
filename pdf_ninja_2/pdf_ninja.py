import tkinter as tk
from tkinter import ttk

import tkinter.messagebox
import customtkinter
from pdf_toolbox import PdfToolbox
from file_mgr import FileMgr
import os
from PIL import Image, ImageTk

from constants import *

from page import Page

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
#
# THEME_COLOR = '#0c134f'
# ICON_BACKGROUND_COLOR = '#2b2b2b'
# BACKGROUND_COLOR = '#0c134f'
# TEXT_COLOR = '#0cb3f0'
# SIDEBAR_BACKGROUND_COLOR = '#2b2b2b'
#
# NAVY_BLUE = '#05445E'
# BLUE_GROTTO = '#189AB4'
# BLUE_GREEN = '#75E6DA'
# BABY_BLUE = '#D4F1F4'

COL_SPAN = 5
PDF_DIR = './pdf_files'
FILES_C_WIDTH = 900
FILES_C_HEIGHT = 200

# windo geometry
W_X_POS = 500
W_Y_POS = 5
W_X_SIZE = 1100
W_Y_SIZE = 580

# messages
NOTHING_SELECTED = 'NOTHING_SELECTED'

# file locations
PDF_FILES = './pdf_files'
PDF_PAGES = './pdf_files/pdf_pages'
PDF_COMBO = './pdf_files/pdf_combo'

# ICON
W_ICON = './images/pngtree-pdf-file-icon-png-png-image_4899509.jpeg'

# class App(customtkinter.CTk):


class PdfApp(Page):
    #
    # def __init__(self, *args, **kwargs):
    #     super().__init__()
    #     page = Page.__init__(self, *args, **kwargs)
    #

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        # -------------- STYLING --------------
        s = ttk.Style(self)
        s.configure('ninjaFrame.TFrame', background=PALETTE_DARK)

        # s.configure('ninjaFrame.TFrame', width=APP_FRAME_WIDTH)
        # s.configure('ninjaFrame.TFrame', height=APP_FRAME_HEIGHT)

        ninjaFrame = ttk.Frame(self)
        ninjaFrame.configure(style='ninjaFrame.TFrame')
        ninjaFrame.grid(row=0, column=0, sticky='EW')
        #
        # label = tk.Label(ninjaFrame, text="Ninja page", fg=TEXT_COLOR, bg=THEME_COLOR, font=("", 20, "bold"))
        # # label.pack(side="top", fill="both", expand=True)
        # label.grid(row=0, column=0, columnspan=1, sticky='S')
        #
        #
        # commandFrame = tkinter.Frame(ninjaFrame)
        # commandFrame.configure(bg=F_BACKGROUND_1)
        # commandFrame.grid(row=0, column=0, columnspan=1, padx=0)

        # print(f'APP_FRAME_WIDTH: {APP_FRAME_WIDTH}')
        # print(f'APP_FRAME_HEIGHT: {APP_FRAME_HEIGHT}')

        ##################################
        # controls tab

        self.tabview_t = customtkinter.CTkTabview(master=ninjaFrame, bg_color=PALETTE_DARK, width=APP_FRAME_WIDTH, height=APP_FRAME_HEIGHT)
        # self.tabview_t.grid(row=0, column=0, padx=(20, 0), pady=(20, 0), rowspan=1, sticky='W')
        # self.tabview_t.configure(bg='blue')
        self.tabview_t.grid(row=0, column=0, padx=20, pady=0, rowspan=1, sticky='NSEW')

        self.tabview_t.add("commands")  # add tab at the end
        self.tabview_t.add("user flow")  # add tab at the end
        self.tabview_t.set("user flow")  # set currently visible tab

        ####################################
        # user_entry
        self.user_entry = customtkinter.CTkEntry(
            master=self.tabview_t.tab("commands"),
            placeholder_text="combo filename")
        self.user_entry.grid(row=0, column=0, padx=(20, 0), pady=(20, 0), sticky='N')

        #
        # labelFrame = tkinter.Frame(ninjaFrame)
        # labelFrame.config(bg=SIDEBAR_BACKGROUND_COLOR, width=0, height=0)
        # labelFrame.grid(row=1, column=1, columnspan=1)

        # # label.pack(side="top", fill="both", expand=True)
        # label.grid(row=2, column=0, columnspan=1)

        ####################################
        # icon display
        self.pdf_t = PdfToolbox()
        #
        # python_image = self.file_icon_build()
        # self.icon = tkinter.Label(self.tabview_t.tab("commands"), image=python_image)
        # self.icon.grid(row=1, column=0, padx=(20, 0), pady=(20, 0), sticky='N')

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self.tabview_t.tab("commands"), width=250, height=80)
        t_colspan = 1
        t_rowspan = 6
        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="N", columnspan=t_colspan, rowspan=t_rowspan)

        ####################################
        # list PDFs
        self.button_ls_pdfs = customtkinter.CTkButton(
            master=self.tabview_t.tab("commands"),
            text='List Pdfs',
            command=self.display_pdf_listing
        )
        self.button_ls_pdfs.grid(row=2, column=0, padx=(20, 0), pady=(20, 0), sticky='N')


        ####################################
        # display info
        self.button_display_pdf_info = customtkinter.CTkButton(
            master=self.tabview_t.tab("commands"),
            text='Display PDF Info',
            command=lambda: self.display_info()
        )
        self.button_display_pdf_info.grid(row=3, column=0, padx=(20, 0), pady=(20, 0))

        ####################################
        # create pages
        self.button_create_pages = customtkinter.CTkButton(
            master=self.tabview_t.tab("commands"),
            text='Create Pages',
            command=self.split_execute
        )
        self.button_create_pages.grid(row=4, column=0, padx=(20, 0), pady=(20, 0))

        ####################################
        # merge pages
        self.button_merge_pages = customtkinter.CTkButton(
            master=self.tabview_t.tab("commands"),
            text='Merge Pages',
            command=self.merge_pages
        )
        self.button_merge_pages.grid(row=5, column=0, padx=(20, 0), pady=(20, 0))

        ####################################
        # refresh listings
        self.button_combine_pages = customtkinter.CTkButton(
            master=self.tabview_t.tab("commands"),
            text='Refresh Listings',
            command=self.refresh_listings
        )
        self.button_combine_pages.grid(row=6, column=0, padx=(20, 0), pady=(20, 0))

        ####################################
        # file manager
        #####################################
        self.tabview_files = customtkinter.CTkTabview(
            master=self.tabview_t.tab("commands"),
            width=5)

        self.tabview_files.grid(row=0, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew", rowspan=6)

        self.tabview_files.add("file listing")  # add tab at the end
        self.tabview_files.add  ("page listing")  # add tab at the end
        self.tabview_files.add("combo listing")  # add tab at the end
        self.tabview_files.add("icon view")  # add tab at the end

        self.tabview_files.set("icon view")  # set currently visible tab

        # file listing
        self.file_list_scrollable_frame = customtkinter.CTkScrollableFrame(
            master=self.tabview_files.tab("file listing"),
            label_text="PDF File Listing")
        self.file_list_scrollable_frame.grid(row=1, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

        self.file_list_scrollable_frame.grid_columnconfigure(0, weight=1)
        self.f_scrollable_frame_switches = []
        row = 0
        s_lst = self.get_listing()
        # print(f's_listing: {s_lst}')
        for f in s_lst:
            switch_name = customtkinter.CTkSwitch(master=self.file_list_scrollable_frame, text=f"{f}")
            switch_name.grid(row=row, column=0, padx=10, pady=(0, 20))
            row += 1
            self.f_scrollable_frame_switches.append(switch_name)
        # print(f'switches: {self.f_scrollable_frame_switches}')

        # page listing
        self.page_listing_frame = customtkinter.CTkScrollableFrame(
            master=self.tabview_files.tab("page listing"),
            label_text="PDF Pages")
        self.page_listing_frame.grid(row=1, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.pages_refresh()

        # icon view
        # print(f'icon view')
        self.icon_listing_frame = customtkinter.CTkScrollableFrame(
            master=self.tabview_files.tab("icon view"),
            label_text="Icon View")
        self.icon_listing_frame.grid(row=0, column=2, padx=(20, 0), pady=(20, 0))

        self.icon_listing_frame_switches = []

        # build image
        icon_img = Image.open(W_ICON)
        icon_resize = icon_img.resize((50, 50))
        display_img = ImageTk.PhotoImage(icon_resize, width=50)
        print(f'icon_img: {icon_img} :: display_img: {display_img}')
        i_lst = self.get_pages_listing()

        # icon file listing
        i_row = 0
        for i in i_lst:
            self.icon_img_lbl = tkinter.Label(
                self.icon_listing_frame,
                text=f'{i}',
                # image=display_img,
                compound=tkinter.LEFT,
                bg='grey',
                fg='white',
                padx=10
            )
            self.icon_img_lbl.grid(row=i_row, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")

            # # switch_name = customtkinter.CTkCheckBox(master=self.icon_listing_frame, text=f"{i}")
            # switch_name = customtkinter.CTkSwitch(master=self.icon_listing_frame, text=f"{i}")
            # switch_name.grid(row=i_row, column=0, padx=10, pady=(0, 20))
            # self.icon_listing_frame_switches.append(switch_name)

            i_row += 1

        ####################################
        # combo listing
        self.combo_listing_frame = customtkinter.CTkScrollableFrame(master=self.tabview_files.tab("combo listing"), label_text="Combo PDF")
        self.combo_listing_frame.grid(row=1, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.combo_listing_frame.grid_columnconfigure(0, weight=1)
        self.combo_refresh()

        #######################################
        # USER FLOW
        #######################################
        # self.pdf_user_flow = PdfToolbox()
        #
        # # display 'pages'
        # pagesList = self.pdf_user_flow.list_pages_dir()
        # print(pagesList)
        #
        # print(f'APP_FRAME_WIDTH: {APP_FRAME_WIDTH}')
        #
        # u_style = ttk.Style(self)
        # u_style.configure('u_pageListFrame.TFrame', width=APP_FRAME_WIDTH, height=APP_FRAME_HEIGHT, background=PALETTE_DARK)
        #
        # # TODO: display list of current files
        # pageListFrame = ttk.Frame(self, style='u_pageListFrame.TFrame')
        # # pageListFrame = ttk.Frame(self)
        # pageListFrame.grid(row=0, column=0, sticky='NW')
        #
        # # page listing
        # self.page_listing_frame = customtkinter.CTkScrollableFrame(
        #     master=self.tabview_files.tab("page listing"),
        #     label_text="PDF Pages")
        # self.page_listing_frame.grid(row=1, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        # self.pages_refresh()
        #
        U_WIDTH = APP_FRAME_WIDTH - 150
        U_HEIGHT = APP_FRAME_HEIGHT - 250

        self.u_tabview_files = customtkinter.CTkTabview(
            master=self.tabview_t.tab("user flow"),
            width=5)
        self.u_tabview_files.configure(width=U_WIDTH)

        self.u_tabview_files.grid(row=0, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew", rowspan=6)

        self.u_tabview_files.add ("PDF page listing")  # add tab at the end
        self.u_tabview_files.add("TST combo listing")  # add tab at the end
        self.u_tabview_files.add("TST icon view")  # add tab at the end

        self.u_tabview_files.set("PDF page listing")  # set currently visible tab

        # page listing
        self.u_page_listing_frame = customtkinter.CTkScrollableFrame(
            master=self.u_tabview_files.tab("PDF page listing"),
            label_text="PDF Pages Listing",
            width=U_WIDTH,
            height=U_HEIGHT
        )
        self.u_page_listing_frame.grid(row=0, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.u_pages_icon_refresh()

        ####################################
        # merge pages
        self.u_button_merge_pages = customtkinter.CTkButton(
            master=self.tabview_t.tab("user flow"),
            text='Merge Pages',
            command=self.merge_pages
        )
        self.u_button_merge_pages.grid(row=5, column=0, padx=(20, 0), pady=(20, 0))

        # # TODO: file icons - display as image of file
        # # TODO: file icons - generate image based on contents
        # # TODO: use file icons in display listing
        # # TODO: Enable drab'n'drop
        # # TODO: generate combo file based pn select/sort settings


    def u_pages_refresh(self):
        # print(f'in pages_refresh')
        self.u_page_listing_frame.grid_columnconfigure(0, weight=1)
        self.u_page_listing_frame_switches = []
        row = 0
        u_pages_lst = self.get_pages_listing()
        # print(f'c_lst: {c_lst}')
        for f in u_pages_lst:
            # print(f'f:{f}')
            u_switch_name = customtkinter.CTkSwitch(master=self.u_page_listing_frame, text=f"{f}")
            u_switch_name.grid(row=row, column=0, padx=10, pady=(0, 20))
            row += 1
            self.u_page_listing_frame_switches.append(u_switch_name)
        # print(f'switches: {self.scrollable_frame_switches}')

    def u_pages_icon_refresh(self):
        print(f'in u_pages_icon_refresh')
        self.u_page_listing_frame.grid_columnconfigure(0, weight=1)
        self.u_page_listing_frame_switches = []
        # row = 0
        u_row = 0
        u_col = 2
        col_index = 0
        u_pages_lst = self.get_pages_listing()
        # print(f'c_lst: {c_lst}')
        for f in u_pages_lst:
            # print(f'f:{f}')
            if col_index >= u_col:
                col_index = 0
                u_row += 1
            u_switch_name = customtkinter.CTkSwitch(master=self.u_page_listing_frame, text=f'u_row: {u_row} :: u_col: {col_index} :: NEW: {f}')
            u_switch_name.grid(row=u_row, column=col_index, padx=10, pady=(0, 20))
            self.u_page_listing_frame_switches.append(u_switch_name)

            col_index += 1

    def refresh_listings(self):
        self.refresh_f_listings()
        self.combo_refresh()
        self.pages_refresh()

    def merge_pages(self):
        print(f'c_ui:merge_pages:merge_pages')
        outfile = f'{self.user_entry.get()}'
        print(f'c_ui:outfile: {outfile}')
        if len(outfile) == 0:
            print(f'no Entry')
            self.textbox.delete("0.0", "end")  # delete all text
            out_txt = 'No Entry'
            self.textbox.insert("0.0", out_txt)
        else:
            print(f'merge_pages:outfile: {outfile}')
            selection = self.get_page_selection()
            print(f'merge_pages:selection: {selection}')
            self.pdf_t.merge_files(selection, outfile)
            c_lst_frame = self.combo_listing_frame.grid_columnconfigure(0, weight=1)
            self.combo_refresh()
            # FileMgr.combo_refresh(c_lst_frame)

    def get_page_selection(self):
        listing = self.pdf_t.list_pages_dir()
        # print(f'get_page_selection:listing[]: {listing}')
        selection = []
        for i in range(len(listing)):
            is_selected = self.page_listing_frame_switches[i].get()
            # print(f'get_page_selection:is_selected: {is_selected} :: file: {listing[i]}')
            if is_selected == 1:
                selection.append(listing[i])
        # print(f'get_page_selection:selection[]: {selection}')
        return selection

    def split_execute(self):
        listing = self.pdf_t.list_pdf_dir()
        selection = []
        for i in range(len(self.f_scrollable_frame_switches)):
            is_selected = self.f_scrollable_frame_switches[i].get()
            if is_selected == 1:
                selection.append(listing[i])

        # print(f'split_execute:selection: {selection}')

        for selected in selection:
            # selection = f'{selection}'
            # print(f'split_execute:selection: {selection}')
            self.pdf_t.split_pdf_into_pages(selected, f'{selected}_split')
            # return True

        self.pages_refresh()

    def get_pages_listing(self):
        listing = self.pdf_t.list_pages_dir()
        return listing

    def get_combo_listing(self):
        listing = self.pdf_t.list_combo_dir()
        return listing

    def combo_refresh(self):
        self.combo_listing_frame.grid_columnconfigure(0, weight=1)
        self.combo_listing_frame_switches = []
        row = 0
        c_lst = self.get_combo_listing()
        # print(f'c_lst: {c_lst}')
        for f in c_lst:
            print(f'f:{f}')
            switch_name = customtkinter.CTkSwitch(master=self.combo_listing_frame, text=f"{f}")
            switch_name.grid(row=row, column=0, padx=10, pady=(0, 20))
            row += 1
            self.combo_listing_frame_switches.append(switch_name)
        # print(f'switches: {self.scrollable_frame_switches}')

    def pages_refresh(self):
        # print(f'in pages_refresh')
        self.page_listing_frame.grid_columnconfigure(0, weight=1)
        self.page_listing_frame_switches = []
        row = 0
        c_lst = self.get_pages_listing()
        # print(f'c_lst: {c_lst}')
        for f in c_lst:
            # print(f'f:{f}')
            switch_name = customtkinter.CTkSwitch(master=self.page_listing_frame, text=f"{f}")
            switch_name.grid(row=row, column=0, padx=10, pady=(0, 20))
            row += 1
            self.page_listing_frame_switches.append(switch_name)
        # print(f'switches: {self.scrollable_frame_switches}')


    def get_listing(self):
        listing = self.pdf_t.list_pdf_dir()
        # print(f'get_listing:listing: {listing}')
        return listing

    def file_icon_build(self):
        icon_img = Image.open(W_ICON)
        icon_resize = icon_img.resize((50, 50))
        # print(f'file_icon_build:icon_resize: {icon_resize}')
        python_img = ImageTk.PhotoImage(icon_resize, width=50)
        return python_img

    def display_pdf_listing(self):
        listing = self.pdf_t.list_pdf_dir()
        # print(f'display_pdf_listing: {listing}')
        self.display_listing(listing)

    def display_listing(self, lst):
        # print(f'display_pdf_listing:lst: {lst}')
        out_txt = ''
        for f in lst:
            out_txt += f'{f}\n'
        self.textbox.delete("0.0", "end")  # delete all text
        self.textbox.insert("0.0", out_txt)

    def display_info(self):
        # print('display_info')
        self.textbox.delete("0.0", "end")  # delete all text
        listing = self.pdf_t.list_pdf_dir()
        # print(f'display_info:listing: {listing}')
        selection = []
        for i in range(len(self.f_scrollable_frame_switches)):
            is_selected = self.f_scrollable_frame_switches[i].get()
            if is_selected == 1:
                selection.append(listing[i])
        self.display_listing(selection)
        # print(f'display_info:selection: {selection}')



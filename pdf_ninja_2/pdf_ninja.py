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

from pdf2image import convert_from_path

from tkinter import filedialog as fd


customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

COL_SPAN = 5
PDF_DIR = './pdf_files'
FILES_C_WIDTH = 900
FILES_C_HEIGHT = 200

# window geometry
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


class PdfApp(Page):

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        # -------------- STYLING --------------
        s = ttk.Style(self)
        s.configure('ninjaFrame.TFrame', background=PALETTE_DARK)

        # s.configure('ninjaFrame.TFrame', width=APP_FRAME_WIDTH)
        # s.configure('ninjaFrame.TFrame', height=APP_FRAME_HEIGHT)

        ninjaFrame = tk.Frame(self)
        # ninjaFrame.configure(style='ninjaFrame.TFrame')
        ninjaFrame.configure(
            width=APP_FRAME_WIDTH,
            height=APP_FRAME_HEIGHT,
            bg=MAIN_BACKGROUND_COLOR,
        )
        # ninjaFrame.columnconfigure(0, weight=3)
        # ninjaFrame.columnconfigure(1, weight=1)
        # ninjaFrame.columnconfigure(2, weight=1)
        ninjaFrame.grid(row=0, column=0, sticky='NSEW')

        ##################################
        # controls tab
        self.tabview_t = customtkinter.CTkTabview(
            master=ninjaFrame,
            bg_color=PALETTE_DARK,
            width=APP_FRAME_WIDTH,
            height=APP_FRAME_HEIGHT
        )
        # self.tabview_t.grid(row=0, column=0, padx=(20, 0), pady=(20, 0), rowspan=1, sticky='W')
        # self.tabview_t.configure(bg='blue')
        self.tabview_t.grid(row=0, column=0, padx=0, pady=0, rowspan=1, sticky='NSEW')

        self.tabview_t.add("New Combo")  # add tab at the end
        self.tabview_t.add("Re-Order Combo")  # add tab at the end

        # set default tab
        # self.tabview_t.set("New Combo")  # set currently visible tab
        self.tabview_t.set("Re-Order Combo")  # set currently visible tab


        # icon display
        self.pdf_t = PdfToolbox()

        self.nj_user_support_textbox()

        self.load_file_frame = customtkinter.CTkFrame(
            master=self.tabview_t.tab("New Combo"),
            width=200,
            height=200,
            fg_color=ICON_BACKGROUND_COLOR
        )
        self.load_file_frame.grid(row=0, column=0, padx=(0, 0), pady=(0, 0))

        self.nj_support_load_pdf_btn()

        self.nj_support_generate_pages_btn()


        ####################################
        # file manager
        #####################################
        self.tabview_files = customtkinter.CTkTabview(
            master=self.tabview_t.tab("New Combo"),
            width=SUPPORT_CONTAINER_WIDTH,
            height=SUPPORT_CONTAINER_HEIGHT,
        )
        self.tabview_files.grid(row=0, column=2, padx=(0, 0), pady=(0, 0), sticky="nsew", rowspan=6)

        self.tabview_files.add("Input PDF")  # add tab at the end
        self.tabview_files.add("Pages Listing")  # add tab at the end
        self.tabview_files.add("List Combos")  # add tab at the end
        self.tabview_files.add("icon view")  # add tab at the end

        self.tabview_files.set("Input PDF")  # set currently visible tab

        self.nj_support_pdf_listing()

        self.nj_support_pages_listing()

        self.nj_support_combo_listing()

        self.nj_support_icon_listing()

        #######################################
        # USER FLOW
        #######################################
        self.u_tabview_files = customtkinter.CTkTabview(
            master=self.tabview_t.tab("Re-Order Combo"),
            width=1000,
            height=1000)
        self.u_tabview_files.configure(width=U_WIDTH)
        self.u_tabview_files.grid(row=0, column=0, padx=(0, 0), pady=(0, 0), sticky="nsew", rowspan=1)

        self.u_tabview_files.add("PDF Infiles Listing")  # add tab at the end
        self.u_tabview_files.add("PDF Combo")  # add tab at the end
        self.u_tabview_files.add("TST icon view")  # add tab at the end

        # set default tab
        # self.u_tabview_files.set("PDF Combo")  # set currently visible tab
        self.u_tabview_files.set("PDF Combo")  # set currently visible tab

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#         self.u_tabview_files("PDF Combo") #.grid_columnconfigure(0, weight=1)
        # self.page_listing_frame.grid_columnconfigure(0, weight=1)

        self.support_container_frame = tk.Frame(
            master=self.u_tabview_files.tab("PDF Combo"),
            width=100,
            height=100,
            bg='pink'
        )
        # self.support_container_frame.configure(
        #     # width=APP_FRAME_WIDTH,
        #     # height=APP_FRAME_HEIGHT,
        #     width=1000,
        #     height=1000,
        #     bg='blue'
        #     # bg=HEADER_BACKGROUND_COLOR
        # )
        self.support_container_frame.grid(row=2, column=0, columnspan=1, padx=(0, 0), pady=(20, 20), sticky='ew')

        self.u_tabview_files.tab("PDF Combo").grid_columnconfigure(0, weight=1)

        self.support_operations_bottom_frame = tk.Frame(
            master=self.u_tabview_files.tab("PDF Combo"),
            bg='grey',
            width=960,
            height=50,
        )
        self.support_operations_bottom_frame.grid(row=1, column=0, columnspan=1, padx=(0, 0), pady=(5, 5), sticky='nsew')

        self.support_operations_top_frame = tk.Frame(
            master=self.u_tabview_files.tab("PDF Combo"),
            bg='blue',
            width=960,
            height=50,
            # width=1000,
            # height=50,
        )
        self.support_operations_top_frame.grid(row=0, column=0, columnspan=1, padx=(0, 0), pady=(0, 0), sticky='nsew')

        # top control bar - DASHBOARD
        # self.dnd_sort_list_control_bar = tk.Frame(
        #     master=self.u_tabview_files.tab("PDF Infiles Listing"),
        #     width=1000,
        #     height=1000,
        #     bg='black'
        # )
        # self.dnd_sort_list_control_bar.grid(row=5, column=0, columnspan=1, padx=(0, 0), pady=(0, 0))

        self.nj_user_dashboard_dnd_infiles_frame()

    def full_wash_cycle(self):
        print(f'\nfull_wash_cycle')
        self.load_PDF_file()

        print(f'full_wash_cycle:gen pdf pages')
        self.gen_pdf_pages_from_all_infiles()

        print(f'full_wash_cycle: building combo')
        self.build_combo_all()

        print(f'full_wash_cycle: building combo pages')
        self.gen_all_combo_pages_from_combo()

        print(f'full_wash_cycle: building combo pages images')
        combo_pages_listing = self.get_combo_pages_listing()
        combo_pages_in_dir = COMBO_PAGES_DIR
        self.refresh_all_combo_pages_images(combo_pages_listing, combo_pages_in_dir)

        # refreshing dnd listing
        self.combo_sort_refresh()


    ############################
    # DASHBOARD FUNCTIONS
    #
    def nj_user_dashboard_combo_infiles_listing(self):
        # combo_sort_listing_frame
        # combo_sort_infiles_listing_frame
        self.combo_sort_infiles_listing_frame = customtkinter.CTkScrollableFrame(
            master=self.support_operations_bottom_frame,
            label_text="Combo Infiles Listing - DASH",
            # width=COMBO_LISTING_FRAME_WIDTH,
            # height=COMBO_LISTING_FRAME_HEIGHT,
            # style='comboInfilesListingFrame.TFrame'
            width=SUPPORT_LISTINGS_WIDTH,
            height=SUPPORT_LISTINGS_HEIGHT,
        )
        self.combo_sort_infiles_listing_frame.grid(row=0, column=0, padx=(5, 5), pady=(5, 5), sticky='we')
        self.combo_sort_infiles_listing_frame_switches = []

        self.combo_infiles_refresh()

    def nj_user_dashboard_combo_pages_listing(self):
        self.combo_pages_listing_frame = customtkinter.CTkScrollableFrame(
            master=self.support_operations_bottom_frame,
            label_text="Combo Page Listing",
            # width=COMBO_LISTING_FRAME_WIDTH,
            # height=COMBO_LISTING_FRAME_HEIGHT,
            width=SUPPORT_LISTINGS_WIDTH,
            height=SUPPORT_LISTINGS_HEIGHT,
        )
        self.combo_pages_listing_frame.grid(row=0, column=1, padx=(0, 5), pady=(0, 0), sticky='w')
        self.combo_pages_listing_frame_switches = []

        self.combo_pages_refresh()

        # self.combo_refresh()

    def nj_user_dashboard_combo_pages_image_listing(self):
        self.disp_combo_images_frame = customtkinter.CTkScrollableFrame(
            master=self.support_operations_bottom_frame,
            label_text="Combo Page Image Listing",
            # width=COMBO_LISTING_FRAME_WIDTH,
            # height=COMBO_LISTING_FRAME_HEIGHT,
            fg_color=PALETTE_DARK,
            width=SUPPORT_LISTINGS_WIDTH,
            height=SUPPORT_LISTINGS_HEIGHT,
        )
        self.disp_combo_images_frame.grid(row=0, column=2, padx=(0, 5), pady=(0, 0), sticky="")
        self.disp_combo_images_frame_switches = []

        self.combo_images_refresh()

#cccccccccccccccccccccccccccccccccccc


    def nj_user_dashboard_refresh_combo_infiles_btn(self):
        # refesh combo infiles listing
        self.refresh_combo_infiles_btn = customtkinter.CTkButton(
            master=self.support_operations_top_frame,
            width=100,
            text='Refresh Combo Infiles',
            command=self.combo_infiles_refresh
        )
        self.refresh_combo_infiles_btn.grid(row=0, column=1, padx=(0, 10), pady=(0, 0))

    def nj_user_dashboard_generate_combo_pages_btn(self):
        # split combo selection
        self.combo_split_pages_btn = customtkinter.CTkButton(
            master=self.support_container_frame,
            width=10,
            text='Generate Combo Pages - SUPPORT',
            command=self.gen_combo_pages_from_combo
        )
        self.combo_split_pages_btn.grid(row=0, column=1, padx=(10, 10), pady=(10, 10))
    #
    # def nj_user_dashboard_generate_combo_pages_all_btn(self):
    #     # split combo selection
    #     self.combo_split_pages_all_btn = customtkinter.CTkButton(
    #         master=self.combo_dnd_operations,
    #         width=10,
    #         text='Generate Combo Pages - ALL',
    #         command=self.gen_all_combo_pages_from_combo
    #     )
    #     self.combo_split_pages_all_btn.grid(row=1, column=2, padx=(0, 5), pady=(0, 0))

    def nj_user_dashboard_refresh_combo_pages_btn(self):
        self.refresh_combo_pages_btn = customtkinter.CTkButton(
                master=self.support_container_frame,
                text='Refresh Combo Pages Listing - SUPPORT',
                command=self.combo_pages_refresh
        )
        self.refresh_combo_pages_btn.grid(row=0, column=2, padx=(5, 0), pady=(0, 0))

#wwwwwwwwwwwwwwwww
    def nj_user_support_refresh_combo_pages_btn(self):
        self.support_refresh_combo_pages_btn = customtkinter.CTkButton(
                master=self.support_operation_bottom_frame,
                text='Refresh Combo Pages Listingxxxx',
                command=self.combo_pages_refresh
        )
        self.support_refresh_combo_pages_btn.grid(row=0, column=2, padx=(5, 0), pady=(0, 0))

    def nj_dashboard_merge_combo_pages_btn(self):
        # create new combo from selection
        self.combo_merge_pages_btn = customtkinter.CTkButton(
            master=self.combo_dnd_merge_file_entry,
            width=10,
            text='Merge Final Pages',
            command=self.build_combo_output
        )
        self.combo_merge_pages_btn.grid(row=1, column=1, padx=(5, 5), pady=(5, 5))

    def nj_dashboard_combo_filename_entry(self):
        self.combo_filename_entry = customtkinter.CTkEntry(
            master=self.combo_filename_dnd_entry,
            placeholder_text="combo filename")
        self.combo_filename_entry.grid(row=1, column=0, padx=(5, 5), pady=(5, 5), sticky='N')

    def nj_user_dashboard_build_combo_all_btn(self):
        # assemble combo
        self.button_merge_pages = customtkinter.CTkButton(
            master=self.combo_filename_dnd_entry,
            text='Build Combo',
            command=self.build_combo_all
        )
        self.button_merge_pages.grid(row=2, column=0, padx=(5, 5), pady=(5, 5))

    def nj_dashboard_full_wash_cycle_btn(self):
        self.full_wash_cycle_btn = customtkinter.CTkButton(
            master=self.combo_dnd_operations,
            text='Full Wash Cycle',
            command=self.full_wash_cycle
        )
        self.full_wash_cycle_btn.grid(row=0, column=2, padx=(0, 0), pady=(5, 0))

    def nj_dashboard_generate_gen_pdf_from_selected_btn(self):
        # create new combo from selection
        self.combo_group_pages_btn = customtkinter.CTkButton(
            master=self.combo_dnd_operations,
            width=10,
            text='Gen Doc based on Selection',
            command=self.gen_pdf_from_selected_pages
        )
        self.combo_group_pages_btn.grid(row=1, column=0, padx=(5, 5), pady=(5, 5))

    def nj_dashboard_load_pdf_btn(self):
        self.load_pdf_file_btn = customtkinter.CTkButton(
            master=self.combo_dnd_operations,
            text='Load PDF File xxx',
            command=self.load_PDF_file
        )
        self.load_pdf_file_btn.grid(row=0, column=0, padx=(0, 0), pady=(5, 0))

    def nj_dashboard_generate_gen_pdf_from_selected_btn(self):
        # create new combo from selection
        self.combo_group_pages_btn = customtkinter.CTkButton(
            master=self.combo_dnd_operations,
            width=10,
            text='Gen Doc based on Selection',
            command=self.gen_pdf_from_selected_pages
        )
        self.combo_group_pages_btn.grid(row=1, column=0, padx=(5, 5), pady=(5, 5))

    def nj_dashboard_refresh_combo_btn(self):
        print(f'nj_dashboard_refresh_combo_btn')
        self.refresh_combo_pages_btn = customtkinter.CTkButton(
                master=self.combo_dnd_operations,
                text='Refresh Combo Pages  -- Listing',
                command=self.combo_pages_refresh
        )
        self.refresh_combo_pages_btn.grid(row=0, column=1, padx=(5, 5), pady=(5, 5))
    #
    # def nj_dashboard_refresh_combo_pages_images_btn(self, combo_pages_listing, combo_pages_in_dir):
    #     # combo_pages_in_dir = COMBO_PAGES_DIR
    #     # refresh combo_pages images
    #     self.refresh_combo_images_btn = customtkinter.CTkButton(
    #         master=self.combo_dnd_operations,
    #         text='Refresh Combo Pages Images xxx',
    #         command=lambda: self.refresh_combo_pages_images(combo_pages_listing, combo_pages_in_dir)
    #     )
    #     self.refresh_combo_images_btn.grid(row=1, column=1, columnspan=1, padx=(5, 5), pady=(5, 5))
    #
    # def nj_support_refesh_combo_pages_images_btn(self, combo_pages_listing, combo_pages_in_dir):
    #     # combo_pages_in_dir = COMBO_PAGES_DIR
    #     # refresh combo_pages images
    #     self.operations_refresh_combo_images_btn = customtkinter.CTkButton(
    #         master=self.combo_infiles_operation_frame,
    #         text='Refresh Combo Pages Imagesxxxxxx',
    #         command=lambda: self.refresh_combo_pages_images(combo_pages_listing, combo_pages_in_dir)
    #     )
    #     self.operations_refresh_combo_images_btn.grid(row=0, column=0, columnspan=1, padx=(5, 5), pady=(5, 5))

    def nj_dashboard_combo_operations_frame(self):
        #
        # self.combo_infiles_top_bar_operation_frame = customtkinter.CTkFrame(
        #     master=self.u_tabview_files.tab("PDF Combo"),
        #     width=100,
        #     height=100,
        #     # fg_color=ICON_BACKGROUND_COLOR,
        #     fg_color='cyan',
        # )
        # self.combo_infiles_top_bar_operation_frame.grid(row=0, column=0, columnspan=1, padx=(0, 0), pady=(0, 0))

        #
        # self.support_container_frame = tk.Frame(
        #     master=self.u_tabview_files.tab("PDF Combo"),
        #     width=200,
        #     height=500,
        #     bg=BRANDING_BACKGROUND
        # )
        # self.support_container_frame.grid(row=2, column=0, columnspan=3, padx=(0, 0), pady=(20, 20))

## ttttttttttttttttttttttttttttttttttttttttttttt

        # self.support_operation_bottom_frame = tk.Frame(
        #     master=self.combo_listing_frame,
        #     # width=APP_FRAME_WIDTH,
        #     # height=APP_FRAME_HEIGHT,
        #     width=100,
        #     height=50,
        #     bg='purple'
        # )
        # self.support_operation_bottom_frame.grid(row=2, column=0, columnspan=1, padx=(20, 20), pady=(15, 15), sticky='ew')

        self.nj_user_dashboard_refresh_combo_infiles_btn()

        self.nj_user_dashboard_generate_combo_pages_btn()

        self.nj_user_dashboard_refresh_combo_pages_btn()

        self.nj_user_dashboard_refresh_combo_pages_images_btn()

        self.nj_user_support_refresh_combo_pages_images_btn()

    def nj_user_dashboard_refresh_combo_pages_images_btn(self):
        combo_pages_listing = self.get_combo_pages_listing()
        combo_pages_in_dir = COMBO_PAGES_DIR
        # refresh combo_pages images
        self.refresh_combo_images_btn = customtkinter.CTkButton(
            master=self.support_container_frame,
            text='Refresh Combo Pages Images - DB',
            command=lambda: self.refresh_combo_pages_images(combo_pages_listing, combo_pages_in_dir)
        )
        self.refresh_combo_images_btn.grid(row=0, column=3, columnspan=2, padx=(10, 10), pady=(10, 10))

# oooooooooooooooooooooooooooooooooooo

    def nj_user_support_refresh_combo_pages_images_btn(self):
        combo_pages_listing = self.get_combo_pages_listing()
        combo_pages_in_dir = COMBO_PAGES_DIR
        # refresh combo_pages images
        self.refresh_combo_images_btn = customtkinter.CTkButton(
            master=self.support_operations_top_frame,
            text='Refresh Combo Pages Images - TOP BAR',
            command=lambda: self.refresh_combo_pages_images(combo_pages_listing, combo_pages_in_dir)
        )
        self.refresh_combo_images_btn.grid(row=0, column=0, columnspan=1, padx=(10, 10), pady=(10, 10))

    def nj_user_dashboard_combo_sort_operations_frame_btn(self):
        self.combo_dnd_operations = tk.Frame(
            master=self.dashboard_operations_bottom,
            bg='yellow'
        )
        self.combo_dnd_operations.grid(row=0, column=2, padx=(5, 5), pady=(5, 5), sticky='N')

        # self.nj_dashboard_load_pdf_btn()

        self.nj_dashboard_generate_gen_pdf_from_selected_btn()

        # self.nj_dashboard_full_wash_cycle_btn()

        # self.nj_dashboard_refresh_combo_btn()

        # self.nj_user_dashboard_generate_combo_pages_all_btn()

        self.nj_user_dashboard_build_combo_all_btn()

        p_listing = self.get_combo_pages_listing()
        p_dir = COMBO_PAGES_DIR
        # self.nj_dashboard_refresh_combo_pages_images_btn(p_listing, p_dir)

    def nj_user_dashboard_build_combo_frame(self):
        # output filename entry btn
        self.final_output_filename_entry = customtkinter.CTkEntry(
            master=self.combo_dnd_merge_file_entry,
            placeholder_text="output file name",
        )
        self.final_output_filename_entry.grid(row=0, column=1, padx=(5, 5), pady=(5, 5))

        self.combo_filename_dnd_entry = tk.Frame(
            master=self.dashboard_operations_bottom,
            bg='pink'
        )
        self.combo_filename_dnd_entry.grid(row=0, column=1, padx=(5, 5), pady=(5, 0), sticky='N')

        self.nj_dashboard_combo_filename_entry()

        self.nj_user_dashboard_combo_sort_operations_frame_btn()
        #
        # self.support_operations_top_frame = tk.Frame(
        #     master=self.combo_listing_frame,
        #     width=900,
        #     height=100,
        #     bg='black',
        # )
        # self.support_operations_top_frame.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky='ew')
        #
        # self.support_operations_bottom_1_frame = tk.Frame(
        #     master=self.combo_listing_frame,
        #     width=100,
        #     height=100,
        #     bg='green',
        # )
        # self.support_operations_bottom_1_frame.grid(row=4, column=0, padx=(5, 5), pady=(5, 5), sticky='ew')

        self.top_dashboard_listings_frame = tk.Frame(
            master=self.combo_listing_frame,
            width=10,
            height=10,
            bg='black',
        )
        self.top_dashboard_listings_frame.grid(row=1, column=0, padx=(5, 5), pady=(5, 5), sticky='ew')


 #qqqqqqqqqqqqqqqqqqqqqqqqqqqq

        self.nj_user_dashboard_combo_infiles_listing()

        self.nj_user_dashboard_combo_pages_listing()

        self.nj_user_dashboard_combo_pages_image_listing()

        # self.combo_dnd_pages_refresh()

        self.combo_sort_refresh()

        self.nj_dashboard_combo_operations_frame()

    def nj_user_dashboard_dnd_infiles_frame(self):
        self.dashboard_listing_frame = tk.Frame(
            master=self.u_tabview_files.tab("PDF Infiles Listing"),
            width=50,
            height=50,
            bg='orange'
         )
        self.dashboard_listing_frame.grid(row=0, column=0, padx=(0, 0), pady=(0, 0), sticky="ew")

        #




        self.nj_support_sort_list_frame()

        self.nj_user_dashboard_sort_operations_frame()

    def nj_user_dashboard_sort_operations_frame(self):

        self.nj_user_dashboard_combo_listing_frame()

        self.dashboard_operations_bottom = tk.Frame(
            master=self.u_tabview_files.tab("PDF Infiles Listing"),
            bg='black',
        )
        self.dashboard_operations_bottom.grid(row=2, column=0, padx=(5, 5), pady=(5, 5), sticky='nsew')

        self.dashboard_operations_top = tk.Frame(
            master=self.u_tabview_files.tab("PDF Infiles Listing"),
            # width=DND_TOPBAR_HEIGHT,
            # height=DND_TOPBAR_HEIGHT,
            width=1000,
            height=1000,
            bg='black',
        )
        self.dashboard_operations_top.grid(row=0, column=0, padx=(5, 5), pady=(5, 5), sticky='nsew')

       # load pdf btn
        self.topbar_load_pdf_file_btn = customtkinter.CTkButton(
            master=self.dashboard_operations_top,
            text='Load PDF File - DASH',
            command=self.load_PDF_file
        )
        self.topbar_load_pdf_file_btn.grid(row=0, column=0, padx=(5, 5), pady=(5, 5), sticky='nsew')

       # load gen pages from pdf_infiles
        self.topbar_gen_pages_from_pdf_infiles_btn = customtkinter.CTkButton(
            master=self.dashboard_operations_top,
            text='Generate PDF Pages',
            command=self.gen_pdf_pages_from_all_infiles
        )
        self.topbar_gen_pages_from_pdf_infiles_btn.grid(row=0, column=1, padx=(5, 5), pady=(5, 5), sticky='nsew')

        # load gen combo_infiles
        self.topbar_gen_combo_infiles_all_btn = customtkinter.CTkButton(
            master=self.dashboard_operations_top,
            text='Generate Combo Infiles',
            command=self.build_combo_all

        )
        self.topbar_gen_combo_infiles_all_btn.grid(row=0, column=2, padx=(5, 5), pady=(5, 5), sticky='nsew')

        # load gen combo_pages from combo_infiles
        self.topbar_gen_combo_pages_from_pdf_infiles_btn = customtkinter.CTkButton(
            master=self.dashboard_operations_top,
            text='Generate Combo Pages - DASHBOARD',
            command=self.gen_all_combo_pages_from_combo
        )
        self.topbar_gen_combo_pages_from_pdf_infiles_btn.grid(row=0, column=3, padx=(5, 5), pady=(5, 5), sticky='nsew')

#qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq

        # load gen combo_images from combo_pages
        combo_pages_listing = self.get_combo_pages_listing()
        combo_pages_in_dir = COMBO_PAGES_DIR
        self.topbar_gen_combo_images_from_combo_infiles_btn = customtkinter.CTkButton(
            master=self.dashboard_operations_top,
            text='Generate Combo Images',
            command=lambda: self.refresh_combo_pages_images(combo_pages_listing, combo_pages_in_dir)
        )
        self.topbar_gen_combo_images_from_combo_infiles_btn.grid(row=0, column=4, padx=(5, 5), pady=(5, 5))

        # run full was cycle
        self.topbar_full_was_cycle_btn = customtkinter.CTkButton(
            master=self.dashboard_operations_top,
            text='full Wash Cycle',
            command=self.full_wash_cycle
        )
        self.topbar_full_was_cycle_btn.grid(row=0, column=5, padx=(5, 5), pady=(5, 5))

        ####################################
        # OPERATIONS

        self.nj_user_dashboard_merge_file_entry_frame()

#qqqqqqqqqqqqqqq
    def nj_user_dashboard_combo_listing_frame(self):
        # pdf_combo
        self.combo_listing_frame = tk.Frame(
            master=self.support_container_frame,
            bg='red',
            # width=APP_FRAME_WIDTH,
            # height=APP_FRAME_HEIGHT,
            width=970,
            height=50,
        )
        self.combo_listing_frame.columnconfigure(0, weight=1)
        # self.combo_listing_frame.grid(row=0, column=0, padx=(5, 5), pady=(5, 5), sticky='', columnspan=1)
        self.combo_listing_frame_switches = []

    def nj_user_dashboard_merge_file_entry_frame(self):

        self.combo_dnd_merge_file_entry = tk.Frame(
            master=self.dashboard_operations_bottom,
            bg='red'
        )
        self.combo_dnd_merge_file_entry.grid(row=0, column=0, padx=(5, 5), pady=(5, 5), sticky='N')

        self.nj_dashboard_merge_combo_pages_btn()

        self.nj_user_dashboard_build_combo_frame()

    ############################
    # SUPPORT FUNCTIONS

    def nj_user_support_textbox(self):
        # create textbox
        self.textbox = customtkinter.CTkTextbox(
            self.tabview_t.tab("New Combo"),
            width=250,
            height=80)

        t_colspan = 1
        t_rowspan = 6
        self.textbox.grid(row=10, column=0, padx=(0, 0), pady=(0, 0), sticky="N", columnspan=t_colspan, rowspan=t_rowspan)

    def nj_support_pdf_listing(self):
        print(f'nj_support_pdf_listing\n')
        # file Input PDF
        self.file_list_scrollable_frame = customtkinter.CTkScrollableFrame(
            master=self.tabview_files.tab("Input PDF"),
            label_text="Input PDF File Listing",
            width=CMD_FILE_LISTING_WIDTH,
        )
        self.file_list_scrollable_frame.grid(row=1, column=1, padx=(0, 0), pady=(0, 0), sticky="nsew")
        # self.file_list_scrollable_frame.grid_columnconfigure(0, weight=1)
        self.file_list_scrollable_frame_switches = []
        #
        # ensure pdf listing update
        self.refresh_pdf_infiles_listing()

    def nj_support_pages_listing(self):
        # page listing
        self.page_listing_frame = customtkinter.CTkScrollableFrame(
            master=self.tabview_files.tab("Pages Listing"),
            label_text="PDF Pages",
            width=CMD_FILE_LISTING_WIDTH
        )
        self.page_listing_frame.grid(row=1, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")

        listing = self.pdf_pages_refresh()

    def nj_support_combo_listing(self):
        ####################################
        # 'command' combo listing
        self
        self.combo_list_combos_frame = customtkinter.CTkScrollableFrame(
            master=self.tabview_files.tab("List Combos"),
            label_text="Combo PDF Listing",
            width=CMD_FILE_LISTING_WIDTH
        )
        self.combo_list_combos_frame.grid(row=1, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        # self.combo_list_combos_frame.grid_columnconfigure(0, weight=1)

        self.combo_refresh()

    def nj_support_icon_listing(self):
        # icon view
        # print(f'icon view')
        self.icon_listing_frame = customtkinter.CTkScrollableFrame(
            master=self.tabview_files.tab("icon view"),
            label_text="Icon View",
            width=CMD_FILE_LISTING_WIDTH
        )
        self.icon_listing_frame.grid(row=0, column=2, padx=(20, 0), pady=(20, 0))
        self.icon_listing_frame_switches = []

    def nj_support_load_pdf_btn(self):
        #################################
        # load pdf frame
        #
        # load pdf btn
        self.load_pdf_file_btn = customtkinter.CTkButton(
            master=self.load_file_frame,
            text='Load PDF File',
            command=self.full_wash_cycle
        )
        self.load_pdf_file_btn.grid(row=1, column=0, padx=(0, 0), pady=(5, 0))

    def nj_support_generate_pages_btn(self):
        # generate pages btn
        self.generate_pdf_pages_btn = customtkinter.CTkButton(
            master=self.load_file_frame,
            text='Generate Pages',
            command=self.gen_pdf_pages_from_infile
        )
        self.generate_pdf_pages_btn.grid(row=2, column=0, padx=(0, 0), pady=(5, 0))

    def nj_support_sort_list_frame(self):
        # main sort window
        self.dashboard_listing_frame = customtkinter.CTkScrollableFrame(
            # master=self.dashboard_listing_frame,
            master=self.u_tabview_files.tab("PDF Infiles Listing"),
            label_text="Combo DnD Sort Listing",
            fg_color='red',
            width=DND_LISTING_WIDTH,
            height=DND_LISTING_HEIGHT,
        )
        self.dashboard_listing_frame.configure(scrollbar_button_color='red')
        self.dashboard_listing_frame.grid(row=1, column=0, padx=(0, 0), pady=(0, 0), sticky="nsew")
        self.dashboard_listing_frame_switches = []








    def load_PDF_file(self):
        # self.refresh_f_listings()
        print(f'in load_PDF_file')

        # get entry value
        # load_pdf_file_name = f'{self.load_file_entry.get()}'

        load_pdf_file = fd.askopenfilename()
        # print(f'loading: {load_pdf_file}')

        # read input file'
        try:
            with open(load_pdf_file, 'rb') as in_img:
                pdf_contents = in_img.read()
                # print(f'pdf_contents: {pdf_contents}')
        except:
            print(f'unable to open: {load_pdf_file}')

        # write local infile
        out_split = load_pdf_file.split('/')[-1]
        # print(f'out_split: {out_split}')

        pdf_save_file = f'{PDF_INFILES}/{out_split}'
        # print(f'pdf_save_file: {pdf_save_file}')
        try:
            with open(pdf_save_file, 'wb') as save_file:
                save_file.write(pdf_contents)
        except FileNotFoundError:
            print(f'unable to save file: {pdf_save_file}')
        # print(f'load_PDF_file:calling display_pdf_listing')
        self.refresh_pdf_infiles_listing()

    def build_combo(self):
        print(f'##############xxx######### in build_combo')
        outfile = f'{self.combo_filename_entry.get()}'
        print(f'build_combo:outfile: {outfile}')

        if len(outfile) == 0:
            print(f'build_combo:no Entry')
            self.textbox.delete("0.0", "end")  # delete all text
            out_txt = 'No Entry'
            self.textbox.insert("0.0", out_txt)
        else:
            print(f'build_combo:outfile: {outfile}')
            print(f'build_combo:selection: {outfile}')
            if len(outfile) == 0:
                print(f'No Pages Selected...')
            else:
                selection = self.get_page_selection()
                print(f'build_combo:selection: {selection}')
                self.pdf_t.merge_files(selection, outfile)
                # c_lst_frame = self.combo_listing_frame.grid_columnconfigure(0, weight=1)
                # self.combo_refresh()
                # FileMgr.combo_refresh(c_lst_frame)
        print(f'xxxxxxxxxx-#####-xxxxxxxx: build_combo: calling combo refresh')
        self.combo_refresh()
    #
    # def build_combo_all(self):
    #     print(f'in \n#####################################################################\n################build_combo_all')

    def build_combo_all(self):
        print(f'in \n#####################################################################\n################build_combo_all')
        # outfile = f'{self.combo_filename_entry.get()}'
        outfile = f'system_combo_workfile.pdf'
        print(f'build_combo_all:outfile: {outfile}')

        if len(outfile) == 0:
            print(f'build_combo_all:no Entry')
            self.textbox.delete("0.0", "end")  # delete all text
            out_txt = 'No Entry'
            self.textbox.insert("0.0", out_txt)
        else:
            print(f'build_combo_all:outfile: {outfile}')
            print(f'build_combo_all:selection: {outfile}')
            if len(outfile) == 0:
                print(f'No Pages Selected...')
            else:
                selection = self.get_page_all_selected()
                print(f'build_combo_all:selection: {selection}')
                self.pdf_t.merge_files(selection, outfile)
                # c_lst_frame = self.combo_listing_frame.grid_columnconfigure(0, weight=1)
                # self.combo_refresh()
                # FileMgr.combo_refresh(c_lst_frame)
        print(f'xxxxxxxxxx-#####-xxxxxxxx: build_combo_all: calling combo refresh')
        self.combo_refresh()

    def build_combo_output(self):
        print(f'in build_combo_output')
        outfile = f'{self.final_output_filename_entry.get()}'
        print(f'yy:build_combo_output:outfile: {outfile}')

        if len(outfile) == 0:
            print('No Ouput File')
            return

        if len(outfile) == 0:
            # print(f'no Entry')
            self.textbox.delete("0.0", "end")  # delete all text
            out_txt = 'No Entry'
            self.textbox.insert("0.0", out_txt)
        else:
            # print(f'merge_pages:outfile: {outfile}')
            selection = self.get_page_selection()
            print(f'merge_pages:selection: {outfile}')
            if len(outfile) == 0:
                print(f'No Pages Selected...')
            else:
                self.pdf_t.merge_files(selection, outfile)
                # c_lst_frame = self.combo_listing_frame.grid_columnconfigure(0, weight=1)
                self.combo_refresh()
                # FileMgr.combo_refresh(c_lst_frame)

        self.combo_refresh()

    def pdf_pages_refresh(self):
        # print(f'in pages_refresh')
        # self.page_listing_frame.grid_columnconfigure(0, weight=1)
        self.page_listing_frame_switches = []
        row = 0

        c_lst = self.get_pages_listing()

        for f in c_lst:
            # print(f'pdf_pages_refresh:pages_refresh:f:{f}')
            switch_name = customtkinter.CTkSwitch(master=self.page_listing_frame, text=f"{f}")
            switch_name.grid(row=row, column=0, padx=10, pady=(0, 20))
            row += 1
            self.page_listing_frame_switches.append(switch_name)
        # print(f'switches: {self.scrollable_frame_switches}')
        # print(f'pages_refresh:switches: switch complete')
        # print(f'pages_refresh:c_lst: {c_lst}')
        return c_lst

    def combo_pages_refresh(self):
        # print(f'\ncombo_pages_refresh')
        # self.combo_pages_listing_frame.grid_columnconfigure(0, weight=1)
        self.combo_pages_listing_frame_switches = []
        row = 0
        combo_lst = self.get_combo_pages_listing()
        # print(f'combo_pages_refresh:combo_lst: {combo_lst}')

        s = ttk.Style(self)
        s.configure('switchFrame.TFrame', background=PALETTE_LIGHTEST)
        # s.configure('comboInfilesListingFrame.TFrame', background=PALETTE_LIGHTEST)

        for combo in combo_lst:
            # print(f'combo_pages_refresh:combo:{combo}')
            switch_name = customtkinter.CTkSwitch(
                master=self.combo_pages_listing_frame,
                text=f"{combo}",
                fg_color='yellow',
            )
            switch_name.grid(row=row, column=0, padx=(5, 5), pady=(5, 5))
            row += 1
            self.combo_pages_listing_frame_switches.append(switch_name)

    def combo_images_refresh(self):
        print(f'\ncombo_images_refresh')
        # self.disp_combo_images_frame.grid_columnconfigure(0, weight=1)
        self.disp_combo_images_frame_switches = []
        row = 0
        combo_lst = self.get_combo_images_listing()
        print(f'combo_pages_refresh:combo_lst: {combo_lst}')

        s = ttk.Style(self)
        s.configure('comboImagesFrame.TFrame', background=PALETTE_LIGHTEST)
        # s.configure('comboInfilesListingFrame.TFrame', background=PALETTE_LIGHTEST)

        combo_pages_image_frame = ttk.Frame(
            master=self.disp_combo_images_frame,
        )
        combo_pages_image_frame.grid(row=row, column=0, padx=(0, 0), pady=(0, 20))

        for combo in combo_lst:
            # print(f'combo_images_refresh:combo:{combo}')
            sz_w = COMBO_ICON_WIDTH
            sz_h = int(sz_w * 1.41)

            icon_img = Image.open(f'{COMBO_IMAGES_DIR}/{combo}').resize((sz_w, sz_h))
            photo_img = ImageTk.PhotoImage(icon_img)

            combo_pages_image_label = customtkinter.CTkLabel(
                master=self.disp_combo_images_frame,
                image=photo_img,
                width=100,
                text=combo,
                fg_color='green',
                compound='top'
            )
            combo_pages_image_label.grid(row=row, column=0, padx=(0, 0), pady=(0, 20))
            #
            # switch_name = customtkinter.CTkSwitch(
            #     master=self.disp_combo_images_frame,
            #     text='',
            #     # text=f"{combo}",
            #     fg_color='yellow',
            # )
            # switch_name.grid(row=row, column=1, padx=0, pady=(0, 20))
            # self.disp_combo_images_frame_switches.append(switch_name)

            row += 1

    def combo_sort_refresh(self):
        print(f'\ncombo_sort_refresh')
        # self.combo_sort_listing_frame.grid_columnconfigure(0, weight=1)

        combo_lst = self.get_combo_images_listing()
        combo_pages_lst = self.get_combo_pages_listing()

        # print(f'combo_sort_refresh:combo_lst: {combo_lst}')
        # print(f'combo_sort_refresh:combo_pages_lst: {combo_pages_lst}')

        s = ttk.Style(self)
        s.configure('comboImagesFrame.TFrame', background=PALETTE_LIGHTEST)
        # s.configure('comboInfilesListingFrame.TFrame', background=PALETTE_LIGHTEST)

        row = 0

# qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq
        self.combo_sort_image_frame = tk.Frame(
            master=self.dashboard_listing_frame,
            bg='navy',
         )
        self.combo_sort_image_frame.grid(row=row, column=0, padx=(20, 20), pady=(20, 20))

        g_row = 0
        g_col = 0
        num_rows = 4
        num_cols = COMBO_DND_LISTING_NUM_COLS
        for combo in combo_pages_lst:
            print(f'combo_sort_refresh:combo:{combo}')

            combo_img = f'{combo}.png'
            # print(f'combo_sort_refresh:combo_img: {combo_img}')

            if g_col >= num_cols:
                g_col = 0
                g_row += 1

            sz_w = COMBO_ICON_WIDTH
            sz_h = int(sz_w * 1.41)

            icon_img = Image.open(f'{COMBO_IMAGES_DIR}/{combo_img}').resize((sz_w, sz_h))
            photo_img = ImageTk.PhotoImage(icon_img)

            self.combo_entry_frame = tk.Frame(
                master=self.combo_sort_image_frame,
                bg='magenta',
            )
            self.combo_entry_frame.grid(row=g_row, column=g_col, padx=(5, 5), pady=(5, 5))

            combo_display_name = combo.split('.')[0]
            # print(f'combo_sort_refresh:combo_display_name: {combo_display_name}')

            combo_sort_label_frame = customtkinter.CTkLabel(
                master=self.combo_entry_frame,
                image=photo_img,
                width=50,
                text=combo_display_name,
                fg_color='green',
                compound='top'
            )
            # print(f'label complete...combo: {combo}')
            combo_sort_label_frame.grid(row=0, column=0, padx=(10, 10), pady=(10, 10))

            combo_sort_switch_name = customtkinter.CTkSwitch(
                master=self.combo_entry_frame,
                text='',
                # text=f"{combo}",
                width=10,
                fg_color='yellow',
            )
            combo_sort_switch_name.grid(row=2, column=0, padx=(0, 0), pady=(0, 0))

            self.disp_combo_images_frame_switches.append(combo_sort_switch_name)

            g_col += 1
        g_row += 1

    def combo_infiles_refresh(self):
        print(f'combo_infiles_refresh')
        # self.combo_sort_infiles_listing_frame.grid_columnconfigure(0, weight=1)
        # self.combo_sort_listing_frame_switches = []
        row = 0

        combo_infiles_lst = self.combo_infiles_listing()

        #
        # # print(f'combo_infiles_refresh:combo_infiles_lst: {combo_infiles_lst}')
        # for combo_infile in combo_infiles_lst:
        #     # print(f'combo_infiles_refresh:combo_infile:{combo_infile}')
        #     switch_name = customtkinter.CTkSwitch(
        #         master=self.combo_infiles_listing_frame,
        #         text=f"{combo_infile}",
        #         fg_color='yellow',
        #     )

        for in_file in combo_infiles_lst:
            # print(f'combo_pages_refresh:combo:{combo}')
            switch_name = customtkinter.CTkSwitch(
                master=self.combo_sort_infiles_listing_frame,
                text=f"{in_file}",
                fg_color='yellow',
            )
            switch_name.grid(row=row, column=0, padx=10, pady=(0, 20))
            row += 1
            self.combo_sort_infiles_listing_frame_switches.append(switch_name)

        # print(f'switches: {self.scrollable_frame_switches}')
        # print(f'pages_refresh:switches: switch complete')
        # print(f'pages_refresh:c_lst: {c_lst}')
        return combo_infiles_lst

    def combo_dnd_pages_refresh(self):
        print(f'combo_dnd_pages_refresh')
        # self.combo_sort_listing_frame.grid_columnconfigure(0, weight=1)
        # self.combo_sort_listing_frame_switches = []
        row = 0

        combo_infiles_lst = self.combo_infiles_listing()
        print(f'combo_dnd_pages_refresh:combo_infiles_lst: {combo_infiles_lst}')

        #
        # # print(f'combo_infiles_refresh:combo_infiles_lst: {combo_infiles_lst}')
        # for combo_infile in combo_infiles_lst:
        #     # print(f'combo_infiles_refresh:combo_infile:{combo_infile}')
        #     switch_name = customtkinter.CTkSwitch(
        #         master=self.combo_infiles_listing_frame,
        #         text=f"{combo_infile}",
        #         fg_color='yellow',
        #     )

        for in_file in combo_infiles_lst:
            # print(f'combo_pages_refresh:combo:{combo}')
            switch_name = customtkinter.CTkSwitch(
                master=self.dashboard_listing_frame,
                text=f"{in_file}",
                fg_color='yellow',
            )
            switch_name.grid(row=row, column=0, padx=10, pady=(0, 20))
            row += 1
            self.combo_sort_listing_frame_switches.append(switch_name)

        # print(f'switches: {self.scrollable_frame_switches}')
        # print(f'pages_refresh:switches: switch complete')
        # print(f'pages_refresh:c_lst: {c_lst}')
        return combo_infiles_lst

    def file_icon_build(self):
        icon_img = Image.open(W_ICON)
        icon_resize = icon_img.resize((50, 50))
        # print(f'file_icon_build:icon_resize: {icon_resize}')
        python_img = ImageTk.PhotoImage(icon_resize, width=50)
        return python_img

    def refresh_combo_pages_images(self, listing, in_dir):
        print(f'\nrefresh_combo_images:listing: {listing} ')
        print(f'\nrefresh_combo_images:in_dir: {in_dir} ')

        # self.combo_listing_frame.grid_columnconfigure(0, weight=1)
        self.combo_listing_frame_switches = []

        # in_dir = COMBO_PAGES_DIR
        row = 0
        c_lst = self.get_combo_pages_listing()

        # listing = f'{in_dir}/{c_lst}'

        # print(f'refresh_combo_combo_images:c_lst: {c_lst} ')

        lst = ''
        lst = f'{in_dir}/{c_lst}'
        # print(f'refresh_combo_combo_images:c_lst: {c_lst}')
        # print(f'3:refresh_combo_combo_images:listing[0]: {listing[0]}')
        # print(f'refresh_combo_combo_images:lst: {lst}')
        # listing = self.get_combo_infiles_listing()

        # self.split_combo_combo_into_pages(listing, in_dir)
        # self.split_combo_combo_into_pages()

        # print(f'u_images_lst: {listing}')
        u_page_listing_frame_switches = []

        # define out images
        folder_img = ImageTk.PhotoImage(Image.open(DIR_IMG).resize((35, 35)))
        list_image = ImageTk.PhotoImage(Image.open(LIST_IMG).resize((60, 60)))
        # self.icon_img = ImageTk.PhotoImage(Image.open(ICON_IMG).resize((60, 60)))
        icon_lst = []
        for in_file in c_lst:
            print(f'refresh_combo_combo_images:in_file: {in_file}')
            with open(in_file, 'wb') as in_img:
                f_path = f'{COMBO_PAGES_DIR}/{in_file}'
                print(f'refresh_combo_combo_images:f_path: {f_path}')
                img = convert_from_path(f_path)

                for i in range(len(img)):
                    # Save pages as images in the pdf
                    # save_file = f'{PDF_IMG_DIR}/{img}'
                    save_file = COMBO_IMAGES_DIR + '/' + in_file + '.png'
                    print(f'refresh_combo_combo_images:save_file: {save_file}')

                    # images[i].save('page'+ str(i) +'.jpg', 'JPEG')

                    img[i].save(save_file, 'PNG')

                # icon_img = ImageTk.PhotoImage(Image.open(ICON_IMG).resize((60, 60)))
                # icon_lst.append(icon_img)
                # out_img.write(out_file)

        self.combo_images_refresh()

        self.combo_sort_refresh()

        # print(f'icon_lst: {icon_lst}')

    def refresh_all_combo_pages_images(self, listing, in_dir):
        print(f'refresh_combo_images:listing: {listing} ')

        # self.combo_listing_frame.grid_columnconfigure(0, weight=1)
        self.combo_listing_frame_switches = []

        # in_dir = COMBO_PAGES_DIR
        row = 0
        c_lst = self.get_combo_pages_listing()

        # listing = f'{in_dir}/{c_lst}'

        # print(f'refresh_combo_combo_images:c_lst: {c_lst} ')

        lst = ''
        lst = f'{in_dir}/{c_lst}'
        # print(f'refresh_combo_combo_images:c_lst: {c_lst}')
        # print(f'3:refresh_combo_combo_images:listing[0]: {listing[0]}')
        # print(f'refresh_combo_combo_images:lst: {lst}')
        # listing = self.get_combo_infiles_listing()

        # self.split_combo_combo_into_pages(listing, in_dir)
        # self.split_combo_combo_into_pages()

        # print(f'u_images_lst: {listing}')
        u_page_listing_frame_switches = []

        # define out images
        folder_img = ImageTk.PhotoImage(Image.open(DIR_IMG).resize((35, 35)))
        list_image = ImageTk.PhotoImage(Image.open(LIST_IMG).resize((60, 60)))
        # self.icon_img = ImageTk.PhotoImage(Image.open(ICON_IMG).resize((60, 60)))
        icon_lst = []
        for in_file in c_lst:
            print(f'refresh_combo_combo_images:in_file: {in_file}')

            # if file exists then skip file


            with open(in_file, 'wb') as in_img:
                f_path = f'{COMBO_PAGES_DIR}/{in_file}'
                print(f'refresh_combo_combo_images:f_path: {f_path}')
                img = convert_from_path(f_path)

                for i in range(len(img)):
                    # Save pages as images in the pdf
                    # save_file = f'{PDF_IMG_DIR}/{img}'
                    save_file = COMBO_IMAGES_DIR + '/' + in_file + '.png'
                    print(f'refresh_combo_combo_images:save_file: {save_file}')

                    # images[i].save('page'+ str(i) +'.jpg', 'JPEG')

                    img[i].save(save_file, 'PNG')

                # icon_img = ImageTk.PhotoImage(Image.open(ICON_IMG).resize((60, 60)))
                # icon_lst.append(icon_img)
                # out_img.write(out_file)

        self.combo_images_refresh()

        # print(f'icon_lst: {icon_lst}')

    #
    # def combo_pages_refresh(self):
    #     # print(f'in pages_refresh')
    #     self.disp_combo_files_frame.grid_columnconfigure(0, weight=1)
    #     self.disp_combo_files_frame_switches = []
    #     row = 0
    #
    #     c_lst = self.get_combo_pages_listing()
    #
    #     for f in c_lst:
    #         print(f'combo_pages_refresh:f:{f}')
    #         switch_name = customtkinter.CTkSwitch(master=self.disp_combo_files_frame, text=f"{f}")
    #         switch_name.grid(row=row, column=0, padx=10, pady=(0, 20))
    #         row += 1
    #         self.disp_combo_files_frame_switches.append(switch_name)
    #     # print(f'switches: {self.scrollable_frame_switches}')
    #     # print(f'pages_refresh:switches: switch complete')
    #     # print(f'pages_refresh:c_lst: {c_lst}')
    #     return c_lst

    def gen_pdf_from_selected_pages(self):
        print(f'gen_pdf_from_selected_pages')
        # get selection
        row = 0

        # get list of selected files

        # create & save new pdf with selected pages

        combo_page_lst = self.get_combo_pages_listing()
        print(f'gen_combo_pages_from_combo:combo_page_lst: {combo_page_lst}')

        # which combo infiles have been selected
        selection = []
        row = 0
        for in_file in combo_page_lst:
            # print(f'gen_pdf_from_selected_pages:in_file: {in_file}')
            is_set = self.disp_combo_images_frame_switches[row].get()
            # is_set = 1
            # print(f'gen_pdf_from_selected_pages:is_set: {is_set} ::  row: {row}')
            # print(f'gen_pdf_from_selected_pages:in_file: {in_file}')

            # print(f'is_set:    {is_set} :: infile: {infile}')
            if is_set:
                selection.append(in_file)
            row += 1
        print(f'gen_combo_pages_from_combo:selection: {selection}')

        # generate output pdf
        for combo_infile in selection:
            combo_infile = f'{combo_infile}'
            name_of_split = f'{combo_infile}-page'
            in_dir = COMBO_INFILES_DIR
            out_dir = COMBO_OUTPUT_DIR
            # print(f'out_dir: {out_dir}')

            # print(f'gen_pdf_pages_from_infile:combo_infile: {combo_infile}')
            self.pdf_t.split_combo_infiles_2_pages(
                combo_infile,
                name_of_split,
                in_dir,
                out_dir
            )

            print(f'gen_combo_pages_from_combo: calling combo_images_refresh')
            self.combo_pages_refresh()
            # self.combo_images_refresh()

    def gen_combo_pages_from_combo(self):
        print(f'\ngen_combo_pages_from_combo')
        # get selection
        row = 0

        combo_infiles_lst = self.combo_infiles_listing()
        print(f'gen_combo_pages_from_combo:combo_infiles_lst: {combo_infiles_lst}')

        # which combo infiles have been selected
        selection = []
        row = 0
        for in_file in combo_infiles_lst:
            is_set = self.combo_sort_infiles_listing_frame_switches[row].get()
            print(f'gen_combo_pages_from_combo:is_set: {is_set}')
            print(f'gen_combo_pages_from_combo:in_file: {in_file}')

            # print(f'is_set:    {is_set} :: infile: {infile}')
            if is_set:
                selection.append(in_file)
            row += 1

        # print(f'gen_combo_pages_from_combo:selection: {selection}')
        # generate combo_pages from selected combo_infiles
        for combo_infile in selection:
            combo_infile = f'{combo_infile}'
            name_of_split = f'{combo_infile}-path'
            in_dir = COMBO_INFILES_DIR
            out_dir = COMBO_PAGES_DIR
            # print(f'out_dir: {out_dir}')

            # print(f'gen_pdf_pages_from_infile:combo_infile: {combo_infile}')
            self.pdf_t.split_combo_infiles_2_pages(
                combo_infile,
                name_of_split,
                in_dir,
                out_dir
            )

            print(f'gen_combo_pages_from_combo: calling combo_images_refresh')
            self.combo_pages_refresh()
            # self.combo_images_refresh()

    def gen_all_combo_pages_from_combo(self):
        print(f'\ngen_all_combo_pages_from_combo')
        # get selection
        row = 0

        combo_infiles_lst = self.combo_infiles_listing()
        print(f'gen_all_combo_pages_from_combo:combo_infiles_lst: {combo_infiles_lst}')

        # which combo infiles have been selected
        selection = []
        row = 0
        for in_file in combo_infiles_lst:
            is_set = 1
            # is_set = self.combo_sort_infiles_listing_frame_switches[row].get()
            print(f'gen_all_combo_pages_from_combo:is_set: {is_set}')
            print(f'gen_all_combo_pages_from_combo:in_file: {in_file}')

            # print(f'is_set:    {is_set} :: infile: {infile}')
            if is_set:
                selection.append(in_file)
            row += 1

        # print(f'gen_all_combo_pages_from_combo:selection: {selection}')
        # generate combo_pages from selected combo_infiles
        for combo_infile in selection:
            combo_infile = f'{combo_infile}'
            name_of_split = f'{combo_infile}-path'
            in_dir = COMBO_INFILES_DIR
            out_dir = COMBO_PAGES_DIR
            # print(f'out_dir: {out_dir}')

            # print(f'gen_all_combo_pages_from_combo:combo_infile: {combo_infile}')
            self.pdf_t.split_combo_infiles_2_pages(
                combo_infile,
                name_of_split,
                in_dir,
                out_dir
            )

            print(f'gen_all_combo_pages_from_combo: calling combo_images_refresh')
            self.combo_pages_refresh()
            # self.combo_images_refresh()

    def gen_pdf_pages_from_infile(self):
        print(f'in gen_pdf_pages_from_infile')

        # get selection
        row = 0

        pdf_infiles_list = self.pdf_infiles_listing()
        # print(f'pdf_infiles_list: {pdf_infiles_list}')

        selection = []
        row = 0
        for infile in pdf_infiles_list:
            # test if set
            is_set = self.file_list_scrollable_frame_switches[row].get()
            # print(f'is_set: {is_set} :: infile: {infile}')
            if is_set:
                selection.append(infile)
            row += 1

        print(f'selection: {selection}')

        #TODO enforce as least one selection

        # for each of selection
            # split into pages & save to pdf_pages directory

        for pdf_infile in selection:
            pdf_file = f'{pdf_infile}'
            print(f'gen_pdf_pages_from_infile:pdf_file: {pdf_file}')
            name_of_split = f'{pdf_file}-split'
            in_dir = PDF_INFILES
            out_dir = PDF_PAGES
            # print(f'out_dir: {out_dir}')
            print(f'gen_pdf_pages_from_infile:pdf_file 2: {pdf_file}')

            self.pdf_t.split_pdf_infiles_2_pages(
                pdf_file,
                name_of_split,
                in_dir,
                out_dir
            )

            self.pdf_pages_refresh()

    def gen_pdf_pages_from_all_infiles(self):
        print(f'\nXXX:gen_pdf_pages_from_all_infiles')

        # get selection
        row = 0

        pdf_infiles_list = self.pdf_infiles_listing()
        # print(f'pdf_infiles_list: {pdf_infiles_list}')

        selection = []
        row = 0
        for infile in pdf_infiles_list:
            # test if set
            is_set = 1
            # is_set = self.file_list_scrollable_frame_switches[row].get()
            # print(f'is_set: {is_set} :: infile: {infile}')
            if is_set:
                print(f'gen_pdf_pages_from_all_infiles: {infile}')
                selection.append(infile)
            row += 1

        print(f'gen_pdf_pages_from_all_infiles:selection: {selection}')

        #TODO enforce as least one selection

        # for each of selection
            # split into pages & save to pdf_pages directory

        for pdf_infile in selection:
            pdf_file = f'{pdf_infile}'
            print(f'gen_pdf_pages_from_all_infiles:pdf_file: {pdf_file}')
            name_of_split = f'{pdf_file}-split'
            in_dir = PDF_INFILES
            out_dir = PDF_PAGES
            # print(f'out_dir: {out_dir}')
            print(f'gen_pdf_pages_from_all_infiles:pdf_file: {pdf_file}')

            self.pdf_t.split_pdf_infiles_2_pages(
                pdf_file,
                name_of_split,
                in_dir,
                out_dir
            )

            self.pdf_pages_refresh()
    #
    # def gen_pdf_pages_from_all_infiles(self):
    #     print(f'in gen_pdf_pages_from_all_infiles')
    #
    #     # get selection
    #     row = 0
    #
    #     pdf_infiles_list = self.pdf_infiles_listing()
    #     # print(f'pdf_infiles_list: {pdf_infiles_list}')
    #
    #     selection = []
    #     row = 0
    #     for infile in pdf_infiles_list:
    #         # test if set
    #         is_set = self.file_list_scrollable_frame_switches[row].get()
    #         # print(f'is_set: {is_set} :: infile: {infile}')
    #         if is_set:
    #             selection.append(infile)
    #         row += 1
    #
    #     print(f'selection: {selection}')
    #
    #     #TODO enforce as least one selection
    #
    #     # for each of selection
    #         # split into pages & save to pdf_pages directory
    #
    #     for pdf_infile in selection:
    #         pdf_file = f'{pdf_infile}'
    #         print(f'gen_pdf_pages_from_infile:pdf_file: {pdf_file}')
    #         name_of_split = f'{pdf_file}-split'
    #         in_dir = PDF_INFILES
    #         out_dir = PDF_PAGES
    #         # print(f'out_dir: {out_dir}')
    #         print(f'gen_pdf_pages_from_infile:pdf_file 2: {pdf_file}')
    #
    #         self.pdf_t.split_pdf_infiles_2_pages(
    #             pdf_file,
    #             name_of_split,
    #             in_dir,
    #             out_dir
    #         )
    #
    #         self.pdf_pages_refresh()

    def refresh_pdf_infiles_listing(self):
        row = 0
        pdf_infiles_list = self.pdf_infiles_listing()

        # pdf_infiles_listing
        # print(f's_lst: {s_lst}')
        for in_file in pdf_infiles_list:
            switch_name = customtkinter.CTkSwitch(master=self.file_list_scrollable_frame, text=f"{in_file}")
            switch_name.grid(row=row, column=0, padx=10, pady=(0, 20))
            row += 1
            self.file_list_scrollable_frame_switches.append(switch_name)
        # print(f'switches: {self.f_scrollable_frame_switches}')

    def refresh_pdf_pages_listing(self):
        row = 0
        s_lst = self.display_pdf_listing()
        # print(f's_lst: {s_lst}')
        for f in s_lst:
            switch_name = customtkinter.CTkSwitch(master=self.file_list_scrollable_frame, text=f"{f}")
            switch_name.grid(row=row, column=0, padx=10, pady=(0, 20))
            row += 1
            self.file_list_scrollable_frame_switches.append(switch_name)
        # print(f'switches: {self.f_scrollable_frame_switches}')

    def refresh_combo_pages_listing(self):
        row = 0
        s_lst = self.display_pdf_listing()
        # print(f's_lst: {s_lst}')
        for f in s_lst:
            switch_name = customtkinter.CTkSwitch(master=self.file_list_scrollable_frame, text=f"{f}")
            switch_name.grid(row=row, column=0, padx=10, pady=(0, 20))
            row += 1
            self.file_list_scrollable_frame_switches.append(switch_name)
        # print(f'switches: {self.f_scrollable_frame_switches}')

    def refresh_combo_combo_listing(self, listing, frame):
        print(f'refresh_combo_combo_listing:listing: {listing}')
        self.test_combo_combo_listing(
            listing,
            COMBO_INFILES_DIR,
            COMBO_IMAGES_DIR,
            self.disp_combo_files_frame)
        # print(f'refresh_combo_combo_listing:listing: {listing}')

    def refresh_listings(self):
        # self.refresh_f_listings()
        self.combo_refresh()
        self.display_pdf_listing()
        self.combo_refresh()
        self.display_pdf_listing()

    def refresh_combo_listing(self):
        listing = self.get_pages_listing()
        # print(f'refresh_combo_listing:listing: {listing}')
        u_page_listing_frame_switches = []

        # define out images
        folder_img = ImageTk.PhotoImage(Image.open(DIR_IMG).resize((35, 35)))
        list_image = ImageTk.PhotoImage(Image.open(LIST_IMG).resize((60, 60)))
        # self.icon_img = ImageTk.PhotoImage(Image.open(ICON_IMG).resize((60, 60)))
        icon_lst = []
        for in_file in listing:
            with open(in_file, 'w') as in_img:

                # print(f'convert file: {PAGES_DIR}/{in_file}')
                img = convert_from_path(f'{PAGES_DIR}/{in_file}')

                for i in range(len(img)):
                    # print(f'in_file: {in_file} :: {img[i]}')

                    # Save pages as images in the pdf
                    # save_file = f'{PDF_IMG_DIR}/{img}'
                    save_file = IMAGES_DIR + '/' + in_file + '.png'
                    # print(f'save_file: {save_file}')

                    # images[i].save('page'+ str(i) +'.jpg', 'JPEG')

                    img[i].save(save_file, 'PNG')

                # icon_img = ImageTk.PhotoImage(Image.open(ICON_IMG).resize((60, 60)))
                # icon_lst.append(icon_img)
                # out_img.write(out_file)

        # print(f'icon_lst: {icon_lst}')

        u_row_idx = 0
        u_col_idx = 0
        num_cols = 3
        for p_img in listing:
            if u_col_idx >= num_cols:
                u_col_idx = 0
                u_row_idx += 1

            # OUT_FILE = f'{PDF_IMG_DIR}/{p_img}'
            # IMG_FILE = f'{PDF_IMG_DIR}/{p_img}'
            # IN_FILE = f'{PAGES_DIR}/{p_img}'

            # Create a photoimage object of the image in the path

            sz_w = 60
            sz_h = int(sz_w*1.41)
            load_file = IMAGES_DIR + '/' + p_img + '.png'

            # print(f'load_file: {load_file}')

            icon_img = Image.open(load_file).resize((sz_w, sz_h))
            photo_img = ImageTk.PhotoImage(icon_img)
            pdf_lbl = tkinter.Label(image=photo_img)
            pdf_lbl.image = photo_img
            # label1.grid(row=u_row, column=0, padx=10, pady=(0, 20))
            #
            # u_switch_name = customtkinter.CTkSwitch(master=self.image_listing_frame, text=IN_FILE)
            # u_switch_name.grid(row=u_row_idx, column=u_col_idx, padx=10, pady=(0, 20))
            # u_page_listing_frame_switches.append(u_switch_name)

            u_img_lbl = tkinter.Label(
                master=self.disp_combo_files_frame,
                image=pdf_lbl.image,
                # image=self.list_image,
                text=load_file,
                compound='top',
                fg='white',
                # background='grey',
                # width=100
                background='#2b2b2b'
            )
            u_img_lbl.grid(row=u_row_idx, column=u_col_idx, padx=10, pady=(0, 20))
            u_col_idx += 1

    def u_combo_listing_refresh(self):
        print('u_combo_listing_refresh')
        # self.combo_sort_listing_frame.grid_columnconfigure(0, weight=1)
        # self.co = []
        row = 0
        c_lst = self.get_combo_infiles_listing()
        # print(f'u_combo_listing_refresh:c_lst: {c_lst}')
        for f in c_lst:
            # print(f'u_combo_listing_refresh:f:{f}')
            switch_name = customtkinter.CTkSwitch(master=self.disp_combo_files_frame, text=f"{f}")
            switch_name.grid(row=row, column=0, padx=10, pady=(0, 20))
            row += 1
            self.combo_combo_listing_frame_switches.append(switch_name)

    def u_combo_combo_listing_refresh(self):
        print('################# in u_combo_combo_listing_refresh')
        # self.disp_combo_files_frame.grid_columnconfigure(0, weight=1)
        # self.combo_combo_listing_frame_switches = []
        row = 0
        c_lst = self.get_combo_infiles_listing()
        # print(f'u_combo_listing_refresh:c_lst: {c_lst}')
        for f in c_lst:
            # print(f'u_combo_listing_refresh:f:{f}')
            switch_name = customtkinter.CTkSwitch(master=self.combo_pages_listing_frame, text=f"{f}")
            switch_name.grid(row=row, column=0, padx=10, pady=(0, 20))
            row += 1
            self.combo_listing_frame_switches.append(switch_name)

    def u_pages_icon_refresh(self):
        u_pages_lst = self.get_pages_listing()
        print(f'u_pages_icon_refresh:u_images_lst: {u_pages_lst}')
        u_page_listing_frame_switches = []

        # define out images
        folder_img = ImageTk.PhotoImage(Image.open(DIR_IMG).resize((35, 35)))
        list_image = ImageTk.PhotoImage(Image.open(LIST_IMG).resize((60, 60)))
        # self.icon_img = ImageTk.PhotoImage(Image.open(ICON_IMG).resize((60, 60)))
        icon_lst = []
        for in_file in u_pages_lst:
            with open(in_file, 'w') as in_img:

                # print(f'convert file: {PAGES_DIR}/{in_file}')
                img = convert_from_path(f'{PAGES_DIR}/{in_file}')

                for i in range(len(img)):
                    # print(f'in_file: {in_file} :: {img[i]}')

                    # Save pages as images in the pdf
                    # save_file = f'{PDF_IMG_DIR}/{img}'
                    save_file = './pdf_files/pdf_images/' + in_file + '.png'
                    # print(f'save_file: {save_file}')

                    # images[i].save('page'+ str(i) +'.jpg', 'JPEG')

                    img[i].save(save_file, 'PNG')

                # icon_img = ImageTk.PhotoImage(Image.open(ICON_IMG).resize((60, 60)))
                # icon_lst.append(icon_img)
                # out_img.write(out_file)

        # print(f'icon_lst: {icon_lst}')

        u_row_idx = 0
        u_col_idx = 0
        num_cols = 3
        for p_img in u_pages_lst:
            if u_col_idx >= num_cols:
                u_col_idx = 0
                u_row_idx += 1
            OUT_FILE = f'{PDF_IMG_DIR}/{p_img}'
            IMG_FILE = f'{PDF_IMG_DIR}/{p_img}'
            IN_FILE = f'{PAGES_DIR}/{p_img}'

            # Create a photoimage object of the image in the path

            sz_w = 60
            sz_h = int(sz_w*1.41)
            load_file = './pdf_files/pdf_images/' + p_img + '.png'

            # print(f'load_file: {load_file}')

            icon_img = Image.open(load_file).resize((sz_w, sz_h))
            photo_img = ImageTk.PhotoImage(icon_img)
            # pdf_lbl = tkinter.Label(image=photo_img)
            # pdf_lbl.image = photo_img
            # label1.grid(row=u_row, column=0, padx=10, pady=(0, 20))

            u_switch_name = customtkinter.CTkSwitch(master=self.combo_listing_frame, text=IN_FILE)
            u_switch_name.grid(row=u_row_idx, column=u_col_idx, padx=10, pady=(0, 20))
            u_page_listing_frame_switches.append(u_switch_name)

            u_img_lbl = tkinter.Label(
                master=self.combo_listing_frame,
                image=photo_img,
                # image=self.list_image,
                text=load_file,
                compound='top',
                fg='white',
                # background='grey',
                # width=100
                background='#2b2b2b'
            )
            u_img_lbl.grid(row=u_row_idx, column=u_col_idx, padx=10, pady=(0, 20))
            u_col_idx += 1

    def combo_refresh(self):
        # print(f'in combo_refresh')
        # self.combo_list_combos_frame.grid_columnconfigure(0, weight=1)
        self.combo_list_combos_frame_switches = []
        row = 0
        combo_lst = self.get_combo_listing()
        # print(f'combo_refresh:combo_lst: {combo_lst}')
        for combo in combo_lst:
            # print(f'combo_refresh:-xxx-combo:{combo}')
            switch_name = customtkinter.CTkSwitch(master=self.combo_list_combos_frame, text=f"{combo}")
            switch_name.grid(row=row, column=0, padx=10, pady=(0, 20))
            row += 1
            self.combo_list_combos_frame_switches.append(switch_name)
        # print(f'combo_refresh:switches: {self.combo_listing_frame_switches}')

    def combo_combo_refresh(self):
        print(f'in combo_combo_refresh')
        # self.combo_pages_listing_frame.grid_columnconfigure(0, weight=1)
        self.combo_listing_frame_switches = []
        row = 0
        combo_lst = self.get_combo_listing()
        print(f'combo_refresh:combo_lst: {combo_lst}')
        for combo in combo_lst:
            print(f'combo:{combo}')
            switch_name = customtkinter.CTkSwitch(master=self.combo_pages_listing_frame, text=f"{combo}")
            switch_name.grid(row=row, column=0, padx=10, pady=(0, 20))
            row += 1
            self.combo_listing_frame_switches.append(switch_name)

    def test_combo_combo_listing(self, listing, in_dir, image_dir, out_frame):
        print(f'in test_combo_combo_listing')
        # listing = self.get_combo_infiles_listing()
        # print(f'test_combo_combo
        # listing:listing[0]: {listing[0]}')
        # image_file_test = image_dir + '/' + listing[0] + '.png'
        self.split_combo_combo_into_pages()
        # if pmg file(s) exist give option to skip
        print(f'11:test_combo_combo_listing:listing {listing}')
        # print(f'test_combo_combo_listing:listing[0] {listing[0]}')

        if len(listing) == 0:
            print(f'8:test_combo_combo_listing:listing:EMPTY')
            image_file_test = ''
        else:
            print(f'8:test_combo_combo_listing:image_dir: {image_dir}')
            image_file_test = image_dir + '/' + listing[0] + '.png'
            print(f'9:test_combo_combo_listing:image_file_test: {image_file_test}')
            # print(f'test_combo_combo_listing:listing[0]: {listing[0]}')


        print(f'6: ################ : test_combo_combo_listing:image_file_test: {image_file_test}')

        try:
            with open(image_file_test, 'r') as img_tst:
                print(f'10:test_combo_combo_listing:image_file_test: {img_tst} ALREADY EXISTS')
        except FileNotFoundError:
            print(f'test_combo_combo_listing:image_file_test 2: {image_file_test} DOES NOT EXIST')
            self.refresh_combo_combo_images(listing, in_dir)

            u_row_idx = 0
            u_col_idx = 0
            num_cols = 3
            for p_img in listing:
                if u_col_idx >= num_cols:
                    u_col_idx = 0
                    u_row_idx += 1
                #
                # OUT_FILE = f'{PDF_IMG_DIR}/{p_img}'
                # IMG_FILE = f'{PDF_IMG_DIR}/{p_img}'
                # IN_FILE = f'{PAGES_DIR}/{p_img}'

                # Create a photoimage object of the image in the path

                sz_w = COMBO_ICON_WIDTH
                sz_h = int(sz_w*1.41)
                load_file = image_dir + '/' + p_img + '.png'
                # print(f'test_combo_combo_listing:load_file: {load_file}')
                # print(f'test_combo_combo_listing:image_dir: {image_dir}')
                # print(f'test_combo_combo_listing:p_img: {p_img}')
                # load_file_txt = load_file}'
                # print(f'test_combo_combo_listing:load_file_txt: {load_file_txt}: load_file: {load_file}')

                # load_file = f'COMBO_INFILES_DIR/{listing[0]}

                icon_img = Image.open(load_file).resize((sz_w, sz_h))
                photo_img = ImageTk.PhotoImage(icon_img)
                pdf_lbl = tkinter.Label(image=photo_img)
                pdf_lbl.image = photo_img
                # label1.grid(row=u_row, column=0, padx=10, pady=(0, 20))
                #
                # u_switch_name = customtkinter.CTkSwitch(master=self.image_listing_frame, text=IN_FILE)
                # u_switch_name.grid(row=u_row_idx, column=u_col_idx, padx=10, pady=(0, 20))
                # u_page_listing_frame_switches.append(u_switch_name)

                u_img_lbl = tkinter.Label(
                    master=out_frame,
                    image=pdf_lbl.image,
                    # image=self.list_image,
                    text=p_img,
                    compound='top',
                    fg='white',
                    # width=100,
                    # background='grey',
                    background='#2b2b2b'
                )
                u_img_lbl.grid(row=u_row_idx, column=u_col_idx, padx=10, pady=(0, 20))
                u_col_idx += 1

    def display_pdf_listing(self):
        listing = self.pdf_t.list_pdf_dir()
        # print(f'display_pdf_listing:listing: {listing}')
        self.display_listing(listing)
        return listing

    def pdf_infiles_listing(self):
        listing = self.pdf_t.pdf_infiles_listing()
        # print(f'pdf_infiles_listing:listing: {listing}')
        self.display_listing(listing)
        return listing

    def combo_infiles_listing(self):
        listing = self.pdf_t.combo_infiles_listing()
        # print(f'combo_infiles_listing:listing: {listing}')
        self.display_listing(listing)
        return listing

    def display_listing(self, lst):
        # print(f'display_pdf_listing:lst: {lst}')
        out_txt = ''
        for f in lst:
            out_txt += f'{f}\n'
        self.textbox.delete("0.0", "end")  # delete all text
        self.textbox.insert("0.0", out_txt)

    def get_combo_selection(self):
        listing = self.pdf_t.list_combo_dir()
        # print(f'get_combo_selection:listing[]: {listing}')
        selection = []
        for i in range(len(listing)):
            is_selected = self.combo_listing_frame_switches[i].get()
            # print(f'get_page_selection:is_selected: {is_selected} :: file: {listing[i]}')
            if is_selected == 1:
                selection.append(listing[i])
        # print(f'get_page_selection:selection[]: {selection}')
        return selection

    def split_combo_combo_into_pages(self):
        print(f'\nsplit_combo_combo_into_pages')
        listing = self.pdf_t.list_combo_pages_dir()
        print(f'split_combo_combo_into_pages:listing: {listing}')

        selection = []

        # self.combo_pages_listing_frame = customtkinter.CTkScrollableFrame(
        #     master=self.u_tabview_files.tab("PDF Combo"),
        #     label_text="COMBO Re-Order",
        # )
        # self.combo_pages_listing_frame.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="")
        #
        # for i in range(len(self.combo_listing_frame_switches)):
        #     is_selected = self.combo_listing_frame_switches[i].get()
        #     if is_selected == 1:
        #         # print(f'is_selected: {is_selected}')
        #         selection.append(listing[i])

        print(f'split_combo_combo_into_pages:selection: {selection}')

        # print(f'split_execute:selection: {selection}')

        for selected in selection:
            # selection = f'{selection}'
            # print(f'split_execute:selection: {selection}')
            # print(f'split_combo_combo_into_pages:selected: {selected}')
            # print(f'50:split_combo_combo_into_pages:COMBO_INFILES_DIR: {COMBO_INFILES_DIR}')
            # print(f'split_combo_combo_into_pages:calling:split_combo_pdf_into_pages...')

            self.pdf_t.split_combo_pdf_into_pages(
                COMBO_INFILES_DIR,
                selected,
                f'{selected}',
                COMBO_PAGES_DIR
            )
            # print(f'######################')
            # selected, f'{selected}_split', COMBO_INFILES_DIR, COMBO_PAGES_DIR
            # return True

        # self.u_combo_listing_refresh()
        # self.refresh_combo_combo_listing(listing)

        # print(f'refresh_combo_combo_listing:listing: {listing}')

        listing = self.get_combo_combo_pages_listing()
        # print(f'split_combo_combo_into_pages:listing: {listing}')

        # self.refresh_combo_combo_listing(listing, self.user_flow_combo_listing_frame)

        ####################################
        # 'user flow' combo listing
        self.u_combo_combo_listing_refresh()
        # print(f'50:split_combo_combo_into_pages:COMBO_INFILES_DIR: {COMBO_INFILES_DIR}')
        # self.test_combo_combo_listing(
        #     listing,
        #     COMBO_INFILES_DIR,
        #     COMBO_IMAGES_DIR,
        #     self.user_flow_combo_listing_frame)
        # print(f'split_combo_combo_into_pages:listing: {listing}')

    def new_combo_combo_listing(self, listing, in_dir, image_dir, out_frame):
        # listing = self.get_combo_infiles_listing()

        self.refresh_combo_combo_images(listing, in_dir)

        u_row_idx = 0
        u_col_idx = 0
        num_cols = 3
        for p_img in listing:
            if u_col_idx >= num_cols:
                u_col_idx = 0
                u_row_idx += 1
            #
            # OUT_FILE = f'{PDF_IMG_DIR}/{p_img}'
            # IMG_FILE = f'{PDF_IMG_DIR}/{p_img}'
            # IN_FILE = f'{PAGES_DIR}/{p_img}'

            # Create a photoimage object of the image in the path

            sz_w = 100
            sz_h = int(sz_w*1.41)
            load_file = image_dir + '/' + p_img + '.png'

            # print(f'load_file: {load_file}')

            icon_img = Image.open(load_file).resize((sz_w, sz_h))
            photo_img = ImageTk.PhotoImage(icon_img)
            pdf_lbl = tkinter.Label(image=photo_img)
            pdf_lbl.image = photo_img
            # label1.grid(row=u_row, column=0, padx=10, pady=(0, 20))
            #
            # u_switch_name = customtkinter.CTkSwitch(master=self.image_listing_frame, text=IN_FILE)
            # u_switch_name.grid(row=u_row_idx, column=u_col_idx, padx=10, pady=(0, 20))
            # u_page_listing_frame_switches.append(u_switch_name)

            u_img_lbl = tkinter.Label(
                master=out_frame,
                image=pdf_lbl.image,
                # image=self.list_image,
                text=p_img,
                compound='top',
                fg='white',
                # width=100,
                # background='grey',
                background='#2b2b2b'
            )
            u_img_lbl.grid(row=u_row_idx, column=u_col_idx, padx=10, pady=(0, 20))
            u_col_idx += 1

    def generate_combo_sort_files(self, in_file):
        pass

    def split_combo_into_pages(self):
        print(f'\nin split_combo_into_pages')
        listing = self.pdf_t.list_combo_dir()
        print(f'20:split_combo_into_pages:listing: {listing}')
        selection = []

        for i in range(len(self.combo_listing_frame_switches)):
            is_selected = self.combo_listing_frame_switches[i].get()
            if is_selected == 1:
                print(f'is_selected: {is_selected}')
                selection.append(listing[i])

        print(f'split_combo_into_pages:selection: {selection}')

        for selected in selection:
            # selection = f'{selection}'
            # print(f'split_execute:selection: {selection}')
            self.pdf_t.split_combo_pdf_into_pages(COMBO_INFILES_DIR, selected, f'{selected}', COMBO_PAGES_DIR)
            # return True

    # def split_combo_pdf_into_pages(self, in_dir, pdf_file, name_of_split, out_dir):
        print(f'u_pages_icon_refresh: calling refresh')
        self.u_pages_icon_refresh()
        self.u_combo_combo_listing_refresh()

    def display_meta_info(self):
        # print('display_info')
        self.textbox.delete("0.0", "end")  # delete all text
        listing = self.pdf_t.list_pdf_dir()
        # print(f'display_info:listing: {listing}')
        selection = []
        for i in range(len(self.f_scrollable_frame_switches)):
            is_selected = self.f_scrollable_frame_switches[i].get()
            if is_selected == 1:
                selection.append(listing[i])
        self.display_pdf_listing(selection)

    def split_pdf_2_pages(self):
        # print(f'in split_pdf_2_pages')
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
            self.pdf_t.split_pdf_into_pages(PDF_INFILES, selected, f'{selected}')
            # return True
        self.pdf_pages_refresh()

    def split_pdf_lst_2_pages(self, listing, in_dir):
        print(f'in split_pdf_lst_2_pages')
        # listing = self.pdf_t.list_pdf_dir()
        selection = []
        for i in range(len(self.f_scrollable_frame_switches)):
            is_selected = self.f_scrollable_frame_switches[i].get()
            if is_selected == 1:
                selection.append(listing[i])

        # print(f'split_execute:selection: {selection}')

        for selected in selection:
            # selection = f'{selection}'
            # print(f'split_execute:selection: {selection}')
            self.pdf_t.split_pdf_into_pages(in_dir, selected, f'{selected}')
            # return True
        self.pdf_pages_refresh()

    def split_combo_pdf_lst_2_pages(self, listing, in_dir):
        # self.combo_combo_listing_frame.grid_columnconfigure(0, weight=1)
        self.combo_combo_listing_frame_switches = []
        row = 0
        c_lst = self.get_combo_listing()
        print(f'split_combo_pdf_lst_2_pages:in split_pdf_2_pages')
        # listing = self.pdf_t.list_pdf_dir()
        selection = []
        for i in range(len(self.combo_combo_listing_frame_switches)):
            is_selected = self.combo_combo_listing_frame_switches[i].get()
            if is_selected == 1:
                selection.append(listing[i])

        # print(f'split_execute:selection: {selection}')

        for selected in selection:
            # selection = f'{selection}'
            # print(f'split_execute:selection: {selection}')
            self.pdf_t.split_pdf_into_pages(in_dir, selected, f'{selected}')
            # return True
        self.pdf_pages_refresh()

    def get_page_selection(self):
        listing = self.pdf_t.list_pages_dir()
        print(f'get_page_selection:listing[]: {listing}')
        selection = []
        for i in range(len(listing)):
            is_selected = self.page_listing_frame_switches[i].get()

            print(f'get_page_selection: is_selected; {is_selected}')
            # print(f'get_page_selection:is_selected: {is_selected} :: file: {listing[i]}')
            if is_selected == 1:
                selection.append(listing[i])
        print(f'get_page_selection:selection[]: {selection}')
        return selection

    def get_page_all_selected(self):
        listing = self.pdf_t.list_pages_dir()
        print(f'get_page_selection:listing[]: {listing}')
        selection = []
        for i in range(len(listing)):
            is_selected = 1
            # is_selected = self.page_listing_frame_switches[i].get()

            print(f'get_page_selection: is_selected; {is_selected}')
            # print(f'get_page_selection:is_selected: {is_selected} :: file: {listing[i]}')
            if is_selected == 1:
                selection.append(listing[i])
        print(f'get_page_selection:selection[]: {selection}')
        return selection

    def get_pages_listing(self):
        listing = self.pdf_t.list_pages_dir()
        # print(f'get_pages_listing:listing: {listing}')
        return listing

    def get_combo_images_listing(self):
        listing = self.pdf_t.list_combo_images_dir()
        # print(f'get_pages_listing:listing: {listing}')
        return listing

    def get_images_listing(self):
        listing = self.pdf_t.list_images_dir()
        return listing

    def get_combo_listing(self):
        listing = self.pdf_t.list_combo_dir()
        # print(f'get_combo_listing:listing: {listing}')
        return listing

    def get_combo_pages_listing(self):
        listing = self.pdf_t.list_combo_pages_dir()
        # print(f'XXXX:get_combo_pages_listing: {listing}')
        return listing

    def get_combo_combo_pages_listing(self):
        listing = self.pdf_t.list_combo_combo_pages_dir()
        print(f'get_combo_combo_pages_listing: {listing}')
        return listing

    def get_combo_infiles_listing(self):
        listing = self.pdf_t.list_combo_infiles_dir()
        # print(f'get_combo_infiles_listing: {listing}')
        return listing

    def get_combo_combo_infiles_listing(self):
        listing = self.pdf_t.list_combo_combo_infiles_dir()
        # print(f'get_combo_combo_infiles_listing:listing:[0]: {listing[0]}')
        return listing




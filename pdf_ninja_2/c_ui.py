import tkinter
import tkinter.messagebox
import customtkinter
from pdf_toolbox import PdfToolbox
from file_mgr import FileMgr
import os
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

THEME_COLOR = '#0c134f'
ICON_BACKGROUND_COLOR = '#2b2b2b'

NAVY_BLUE = '#05445E'
BLUE_GROTTO = '#189AB4'
BLUE_GREEN = '#75E6DA'
BABY_BLUE = '#D4F1F4'

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


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.pdf_t = PdfToolbox()

        # configure window
        self.wm_title("PDF Ninja")
        self.geometry(f"{W_X_SIZE}x{W_Y_SIZE}+{W_X_POS}+{W_Y_POS}")
        #
        # img = tkinter.PhotoImage(file=W_ICON)
        # self.iconphoto(False, img)

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)


        ###############################################
        # top menu bar
        # self.option_add('*tearOff', False)
        self.menubar = tkinter.Menu(self)
        self.menubar.config(bg="GREEN", fg="WHITE")
        self.config(menu=self.menubar)


        # file menu
        self.file_menu = tkinter.Menu(self.menubar, background='pink')
        self.file_menu.add_command(
            label='Open',
            command=self.open_file
        )
        self.file_menu.add_command(
            label='Exit',
            command=self.destroy
        )
        self.menubar.add_cascade(
            label="File",
            menu=self.file_menu
        )

        # about menu
        self.about_menu = tkinter.Menu(self.menubar)
        self.menubar.add_command(
            label='About',
            command=self.about_the_app
        )

        ###############################################
        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="PDF Ninja", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, text='Create Pages', command=self.sidebar_button_event)
        self.sidebar_button_4.grid(row=0, column=0, padx=20, pady=10)

        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text='List Pdfs', command=self.display_pdf_listing)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)

        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text='Display PDF Info', command=self.sidebar_button_event)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)

        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, text='NEW: Display PDF Info', command=self.sidebar_button_event)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)

        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, text='Create Pages', command=self.sidebar_button_event)
        self.sidebar_button_4.grid(row=4, column=0, padx=20, pady=10)

        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # create main entry and button
        self.entry = customtkinter.CTkEntry(self, placeholder_text="CTkEntry")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self, width=250, height=80)
        t_colspan = 5
        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew", columnspan=t_colspan)

        ####################################
        # controls tab
        self.tabview_t = customtkinter.CTkTabview(master=self, width=250)
        self.tabview_t.grid(row=1, column=2, padx=(20, 0), pady=(20, 0), rowspan=2, sticky="nsew")
        self.tabview_t.add("commands")  # add tab at the end
        self.tabview_t.add("tab 2")  # add tab at the end
        self.tabview_t.set("commands")  # set currently visible tab

        ####################################
        # user_entry
        self.user_entry = customtkinter.CTkEntry(
            master=self.tabview_t.tab("commands"),
            placeholder_text="combo filename")
        self.user_entry.grid(row=6, column=2, padx=(20, 0), pady=(20, 0))

        ####################################
        # icon display
        python_image = self.file_icon_build()
        self.icon = tkinter.Label(self.tabview_t.tab("commands"), image=python_image)
        self.icon.grid(row=0, column=2, padx=(20, 0), pady=(20, 0))

        ####################################
        # list PDFs
        self.button_ls_pdfs = customtkinter.CTkButton(
            master=self.tabview_t.tab("commands"),
            text='List Pdfs',
            command=self.display_pdf_listing
        )
        self.button_ls_pdfs.grid(row=1, column=2, padx=(20, 0), pady=(20, 0))

        ####################################
        # display info
        self.button_display_pdf_info = customtkinter.CTkButton(
            master=self.tabview_t.tab("commands"),
            text='Display PDF Info',
            command=lambda: self.display_info()
        )
        self.button_display_pdf_info.grid(row=2, column=2, padx=(20, 0), pady=(20, 0))

        ####################################
        # create pages
        self.button_create_pages = customtkinter.CTkButton(
            master=self.tabview_t.tab("commands"),
            text='Create Pages',
            command=self.split_execute
        )
        self.button_create_pages.grid(row=3, column=2, padx=(20, 0), pady=(20, 0))

        ####################################
        # merge pages
        self.button_merge_pages = customtkinter.CTkButton(
            master=self.tabview_t.tab("commands"),
            text='Merge Pages',
            command=self.merge_pages
        )
        self.button_merge_pages.grid(row=4, column=2, padx=(20, 0), pady=(20, 0))

        ####################################
        # refresh listings
        self.button_combine_pages = customtkinter.CTkButton(
            master=self.tabview_t.tab("commands"),
            text='Refresh Listings',
            command=self.refresh_listings
        )
        self.button_combine_pages.grid(row=5, column=2, padx=(20, 0), pady=(20, 0))

        ####################################
        # file manager
        #####################################
        self.tabview_files = customtkinter.CTkTabview(master=self, width=5)
        self.tabview_files.grid(row=1, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

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
        print(f'icon view')
        self.icon_listing_frame = customtkinter.CTkScrollableFrame(
            master=self.tabview_files.tab("icon view"),
            label_text="Icon View")
        self.icon_listing_frame.grid(row=0, column=2, padx=(20, 0), pady=(20, 0))

        self.icon_listing_frame_switches = []

        # build image
        icon_img = Image.open(W_ICON)
        icon_resize = icon_img.resize((50, 50))
        display_img = ImageTk.PhotoImage(icon_resize, width=50)
        i_lst = self.get_pages_listing()

        # icon file listing
        i_row = 0
        for i in i_lst:
            self.icon_img_lbl = tkinter.Label(
                self.icon_listing_frame,
                text=f'{i}',
                image=display_img,
                compound=tkinter.LEFT,
                bg=ICON_BACKGROUND_COLOR,
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

        # set default values
        self.sidebar_button_3.configure(state="disabled", text="Disabled CTkButton")
        # self.checkbox_3.configure(state="disabled")
        # self.checkbox_1.select()
        self.f_scrollable_frame_switches[0].select()
        # self.page_listing_frame_switches[0].select()
        # self.scrollable_frame_switches[4].select()
        # self.radio_button_3.configure(state="disabled")
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")
        # self.optionmenu_1.set("CTkOptionmenu")
        # self.combobox_1.set("CTkComboBox")
        # self.slider_1.configure(command=self.progressbar_2.set)
        # self.slider_2.configure(command=self.progressbar_3.set)
        # self.progressbar_1.configure(mode="indeterminnate")
        # self.progressbar_1.start()
        self.textbox.insert("0.0", "CTkTextbox\n\n" + "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.\n\n" * 20)
        # self.seg_button_1.configure(values=["CTkSegmentedButton", "Value 2", "Value 3"])
        # self.seg_button_1.set("Value 2")

        self.mainloop()

    def open_file(self):
        print('menu: file->open file')

    def about_the_app(self):
        print('menu: about')

    def file_icon_build(self):
        icon_img = Image.open(W_ICON)
        icon_resize = icon_img.resize((50, 50))
        print(f'icon_resize: {icon_resize}')
        python_img = ImageTk.PhotoImage(icon_resize, width=50)
        return python_img

    def refresh_f_listings(self):
        dir_contents = [f for f in os.listdir(PDF_PAGES) if os.path.isfile(os.path.join(PDF_PAGES, f))]
        print(f'refresh_f_listings:dir_contents: {dir_contents}')

    def refresh_listings(self):
        self.refresh_f_listings()
        self.combo_refresh()
        self.pages_refresh()

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
        print(f'in pages_refresh')
        self.page_listing_frame.grid_columnconfigure(0, weight=1)
        self.page_listing_frame_switches = []
        row = 0
        c_lst = self.get_pages_listing()
        print(f'c_lst: {c_lst}')
        for f in c_lst:
            # print(f'f:{f}')
            switch_name = customtkinter.CTkSwitch(master=self.page_listing_frame, text=f"{f}")
            switch_name.grid(row=row, column=0, padx=10, pady=(0, 20))
            row += 1
            self.page_listing_frame_switches.append(switch_name)
        # print(f'switches: {self.scrollable_frame_switches}')

    def icon_refresh(self):
        print(f'in pages_refresh')
        self.icon_listing_frame.grid_columnconfigure(0, weight=1)
        self.icon_listing_frame_switches = []
        row = 0
        c_lst = self.get_pages_listing()
        print(f'icon_refresh:c_lst: {c_lst}')

        icon_image = self.file_icon_build()

        self.icon = tkinter.Label(self.tabview_t.tab("commands"), image=python_image)

        self.icon = tkinter.Label(self.icon_listing_frame, image=icon_image)
        self.icon.grid(row=0, column=2, padx=(20, 0), pady=(20, 0))


        for f in c_lst:
            print(f'f:{f}')
            switch_name = customtkinter.CTkSwitch(master=self.icon_listing_frame, text=f"{f}")
            switch_name.grid(row=row, column=0, padx=10, pady=(0, 20))
            row += 1
            self.icon_listing_frame_switches.append(switch_name)
        # print(f'switches: {self.scrollable_frame_switches}')

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

    def get_listing(self):
        listing = self.pdf_t.list_pdf_dir()
        # print(f'get_listing:listing: {listing}')
        return listing

    def get_pages_listing(self):
        listing = self.pdf_t.list_pages_dir()
        return listing

    def get_combo_listing(self):
        listing = self.pdf_t.list_combo_dir()
        return listing

    def display_pdf_listing(self):
        listing = self.pdf_t.list_pdf_dir()
        self.display_listing(listing)

    def display_listing(self, lst):
        # print(f'display_pdf_listing:lst: {lst}')
        out_txt = ''
        for f in lst:
            out_txt += f'{f}\n'
        self.textbox.delete("0.0", "end")  # delete all text
        self.textbox.insert("0.0", out_txt)

        # self.info_canvas.itemconfig(self.info_text, text=out_txt)

    def display_info(self):
        # print('start')
        self.textbox.delete("0.0", "end")  # delete all text

        listing = self.pdf_t.list_pdf_dir()

        selection = []
        for i in range(len(self.f_scrollable_frame_switches)):
            is_selected = self.f_scrollable_frame_switches[i].get()
            if is_selected == 1:
                selection.append(listing[i])
        # print(f'display_info:selection: {selection}')

        for selected in selection:
            f_name = selected
            # print(f'displaying info:f_name: {f_name}')
            msg = self.pdf_t.extract_information(f_name)
            self.textbox.insert("0.0", msg)
            # self.info_canvas.itemconfig(self.info_text, text=msg)

    def get_selection(self):
        # value = self.checkbox_slider_frame.curselection()
        value = self.f_scrollable_frame_switches[0].get()
        # value = ()
        # print(f'get_selection:value: {value}')
        if value == None:
            # print(f'get_selection:{NOTHING_SELECTED}')
            selection = NOTHING_SELECTED
        else:
            selection = value
            # print(f'get_selection:value FOUND: {value}')
            # selection = self.dir_listing_lb.get(self.dir_listing_lb.curselection())
        return selection

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")

#
# if __name__ == "__main__":
#     app = App()
#     app.mainloop()



        self.nj_support_sort_list_frame()


    def nj_dashboard_sort_list_frame(self):








 self.combo_filename_dnd_entry = tk.Frame(
            master=self.dashboard_operations_bottom,
        self.combo_filename_dnd_entry.grid(row=1, column=0, padx=(0, 0), pady=(5, 0), sticky='N')




    def gen_combo_pages_from_combo(self):
            is_set = self.combo_pages_listing_frame_switches[row].get()


combo_sort_infiles_listing_frame















combo_listing_frame

combo_list_combos_frame


combo_pages_listing_frame_switches
combo_pages_listing_frame

combo_sort_infiles_listing_frame_switches
combo_pages_listing_frame


        self.combo_refresh()

      self.combo_listing_frame = customtkinter.CTkScrollableFrame(
            master=self.tabview_files.tab("List Combos"),
            label_text="Combo PDF Listing",
            width=CMD_FILE_LISTING_WIDTH
        )
        self.combo_listing_frame.grid(row=1, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.combo_listing_frame.grid_columnconfigure(0, weight=1)



    def combo_refresh(self):
        print(f'in combo_refresh')
        self.combo_listing_frame.grid_columnconfigure(0, weight=1)
        self.combo_listing_frame_switches = []
        row = 0
        combo_lst = self.get_combo_listing()
        print(f'combo_refresh:combo_lst:xxx: {combo_lst}')

        for combo in combo_lst:
            # print(f'combo:{combo}')
            switch_name = customtkinter.CTkSwitch(master=self.combo_listing_frame, text=f"{combo}")
            switch_name.grid(row=row, column=0, padx=10, pady=(0, 20))
            row += 1
            self.combo_listing_frame_switches.append(switch_name)
        print(f'switches: {self.combo_listing_frame_switches}')


    def pdf_pages_refresh(self):
        # print(f'in pages_refresh')
        self.page_listing_frame.grid_columnconfigure(0, weight=1)
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






299
        self.combo_listing_frame = tk.Frame(
            master=self.u_tabview_files.tab("PDF Combo"),
            bg='red',
            width=1000,
            height=1000,
        )

combo_listing_frame





        self.combo_refresh()


combo_listing_frame

        # main sort window
        ##### combo_dnd_listing_frame
        self.dashboard_listing_frame = customtkinter.CTkScrollableFrame(
            master=self.dashboard_listing_frame,

        # combo_infiles_listing_frame
        self.combo_sort_infiles_listing_frame = customtkinter.CTkScrollableFrame(
            master=self.combo_listing_frame,




 267       self.dashboard_listing_frame = customtkinter.CTkScrollableFrame(
            master=self.dashboard_listing_frame,
            label_text="Combo Sort Listing",


307     self.dashboard_listing_frame = customtkinter.CTkScrollableFrame(
            master=self.combo_listing_frame,
            label_text="Combo Infiles Listing",


386            combo_sort_listing_frame = customtkinter.CTkScrollableFrame(
                        master=self.combo_listing_frame,
                        label_text="Combo Infiles Listing",

           def combo_sort_refresh(self):
                print(f'\ncombo_sort_refresh')
552             self.dashboard_listing_frame.grid_columnconfigure(0, weight=1)

                ...

                self.combo_sort_image_frame = ttk.Frame(
                    master=self.dashboard_listing_frame,
                )

          def u_combo_listing_refresh(self):
                print('u_combo_listing_refresh')
831              self.dashboard_listing_frame.grid_columnconfigure(0, weight=1)


        def combo_infiles_refresh(self):
                print(f'combo_infiles_refresh')
1381            self.dashboard_listing_frame.grid_columnconfigure(0, weight=1)
                # self.combo_infiles_listing_frame_switches = []




# combo_pages_listing_frame

        self.dashboard_listing_frame = ttk.Frame(
            # self,
            master=self.u_tabview_files.tab("PDF Combo"),
            width=100,
            # width=SIDEBAR_WIDTH,
            height=BRAND_FRAME_HEIGHT,
            # style='comboInfilesListingFrame.TFrame'
        )
        self.dashboard_listing_frame.grid(row=0, column=1, sticky='NSEW')

        #
        # self.disp_combo_infiles_frame = customtkinter.CTkFrame(
        #     master=self.combo_infiles_listing_frame,
        #     # label_text="Combo Page XXX",
        #     width=200,
        #     # width=U_WIDTH - 200,
        #     height=U_HEIGHT,
        #     fg_color=PALETTE_DARK
        # )
        # self.disp_combo_infiles_frame.grid(row=0, column=2, padx=(0, 0), pady=(0, 0), sticky="")
        # self.disp_combo_infiles_frame_switches = []

        self.disp_combo_files_frame = customtkinter.CTkScrollableFrame(
            master=self.dashboard_listing_frame,
            label_text="COMBO Page-Sort",
            width=200,
            # width=U_WIDTH - 200,
            height=U_HEIGHT
        )
        self.disp_combo_files_frame.grid(row=0, column=1, padx=(0, 0), pady=(0, 0), sticky="")
        self.disp_combo_files_frame_switches = []


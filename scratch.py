
support_container_frame


support_operations_bottom_frame



master=self.u_tabview_files.tab("PDF Infiles Listing"),



ninjaFrame
    self.tabview_t.tab("Re-Order Combo")
        self.u_tabview_files.tab("PDF Infiles Listing"),
               # dnd_sort_list_control_bar

768            dashboard_listing_frame
558            dashboard_listing_frame

580            dashboard_operations_bottom

585            dashboard_operations_top
                    topbar_load_pdf_file_btn
                    topbar_gen_pages_from_pdf_infiles_btn
                    topbar_gen_combo_infiles_all_btn
                    topbar_gen_combo_pages_from_pdf_infiles_btn
                    topbar_gen_combo_images_from_combo_infiles_btn
                    topbar_full_was_cycle_btn


ninjaFrame
    self.tabview_t.tab("Re-Order Combo")
        self.u_tabview_files.tab("PDF Combo")
183            support_operations_top_frame
175            support_operations_bottom_frame
                    dashboard_listings_frame


            support_container_frame
                combo_listing_frame
# 518                    support_operations_top_frame

                    support_operations_bottom_1_frame

                    top_dashboard_listings_frame
                        combo_sort_infiles_listing_frame
                        combo_pages_listing_frame
                        disp_combo_images_frame









                combo_listing_frame
                    top_dashboard_listings_frame
                        combo_pages_listing_frame
                        combo_sort_infiles_listing_frame
                        disp_combo_images_frame

                    support_operations_top_frame
                        refresh_combo_infiles_btn
                        refresh_combo_images_btn

                    support_operations_top_frame_PROTO
                        combo_split_pages_btn
                        refresh_combo_pages_btn

                    # ISSUE?
                    top_dashboard_listings_frame (yellow)

                    # DUPLICATES
                    support_operations_bottom_frame
                        combo_split_pages_btn
                        refresh_combo_pages_btn
                        support_refresh_combo_pages_btn







ninjaFrame
    self.tabview_t.tab("Re-Order Combo")
        self.u_tabview_files.tab("PDF Combo")
            support_container_frame
                combo_listing_frame
                    # support_operations_top_frame_PROTO
                    support_operations_top_frame
                        refresh_combo_infiles_btn
                        refresh_combo_images_btn
                    # DUPLICATES
                    support_operations_bottom_frame
                        combo_split_pages_btn
                        refresh_combo_pages_btn
                        support_refresh_combo_pages_btn

#
# self.support_container_frame = tk.Frame(
#     master=self.u_tabview_files.tab("PDF Combo"),
#
#     self.top_dashboard_listings_frame = tk.Frame(
#         master=support_container_frame,
#
#     self.support_operations_top_frame = tk.Frame(
#     master=support_container_frame,
#
#             self.refresh_combo_images_btn = customtkinter.CTkButton(
#                 master=self.support_operations_top_frame,
#
#             self.refresh_combo_infiles_btn = customtkinter.CTkButton(
#                 master=self.support_operations_top_frame,
#
#     self.support_operation_bottom_frame = tk.Frame(
#         master=self.support_container_frame,
#
#     # DUPLICATE
#     self.support_operation_bottom_frame = tk.Frame(
#         master=self.support_container_frame,

    self.support_operation_bottom_frame = tk.Frame(
        master=self.support_container_frame,

        self.refresh_combo_images_btn = customtkinter.CTkButton(
            master=self.support_operation_bottom_frame,

        self.refresh_combo_pages_btn = customtkinter.CTkButton(
                master=self.support_operation_bottom_frame,

        self.combo_split_pages_btn = customtkinter.CTkButton(
            master=self.support_operation_bottom_frame,



#
# self.top_dashboard_listings_frame = tk.Frame(
#     master=self.u_tabview_files.tab("PDF Combo"),

#
# self.support_container_frame = tk.Frame(
# master=self.u_tabview_files.tab("PDF Combo"),

self.support_operations_top_frame = tk.Frame(
    master=self.u_tabview_files.tab("PDF Combo"),



refresh combo pages images - DB

refresh combo pages images - TOP BAR



nj_user_dashboard_combo_infiles_listing

top_bar_controls_frame


combo_listing_frame

combo_sort_refresh

        self.build_combo_all()

       # load gen pages from pdf_infiles
        self.topbar_gen_pages_from_pdf_infiles_btn = customtkinter.CTkButton(
            master=self.dashboard_operations_top,
            text='Generate Combo Pages',
            command=self.gen_pdf_pages_from_all_infiles
        )
        self.topbar_gen_pages_from_pdf_infiles_btn.grid(row=0, column=1, padx=(5, 5), pady=(5, 5))





        combo_pages_listing = self.get_combo_pages_listing()
        combo_pages_in_dir = COMBO_PAGES_DIR
        self.refresh_all_combo_pages_images(combo_pages_listing, combo_pages_in_dir)


self.refresh_combo_pages_images(combo_pages_listing, combo_pages_in_dir)


combo_dnd_operations

full_wash_cycle(

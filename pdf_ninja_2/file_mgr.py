import tkinter
import tkinter.messagebox
import customtkinter
from pdf_toolbox import PdfToolbox
import os
from PIL import Image, ImageTk


class FileMgr:

    def __init__(self):

        self.pdf_t = PdfToolbox()

        ####################################
        # file manager utile

    def get_listing(self):
        listing = self.pdf_t.list_pdf_dir()
        # print(f'get_listing:listing: {listing}')
        return listing

    def get_pages_listing(self):
        listing = self.pdf_t.list_pages_dir()
        # print(f'get_listing:listing: {listing}')
        return listing

    def get_combo_listing(self):
        listing = self.pdf_t.list_combo_dir()
        print(f'get_combo_listing:listing: {listing}')
        return listing

    def file_icon_build(self):
        icon_img = Image.open(W_ICON)
        icon_resize = icon_img.resize((50, 50))
        print(f'icon_resize: {icon_resize}')
        python_img = ImageTk.PhotoImage(icon_resize, width=50)
        return python_img



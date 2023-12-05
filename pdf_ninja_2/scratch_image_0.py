from tkinter import *
import customtkinter
from PIL import Image, ImageTk

ICON_IMG = './images/3876391_.ico_icon.ico'
DIR_IMG = './images/icons8-folder-48.png'
LIST_IMG = './images/icons8-pdf-48.png'

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

root = customtkinter.CTk()

root.title('PDF Jinja')
root.iconbitmap(ICON_IMG)
root.geometry('500x170+1000+100')

# define out images
add_folder_image = ImageTk.PhotoImage(Image.open(DIR_IMG).resize((35, 35)))
add_list_image = ImageTk.PhotoImage(Image.open(LIST_IMG).resize((35, 35)))

# create buttons
button_1 = customtkinter.CTkButton(
    master=root,
    image=add_folder_image,
    text='Add Folder',
    width=150,
    height=40,
    compound='left',
)
button_1.pack(padx=20, pady=20)

button_2 = customtkinter.CTkButton(
    master=root,
    image=add_list_image,
    text='Add List',
    width=150,
    height=40,
    compound='right',
    fg_color='#D35B58',
    hover_color='#C77C78'
)
button_2.pack(padx=20, pady=20)




root.mainloop()

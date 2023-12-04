import tkinter as tk
from tkinter import *
my_w = tk.Tk()
my_w.geometry("410x200")  # Size of the window

my_w.columnconfigure(0,weight=1)
my_w.rowconfigure(0, weight=1)
my_w.rowconfigure(1, weight=1) # change weight to 4
my_w.rowconfigure(2, weight=1)

frame_top=tk.Frame(my_w,bg='red')
frame_middle=tk.Frame(my_w,bg='yellow')
frame_bottom=tk.Frame(my_w,bg='blue')
#placing in grid
frame_top.grid(row=0,column=0,sticky='WENS')
frame_middle.grid(row=1,column=0,sticky='WENS')
frame_bottom.grid(row=2,column=0,sticky='WENS')
#adding labels to frame
l1=tk.Label(frame_top,text='frame_top')
l1.grid(row=0,column=0,padx=10,pady=2)

l2=tk.Label(frame_middle,text='frame_middle')
l2.grid(row=0,column=0,padx=10,pady=2)

l3=tk.Label(frame_bottom,text='frame_bottom')
l3.grid(row=0,column=0,padx=10,pady=2)
my_w.mainloop()  # Keep the window open

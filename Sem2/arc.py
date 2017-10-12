# !/usr/bin/python3
from tkinter import *

from tkinter import messagebox

top = Tk()

C = Canvas(top, bg = "yellow", height = 250, width = 300)

coord = 10, 50, 240, 210
arc = C.create_arc(coord, start = 0, extent = 110, fill = "red")
line = C.create_line(10,10,190,200,fill = 'blue')
C.pack()
top.mainloop()

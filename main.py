from tkinter import *
from PIL import ImageTk, Image

import numpy as np
import cv2

root = Tk()
root.title('Credential Printing')
#Geometry WidthxHeight+Horizontal+Vertical
root.geometry('1250x650+60+30')
root.rowconfigure(0, minsize=650, weight=1)
root.columnconfigure([0,1], minsize=625, weight=1)

frame_1 = Frame(root, bg='black')
frame_1.grid(row=0, column=0)

filename = PhotoImage(file = "fot.png")
background_label = Label(frame_1, height=400, image=filename)
background_label.pack()

# label = Label(frame_1, text='Yomero')
# label.pack()

root.mainloop()
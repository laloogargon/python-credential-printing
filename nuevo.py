from tkinter import *
from PIL import ImageTk, Image

import cv2
import numpy as np

window = Tk()

frame1 = Frame(window, width=1000, height=500)
frame1.grid()

lImage = Label(frame1)
lImage.grid()

src = cv2.imread('ima.png', cv2.IMREAD_UNCHANGED)

scale_percent = 50
width = int(src.shape[1] * scale_percent / 100)
height = int(src.shape[0] * scale_percent / 100)
desired_size = (width, height)

image_front_resize = cv2.resize(src, desired_size)

cv2image = cv2.cvtColor(image_front_resize, cv2.COLOR_BGR2RGBA)

img = Image.fromarray(cv2image)
imgtk = ImageTk.PhotoImage(image=img)
lImage.imgtk = imgtk
lImage.configure(image=imgtk)
# lImage.after(1, video_stream) 
window.mainloop()